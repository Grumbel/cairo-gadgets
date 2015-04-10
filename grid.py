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


import random
import math

from applet import Applet


class GridApplet(Applet):

    def setup(self):
        self.set_title("Grid Effect")
        self.set_size(640, 480)

    def draw(self, canvas):
        cr = canvas.cr

        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.rectangle(0, 0, canvas.width, canvas.height)
        cr.fill()

        n = random.randint(6, 64)
        x_step = canvas.width / (n - 1)
        y_step = canvas.height / (n - 1)

        cr.set_source_rgb(1.0, 0.0, 0.0)
        for i in range(n):
            cr.move_to(0, i * y_step)
            cr.line_to((n - i - 1) * x_step, 0)
        cr.stroke()

        cr.set_source_rgb(0.0, 0.0, 1.0)
        for i in range(n):
            cr.move_to(0, i * y_step)
            cr.line_to(i * x_step, canvas.height)
        cr.stroke()

        cr.set_source_rgb(0.0, 1.0, 1.0)
        for i in range(n):
            cr.move_to(canvas.width, (n - i - 1) * y_step)
            cr.line_to(i * x_step, canvas.height)
        cr.stroke()

        cr.set_source_rgb(1.0, 0.0, 1.0)
        for i in range(n):
            cr.move_to(canvas.width, (n - i - 1) * y_step)
            cr.line_to((n - i - 1) * x_step, 0)
        cr.stroke()


if __name__ == "__main__":
    applet = GridApplet()
    applet.run()


# EOF #