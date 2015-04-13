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


from applet import Applet


def draw(canvas):
    cr = canvas.cr

    n = 16
    cw = canvas.width / n
    ch = canvas.height / n

    for y in range(0, n):
        for x in range(0, n):
            cr.rectangle(x * cw, y * ch, cw, ch)

            if (x + y) % 2 == 0:
                cr.set_source_rgb(1, 1, 1)
            else:
                cr.set_source_rgb(0, 0.5, 0)
            cr.fill()

    scw = cw / 6
    sch = ch / 6

    for y in range(0, n):
        for x in range(0, n):
            p1x = x * cw + scw * 0.25
            p1y = y * ch + sch * 0.25

            p2x = x * cw + cw - scw * 1.25
            p2y = y * ch + ch - sch * 1.25

            if x % 2 == 0:
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
