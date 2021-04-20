import pygame
from pygame.locals import *
import time
import random
import os
import re
import game
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
                            if reg.findall(line) == ["HitObjects"]:
                                hit = True
                    if hit2:
                        maps[a].append(songtitles[a] + "/" + str(x))

            break
    return songtitles, maps
def music(fn):
    a = open(fn, "r")
    hit = False
    for line in a.readlines():
        if "AudioFilename" in line:
            return line.split(":")[1].strip()
def update_particle(screen,p,size,currenttime,color,d,g,f):

    for index in range(0,len(p)):
        rm=[]
        if p[index][6]>0:
            elp=p[index][0]-currenttime
            p[index][1]=p[index][1]+p[index][3]
            p[index][2]=p[index][2]+p[index][4]
            if f:
                if p[index][3]>0:
                    p[index][3]-=p[index][5]
                else:
                    p[index][3]+=p[index][5]
            if g:
                if p[index][4]>0:
                    p[index][4]-=p[index][5]
                else:
                    p[index][4]+=p[index][5]
            p[index][6]-=d
            
            pygame.draw.circle(screen,color,(p[index][1],p[index][2]),int(p[index][6]))
        else:
            rm.append(index)
    for a in rm:
        p.pop(a)
    return p
def offset(x,y,x2,y2,m):
    normalx=x-(x2/2)
    normaly=y-(y2/2)
    return (((normalx/x2)*(-1*m))-m,((normaly/y2)*(-1*m))-m)
def button(screen,x,y,width,height,text,color,multi,fontname,fontcolor,moupos,event,fun):
    if (moupos[0]>x and moupos[0]<(x+width)) and (moupos[1]>y and moupos[1]<(y+height)):
        pygame.draw.rect(screen,fontcolor,(x-multi,y,width+(2*multi),height))
        pygame.draw.rect(screen,color,(x-multi,y,width+(2*multi),height),width=5)
        t=pygame.font.SysFont(fontname, int((height/1.2))).render(text,True,color)
        text_rect = t.get_rect(midright=(x+(width), y+(height/2)))
        screen.blit(t,text_rect)
        for e in event:
            if e.type == pygame.KEYDOWN:
                if e.key==K_RETURN:
                    fun(text)
        return True
    else:
        pygame.draw.rect(screen,color,(x,y,width,height))
        pygame.draw.rect(screen,fontcolor,(x,y,width,height),width=5)
        t=pygame.font.SysFont(fontname, int(height/1.5)).render(text,True,fontcolor)
        text_rect = t.get_rect(midright=(x+(width-multi), y+(height/2)))
        screen.blit(t,text_rect)
        return False
def selectsong(wid,hei):
    def pri(a):
        nonlocal scr,index,curentindex,songs,maps,index2,wid,hei
        curentindex=(hei/80)
        print(index)
        if index<0:
            index2=a
            index=songs.index(a)
        else:
            game.rungame(
                0,
                550,
                wid,
                hei,
                a,
                './Songs/'+index2+'/',
                [K_a, K_s, K_d, K_SPACE, K_j, K_k, K_l],
                0,
                [(245, 93, 62),#Orange Soda
                (135, 142, 136),#Battleship Grey
                (247, 203, 21)],
            )
    pygame.init()
    colors=[(245, 93, 62),#Orange Soda
            (135, 142, 136),#Battleship Grey
            (247, 203, 21),#Yellow Ochre PC 942
            (255, 255, 255),#White
            (118, 190, 208)]#Dark Sky Blue
    pygame.mixer.init()
    screen=pygame.display.set_mode((wid,hei),pygame.RESIZABLE)
    clock=pygame.time.Clock()
    running=True
    p=[]
    index=-1
    songs,maps=getmaps()
    scr=songs
    index2=0
    curentindex=(hei/80)
    st=time.time()
    mousev=0
    cur=0
    while running:
        x=(wid/2)+100
        y=(hei/2)+10
        screen.fill(colors[1])
        clock.tick(60)
        elp=time.time()-st
        events=pygame.event.get()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(screen,(100,100,100),(0,(hei/2),wid,30))
        if index==-1:
            scr=songs
        else:
            scr=[x[(1*len(songs[index]))+1:] for x in maps[index]]
        for e in events:
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.VIDEORESIZE:
                scrsize = e.size  # or event.w, event.h
                screen = pygame.display.set_mode(scrsize,pygame.RESIZABLE)
                wid,hei=scrsize
                curentindex=(hei/80)
            if e.type==pygame.KEYDOWN:
                if e.key==K_ESCAPE:
                    if index!=-1:
                        index=-1
                        if index==-1:
                            
                            scr=songs
                            curentindex=(hei/80)
                        else:
                            
                            scr=[x[len(songs[index])+1:] for x in maps[index]]
                            curentindex=(hei/80)
                    else:
                        running=False
                if e.key==K_UP:
                    
                    curentindex = min(curentindex + 1,(hei/80))
                if e.key==K_DOWN:
                    
                    curentindex = max(curentindex -1,((len(scr)-1)*-1)+(hei/80))
    #         if e.type==pygame.MOUSEMOTION:
    #             x, y = pygame.mouse.get_pos()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4:
                    if mousev<0:
                        mousev=0
                    mousev=min(mousev+1,15)
                    curentindex = min(curentindex + mousev,(hei/80))
                if e.button == 5:
                    if mousev>0:
                        mousev=0
                    mousev=max(mousev-1,-15)
                    curentindex = max(curentindex + mousev,((len(scr)-1)*-1)+(hei/80))
        if mousev>0:
            mousev-=1
        else:
            mousev+=1
        for l in range(0,len(scr)):
            y2=(l*40)+(curentindex*40)
            if y2<hei and y2>-30:
                button(screen,wid/2,y2,(wid/2)-10,25,scr[l],colors[1],50,'DelaGothicOne-Regular.ttf',colors[4],(x,y),events,pri)
                if cur!=l and button(screen,wid/2,y2,(wid/2)-10,25,scr[l],colors[1],50,'DelaGothicOne-Regular.ttf',colors[4],(x,y),events,pri):
                    
                    cur=l
                    if index>-1:
                        pygame.mixer.music.load('./Songs/'+ songs[index]+'/'+ music('./Songs/'+maps[index][cur]))
                        pygame.mixer.music.play()
                    else:
                        pygame.mixer.music.load('./Songs/'+ songs[cur]+'/'+ music('./Songs/'+maps[cur][0]))
                        pygame.mixer.music.play()
                    
            
        pygame.display.flip()
    return wid,hei

    