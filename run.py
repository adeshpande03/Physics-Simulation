import pygame
import math
import pymunk
import Rsolid


def run(length=960, width=594, fps=60, color=(0, 0, 0)):
    pygame.init()
    win = pygame.display.set_mode((length, width))
    win.fill(color)
    running = True
    clock = pygame.time.Clock()
    # x = 100
    # y = 50
    while running:
        for instance in pygame.event.get():
            if instance.type == pygame.QUIT:
                running = False
                break
        # x -= 1
        win.fill(color)
        # pygame.draw.rect(win, (0, 0, 128), (x, y, 16, 16))
        pygame.display.update()

        clock.tick(fps)
