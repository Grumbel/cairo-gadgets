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


import random

from applet import Applet


def midp(p1, p2):
    a = random.random() * 0.33 + 0.33
    return (a * p1[0] + (1 - a) * p2[0],
            a * p1[1] + (1 - a) * p2[1])


class Labyrinth:

    def draw(self, canvas):
        cr = canvas.cr

        self.draw_room(cr,
                       0, 0,
                       canvas.width, canvas.height)
        cr.stroke()

    def draw_room(self, cr, x, y, w, h, depth=0):
        i = random.randint(0, 3)
        if i == 0:
            cr.move_to(x, y + h/2)
        elif i == 1:
            cr.move_to(x + w, y + h/2)
        elif i == 2:
            cr.move_to(x + w/2, y)
        elif i == 3:
            cr.move_to(x + w/2, y + h)

        cr.line_to(x + w/2, y + h/2)
        cr.close_path()

        if depth < 5:
            self.draw_room(cr, x, y, w/2, h/2, depth+1)
            self.draw_room(cr, x + w/2, y, w/2, h/2, depth+1)
            self.draw_room(cr, x, y + h/2, w/2, h/2, depth+1)
            self.draw_room(cr, x + w/2, y + h/2, w/2, h/2, depth+1)

if __name__ == "__main__":
    applet = Applet()
    applet.set_size(512, 512)
    applet.run(Labyrinth().draw)


# EOF #
