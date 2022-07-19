# Stuff to do
# hold notes DONE!
# scaling done!
# offset (done!)
# error bar (scale left)
# func

# declare
import time
import pygame
import re
import os
from pygame.locals import *
import rescreen

def getmaps():
    songtitles = []
    for (dirpath, dirnames, filenames) in os.walk("Songs"):
        songtitles.extend(dirnames)
        break

    maps = [[] for x in songtitles]
    for a in range(0, len(songtitles)):

        for (dirpath, dirnames, filenames) in os.walk("./Songs/" + songtitles[a]):
            for x in filenames:
                if x[-4:] == ".osu":
                    maps[a].append(songtitles[a] + "/" + str(x))

            break
    return songtitles, maps


def rungame(w, h, s, c, o, scr,skin,n, n2):
    # w: screen width
    # h: screen height
    # s: seperation
    # c: colors for lanes
    # scr: scroll speed
    # name2: path to osu file
    # name: folder of osu file (no end with /)
    screen_width = w
    screen_height = h
    seperation = s
    colors = c
    offset = o
    roll = scr

    # culculated:
    held=[-1,-1,-1,-1]
    barheight = 20 / 600 * screen_height
    wid = int((3 / 600) * screen_height)
    juy = int(screen_height * (5 / 6))
    sirclick = int(25 * (screen_height / 600))
    offset2 = []
    diff = 0
    hold = [[], [], [], []]
    length = 0
    running = True
    color = [0, 0, 0, 0]
    song = [[], [], [], []]
    scores = [0]
    lanes = [
        int((screen_width / 2) - ((3 * sirclick) + (2 * seperation))),
        int((screen_width / 2) - (((sirclick) + seperation))),
        int((screen_width / 2) + sirclick),
        int((screen_width / 2) + 3 * sirclick)+seperation,
    ]
    size = (int((lanes[3] - lanes[0]) + sirclick + sirclick)+(2*wid), int(screen_height))

    # get file
    name = n
    name2 = n2

    file1 = open(
        "./Songs/" + name2,
        "r",
    )

    # file formatting
    reg = re.compile("\[(.*)\]")
    Lines = file1.readlines()
    hit = False
    score = 0
    a = 0
    dis = 0
    for line in Lines:

        if hit:
            line = line.split(",")[:-1] + [line.split(",")[5].split(":")[0]]

            if int(line[3]) == 128:
                length = int(line[5])
                if int(line[0]) == 64:
                    hold[0].append([int(line[2]), int(line[5])])
                elif int(line[0]) == 192:
                    hold[1].append([int(line[2]), int(line[5])])
                elif int(line[0]) == 320:
                    hold[2].append([int(line[2]), int(line[5])])
                elif int(line[0]) == 448:
                    hold[3].append([int(line[2]), int(line[5])])

            else:
                length = int(line[2])
            if int(line[0]) == 64:
                song[0].append(int(line[2]))
            elif int(line[0]) == 192:
                song[1].append(int(line[2]))
            elif int(line[0]) == 320:
                song[2].append(int(line[2]))
            elif int(line[0]) == 448:
                song[3].append(int(line[2]))
        else:
            if reg.findall(line) == ["HitObjects"]:
                hit = True
    hold[0].append([999999999999999999, 999999999999999999])
    hold[1].append([999999999999999999, 999999999999999999])
    hold[2].append([999999999999999999, 999999999999999999])
    hold[3].append([999999999999999999, 999999999999999999])
    song[0].append(999999999999999999)
    song[1].append(999999999999999999)
    song[2].append(999999999999999999)
    song[3].append(999999999999999999)
    yes = False

    for line in Lines:
        if "AudioFilename" in line:
            namex = line.split(":")[1].strip()
        if "[Events]" in line:
            yes = True
        elif yes and line[:2] != "//":
            try:
                temp = int(line.split(",")[0])
                bg = line.split(",")[2][1:-1]
            except:
                pass
            try:
                if bg:
                    pass
            except:
                break
        if "TimingPoints" in line:
            yes = False

    # init cont.
    # here might not need:
    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height],pygame.RESIZABLE)

    try:
        background_image = pygame.image.load("./Songs/" + name + "/" + bg).convert()
        background_image = pygame.transform.scale(
            background_image, (screen_width, screen_height)
        )
    except:
        pass
    font = pygame.font.SysFont("DelaGothicOne-Regular.ttf", 48)
    judge = [
        font.render("", True, (255, 0, 0)),
        font.render("MISS", True, (255, 0, 0)),
        font.render("GOOD", True, (255, 0, 0)),
        font.render("GREAT", True, (0, 100, 0)),
        font.render("PERFECT", True, (255, 255, 0)),
        font.render("EXCELLENT", True, (255, 255, 255)),
    ]
    combo = 0
    pygame.mixer.init()
    pygame.mixer.music.load("./Songs/" + name + "/" + namex)
    ogstart = (time.time() * 1000) + 3000
    starttime = ogstart + offset

    # 3sloop
    while running:
        screen_width=screen.get_width()
        screen_height=screen.get_height()
        try:
            background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
            screen.blit(background_image, [0, 0])
        except:
            screen.fill((0, 0, 0))

        timepassed = (time.time() * 1000) - starttime

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pass
                else:
                    color[0] = 0
                    a = 0
                if event.key == pygame.K_s:

                    pass
                else:
                    color[1] = 0
                    a = 0
                if event.key == pygame.K_k:
                    pass
                else:
                    color[2] = 0
                    a = 0
                if event.key == pygame.K_l:
                    pass
                else:
                    color[3] = 0
                    a = 0
        # funcs
        press = pygame.key.get_pressed()
        # clickkk(timepassed, press)
        s = pygame.Surface(size)  # the size of your rect
        s.set_alpha(180)  # alpha level
        s.fill((100, 100, 100))  # this fills the entire surface
        screen.blit(s, ((screen_width - size[0]) / 2, 0))
        # pressed(press, timepassed)
        if press[K_a]:
            color[0] = 1
        else:
            color[0] = 0
        if press[K_s]:

            color[1] = 1
        else:
            color[1] = 0
        if press[K_k]:

            color[2] = 1
        else:
            color[2] = 0
        if press[K_l]:

            color[3] = 1
        else:
            color[3] = 0

        if skin:
            if color[0]:
                pygame.draw.circle(screen, (220, 220, 220), (lanes[0], juy), sirclick)
            else:
                pygame.draw.circle(
                    screen, (220, 220, 220), (lanes[0], juy), sirclick, width=wid
                )
            if color[1]:
                pygame.draw.circle(screen, (220, 220, 220), (lanes[1], juy), sirclick)
            else:
                pygame.draw.circle(
                    screen, (220, 220, 220), (lanes[1], juy), sirclick, width=wid
                )
            if color[2]:
                pygame.draw.circle(screen, (220, 220, 220), (lanes[2], juy), sirclick)
            else:
                pygame.draw.circle(
                    screen, (220, 220, 220), (lanes[2], juy), sirclick, width=wid
                )
            if color[3]:
                pygame.draw.circle(screen, (220, 220, 220), (lanes[3], juy), sirclick)
            else:
                pygame.draw.circle(
                    screen, (220, 220, 220), (lanes[3], juy), sirclick, width=wid
                )
        else:
            if color[0]:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[0] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                )
            else:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[0] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                    width=wid,
                )
            if color[1]:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[1] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                )
            else:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[1] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                    width=wid,
                )
            if color[2]:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[2] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                )
            else:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[2] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                    width=wid,
                )
            if color[3]:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[3] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                )
            else:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[3] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                    width=wid,
                )

        # scrollhold(roll, timepassed)
        for a in range(0, len(hold)):
            for b in range(0, len(hold[a])):
                if hold[a][b][0] >= timepassed + roll + 100:
                    break
                else:
                    y1 = juy - (((hold[a][b][1] - timepassed) / roll) * juy)
                    y2 = juy - (((hold[a][b][0] - timepassed) / roll) * juy)
                    pygame.draw.rect(
                        screen,
                        colors[a],
                        (lanes[a] - sirclick, y1, sirclick * 2, y2 - y1),
                    )

                    pygame.draw.circle(screen, colors[a], (lanes[a], y1), sirclick)

        # scroll(roll, timepassed)
        for a in range(0, len(song)):
            i = 0
            z = 0
            z = song[a][i]
            while z < timepassed + roll:
                z = song[a][i]
                percent = (z - timepassed) / roll
                pygame.draw.circle(
                    screen, colors[a], (lanes[a], juy - (percent * juy)), sirclick
                )

                i += 1
        # text
        com = font.render(str(combo), False, (255, 255, 255))
        percentage = font.render("100" + "%", False, (255, 255, 255))
        text_rect2 = com.get_rect(center=(screen_width / 2, (screen_height / 2) - 40))
        text_rect = judge[0].get_rect(
            center=(screen_width / 2, (screen_height / 2) - 80)
        )

        pygame.draw.rect(
            screen,
            (20, 20, 20),
            pygame.Rect(
                (screen_width / 2) + ((diff + offset) / 2),
                (screen_width / 2) - 80,
                5,
                10,
            ),
        )

        # blits
        screen.blit(judge[0], text_rect)
        screen.blit(font.render(str(score), True, (0, 0, 0)), (0, 20))
        screen.blit(com, text_rect2)
        screen.blit(percentage, (0, 80))

        # quit
        if timepassed > -2:
            break
        pygame.display.flip()

    pygame.mixer.music.play()

    # main loop
    while running:
        screen_width=screen.get_width()
        screen_height=screen.get_height()
        try:
            background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
            screen.blit(background_image, [0, 0])
        except:
            screen.fill((0, 0, 0))
        timepassed = pygame.mixer.music.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    temp = (timepassed - offset) - hold[0][0][1]
                    if timepassed > hold[0][0][0] and timepassed < hold[0][0][1] + 200:

                        if hold[0][0][1] - 22 < timepassed and timepassed < hold[0][0][1] + 22:
                            diff = temp
                            offset2.append(temp)
                            a=5
                            scores.append(a)
                            hold[0].pop(0)
                        elif hold[0][0][1] - 40 < timepassed and timepassed < hold[0][0][1] + 40:
                            diff = temp
                            offset2.append(temp)
                            a=4
                            scores.append(a)
                            hold[0].pop(0)
                        elif hold[0][0][1] - 90 < timepassed and timepassed < hold[0][0][1] + 90:
                            diff = temp
                            offset2.append(temp)
                            a=3
                            scores.append(a)
                            hold[0].pop(0)
                        elif hold[0][0][1] - 130 < timepassed and timepassed < hold[0][0][1] + 135:
                            diff = temp
                            offset2.append(temp)
                            a=2
                            scores.append(a)
                            hold[0].pop(0)
                        elif hold[0][0][1] - 180 < timepassed and timepassed < hold[0][0][1] + 180:
                            diff = temp
                            offset2.append(temp)
                            a=1
                            scores.append(a)
                            hold[0].pop(0)
                            combo=0
                        elif hold[0][0][1] - 200 < timepassed and timepassed < hold[0][0][1] + 200:
                            diff = temp
                            offset2.append(temp)
                            a=1
                            scores.append(a)
                            hold[0].pop(0)
                            combo=0

                if event.key == pygame.K_s:
                    if timepassed > hold[1][0][0] and timepassed < hold[1][0][1] + 200:

                        if hold[1][0][1] - 22 < timepassed and timepassed < hold[1][0][1] + 22:
                            diff = temp
                            offset2.append(temp)
                            a=5
                            scores.append(a)
                            hold[1].pop(0)
                        elif hold[1][0][1] - 40 < timepassed and timepassed < hold[1][0][1] + 40:
                            diff = temp
                            offset2.append(temp)
                            a=4
                            scores.append(a)
                            hold[1].pop(0)
                        elif hold[1][0][1] - 90 < timepassed and timepassed < hold[1][0][1] + 90:
                            diff = temp
                            offset2.append(temp)
                            a=3
                            scores.append(a)
                            hold[1].pop(0)
                        elif hold[1][0][1] - 130 < timepassed and timepassed < hold[1][0][1] + 135:
                            diff = temp
                            offset2.append(temp)
                            a=2
                            scores.append(a)
                            hold[1].pop(0)
                        elif hold[1][0][1] - 180 < timepassed and timepassed < hold[1][0][1] + 180:
                            diff = temp
                            offset2.append(temp)
                            a=1
                            scores.append(a)
                            hold[1].pop(0)
                            combo=0
                        elif hold[1][0][1] - 200 < timepassed and timepassed < hold[1][0][1] + 200:
                            diff = temp
                            offset2.append(temp)
                            a=1
                            scores.append(a)
                            hold[1].pop(0)
                            combo=0

                if event.key == pygame.K_k:
                    if timepassed > hold[2][0][0] and timepassed < hold[2][0][1] + 200:

                        if hold[2][0][1] - 22 < timepassed and timepassed < hold[2][0][1] + 22:
                            diff = temp
                            offset2.append(temp)
                            a=5
                            scores.append(a)
                            hold[2].pop(0)
                        elif hold[2][0][1] - 40 < timepassed and timepassed < hold[2][0][1] + 40:
                            diff = temp
                            offset2.append(temp)
                            a=4
                            scores.append(a)
                            hold[2].pop(0)
                        elif hold[2][0][1] - 90 < timepassed and timepassed < hold[2][0][1] + 90:
                            diff = temp
                            offset2.append(temp)
                            a=3
                            scores.append(a)
                            hold[2].pop(0)
                        elif hold[2][0][1] - 130 < timepassed and timepassed < hold[2][0][1] + 135:
                            diff = temp
                            offset2.append(temp)
                            a=2
                            scores.append(a)
                            hold[2].pop(0)
                        elif hold[2][0][1] - 180 < timepassed and timepassed < hold[2][0][1] + 180:
                            diff = temp
                            offset2.append(temp)
                            a=1
                            scores.append(a)
                            hold[2].pop(0)
                            combo=0
                        elif hold[2][0][1] - 200 < timepassed and timepassed < hold[2][0][1] + 200:
                            diff = temp
                            offset2.append(temp)
                            a=1
                            scores.append(a)
                            hold[2].pop(0)
                            combo=0

                if event.key == pygame.K_l:
                    if timepassed > hold[3][0][0] and timepassed < hold[3][0][1] + 200:

                        if hold[3][0][1] - 22 < timepassed and timepassed < hold[3][0][1] + 22:
                            diff = temp
                            offset2.append(temp)
                            a=5
                            scores.append(a)
                            hold[3].pop(0)
                        elif hold[3][0][1] - 40 < timepassed and timepassed < hold[3][0][1] + 40:
                            diff = temp
                            offset2.append(temp)
                            a=4
                            scores.append(a)
                            hold[3].pop(0)
                        elif hold[3][0][1] - 90 < timepassed and timepassed < hold[3][0][1] + 90:
                            diff = temp
                            offset2.append(temp)
                            a=3
                            scores.append(a)
                            hold[3].pop(0)
                        elif hold[3][0][1] - 130 < timepassed and timepassed < hold[3][0][1] + 135:
                            diff = temp
                            offset2.append(temp)
                            a=2
                            scores.append(a)
                            hold[3].pop(0)
                        elif hold[3][0][1] - 180 < timepassed and timepassed < hold[3][0][1] + 180:
                            diff = temp
                            offset2.append(temp)
                            a=1
                            scores.append(a)
                            hold[3].pop(0)
                            combo=0
                        elif hold[3][0][1] - 200 < timepassed and timepassed < hold[3][0][1] + 200:
                            diff = temp
                            offset2.append(temp)
                            a=1
                            scores.append(a)
                            hold[3].pop(0)
                            combo=0

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    rescreen.rescreen(screen_width, screen_height, offset2, scores,
                                      sum(scores) / (len(scores) * 5) * 100)
                    running=False
                if event.key == pygame.K_o:
                    offset = sum(offset2) / len(offset2)
                    print(offset)
                    print(offset2)
                    starttime = ogstart + offset
                if event.key == pygame.K_a:

                    # a = check(timepassed, song[0][0])
                    temp = (timepassed - offset) - song[0][0]
                    if song[0][0] - 22 < timepassed and timepassed < song[0][0] + 22:
                        diff = temp
                        offset2.append(temp)
                        combo += 1
                        a = 5
                    elif song[0][0] - 45 < timepassed and timepassed < song[0][0] + 45:
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 4
                    elif song[0][0] - 90 < timepassed and timepassed < song[0][0] + 90:
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 3
                    elif (
                        song[0][0] - 135 < timepassed and timepassed < song[0][0] + 135
                    ):
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 2
                    elif (
                        song[0][0] - 180 < timepassed and timepassed < song[0][0] + 180
                    ):
                        diff = temp
                        combo = 0
                        a = 1
                    elif (
                        song[0][0] - 200 < timepassed and timepassed < song[0][0] + 200
                    ):
                        diff = temp
                        combo = 0
                        # combo break here?
                        a = 0
                    else:
                        a = -1

                    if a != -1:

                        song[0].pop(0)
                        scores.append(a)

                        score += a * 100
                    else:
                        a = 0
                    color[0] = 1
                else:
                    color[0] = 0
                    a = 0
                if event.key == pygame.K_s:

                    # a = check(timepassed, song[1][0])
                    temp = (timepassed - offset) - song[1][0]
                    if song[1][0] - 22 < timepassed and timepassed < song[1][0] + 22:
                        diff = temp
                        offset2.append(temp)
                        combo += 1
                        a = 5
                    elif song[1][0] - 45 < timepassed and timepassed < song[1][0] + 45:
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 4
                    elif song[1][0] - 90 < timepassed and timepassed < song[1][0] + 90:
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 3
                    elif (
                        song[1][0] - 135 < timepassed and timepassed < song[1][0] + 135
                    ):
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 2
                    elif (
                        song[1][0] - 180 < timepassed and timepassed < song[1][0] + 180
                    ):
                        diff = temp
                        combo = 0
                        a = 1
                    elif (
                        song[1][0] - 200 < timepassed and timepassed < song[1][0] + 200
                    ):
                        diff = temp
                        combo = 0
                        # combo break here?
                        a = 0
                    else:
                        a = -1

                    if a != -1:

                        song[1].pop(0)
                        scores.append(a)

                        score += a * 100
                    else:
                        a = 0
                    color[1] = 1
                else:
                    color[1] = 0
                    a = 0
                if event.key == pygame.K_k:
                    # a = check(timepassed, song[2][0])
                    temp = (timepassed - offset) - song[2][0]
                    if song[2][0] - 22 < timepassed and timepassed < song[2][0] + 22:
                        diff = temp
                        offset2.append(temp)
                        combo += 1
                        a = 5
                    elif song[2][0] - 45 < timepassed and timepassed < song[2][0] + 45:
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 4
                    elif song[2][0] - 90 < timepassed and timepassed < song[2][0] + 90:
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 3
                    elif (
                        song[2][0] - 135 < timepassed and timepassed < song[2][0] + 135
                    ):
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 2
                    elif (
                        song[2][0] - 180 < timepassed and timepassed < song[2][0] + 180
                    ):
                        diff = temp
                        combo = 0
                        a = 1
                    elif (
                        song[2][0] - 200 < timepassed and timepassed < song[2][0] + 200
                    ):
                        diff = temp
                        combo = 0
                        # combo break here?
                        a = 0
                    else:
                        a = -1


                    if a != -1:

                        song[2].pop(0)
                        scores.append(a)

                        score += a * 100
                    else:
                        a = 0
                    color[2] = 1
                else:
                    color[2] = 0
                    a = 0
                if event.key == pygame.K_l:
                    # a = check(timepassed, song[3][0])
                    temp = (timepassed - offset) - song[3][0]
                    if song[3][0] - 22 < timepassed and timepassed < song[3][0] + 22:
                        diff = temp
                        offset2.append(temp)
                        combo += 1
                        a = 5
                    elif song[3][0] - 45 < timepassed and timepassed < song[3][0] + 45:
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 4
                    elif song[3][0] - 90 < timepassed and timepassed < song[3][0] + 90:
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 3
                    elif (
                        song[3][0] - 135 < timepassed and timepassed < song[3][0] + 135
                    ):
                        offset2.append(temp)
                        diff = temp
                        combo += 1
                        a = 2
                    elif (
                        song[3][0] - 180 < timepassed and timepassed < song[3][0] + 180
                    ):
                        diff = temp
                        combo = 0
                        a = 1
                    elif (
                        song[3][0] - 200 < timepassed and timepassed < song[3][0] + 200
                    ):
                        diff = temp
                        combo = 0
                        # combo break here?
                        a = 0
                    else:
                        a = -1

                    if a != -1:

                        song[3].pop(0)
                        scores.append(a)

                        score += a * 100
                    else:
                        a = 0
                    color[3] = 1
                else:
                    color[3] = 0
                    a = 0
        # funcs
        press = pygame.key.get_pressed()

        # clickkk(timepassed, press)
        s = pygame.Surface(size)  # the size of your rect
        s.set_alpha(180)  # alpha level
        s.fill((100, 100, 100))  # this fills the entire surface
        screen.blit(s, ((screen_width - size[0]) / 2, 0))
        # pressed(press, timepassed)
        if press[K_a]:
            color[0] = 1
        else:
            color[0] = 0
        if press[K_s]:

            color[1] = 1
        else:
            color[1] = 0
        if press[K_k]:

            color[2] = 1
        else:
            color[2] = 0
        if press[K_l]:

            color[3] = 1
        else:
            color[3] = 0

        if skin:
            if color[0]:
                pygame.draw.circle(screen, (220, 220, 220), (lanes[0], juy), sirclick)
            else:
                pygame.draw.circle(
                    screen, (220, 220, 220), (lanes[0], juy), sirclick, width=wid
                )
            if color[1]:
                pygame.draw.circle(screen, (220, 220, 220), (lanes[1], juy), sirclick)
            else:
                pygame.draw.circle(
                    screen, (220, 220, 220), (lanes[1], juy), sirclick, width=wid
                )
            if color[2]:
                pygame.draw.circle(screen, (220, 220, 220), (lanes[2], juy), sirclick)
            else:
                pygame.draw.circle(
                    screen, (220, 220, 220), (lanes[2], juy), sirclick, width=wid
                )
            if color[3]:
                pygame.draw.circle(screen, (220, 220, 220), (lanes[3], juy), sirclick)
            else:
                pygame.draw.circle(
                    screen, (220, 220, 220), (lanes[3], juy), sirclick, width=wid
                )
        else:
            if color[0]:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[0] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                )
            else:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[0] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                    width=wid,
                )
            if color[1]:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[1] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                )
            else:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[1] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                    width=wid,
                )
            if color[2]:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[2] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                )
            else:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[2] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                    width=wid,
                )
            if color[3]:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[3] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                )
            else:
                pygame.draw.rect(
                    screen,
                    (220, 220, 220),
                    pygame.Rect(
                        lanes[3] - sirclick, juy - barheight, 2 * sirclick, barheight
                    ),
                    width=wid,
                )

        # remove(timepassed)
        count = 0
        for a in song:
            if a[0] < timepassed - 200:
                song[count].pop(0)
                combo = 0
                scores.append(1)
            count += 1
        count = 0
        for a in hold:
            if a[0][1] < timepassed - 200:
                hold[count].pop(0)
            count += 1

        # scroll(roll, timepassed)
        for a in range(0, len(song)):
            i = 0
            z = 0
            z = song[a][i]

            while z < timepassed + roll:
                z = song[a][i]

                percent = (z - timepassed) / roll
                if skin:
                    pygame.draw.circle(
                        screen, colors[a], (lanes[a], juy - (percent * juy)), sirclick
                    )
                else:

                    pygame.draw.rect(
                        screen,
                        colors[a],
                        pygame.Rect(
                            lanes[a] - sirclick,
                            juy - (percent * juy),
                            sirclick * 2,
                            barheight,
                        ),
                    )
                i += 1
            # hold
            for b in range(0, len(hold[a])):
                if hold[a][b][0] >= timepassed + roll + 100:
                    break
                else:
                    y1 = juy - (((hold[a][b][1] - timepassed) / roll) * juy)
                    y2 = juy - (((hold[a][b][0] - timepassed) / roll) * juy)
                    if timepassed > hold[a][b][0] and timepassed < hold[a][b][1] and press[[K_a,K_s,K_k,K_l][a]]:
                        held[a] = 0
                    else :
                        held[a]=-1
                    if ((-1* (held[a]*y2))+((held[a]+1)*(juy)))-y1 >0:
                        pygame.draw.rect(
                            screen,
                            colors[a],
                            (lanes[a] - sirclick, y1, sirclick * 2,  ((-1* (held[a]*y2))+((held[a]+1)*(juy)))-y1),
                        )
                    if skin:
                        pygame.draw.circle(screen, colors[a], (lanes[a], y1), sirclick)
                    else:
                        pygame.draw.rect(
                            screen,
                            colors[a],
                            pygame.Rect(
                                lanes[a] - sirclick,
                                y1 + (barheight / 2),
                                sirclick * 2,
                                barheight,
                            ),
                        )

        # text
        com = font.render(str(combo), False, (255, 255, 255))
        percentage = font.render(
            str(sum(scores) / (len(scores) * 5) * 100)[:4] + "%", False, (255, 255, 255)
        )
        text_rect2 = com.get_rect(center=(screen_width / 2, (screen_height / 2) - 40))
        text_rect = judge[scores[len(scores) - 1]].get_rect(
            center=(screen_width / 2, (screen_height / 2) - 80)
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            pygame.Rect(
                (screen_width / 2) + (((diff + offset) / 200) * size[0]),
                (screen_height / 2) + 20,
                3,
                20,
            ),
        )

        # blits
        screen.blit(judge[scores[len(scores) - 1]], text_rect)
        screen.blit(font.render(str(score), True, (255, 255, 255)), (0, 20))
        screen.blit(com, text_rect2)
        screen.blit(percentage, (0, 80))

        # quit
        if timepassed > length + 3000:
            running=False
        pygame.display.flip()

if __name__ == '__main__':
    name, name2 = getmaps()
    for x in name:
        print(x, name.index(x))
    chosen = int(input("select: "))
    name = name[chosen]

    for x in name2[chosen]:
        print(x, name2[chosen].index(x))

    name2 = name2[chosen][int(input("select: "))]
    rungame(
        800,
        600,
        -5,
        [(243, 243, 243), (100, 210, 225), (100, 210, 225), (243, 243, 243)],
        0,
        500,
        True,
        name,
        name2
    )
