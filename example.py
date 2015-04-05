#!/usr/bin/env python

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


import pygame
from pygame.locals import QUIT, KEYDOWN
pygame.init()

fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))


class Effect:
    pass

radius = 10
frame = 0
while True:
    print fps_clock.get_rawtime()

    screen.fill(pygame.Color(0, 0, 0))
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), (400, 300), radius)

    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
        elif ev.type == KEYDOWN:
            pass
        else:
            pass

    radius += 1
    if radius > 400:
        radius = 10

    pygame.display.update()
    fps_clock.tick(60)
    frame += 1

# EOF #
