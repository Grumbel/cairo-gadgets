#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()

fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

class Effect:
    pass

radius = 10
frame = 0
while True:
    print fps_clock.get_rawtime()

    screen.fill(pygame.Color(0,0,0))
    pygame.draw.circle(screen, pygame.Color(255,0,0), (400,300), radius)

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
