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
from applet import Applet


def draw_eye(ctx, x, y):
    cr = ctx.cr
    cr.save()
    cr.translate(x, y)

    r = 0.9

    sx = ctx.width / 4
    sy = ctx.height / 2

    cr.scale(sx, sy)

    cr.arc(0, 0, r, 0, 2 * math.pi)
    cr.set_source_rgb(0, 0, 0)
    cr.fill()

    cr.arc(0, 0, r * 0.8, 0, 2 * math.pi)
    cr.set_source_rgb(1, 1, 1)
    cr.fill()

    ebx = (ctx.mouse_x - x) / sx
    eby = (ctx.mouse_y - y) / sy

    ebr = r * 0.6
    d = math.sqrt(ebx**2 + eby**2)
    if d > ebr:
        ebx = ebx / d * ebr
        eby = eby / d * ebr

    cr.arc(ebx, eby, r * 0.25, 0, 2 * math.pi)
    cr.set_source_rgb(0, 0, 0)
    cr.fill()

    cr.restore()


def draw(ctx):
    draw_eye(ctx, ctx.width/2 - ctx.width/4, ctx.height/2)
    draw_eye(ctx, ctx.width/2 + ctx.width/4, ctx.height/2)


if __name__ == "__main__":
    applet = Applet()
    applet.set_title("XEyes")
    applet.set_size(256, 256)
    applet.run_animation(draw, 1000 / 30)


# EOF #
