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

from applet import Applet


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


class Landscape:

    def draw(self, canvas):
        cr = canvas.cr

        # Fill the background with gray
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.rectangle(0, 0, canvas.width, canvas.height)
        cr.fill()

        for i in range(0, 500):
            gray = random.random()
            cr.set_source_rgb(gray, gray, gray)
            cr.arc(canvas.width * random.random() + 0.5,
                   canvas.height * random.random() + 0.5,
                   0.1, 0.0, 2 * math.pi)
            cr.stroke()

        c = [random.random(),
             random.random(),
             random.random()]

        xof = (random.random() - 0.5) * 2.0
        yof = (random.random() - 0.5) * 2.0

        for i in range(0, random.randint(1, 2)):
            x = random.randint(0, canvas.width)
            y = random.randint(0, canvas.height // 2)
            radius = random.randint(5, 72)

            self.draw_moon(canvas, x, y, radius, xof * radius, yof * radius,
                           [c[0] * (1.0 - random.random() / 10.0),
                            c[1] * (1.0 - random.random() / 10.0),
                            c[2] * (1.0 - random.random() / 10.0)])

        y = canvas.height / 2.0 * 1.5
        n = 64

        for i in range(0, n):
            cr.set_source_rgb(((i + 1) / float(n) * c[0]) ** 2.2,
                              ((i + 1) / float(n) * c[1]) ** 2.2,
                              ((i + 1) / float(n) * c[2]) ** 2.2)
            self.draw_mountain(canvas, y + 2 ** (7.0 * (float(i) / (n - 1))))

    def draw_moon(self, canvas, x, y, radius, xof, yof, c):
        cr = canvas.cr

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

    def draw_mountain(self, canvas, y):
        cr = canvas.cr

        points = gen_segments(y + (random.random() - 0.5) * 128.0,
                              y + (random.random() - 0.5) * 128.0,
                              8,
                              lambda a, b, d: (a + b) / 2.0 + (random.random() - 0.5) * (canvas.height / 3.0) / 2 ** d)

        cr.move_to(0, canvas.height)
        for idx, p in enumerate(points):
            cr.line_to(canvas.width / float(len(points) - 1) * idx, p)
        cr.line_to(canvas.width, canvas.height)
        cr.fill()


if __name__ == "__main__":
    applet = Applet()
    applet.set_size(640, 480)
    applet.run(Landscape().draw)


# EOF #
