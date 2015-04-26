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


from applet import Applet


def draw(ctx):
    total_frames = int(ctx.time / (1000 / 16))

    cr = ctx.cr

    n = 12

    cw = ctx.width / n * 0.5
    ch = cw

    cx = ctx.width / 2
    cy = ctx.height / 2

    w = (cw * n) + (cw / 2 * (n - 1))

    cr.set_source_rgb(0, 0, 0)
    cr.paint()
    lit2 = ((total_frames - 2) % (2 * n - 2)) - (n - 1)
    lit1 = ((total_frames - 1) % (2 * n - 2)) - (n - 1)
    lit = (total_frames % (2 * n - 2)) - (n - 1)
    for i in range(n):
        if lit == i or lit == -i:
            cr.set_source_rgb(0.75, 0, 0)
            cr.rectangle(cx - cw / 2 - w / 2 + i * (cw + cw / 2) - cw / 4,
                         cy - ch / 2 - cw / 4,
                         cw + cw / 2, ch + cw / 2)
            cr.fill()

            cr.set_source_rgb(1, 0, 0)
            cr.rectangle(cx - cw / 2 - w / 2 + i * (cw + cw / 2) - cw / 8,
                         cy - ch / 2 - cw / 8,
                         cw + cw / 4, ch + cw / 4)
            cr.fill()
        elif lit1 == i or lit1 == -i:
            cr.set_source_rgb(0.5, 0, 0)
            cr.rectangle(cx - cw / 2 - w / 2 + i * (cw + cw / 2) - cw / 8,
                         cy - ch / 2 - cw / 8,
                         cw + cw / 4, ch + cw / 4)
            cr.fill()

            cr.set_source_rgb(0.75, 0, 0)
            cr.rectangle(cx - cw / 2 - w / 2 + i * (cw + cw / 2),
                         cy - ch / 2,
                         cw, ch)
            cr.fill()
        elif lit2 == i or lit2 == -i:
            cr.set_source_rgb(0.25, 0, 0)
            cr.rectangle(cx - cw / 2 - w / 2 + i * (cw + cw / 2) - cw / 16,
                         cy - ch / 2 - cw / 16,
                         cw + cw / 8, ch + cw / 8)
            cr.fill()

            cr.set_source_rgb(0.5, 0, 0)
            cr.rectangle(cx - cw / 2 - w / 2 + i * (cw + cw / 2),
                         cy - ch / 2,
                         cw, ch)
            cr.fill()
        else:
            cr.set_source_rgb(0.2, 0, 0)
            cr.rectangle(cx - cw / 2 - w / 2 + i * (cw + cw / 2),
                         cy - ch / 2,
                         cw, ch)
            cr.fill()


if __name__ == "__main__":
    applet = Applet()
    applet.set_title("Knight Rider")
    applet.run_animation(draw, 1000 / 16)


# EOF #
