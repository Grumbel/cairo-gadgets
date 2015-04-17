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
import cairo


def draw(ctx):
    width = ctx.width
    height = ctx.height
    text = "Hello World"

    cr = ctx.cr

    # draw background
    cr.set_source_rgb(0.4, 0.4, 0.4)
    cr.rectangle(0, 0, width, height)
    cr.fill()

    # draw checkboard pattern
    cr.set_source_rgb(0.6, 0.6, 0.6)
    for y in range(0, 8):
        for x in range(0 + y%2, 8, 2):
            cr.rectangle(x * width/8, y * height/8, width/8, height/8)
            cr.fill()

    cr.set_source_rgba(1.0, 0.0, 0.0, 0.5)
    cr.arc(width/2, height/2, height * 0.4, 0, 2*math.pi)
    cr.fill()

    cr.set_source_rgb(1.0, 1.0, 0.0)
    cr.arc(width/2, height/2, height * 0.3, 0, 2*math.pi)
    cr.fill()

    cr.set_source_rgb(0.0, 1.0, 1.0)
    cr.arc(width/2, height/2, height * 0.15, 0, 2*math.pi)
    cr.fill()

    # outer circle
    cr.set_source_rgb(0.0, 0.0, 0.0)
    cr.arc(0, 0, 24, 0, 2*math.pi)
    cr.stroke()

    cr.arc(width, 0, 24, 0, 2*math.pi)
    cr.stroke()

    cr.arc(width, height, 24, 0, 2*math.pi)
    cr.stroke()

    cr.arc(0, height, 24, 0, 2*math.pi)
    cr.stroke()

    # inner circle
    cr.arc(0, 0, 12, 0, 2*math.pi)
    cr.fill()

    cr.arc(width, 0, 12, 0, 2*math.pi)
    cr.fill()

    cr.arc(width, height, 12, 0, 2*math.pi)
    cr.fill()

    cr.arc(0, height, 12, 0, 2*math.pi)
    cr.fill()

    cr.set_source_rgb(0.0, 0.0, 0.0)
    cr.select_font_face("Ubuntu", cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(24)
    cr.move_to(32, height - 12)
    cr.show_text(text)


if __name__ == "__main__":
    from applet import Applet
    applet = Applet()
    applet.run(draw)


# EOF #
