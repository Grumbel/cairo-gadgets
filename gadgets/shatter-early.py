#! /usr/bin/env python3

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


def midpoint(lst):
    x = 0.0
    y = 0.0
    for el in lst:
        x += el[0]
        y += el[1]
    return (x / len(lst), y / len(lst))


def draw(ctx):
    cr = ctx.cr
    width = ctx.width
    height = ctx.height

    # Fill the background with gray
    cr.set_source_rgb(0.0, 0.0, 0.0)
    cr.rectangle(0, 0, width, height)
    cr.fill()

    cr.set_source_rgba(1.0, 1.0, 1.0, 0.5)

    draw_line(ctx, cr,
              (10, height / 2.0),
              (width - 10, height / 2.0),
              10)

    draw_line(ctx, cr,
              (10, height / 2.0),
              (width - 10, height / 2.0),
              10)
    cr.stroke()


def draw_line(ctx, cr, a, b, r):
    if r == 0:
        cr.move_to(a[0], a[1])
        cr.line_to(b[0], b[1])
    else:
        m = midpoint([a, b])
        m = (m[0], m[1] + (ctx.random.random() * 2.0 - 1.0) * (2.0 ** r) * 0.1)
        draw_line(ctx, cr, a, m, r - 1)
        draw_line(ctx, cr, m, b, r - 1)


if __name__ == "__main__":
    applet = Applet()
    applet.set_size(256, 256)
    applet.run(draw)


# EOF #
