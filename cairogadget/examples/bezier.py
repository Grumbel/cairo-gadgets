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
import random

from cairogadget import Applet


def lerp(p1, p2, t):
    return ((1.0 - t) * p1[0] + t * p2[0],
            (1.0 - t) * p1[1] + t * p2[1])


def bezier(points, t, debug_fn=None):
    if debug_fn is not None:
        debug_fn(points)

    if len(points) == 1:
        return points[0]
    else:
        next_points = []
        for i in range(len(points) - 1):
            next_points.append(lerp(points[i], points[i+1], t))
        return bezier(next_points, t, debug_fn)


class Bezier:

    def __init__(self):
        self.t = 0
        self.setup_points()

    def setup_points(self):
        self.points = []
        for i in range(5):
                self.points.append((random.randint(0, 1280),
                                    random.randint(0, 720)))
        self.curve = []
        for i in range(250+1):
            self.curve.append(bezier(self.points, i/250.0))


    def draw(self, ctx):
        cr = ctx.cr

        cr.set_source_rgb(1, 1, 1)
        cr.paint()

        cr.set_line_width(4.0)

        self.t += ctx.dt / 5000.0

        if self.t > 1.0:
            self.t = 0.0
            self.setup_points()

        def draw(points):
            cr.move_to(points[0][0], points[0][1])
            for p in points[1:]:
                cr.line_to(p[0], p[1])
            cr.set_source_rgba(0.5, 0.5, 0.5, 0.25)
            cr.stroke()

        def draw_curve():
            cr.move_to(self.curve[0][0], self.curve[0][1])
            for p in self.curve[1:]:
                cr.line_to(p[0], p[1])
            cr.set_source_rgb(0.5, 0.0, 0.0)
            cr.stroke()

        p = bezier(self.points, self.t, draw)

        draw_curve()

        cr.set_source_rgb(0, 0, 0)
        cr.arc(p[0], p[1], 8, 0, 2 * math.pi)
        cr.fill()


def main():
    applet = Applet()
    applet.set_size(1280, 720)
    applet.set_title("Bezier")
    applet.run_animation(Bezier().draw, 1000 / 60)


if __name__ == "__main__":
    main()


# EOF #
