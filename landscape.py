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

from applet import Applet


def midpoint(lst):
    x = 0.0
    y = 0.0
    for el in lst:
        x += el[0]
        y += el[1]
    return (x / len(lst), y / len(lst))


def gen_segments(a, b, depth, midfunc):
    def loop(a, b, r):
        if r == 0:
            return [a]
        else:
            m = midfunc(a, b, depth - r)
            return loop(a, m, r - 1) + loop(m, b, r - 1)

    return loop(a, b, depth) + [b]


class Landscape:

    def draw(self, ctx):
        cr = ctx.cr

        # Fill the background with gray
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.rectangle(0, 0, ctx.width, ctx.height)
        cr.fill()

        for i in range(0, 500):
            gray = ctx.random.random()
            cr.set_source_rgb(gray, gray, gray)
            cr.arc(ctx.width * ctx.random.random() + 0.5,
                   ctx.height * ctx.random.random() + 0.5,
                   0.1, 0.0, 2 * math.pi)
            cr.stroke()

        c = [ctx.random.random(),
             ctx.random.random(),
             ctx.random.random()]

        xof = (ctx.random.random() - 0.5) * 2.0
        yof = (ctx.random.random() - 0.5) * 2.0

        for i in range(0, ctx.random.randint(1, 2)):
            x = ctx.random.randint(0, ctx.width)
            y = ctx.random.randint(0, ctx.height // 2)
            radius = ctx.random.randint(5, 72)

            self.draw_moon(ctx, x, y, radius, xof * radius, yof * radius,
                           [c[0] * (1.0 - ctx.random.random() / 10.0),
                            c[1] * (1.0 - ctx.random.random() / 10.0),
                            c[2] * (1.0 - ctx.random.random() / 10.0)])

        y = ctx.height / 2.0 * 1.5
        n = 64

        for i in range(0, n):
            cr.set_source_rgb(((i + 1) / float(n) * c[0]) ** 2.2,
                              ((i + 1) / float(n) * c[1]) ** 2.2,
                              ((i + 1) / float(n) * c[2]) ** 2.2)
            self.draw_mountain(ctx, y + 2 ** (7.0 * (float(i) / (n - 1))))

    def draw_moon(self, ctx, x, y, radius, xof, yof, c):
        cr = ctx.cr

        cr.set_source_rgb(c[0], c[1], c[2])
        cr.arc(x, y, radius * 1.1, 0.0, 2 * math.pi)
        cr.fill()

        cr.set_source_rgb(c[0] * 2.0, c[1] * 2.0, c[2] * 2.0)
        cr.arc(x, y, radius, 0.0, 2 * math.pi)
        cr.fill()

        cr.save()
        cr.arc(x, y, radius * 1.2, 0.0, 2 * math.pi)
        cr.clip()

        cr.new_path()
        cr.set_source_rgb(0, 0, 0)
        cr.arc(x + xof,
               y + yof,
               radius * 1.5, 0.0, 2 * math.pi)
        cr.fill()
        # cr.reset_clip()
        cr.restore()

    def draw_mountain(self, ctx, y):
        cr = ctx.cr

        points = gen_segments(y + (ctx.random.random() - 0.5) * 128.0,
                              y + (ctx.random.random() - 0.5) * 128.0,
                              8,
                              lambda a, b, d: (a + b) / 2.0 + (ctx.random.random() - 0.5) * (ctx.height / 3.0) / 2 ** d)

        cr.move_to(0, ctx.height)
        for idx, p in enumerate(points):
            cr.line_to(ctx.width / float(len(points) - 1) * idx, p)
        cr.line_to(ctx.width, ctx.height)
        cr.fill()


if __name__ == "__main__":
    applet = Applet()
    applet.set_size(640, 480)
    applet.run(Landscape().draw)


# EOF #
