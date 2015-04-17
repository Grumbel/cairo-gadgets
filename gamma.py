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


import math
import cairo
from applet import Applet


class Rect:

    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    @property
    def right(self):
        return self.left + self.width

    @property
    def bottom(self):
        return self.top + self.height

    @property
    def centerx(self):
        return self.left + self.width / 2

    @property
    def centery(self):
        return self.top + self.height / 2

    def __iter__(self):
        return iter([self.left, self.top, self.width, self.height])


class Color:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __iter__(self):
        return iter([self.r, self.g, self.b])


g_current_screen = 0


def draw(ctx):
    global g_current_screen
    cr = ctx.cr

    # enable pixel perfect drawing
    cr.set_antialias(cairo.ANTIALIAS_NONE)
    cr.translate(0.5, 0.5)
    cr.set_line_width(1)

    # draw random test screen
    screens = [
        draw_test_screens,
        draw_test_screens2,
        draw_fs_gamma_ramp,
        draw_fs_red,
        draw_fs_green,
        draw_fs_blue,
        draw_fs_white,
        draw_fs_ramp,
        draw_fs_circle
        ]
    screens[g_current_screen](ctx)
    g_current_screen = (g_current_screen + 1) % len(screens)


def draw_test_screens(ctx):
    draw_grid(
        ctx,
        Color(0, 0, 0),
        Color(1, 1, 1),
        Rect(10, 10, 256, 256))

    draw_grid_pattern(
        ctx,
        Color(0, 0, 0),
        Color(1, 1, 1),
        Rect(300, 10, 256, 256))

    draw_gamma_ramp(
        ctx,
        Color(0, 0, 0),
        Color(1, 0, 1),
        Rect(600, 10, 256, 256))

    draw_ramp(
        ctx,
        Color(1, 0, 1),
        Rect(10, 300, 256, 256),
        16)


def draw_test_screens2(ctx):
    draw_test(ctx,
              Color(1, 0, 0),
              Color(0, 0, 0),
              Color(186, 0, 0),
              Rect(100, 100, 400, 300))

    draw_test(ctx,
              Color(0, 1, 0),
              Color(0, 0, 0),
              Color(0, 186, 0),
              Rect(600, 100, 400, 300))

    draw_test(ctx,
              Color(0, 0, 1),
              Color(0, 0, 0),
              Color(0, 0, 186),
              Rect(100, 500, 400, 300))

    draw_test(ctx,
              Color(1, 1, 1),
              Color(0, 0, 0),
              Color(186, 186, 186),
              Rect(600, 500, 400, 300))

    draw_ramp(ctx,
              Color(1, 1, 1),
              Rect(100, 750, 800, 40),
              10)

    draw_ramp(ctx,
              Color(1, 0, 0),
              Rect(100, 800, 800, 40),
              10)

    draw_ramp(ctx,
              Color(0, 1, 0),
              Rect(100, 850, 800, 40),
              10)

    draw_ramp(ctx,
              Color(0, 0, 1),
              Rect(100, 900, 800, 40),
              10)


def draw_grid(ctx, bg, fg, rect):
    cr = ctx.cr

    cr.set_source_rgb(*bg)
    cr.rectangle(*rect)
    cr.fill()

    cr.set_source_rgb(*fg)
    for x in range(rect.left, rect.right, 2):
        h = min(rect.right - x, rect.height)
        cr.move_to(x, rect.top)
        cr.line_to(x + h, rect.top + h)

    for y in range(rect.top + 2, rect.bottom, 2):
        w = min(rect.bottom - y, rect.width)
        cr.move_to(rect.left, y)
        cr.line_to(rect.left + w, y + w)
    cr.stroke()


def draw_grid_pattern(ctx, bg, fg, rect, tw=32, th=32):
    cr = ctx.cr

    for y in range(0, rect.height, tw):
        for x in range(0, rect.width, th):
            if (x // tw + y // th) % 2 == 0:
                cr.set_source_rgb(*bg)
                cr.rectangle(rect.left + x, rect.top + y, tw, th)
                cr.fill()
            else:
                cr.set_source_rgb(*fg)
                cr.rectangle(rect.left + x, rect.top + y, tw, th)
                cr.fill()


def draw_gamma_ramp(ctx, bg, fg, rect, tw=16):
    cr = ctx.cr

    cr.set_source_rgb(*bg)
    for y in range(0, rect.height, 2):
        cr.move_to(rect.left, y)
        cr.line_to(rect.right, y)
    cr.stroke()

    cr.set_source_rgb(*fg)
    for y in range(0, rect.height, 2):
        cr.move_to(rect.left, y + 1)
        cr.line_to(rect.right, y + 1)
    cr.stroke()

    for y in range(0, rect.height):
        p = float(y) / (rect.height - 1)
        gamma = 1.0 / (2.2 - 0.5 + p)
        cr.set_source_rgb((fg.r * 0.5) ** gamma,
                          (fg.g * 0.5) ** gamma,
                          (fg.b * 0.5) ** gamma)
        cr.move_to(rect.centerx - tw, y)
        cr.line_to(rect.centerx + tw, y)
        cr.stroke()


def draw_test(ctx, bg, fg, c, rect):
    cr = ctx.cr
    draw_grid(ctx, bg, fg, rect)

    cr.set_source_rgb(*c)
    cr.rectangle(rect.left, rect.centery - 16,
                 rect.width, 32)
    cr.fill()

    cr.set_source_rgb(*c)
    cr.rectangle(rect.centerx - 16,
                 rect.top,
                 32, rect.height)
    cr.fill()


def draw_ramp(ctx, color, rect, steps):
    cr = ctx.cr

    w = rect.width / steps

    for p in range(0, steps):
        cr.set_source_rgb(p * color.r / (steps - 1),
                          p * color.g / (steps - 1),
                          p * color.b / (steps - 1))
        cr.rectangle(rect.left + p * w,
                     rect.top,
                     w,
                     rect.height)
        cr.fill()

    cr.set_source_rgb(0.5, 0.5, 0.5)
    cr.rectangle(*rect)
    cr.stroke()


def get_screen_rect(ctx):
    return Rect(0, 0, ctx.width, ctx.height)


def draw_fs_red(ctx):
    draw_test(ctx,
              Color(1, 0, 0),
              Color(0, 0, 0),
              Color(186 / 255, 0, 0),
              get_screen_rect(ctx))


def draw_fs_green(ctx):
    draw_test(ctx,
              Color(0, 1, 0),
              Color(0, 0, 0),
              Color(0, 186 / 255, 0),
              get_screen_rect(ctx))


def draw_fs_blue(ctx):
    draw_test(ctx,
              Color(0, 0, 1),
              Color(0, 0, 0),
              Color(0, 0, 186 / 255),
              get_screen_rect(ctx))


def draw_fs_white(ctx):
    draw_test(ctx,
              Color(1, 1, 1),
              Color(0, 0, 0),
              Color(186 / 255, 186 / 255, 186 / 255),
              get_screen_rect(ctx))


def draw_fs_ramp(ctx):
    draw_ramp(ctx,
              Color(1, 1, 1),
              Rect(100, 750, 800, 40),
              10)

    draw_ramp(ctx,
              Color(1, 0, 0),
              Rect(100, 800, 800, 40),
              10)

    draw_ramp(ctx,
              Color(0, 1, 0),
              Rect(100, 850, 800, 40),
              10)

    draw_ramp(ctx,
              Color(0, 0, 1),
              Rect(100, 900, 800, 40),
              10)


def draw_fs_circle(ctx):
    cr = ctx.cr

    rect = get_screen_rect(ctx)
    draw_grid_pattern(ctx, Color(112 / 255, 112 / 255, 112 / 255), Color(144 / 255, 144 / 255, 144 / 255), rect)
    flip = True
    for r in range(min(rect.width, rect.height) // 2, 0, -32):
        cr.arc(rect.centerx, rect.centery, r, 0, 2 * math.pi)
        if flip:
            cr.set_source_rgb(0, 0, 0)
            cr.fill()
        else:
            cr.set_source_rgb(1, 1, 1)
            cr.fill()
        flip = not flip


def draw_fs_gamma_ramp(ctx):
    rect = get_screen_rect(ctx)
    cr = ctx.cr

    cr.set_source_rgb(0, 0, 0)
    cr.paint()

    params = [(100, Color(0, 0, 0), Color(1, 1, 1)),
              (350, Color(0, 0, 0), Color(1, 0, 0)),
              (600, Color(0, 0, 0), Color(0, 1, 0)),
              (850, Color(0, 0, 0), Color(0, 0, 1))]

    for x, bg, fg in params:
        draw_gamma_ramp(ctx,
                        bg, fg,
                        Rect(x, rect.top, 200, rect.width))


if __name__ == "__main__":
    applet = Applet()
    applet.set_size(1280, 960)
    applet.run(draw)


# EOF #
