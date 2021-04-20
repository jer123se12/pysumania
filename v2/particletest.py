import pygame
import random
import time

def update_particle(screen,p,size,currenttime,color,d,g,f):
    rm=[]
    for index in range(0,len(p)):
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
                #p[index][4]+=p[index][5]
            p[index][6]-=d
            
            pygame.draw.circle(screen,color,(p[index][1],p[index][2]),int(p[index][6]))
        else:
            rm.append(index)
    
    for a in rm:
        try:
            
            p.pop(a)
        except IndexError:
            pass
    return p
pygame.init()
wid=800
hei=600
screen=pygame.display.set_mode((800,600))
starttime=time.time()
clock=pygame.time.Clock()
running=True
p=[]
while running:
    x, y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clock.tick(60)
    screen.fill((0,0,0))
    nowtime=time.time()
    events=pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN or e.type== pygame.KEYDOWN:
            for count in range(100):
                rx=10*((random.random())-0.5)
                ry=20*((random.random())-1)
                p.append([nowtime,x,y,rx,ry,1,5*random.random()])
    
    rx=0
    ry=0
    p.append([nowtime,wid*random.random(),hei*random.random(),rx,ry,0.5,10*random.random()])
#     p.append([nowtime,
#                  x,
#                  y,
#                  rx,
#                  ry,
#                  0.5,
#               20*random.random()])
    p=update_particle(screen,p,5,nowtime,(255,255,255),0.05,True,True)
    pygame.display.flip()