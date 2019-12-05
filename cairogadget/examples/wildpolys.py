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


import random
import types
from cairogadget import Applet


class WildPolys:

    def __init__(self):
        self.points = []
        for _ in range(10):
            self.points.append(types.SimpleNamespace(
                x=random.randint(0, 640),
                y=random.randint(0, 480),
                ax=random.randint(1, 5),
                ay=random.randint(1, 5)))

    def draw(self, ctx):
        cr = ctx.cr

        p = self.points[0]
        cr.line_to(p.x, p.y)
        for p in self.points[1:]:
            cr.line_to(p.x, p.y)
        cr.close_path()
        cr.stroke()

        for p in self.points:
            p.x += p.ax
            p.y += p.ay

            if p.x < 0:
                p.ax = ctx.random.randint(1, 5)
            elif p.x >= ctx.width:
                p.ax = ctx.random.randint(-5, 1)

            if p.y < 0:
                p.ay = ctx.random.randint(1, 5)
            elif p.y >= ctx.height:
                p.ay = ctx.random.randint(-5, 1)


if __name__ == "__main__":
    applet = Applet()
    applet.run_animation(WildPolys().draw, 1000 / 60)


# EOF #
