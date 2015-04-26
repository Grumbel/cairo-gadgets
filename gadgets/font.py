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


import math
import cairo

from applet import Applet


def draw(context):
    cr = context.cr

    text = "Wegzy!ö"

    cr.select_font_face("Ubuntu",
                        cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(context.height * 0.2)

    fascent, fdescent, fheight, fxadvance, fyadvance = cr.font_extents()
    x_bearing, y_bearing, text_width, text_height, x_advance, y_advance = cr.text_extents(text)

    print("Font Porperties:")
    print("  fascent: ", fascent)
    print("  fdescent: ", fdescent)
    print("  fheight: ", fheight)
    print("  fxadvance: ", fxadvance)
    print("  fyadvance: ", fyadvance)
    print()
    print("Text Porperties:")
    print("  text: \"%s\"" % text)
    print("  bearing: ", x_bearing, y_bearing)
    print("  size: %dx%d" % (text_width, text_height))
    print("  advance: ", x_advance, y_advance)
    print()

    # Fill the background with gray
    cr.set_source_rgb(1, 1, 1)
    cr.rectangle(0, 0, context.width, context.height)
    cr.fill()

    x = context.width / 2 - text_width / 2
    y = context.height / 2

    cr.set_source_rgb(0, 0, 0)
    cr.move_to(x, y)
    cr.show_text(text)

    cr.set_line_width(1)

    cr.set_source_rgba(0.5, 0, 0, 0.25)
    cr.rectangle(x, y - fascent, 24, fheight)
    cr.fill()

    cr.set_source_rgba(0, 0, 1, 0.25)
    cr.rectangle(x + x_bearing, y - fascent, text_width, fascent)
    cr.fill()

    cr.set_source_rgba(1, 0, 0, 0.25)
    cr.rectangle(x + x_bearing, y, text_width, fdescent)
    cr.fill()

    cr.set_source_rgb(1, 0, 0)
    cr.rectangle(x + x_bearing, y + y_bearing, text_width, text_height)
    cr.stroke()

    # bearing
    cr.set_source_rgb(1, 0, 0)
    cr.arc(x + x_bearing, y + y_bearing, 3, 0, 2 * math.pi)
    cr.fill()

    # origin
    cr.set_source_rgb(0, 1, 1)
    cr.arc(x, y, 3, 0, 2 * math.pi)
    cr.fill()

    # advance
    cr.set_source_rgb(0, 0, 1)
    cr.arc(x + x_advance, y + y_advance, 3, 0, 2 * math.pi)
    cr.fill()


if __name__ == "__main__":
    applet = Applet()
    applet.set_size(640, 480)
    applet.run(draw)


# EOF #
