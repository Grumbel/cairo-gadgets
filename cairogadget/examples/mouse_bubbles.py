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


class Bubble:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 1


class MouseBubbles:

    def __init__(self):
        self.bubbles = []
        self.flip = 0

    def draw(self, ctx):
        cr = ctx.cr

        # fill background
        cr.set_source_rgb(0, 0, 0)
        cr.paint()

        if self.flip > 4:
            self.bubbles.append(Bubble(ctx.mouse_x, ctx.mouse_y))
            self.flip = 0
        else:
            self.flip += 1

        self.bubbles = [b for b in self.bubbles if b.r < 128]
        for bubble in self.bubbles:
            c = 1 - (bubble.r / 128.0)
            cr.set_source_rgb(c, c, c)
            cr.arc(bubble.x, bubble.y, bubble.r, 0, 2 * math.pi)
            cr.stroke()
            bubble.r += 1


def main():
    applet = Applet()
    applet.set_size(854, 480)
    applet.set_title("Loading Screen")
    applet.run_animation(MouseBubbles().draw, 1000 / 60)


if __name__ == "__main__":
    main()


# EOF #
