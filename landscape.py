#! /usr/bin/env python3

# Simple landscape generator for Gtk
# Copyright (C) 2011 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import random
import math
from gi.repository import Gtk


def midpoint(lst):
    x = 0.0
    y = 0.0
    for el in lst:
        x += el[0]
        y += el[1]
    return (x / len(lst), y / len(lst))


def jitter(p, r):
    return (p[0] + (random.random() * 2.0 - 1.0) * r,
            p[1] + (random.random() * 2.0 - 1.0) * r)


def gen_segments(a, b, depth, midfunc):
    def loop(a, b, r):
        if r == 0:
            return [a]
        else:
            m = midfunc(a, b, depth - r)
            return loop(a, m, r - 1) + loop(m, b, r - 1)

    return loop(a, b, depth) + [b]


def draw_landscape(cr):
    width = cr.get_group_target().get_width()
    height = cr.get_group_target().get_height()

    # Fill the background with gray
    cr.set_source_rgb(0.0, 0.0, 0.0)
    cr.rectangle(0, 0, width, height)
    cr.fill()

    for i in range(0, 500):
        gray = random.random()
        cr.set_source_rgb(gray, gray, gray)
        cr.arc(width * random.random() + 0.5,
               height * random.random() + 0.5,
               0.1, 0.0, 2 * math.pi)
        cr.stroke()

    c = [random.random(),
         random.random(),
         random.random()]

    xof = (random.random() - 0.5) * 2.0
    yof = (random.random() - 0.5) * 2.0

    for i in range(0, random.randint(1, 2)):
        x = random.randint(0, width)
        y = random.randint(0, height // 2)
        radius = random.randint(5, 72)

        draw_moon(cr, x, y, radius, xof * radius, yof * radius,
                  [c[0] * (1.0 - random.random() / 10.0),
                   c[1] * (1.0 - random.random() / 10.0),
                   c[2] * (1.0 - random.random() / 10.0)])

    y = height / 2.0 * 1.5
    n = 64

    for i in range(0, n):
        cr.set_source_rgb(((i + 1) / float(n) * c[0]) ** 2.2,
                          ((i + 1) / float(n) * c[1]) ** 2.2,
                          ((i + 1) / float(n) * c[2]) ** 2.2)
        draw_mountain(cr, y + 2 ** (7.0 * (float(i) / (n - 1))), width, height)


def draw_moon(cr, x, y, radius, xof, yof, c):
    cr.set_source_rgb(c[0], c[1], c[2])
    cr.arc(x, y, radius * 1.1, 0.0, 2 * math.pi)
    cr.fill()

    cr.set_source_rgb(c[0] * 2.0, c[1] * 2.0, c[2] * 2.0)
    cr.arc(x, y, radius, 0.0, 2 * math.pi)
    cr.fill()

    cr.save()
    cr.arc(x, y, radius * 1.2, 0.0, 2 * math.pi)
    cr.clip()

    cr.new_path()
    cr.set_source_rgb(0, 0, 0)
    cr.arc(x + xof,
           y + yof,
           radius * 1.5, 0.0, 2 * math.pi)
    cr.fill()
    # cr.reset_clip()
    cr.restore()


def draw_mountain(cr, y, width, height):
    width = cr.get_group_target().get_width()
    height = cr.get_group_target().get_height()

    points = gen_segments(y + (random.random() - 0.5) * 128.0,
                          y + (random.random() - 0.5) * 128.0,
                          8,
                          lambda a, b, d: (a + b) / 2.0 + (random.random() - 0.5) * (height / 3.0) / 2 ** d)

    cr.move_to(0, height)
    for idx, p in enumerate(points):
        cr.line_to(width / float(len(points) - 1) * idx, p)
    cr.line_to(width, height)
    cr.fill()


def main():
    window = Gtk.Window()
    window.set_size_request(640, 480)
    window.connect("delete-event", Gtk.main_quit)

    vbox = Gtk.VBox()

    widget = Gtk.DrawingArea()
    widget.show()

    widget.connect("draw", lambda widget, cr: draw_landscape(cr))

    button = Gtk.Button("Regenerate")
    button.connect("clicked", lambda ev: widget.queue_draw())
    button.show()

    vbox.pack_start(widget, True, True, 0)
    vbox.pack_start(button, False, True, 0)
    vbox.show()

    window.add(vbox)

    window.present()
    Gtk.main()


if __name__ == "__main__":
    main()


# EOF #
