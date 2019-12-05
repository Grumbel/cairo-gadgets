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

from cairogadget import Applet


class Tunnel:

    def draw(self, ctx):
        cr = ctx.cr
        cx = ctx.width / 2
        cy = ctx.height / 2

        for i in range(0, 40):
            i += ctx.time * 0.05
            i = i % 40
            r = 40 * (i / 10) ** 2
            cr.arc(cx, cy, r, 0, 2 * math.pi)
            cr.stroke()


def main():
    applet = Applet()
    applet.set_size(854, 480)
    applet.set_title("Tunnel")
    applet.run_animation(Tunnel().draw, 1000 / 24)


if __name__ == "__main__":
    main()


# EOF #
