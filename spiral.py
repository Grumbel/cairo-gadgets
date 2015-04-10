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


class SpiralApplet(Applet):

    def setup(self):
        self.set_size(640, 480)

    def draw(self, canvas):
        cr = canvas.cr

        # Fill the background with gray
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.rectangle(0, 0, canvas.width, canvas.height)
        cr.fill()

        self.draw_spiral(canvas,
                         canvas.width / 2.0, canvas.height / 5.0 * 4.0,
                         0,
                         canvas.width / 2.0,
                         random.random() * 0.1 + 0.1)

    def draw_spiral(self, canvas, x, y, angle, length, angle_delta):
        cr = canvas.cr

        if length > 20.0:
            nangle = angle + angle_delta
            seg = length / 30.0

            dx = seg * math.sin(nangle)
            dy = -seg * math.cos(nangle)

            # cr.set_source_rgb(random.random(),
            #                  random.random(),
            #                  random.random())
            # cr.set_line_width(2.0)
            cr.set_source_rgb(1, 1, 1)
            cr.move_to(x,
                       y)
            cr.line_to(x + dx,
                       y + dy)
            cr.stroke()

            if random.randint(0, 15) == 0:
                self.draw_spiral(canvas,
                                 x + dx,
                                 y + dy,
                                 nangle,
                                 length - seg,
                                 -angle_delta)

            self.draw_spiral(canvas,
                             x + dx,
                             y + dy,
                             nangle,
                             length - seg,
                             angle_delta)


if __name__ == "__main__":
    applet = SpiralApplet()
    applet.run()


# EOF #
