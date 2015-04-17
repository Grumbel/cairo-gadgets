#! /usr/bin/env python3

# cairo-gadgets - A collection of gadgets for cairo
# Copyright (C) 2015 Ingo Ruhnke <grumbel@gmail.com>
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


from gi.repository import Gtk
import random


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


# Create a GTK+ widget on which we will draw using Cairo
class Screen(Gtk.DrawingArea):

    # Handle the expose-event by drawing

    def do_draw(self, cr):
        width = self.get_allocated_width()
        height = self.get_allocated_height()

        # Fill the background with gray
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.rectangle(0, 0, width, height)
        cr.fill()

        cr.set_source_rgba(1.0, 1.0, 1.0, 0.5)

        self.draw_line(cr,
                       (10, height / 2.0),
                       (width - 10, height / 2.0),
                       10)

        self.draw_line(cr,
                       (10, height / 2.0),
                       (width - 10, height / 2.0),
                       10)
        cr.stroke()

    def draw_line(self, cr, a, b, r):
        if r == 0:
            cr.move_to(a[0], a[1])
            cr.line_to(b[0], b[1])
        else:
            m = midpoint([a, b])
            m = (m[0], m[1] + (random.random() * 2.0 - 1.0) * (2.0 ** r) * 0.1)
            self.draw_line(cr, a, m, r - 1)
            self.draw_line(cr, m, b, r - 1)


def run(Widget):
    window = Gtk.Window()
    window.connect("delete-event", Gtk.main_quit)
    widget = Widget()
    widget.show()
    window.add(widget)
    window.present()
    Gtk.main()


if __name__ == "__main__":
    run(Screen)


# EOF #
