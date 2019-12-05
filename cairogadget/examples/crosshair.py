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


from cairogadget import Applet


class Crosshair:

    def __init__(self):
        pass

    def draw(self, ctx):
        cr = ctx.cr

        # fill background
        cr.set_source_rgb(0, 0, 0)
        cr.paint()

        r = 16

        cr.set_source_rgb(1, 1, 1)
        cr.move_to(ctx.mouse_x, 0)
        cr.line_to(ctx.mouse_x, ctx.mouse_y - r)
        cr.move_to(ctx.mouse_x, ctx.mouse_y + r)
        cr.line_to(ctx.mouse_x, ctx.height)

        cr.move_to(0, ctx.mouse_y)
        cr.line_to(ctx.mouse_x - r, ctx.mouse_y)
        cr.move_to(ctx.mouse_x + r, ctx.mouse_y)
        cr.line_to(ctx.width, ctx.mouse_y)

        cr.rectangle(ctx.mouse_x - r, ctx.mouse_y - r, 2 * r, 2 * r)

        cr.stroke()


def main():
    applet = Applet()
    applet.set_title("Crosshair")
    applet.run_animation(Crosshair().draw, 1000 / 60)


if __name__ == "__main__":
    main()


# EOF #
