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


def midp(ctx, p1, p2):
    a = ctx.random.random() * 0.33 + 0.33
    return (a * p1[0] + (1 - a) * p2[0],
            a * p1[1] + (1 - a) * p2[1])


class SpacePartition:

    def draw(self, ctx):
        cr = ctx.cr

        cr.set_line_width(0.5)
        self.draw_triangle(ctx, cr,
                           (ctx.width / 2, 0),
                           (ctx.width, ctx.height),
                           (0, ctx.height))
        cr.stroke()

    def draw_triangle(self, ctx, cr, p1, p2, p3, depth=0):
        cr.move_to(p1[0], p1[1])
        cr.line_to(p2[0], p2[1])
        cr.line_to(p3[0], p3[1])
        cr.close_path()

        if depth < 6:
            np1 = midp(ctx, p1, p2)
            np2 = midp(ctx, p2, p3)
            np3 = midp(ctx, p3, p1)

            self.draw_triangle(ctx, cr, p1, np1, np3, depth + 1)
            self.draw_triangle(ctx, cr, np1, p2, np2, depth + 1)
            self.draw_triangle(ctx, cr, np3, np2, p3, depth + 1)
            self.draw_triangle(ctx, cr, np1, np2, np3, depth + 1)


if __name__ == "__main__":
    applet = Applet()
    applet.set_size(512, 512)
    applet.run(SpacePartition().draw)


# EOF #
