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


def draw(ctx):
    cr = ctx.cr
    cx = ctx.width / 2
    cy = ctx.height / 2

    rps = 1

    r = min(ctx.width, ctx.height) / 2 * 0.9

    cr.save()
    cr.translate(cx, cy)
    cr.rotate(ctx.time / 1000.0 * 2 * math.pi * rps)

    cr.set_source_rgb(0, 0, 0)
    cr.arc(0, 0, r, 0, 2 * math.pi)
    cr.fill()

    segments = [
        ("800", (0, 0, 1)),
        ("200", (0, 1, 0)),
        ("Joker", (0, 1, 1)),
        ("750", (1, 0, 0)),
        ("500", (1, 0, 1)),
        ("1000", (1, 1, 0)),
        ("Bonus", (1, 1, 1)),
        ("Bonus", (1, 0, 1)),
        ("500", (1, 0, 1)),
        ("1000", (0, 0, 1)),
        ("15000", (1, 0, 0)),
        ("250", (0, 1, 1)),
        ("300", (0, 1, 0)),
        ("10", (1, 0, 1)),
        ("600", (0, 1, 1))
    ]

    fascent, fdescent, fheight, fxadvance, fyadvance = cr.font_extents()

    cr.set_font_size(r * 0.1)
    cr.set_line_width(1)
    for i, (text, color) in enumerate(segments):
        cr.save()
        cr.rotate(i / len(segments) * 2 * math.pi)

        cr.new_path()
        cr.arc_negative(0, 0, r * 0.25,
                        math.pi / len(segments) * 0.75,
                        -math.pi / len(segments) * 0.75)
        cr.arc(0, 0, r * 0.98,
               -math.pi / len(segments) * 0.9,
               math.pi / len(segments) * 0.9)
        cr.close_path()
        cr.set_source_rgb(*color)
        cr.fill()

        cr.set_source_rgb(0, 0, 0)
        cr.move_to(r * 0.6, fheight / 2)
        cr.show_text(text)
        cr.restore()

    cr.restore()


def main():
    applet = Applet()
    applet.set_title("Wheel of Fortune")
    applet.run_animation(draw, 1000 / 60)


if __name__ == "__main__":
    main()


# EOF #
