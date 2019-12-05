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


class ShapedGUI:

    def draw(self, ctx):
        cr = ctx.cr
        width = ctx.width
        height = ctx.height

        # Fill the background with gray
        cr.set_source_rgb(0, 0, 0)
        cr.paint()

        cr.set_source_rgb(1.0, 1.0, 1.0)

        time = ctx.time
        time *= 0.5

        start = 0
        end = math.pi * time / 1000.0

        cx, cy = width / 2, height / 2

        for r in range(40, 180, 20):
            cr.save()
            cr.translate(cx, cy)
            cr.rotate(0.000035 * time * r)
            # cr.rotate(0.02 + r)
            cr.translate(-cx, -cy)

            cr.arc(width / 2, height / 2, r + 15, start, end)
            cr.arc_negative(width / 2, height / 2, r, end, start)
            cr.close_path()
            cr.fill()
            cr.restore()

        cr.move_to(20, height - 20)
        cr.select_font_face("Deja Vu")
        cr.set_font_size(32.0)

        count = int(time / 100.0)
        if count % 4 == 0:
            cr.show_text("Loading")
        elif count % 4 == 1:
            cr.show_text("Loading.")
        elif count % 4 == 2:
            cr.show_text("Loading..")
        else:
            cr.show_text("Loading...")


if __name__ == "__main__":
    applet = Applet()
    applet.set_size(854, 480)
    applet.set_title("Loading Screen")
    applet.run_animation(ShapedGUI().draw, 1000 / 60)


# EOF #
