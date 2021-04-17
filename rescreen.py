# results screen
import pygame
import re
import os
from pygame.locals import *


def rescreen(screen_width, screen_height, timeings, score, percent):
    def size(x):
        font = pygame.font.SysFont("DelaGothicOne-Regular.ttf", x)
        return font

    pygame.init()
    scores = ["F", "D", "C", "B", "A", "S", "SS"]
    colors = [
        (255, 0, 0),
        (100, 100, 100),
        (100, 100, 150),
        (100, 150, 100),
        (0, 255.0),
        (255, 255, 0),
        (255, 255, 255),
    ]
    screen = pygame.display.set_mode([screen_width, screen_height])
    running = True
    start = 1
    clock = pygame.time.Clock()
    timings = timeings
    scored = score
    i = 0
    if percent > 99:
        per = 6
    elif percent > 95:
        per = 5
    elif percent > 90:
        per = 4
    elif percent > 80:
        per = 3
    elif percent > 70:
        per = 2
    elif percent > 60:
        per = 1
    else:
        percent = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:

                    running = False
        screen.fill((0, 0, 0))
        clock.tick(60)
        s = size(start).render(scores[per], False, colors[per])
        text_rect = s.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(s, text_rect)
        if start < screen_height / 2:
            start = int(start * 1.3) + 1
        else:
            te = size(40).render(str(percent)[:5] + " %", False, (255, 255, 255))
            tere = te.get_rect(center=(screen_width / 2, 20))
            screen.blit(te, tere)
            pygame.draw.rect(
                screen,
                (100, 100, 100),
                pygame.Rect(
                    10,
                    2 * (screen_height / 3),
                    screen_width - 20,
                    (screen_height / 3) - 10,
                ),
            )
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (10, (2.5 * (screen_height / 3)) - 10),
                (screen_width - 10, (2.5 * (screen_height / 3)) - 10),
            )
            for a in [-22, 22, 45, -45, -90, 90, -135, 135, 180, -180]:
                y = ((2.5 * (screen_height / 3)) - 10) + (
                    (((screen_height / 3) - 10) / 400) * a
                )
                pygame.draw.line(
                    screen, (255, 255, 255), (10, y), (screen_width - 10, y), width=2
                )
            i2 = 0
            for a in timings[:i]:

                if scored[i2] < 2:
                    x = 10 + ((screen_width - 20) / len(scored)) * i2
                    pygame.draw.rect(
                        screen,
                        (255, 0, 0),
                        pygame.Rect(
                            x, 2 * (screen_height / 3), 2, (screen_height / 3) - 10
                        ),
                    )
                else:

                    x = 10 + ((screen_width - 20) / len(scored)) * i2
                    y = ((2.5 * (screen_height / 3)) - 10) + (
                        (((screen_height / 3) - 10) / 400) * a
                    )
                    pygame.draw.circle(screen, (50, 50, 150), (x, y), 2)
                i2 += 1
            if i < len(scored):
                i += 1
        pygame.display.flip()


rescreen(800, 600, [0, 0, 0], [0, 0, 0, 0], 80)
