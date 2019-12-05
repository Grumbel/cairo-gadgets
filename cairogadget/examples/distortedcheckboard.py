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

from cairogadget import Applet


def draw(ctx):
    cr = ctx.cr

    # square size
    cw = 32
    ch = 32

    # small square size
    scw = cw / 6
    sch = ch / 6

    xn = int(math.ceil(ctx.width / cw))
    yn = int(math.ceil(ctx.height / ch))

    for y in range(0, yn):
        for x in range(0, xn):
            cr.rectangle(x * cw, y * ch, cw, ch)

            if (x + y) % 2 == 0:
                cr.set_source_rgb(1, 1, 1)
            else:
                cr.set_source_rgb(0, 0.5, 0)
            cr.fill()

    for y in range(0, yn):
        for x in range(0, xn):
            p1x = x * cw + scw * 0.25
            p1y = y * ch + sch * 0.25

            p2x = x * cw + cw - scw * 1.25
            p2y = y * ch + ch - sch * 1.25

            if ctx.random.randint(0, 1):
                cr.rectangle(p1x, p1y, scw, sch)
                cr.rectangle(p2x, p2y, scw, sch)
                # cr.rectangle(p1x, p2y, scw, sch)
                # cr.rectangle(p2x, p1y, scw, sch)
            else:
                cr.rectangle(p2x, p1y, scw, sch)
                cr.rectangle(p1x, p2y, scw, sch)
                # cr.rectangle(p2x, p2y, scw, sch)
                # cr.rectangle(p1x, p1y, scw, sch)

            if (x + y) % 2 == 0:
                cr.set_source_rgb(0, 0.5, 0)
            else:
                cr.set_source_rgb(1, 1, 1)
            cr.fill()


if __name__ == "__main__":
    applet = Applet()
    applet.set_size(512, 512)
    applet.run(draw)


# EOF #
