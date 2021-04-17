import time
import pygame
import re
import os
import math
from pygame.locals import *


def amtofkeys(filename):
    a = open(filename)
    temp = []
    hit = False
    for line in a.readlines():
        if hit:
            line = line.split(",")[:-1] + [line.split(",")[5].split(":")[0]]
            if int(line[0]) in temp:
                pass
            else:
                temp.append(int(line[0]))

        else:
            if "[HitObjects]" in line:
                hit = True
    return len(temp)


def get_song(amoky, finm):
    song = []
    hold = []
    file = open(finm, "r")
    hit = False
    for a in range(1, amoky + 2):
        song.append([])
        hold.append([])
    for line in file.readlines():
        if hit:
            line = line.split(",")[:-1] + [line.split(",")[5].split(":")[0]]

            if int(line[3]) == 128:
                hold[math.floor((int(line[0]) * amoky) / 512)].append(
                    [int(line[2]), int(line[5])]
                )
            else:
                song[math.floor((int(line[0]) * amoky) / 512)].append(int(line[2]))

        else:
            if "[HitObjects]" in line:
                hit = True
    for a in range(0, len(song)):
        song[a].append(999999999999999999)
        hold[a].append([999999999999999999, 999999999999999999])

    return song, hold


def music(fn):
    a = open(fn, "r")
    hit = False
    for line in a.readlines():
        if "AudioFilename" in line:
            return line.split(":")[1].strip()


def light(screen, p, k, l, y, r):
    count = 0
    for a in k:
        if p[a]:
            pygame.draw.circle(screen, (230, 230, 230), (l[count], y), r)
        else:
            pygame.draw.circle(screen, (230, 230, 230), (l[count], y), r, width=5)
        count += 1


def rungame(offset, scroll, scw, sch, finm, path, keys, s, colors):
    # files & song
    pygame.init()
    font = pygame.font.SysFont("DelaGothicOne-Regular.ttf", 48)
    judgetext = [
        font.render("EXCELLENT", True, (255, 255, 255)),
        font.render("PERFECT", True, (255, 255, 0)),
        font.render("GREAT", True, (0, 100, 0)),
        font.render("GOOD", True, (255, 0, 0)),
        font.render("MISS", True, (255, 0, 0)),
        font.render("", True, (255, 0, 0)),
    ]
    amoke = amtofkeys(path + finm)
    wid = scw
    hei = sch
    rad = 25
    judge = [22, 40, 90, 130, 180, 200]
    song, hold = get_song(amoke, path + finm)
    lanes = []
    juy = int(hei * (5 / 6))
    for a in range(1, amoke + 1):
        lanes.append(int((wid / 2) + ((a - ((amoke + 1) / 2)) * (2 * rad))))
    # colors!
    if amoke % 2 == 1:
        colors = (
            [colors[2]]
            + [colors[1] for x in range(0, int(((amoke - 1) / 2) - 1))]
            + [colors[0]]
            + [colors[1] for x in range(0, int(((amoke - 1) / 2) - 1))]
            + [colors[2]]
        )
    else:
        colors = (
            [colors[2]]
            + [colors[1] for x in range(0, int(((amoke) / 2) - 1))]
            + [colors[1] for x in range(0, int(((amoke) / 2) - 1))]
            + [colors[2]]
        )
        keys.pop(int((len(keys)-1)/2))
        print(keys)
    for count in range(0,int(((len(keys)-amoke))/2)):
        keys.pop(0)
        keys.pop(-1)
    print(keys)
    # pygame & music
    screen = pygame.display.set_mode((wid, hei))
    pygame.mixer.init()
    pygame.mixer.music.load(path + music(path + finm))
    # main loop and stuff and data
    scores = [[0, 0]]
    combo=0
    played = True
    running = True
    startime = (time.time() * 1000) + 3000
    while running:
        # fill
        screen.fill((255, 255, 255))
        lg = pygame.Surface(((lanes[-1] - lanes[1]) + (4 * rad), hei))
        lg.set_alpha(180)
        lg.fill((0, 0, 0))
        screen.blit(lg, ((wid - ((lanes[-1] - lanes[1]) + (4 * rad))) / 2, 0))
        # get current stuff
        elp = (time.time() * 1000) - startime
        pressed = pygame.key.get_pressed()
        # play music
        if played and elp > 0:
            played = False
            pygame.mixer.music.play()
            starttime=

        # scrolling
        for lane in range(0, amoke):
            for note in range(0, len(song[lane])):
                if song[lane][note] < elp + scroll:
                    y = juy - (((song[lane][note] - elp) / scroll) * juy)
                    x = lanes[lane]
                    pygame.draw.circle(screen, colors[lane], (x, y), rad)

            for note in range(0, len(hold[lane])):
                if hold[lane][note][0] < elp + scroll:
                    x = lanes[lane]
                    y = juy - (((hold[lane][note][0] - elp) / scroll) * juy)
                    y2 = juy - (((hold[lane][note][1] - elp) / scroll) * juy)
                    if y2 < 0:
                        y2 = 0
                    if (
                        pressed[keys[lane]]
                        and elp > hold[lane][note][0]
                        and elp < hold[lane][0][1] + 200
                    ):
                        size = juy - y2
                    else:
                        size = y - y2
                        pygame.draw.circle(screen, colors[lane], (x, y), rad)
                    if size < 0:
                        size = 0

                    pygame.draw.rect(
                        screen, colors[lane], pygame.Rect(x - rad, y2, 2 * rad, size)
                    )
                    pygame.draw.circle(screen, colors[lane], (x, y2), rad)
            if song[lane][0] < elp - 200:
                combo=0
                scores.append([5, 0])
                song[lane].pop(0)
            if hold[lane][0][1] < elp - 200:
                combo=0
                scores.append([5, 0])
                hold[lane].pop(0)
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                kys = event.key
                for key in range(0, amoke):
                    if (
                        kys == keys[key]
                        and elp > hold[key][0][0]
                        and elp < hold[key][0][1] - 200
                    ):
                        hold[key].pop(0)
                        combo=0
                    elif kys == keys[key] and elp > hold[key][0][0]:
                        for jud in range(0, len(judge)):
                            if elp - judge[jud] < hold[key][0][1] < elp + judge[jud]:
                                scores.append([jud, elp - hold[key][0][0]])
                                hold[key].pop(0)
                                if jud==5:
                                    combo=0
                                else:
                                    combo+=1
            if event.type == pygame.KEYDOWN:
                kys = event.key
                for key in range(0, amoke):
                    if kys == keys[key]:
                        for jud in range(0, len(judge)):
                            if elp - judge[jud] < song[key][0] < elp + judge[jud]:
                                scores.append([jud, elp - song[key][0]])
                                song[key].pop(0)
                                if jud==5:
                                    combo=0
                                else:
                                    combo+=1
                                break
                            if elp - judge[jud] < hold[key][0][0] < elp + judge[jud]:
                                scores.append([jud, elp - hold[key][0][0]])
                                if jud==5:
                                    combo=0
                                else:
                                    combo+=1
                                break
        # texts and stuff

        text_rect = judgetext[scores[-1][0]].get_rect(center=(wid / 2, (hei / 2) - 80))
        screen.blit(judgetext[scores[-1][0]], text_rect)


        #errorbar
        x = (wid / 2) + (scores[-1][1] / 200) * ((lanes[-1] - lanes[1]) + (4 * rad))
        pygame.draw.rect(
            screen, (255, 255, 255), pygame.Rect(x, (hei / 2) + 100, 2, 10)
        )
        pygame.draw.rect(
            screen, (200, 200, 200), pygame.Rect(wid / 2, (hei / 2) + 100, 3, 15)
        )
        x = (wid / 2) + ((sum([x[1] for x in scores]) / len(scores)) / 200) * (
            (lanes[-1] - lanes[1]) + (4 * rad)
        )
        pygame.draw.rect(
            screen, (255, 200, 200), pygame.Rect(x, (hei / 2) + 100, 2, 10)
        )
        # funcs
        light(screen, pressed, keys, lanes, juy, rad)
        # update& fadein
        if elp <-2500:
            fadein = pygame.Surface((wid,hei))
            fadein.set_alpha(225-((elp+2900)*0.45))
            fadein.fill((0, 0, 0))
            screen.blit(fadein,(0,0))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    rungame(
        0,
        550,
        800,
        600,
        "Kikuo - Gangu Kyou Sou Kyoku -Shuuen- (Lirai) [4K EXPERT].osu",
        "./",
        [K_a, K_s, K_d, K_SPACE, K_j, K_k, K_l],
        0,
        [(245, 93, 62),#Orange Soda
        (135, 142, 136),#Battleship Grey
        (247, 203, 21)],
    )

