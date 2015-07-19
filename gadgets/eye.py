#!/usr/bin/env python3

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


import math
import random

from applet import Applet
from gif_applet import GifApplet

class Eye:

    def __init__(self):
        self.crosses = []
        for i in range(750):
            self.crosses.append([random.randint(0, 512),
                                 random.randint(0, 512),
                                 random.random() * math.pi,
                                 (random.random(),
                                  random.random(),
                                  random.random())])

    def draw(self, ctx):
        cr = ctx.cr

        size = 5

        cr.set_source_rgb(0, 0, 0)
        cr.paint()

        cr.set_line_width(3)
        for cross in self.crosses:
            cr.move_to(cross[0], cross[1])
            cr.save()
            cr.rotate(cross[2] + ctx.time * 0.005)
            cr.rel_move_to(0, -size)
            cr.rel_line_to(0, 2*size)
            cr.rel_move_to(-size, -size)
            cr.rel_line_to(2*size, 0)
            cr.set_source_rgb(*cross[3])
            cr.stroke()
            cr.restore()

if __name__ == "__main__":
    applet = Applet()
    applet.set_size(512, 512)
    applet.set_title("Eye")
    applet.run_animation(Eye().draw, 1000 / 24)


# EOF #
