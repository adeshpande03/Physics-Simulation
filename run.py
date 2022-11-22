import pygame
import math
import pymunk
import CSolid


def run(length=960, width=594, fps=60, color=(0, 0, 0)):
    pygame.init()
    win = pygame.display.set_mode((length, width))
    win.fill(color)
    running = True
    clock = pygame.time.Clock()

    while running:
        for instance in pygame.event.get():
            if instance.type == pygame.QUIT:
                running = False
                break
        pygame.display.update()
        clock.tick(fps)
