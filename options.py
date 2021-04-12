import pygame
from pygame.locals import *
import os


def Options(w, h):
    name = [
        "Offset:",
        "scroll:",
        "resolution:",
        "color for lane 1 :",
        "color for lane 2 :",
        "color for lane 3 :",
        "color for lane 4 :",
        "skin(1/0):",
    ]
    if os.stat("./.config").st_size == 0:
        print("yes")
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
    settings = se
    settings[2][0] = w
    settings[2][1] = h
    settings.append(["done", "", ""])
    numbers = [
        pygame.K_0,
        pygame.K_1,
        pygame.K_2,
        pygame.K_3,
        pygame.K_4,
        pygame.K_5,
        pygame.K_6,
        pygame.K_7,
        pygame.K_8,
        pygame.K_9,
    ]
    pygame.init()
    running = True
    screenwidth = w
    screenheight = h
    screen = pygame.display.set_mode([screenwidth, screenheight], pygame.RESIZABLE)
    current = [0, 0]
    font = pygame.font.SysFont("DelaGothicOne-Regular.ttf", 48)
    while running:
        screenwidth = screen.get_width()
        screenheight = screen.get_height()
        screen.fill((100, 100, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if current[0] != len(settings) - 1:
                    for a in range(0, len(numbers)):
                        if event.key == numbers[a] and len(str(settings[current[0]][current[1]]) + str(a)) <= 3:
                            settings[current[0]][current[1]] = int(
                                str(settings[current[0]][current[1]]) + str(a)
                            )

                    if current == [0, 0] and event.key == pygame.K_MINUS:
                        settings[current[0]][current[1]] *= -1
                    if event.key == K_BACKSPACE:
                        temp = str(settings[current[0]][current[1]])[:-1]
                        settings[current[0]][current[1]] = (
                            int(temp) if temp != "" else 0
                        )
                else:
                    if event.key == K_RETURN:
                        running = False
                if event.key == K_UP:
                    temp = current[0] - 1
                    if temp < 0:
                        temp = len(settings) - 1
                    if settings[temp][current[1]] != "":
                        current[0] = temp

                if event.key == K_DOWN:
                    temp = current[0] + 1
                    if temp > len(settings) - 1:
                        temp = 0
                    if settings[temp][current[1]] != "":
                        current[0] = temp

                if event.key == K_LEFT:
                    temp = current[1] - 1
                    if temp < 0:
                        temp = len(settings[0]) - 1
                    if settings[current[0]][temp] != "":
                        current[1] = temp

                if event.key == K_RIGHT:
                    temp = current[1] + 1
                    if temp > len(settings[0]) - 1:
                        temp = 0
                    if settings[current[0]][temp] != "":
                        current[1] = temp

        op = font.render("Options", True, (230, 230, 230))
        screen.blit(op, (10, 10))
        i = 1
        pygame.draw.lines(
            screen,
            (0, 0, 0),
            False,
            [
                (
                    (screenwidth / 2) + ((current[1] + 1) * 90) ,
                    (30 + (40 * (current[0] + 1))) ,
                ),
                (
                    (screenwidth / 2) + ((current[1] + 1) * 90) ,
                    (30 + (40 * (current[0] + 1))) + 25,
                ),
            ],
            5,
        )
        for a in name:
            text = font.render(a, True, (200, 200, 200))
            screen.blit(text, (30, 30 + (40 * i)))
            i += 1
        i = 1
        i2 = 1
        for a in settings:
            i = 1
            for b in a:
                if b != "":
                    text = font.render(str(b), True, (200, 200, 200))
                    screen.blit(text, ((screenwidth / 2) + (i * 90), (30 + (40 * i2))))
                i += 1
            i2 += 1

        pygame.draw.rect(
            screen,
            (230, 230, 230),
            pygame.Rect(10, 50, screenwidth - 20, screenheight - 60),
            width=5,
        )
        pygame.display.flip()

    return (
        settings[2][0],
        settings[2][1],
        2,
        [settings[3], settings[4], settings[5], settings[6]],
        settings[0][0],
        settings[1][0],
        settings[7][0],
    )


if __name__ == "__main__":
    import main

    name, name2 = main.getmaps()
    for x in name:
        print(x, name.index(x))
    chosen = int(input("select: "))
    name = name[chosen]

    for x in name2[chosen]:
        print(x, name2[chosen].index(x))

    name2 = name2[chosen][int(input("select: "))]
    a, b, c, d, e, f, g = options(800, 600)
    print(d)
    main.rungame(a, b, c, d, e, f, g, name, name2)
    pygame.QUIT()
