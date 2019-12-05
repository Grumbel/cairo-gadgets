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


def draw(ctx):
    cr = ctx.cr
    cr.move_to(ctx.width / 2, ctx.height / 2)
    cr.show_text("Hello World")


if __name__ == "__main__":
    applet = Applet()
    applet.set_size(854, 480)
    applet.set_title("Tunnel")
    applet.run(draw)


# EOF #
