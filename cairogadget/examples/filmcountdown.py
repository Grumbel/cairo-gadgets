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


import cairo
import math

from cairogadget import Applet


def film_countdown(context, second, frame, frames):
    cr = context.cr

    # background fill
    cr.set_source_rgb(0.5, 0.5, 0.5)
    cr.paint()

    # progress
    progress = (frame + 1) / frames
    radius = context.width
    cr.move_to(context.width / 2, context.height / 2)
    cr.arc(context.width / 2, context.height / 2, radius,
           0 - math.pi / 2, 2 * math.pi * progress - math.pi / 2)
    cr.close_path()

    cr.set_source_rgb(0.4, 0.4, 0.4)
    cr.fill_preserve()

    cr.set_source_rgb(0.25, 0.25, 0.25)
    cr.stroke()

    # background cross
    cr.move_to(context.width / 2, 0)
    cr.line_to(context.width / 2, context.height)
    cr.move_to(0, context.height / 2)
    cr.line_to(context.width, context.height / 2)

    cr.set_source_rgb(0.25, 0.25, 0.25)
    cr.set_line_width(6.0)
    cr.stroke()

    # two white circles
    radius = context.height / 2 * 0.9
    cr.arc(context.width / 2, context.height / 2, radius,
           0, 2 * math.pi)
    cr.new_sub_path()
    cr.arc(context.width / 2, context.height / 2, radius * 0.8,
           0, 2 * math.pi)

    cr.set_source_rgb(1, 1, 1)
    cr.set_line_width(6.0)
    cr.stroke()

    # progress
    cr.set_source_rgb(0, 0, 0)

    cr.select_font_face("Ubuntu",
                        cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(context.height * 0.8)
    center_text = "%d" % second
    fascent, fdescent, fheight, _fxadvance, fyadvance = cr.font_extents()
    x_bearing, y_bearing, text_width, text_height, x_advance, y_advance = cr.text_extents(center_text)
    cr.move_to(context.width / 2 - x_advance / 2,
               context.height / 2 - fdescent + fheight / 2 - 12)
    cr.show_text(center_text)

    cr.set_font_size(context.height * 0.1)
    frameno_text = "%02d/%02d" % (frame + 1, frames)
    x_bearing, y_bearing, text_width, text_height, x_advance, y_advance = cr.text_extents(frameno_text)
    cr.move_to(context.width - x_advance - 8,
               context.height - 8)
    cr.show_text(frameno_text)


def on_draw(ctx):
    total_frames = int(ctx.time / (1000 / 24))

    second = total_frames / 24
    frame = total_frames % 24

    film_countdown(ctx, second, frame, 24)


def main():
    applet = Applet()
    applet.set_size(854, 480)
    applet.set_title("Film Countdown")
    applet.run_animation(on_draw, 1000 / 24)


if __name__ == "__main__":
    main()


# EOF #
