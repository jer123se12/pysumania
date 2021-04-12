import pygame
import re
import os
from pygame.locals import *
import game, options


def writefile(a, b, c, d, e, f, g):
    settings = [[e, "", ""], [f, "", ""], [a, b, ""]] + d + [[g, "", ""]]
    x = open("./.config", "w")
    x.write("\n".join([",".join([str(y) for y in a]) for a in settings]))
    x.close()


def readfile():

    try:
        if os.stat("./.config").st_size == 0:
            pass
    except FileNotFoundError:
        settings = [
            [0, "", ""],
            [500, "", ""],
            [800, 600, ""],
            [243, 243, 243],
            [100, 210, 224],
            [100, 210, 225],
            [243, 243, 243],
            [1, "", ""],
        ]
        with open("./.config", "w") as testfile1:
            testfile1.write(
                "\n".join([",".join([str(y) for y in a]) for a in settings])
            )
    se = []
    x = open("./.config", "r")
    for a in x.readlines():
        se.append([(int(ced) if ced != "" else ced) for ced in a.strip().split(",")])

    x.close()

    return (
        se[2][0],
        se[2][1],
        2,
        [se[3], se[4], se[5], se[6]],
        se[0][0],
        se[1][0],
        se[7][0],
    )


def getmaps():
    songtitles = []
    for (dirpath, dirnames, filenames) in os.walk("Songs"):
        songtitles.extend(dirnames)
        break

    maps = [[] for x in songtitles]
    for a in range(0, len(songtitles)):
        reg = re.compile("\[(.*)\]")
        for (dirpath, dirnames, filenames) in os.walk("./Songs/" + songtitles[a]):
            for x in filenames:
                if x[-4:] == ".osu":
                    file1 = open("./Songs/" + songtitles[a] + "/" + x)
                    Lines = file1.readlines()
                    hit = False
                    hit2 = True
                    for line in Lines:

                        if hit:
                            line = line.split(",")[:-1] + [
                                line.split(",")[5].split(":")[0]
                            ]

                            if (
                                int(line[0]) == 64
                                or int(line[0]) == 192
                                or int(line[0]) == 320
                                or int(line[0]) == 448
                            ):
                                pass

                            else:

                                hit2 = False

                        else:
                            if reg.findall(line) == ["HitObjects"]:
                                hit = True
                    if hit2:
                        maps[a].append(songtitles[a] + "/" + str(x))

            break
    return songtitles, maps


def middle(a, li):
    temp = [x for x in li]
    for b in range(a):
        temp.append(temp.pop(0))
    return temp


def songselect(width, height):
    a, b, c, d, e, f, g = readfile()
    width = a
    height = b
    pygame.init()
    running = True
    screenwidth = width
    screenheight = height
    screen = pygame.display.set_mode([screenwidth, screenheight], pygame.RESIZABLE)
    name1, name2 = getmaps()
    current = [0, 0]
    font = pygame.font.SysFont("DelaGothicOne-Regular.ttf", 20)
    reg = re.compile("\[(.*)\]")
    try:
        file1 = open(
            "./Songs/" + name2[current[0]][current[1]],
            "r",
        )
    except:
        print('no songs')
        exit()
    Lines = file1.readlines()
    running = True
    pygame.mixer.init()
    reg = re.compile("\[(.*)\]")
    file1 = open(
        "./Songs/" + name2[current[0]][current[1]],
        "r",
    )
    Lines = file1.readlines()
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
            if bg:
                break
        if "TimingPoints" in line:
            yes = False
    try:
        background_image = pygame.image.load(
            "./Songs/" + name1[current[0]] + "/" + bg
        ).convert()
        background_image = pygame.transform.scale(
            background_image, (screenwidth, screenheight)
        )
        screen.blit(background_image, [0, 0])
    except:
        screen.fill((0, 0, 0))
    pygame.mixer.music.load("./Songs/" + name1[current[0]] + "/" + namex)
    pygame.mixer.music.play()
    while running:
        screenwidth = screen.get_width()
        screenheight = screen.get_height()
        a = screenwidth
        b = screenheight
        writefile(a, b, c, d, e, f, g)
        try:
            reg = re.compile("\[(.*)\]")
            file1 = open(
                "./Songs/" + name2[current[0]][current[1]],
                "r",
            )
            Lines = file1.readlines()
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
                    if bg:
                        break
                if "TimingPoints" in line:
                    yes = False
            try:
                background_image = pygame.image.load(
                    "./Songs/" + name1[current[0]] + "/" + bg
                ).convert()
                background_image = pygame.transform.scale(
                    background_image, (screenwidth, screenheight)
                )
                screen.blit(background_image, [0, 0])
            except:
                screen.fill((0, 0, 0))
        except:
            pass
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        a, b, c, d, e, f, g = readfile()
                        a = int(a)
                        b = int(b)
                        game.rungame(
                            a,
                            b,
                            c,
                            d,
                            e,
                            f,
                            g,
                            name1[current[0]],
                            name2[current[0]][current[1]],
                        )
                    if event.key == pygame.K_o:

                        a, b, c, d, e, f, g = options.Options(screenwidth, screenheight)
                        writefile(a, b, c, d, e, f, g)
                        screenwidth = int(a)
                        screenheight = int(b)
                        screen = pygame.display.set_mode(
                            [screenwidth, screenheight], pygame.RESIZABLE
                        )

                    if event.key == K_UP:
                        temp = current[0] - 1
                        if temp < 0:
                            temp = len(name1) - 1

                        current[0] = temp
                        reg = re.compile("\[(.*)\]")
                        file1 = open(
                            "./Songs/" + name2[current[0]][current[1]],
                            "r",
                        )
                        Lines = file1.readlines()
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
                                if bg:
                                    break
                            if "TimingPoints" in line:
                                yes = False
                        try:
                            background_image = pygame.image.load(
                                "./Songs/" + name1[current[0]] + "/" + bg
                            ).convert()
                            background_image = pygame.transform.scale(
                                background_image, (screenwidth, screenheight)
                            )
                            screen.blit(background_image, [0, 0])
                        except:
                            screen.fill((0, 0, 0))
                        pygame.mixer.music.load(
                            "./Songs/" + name1[current[0]] + "/" + namex
                        )
                        pygame.mixer.music.play(-1)

                    elif event.key == K_DOWN:
                        temp = current[0] + 1
                        if temp > len(name1) - 1:
                            temp = 0

                        current[0] = temp
                        file1 = open(
                            "./Songs/" + name2[current[0]][current[1]],
                            "r",
                        )
                        Lines = file1.readlines()
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
                                if bg:
                                    break
                            if "TimingPoints" in line:
                                yes = False
                        try:
                            background_image = pygame.image.load(
                                "./Songs/" + name1[current[0]] + "/" + bg
                            ).convert()
                            background_image = pygame.transform.scale(
                                background_image, (screenwidth, screenheight)
                            )
                            screen.blit(background_image, [0, 0])
                        except:
                            screen.fill((0, 0, 0))

                        pygame.mixer.music.load(
                            "./Songs/" + name1[current[0]] + "/" + namex
                        )
                        pygame.mixer.music.play(-1)

                    elif event.key == K_LEFT:
                        temp = current[1] - 1
                        if temp < 0:
                            temp = len(name2[current[0]]) - 1
                        current[1] = temp

                        file1 = open(
                            "./Songs/" + name2[current[0]][current[1]],
                            "r",
                        )
                        Lines = file1.readlines(-1)
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
                                if bg:
                                    break
                            if "TimingPoints" in line:
                                yes = False
                        try:
                            background_image = pygame.image.load(
                                "./Songs/" + name1[current[0]] + "/" + bg
                            ).convert()
                            background_image = pygame.transform.scale(
                                background_image, (screenwidth, screenheight)
                            )
                            screen.blit(background_image, [0, 0])
                        except:
                            screen.fill((0, 0, 0))

                        pygame.mixer.music.load(
                            "./Songs/" + name1[current[0]] + "/" + namex
                        )
                        pygame.mixer.music.play(-1)

                    elif event.key == K_RIGHT:
                        temp = current[1] + 1
                        if temp > len(name2[current[0]]) - 1:
                            temp = 0
                        current[1] = temp
                        file1 = open(
                            "./Songs/" + name2[current[0]][current[1]],
                            "r",
                        )
                        Lines = file1.readlines()
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
                                if bg:
                                    break
                            if "TimingPoints" in line:
                                yes = False
                        try:
                            background_image = pygame.image.load(
                                "./Songs/" + name1[current[0]] + "/" + bg
                            ).convert()
                            background_image = pygame.transform.scale(
                                background_image, (screenwidth, screenheight)
                            )
                            screen.blit(background_image, [0, 0])
                        except:
                            screen.fill((0, 0, 0))

                        pygame.mixer.music.load(
                            "./Songs/" + name1[current[0]] + "/" + namex
                        )
                        pygame.mixer.music.play(-1)
        except:
            current[1] = 0
        try:
            screen.blit(background_image, [0, 0])
        except:
            screen.fill((0, 0, 0))

        s = pygame.Surface((screenwidth, screenheight))  # the size of your rect
        s.set_alpha(200)  # alpha level
        s.fill((0, 0, 0))  # this fills the entire surface
        screen.blit(s, (0, 0))
        pygame.draw.rect(screen, (100, 200, 100), pygame.Rect(0, 45, screenwidth, 55))
        i = 1
        temp = middle(current[0], name1)
        for z in temp:
            text = font.render(z, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.left = 10
            text_rect.top = i * 50  # align to right to 150px
            screen.blit(text, text_rect)
            i += 1
        i = 1
        temp = middle(current[1], name2[current[0]])
        for z in temp:
            text = font.render(z[len(name1[current[0]]) :], True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.right = screenwidth - 10
            text_rect.top = 25 + (i * 50)  # align to right to 150px
            screen.blit(text, text_rect)
            i += 1

        pygame.display.flip()
    pygame.QUIT()


songselect(800, 600)
