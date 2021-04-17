import pygame
import time
def offset(x,y,x2,y2,m):
    normalx=x-(x2/2)
    normaly=y-(y2/2)
    return (((normalx/x2)*(-1*m))-m,((normaly/y2)*(-1*m))-m)
def button(x,y,width,height,text,color,multi,fontname,fontcolor,moupos,event,fun):
    if moupos[0]>x-multi and moupos[0]<(x+width)+multi and moupos[1]>y-multi and moupos[1]<(y+height)+multi:
        pygame.draw.rect(screen,color,(x-multi,y-multi,width+(2*multi),height+(2*multi)))
        pygame.draw.rect(screen,fontcolor,(x-multi,y-multi,width+(2*multi),height+(2*multi)),width=5)
        t=pygame.font.SysFont(fontname, int((height/1.5)+(multi/2))).render(text,True,fontcolor)
        text_rect = t.get_rect(center=(x+(width/2), y+(height/2)))
        screen.blit(t,text_rect)
        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN:
                fun()
    else:
        pygame.draw.rect(screen,color,(x,y,width,height))
        pygame.draw.rect(screen,fontcolor,(x,y,width,height),width=5)
        t=pygame.font.SysFont(fontname, int(height/1.5)).render(text,True,fontcolor)
        text_rect = t.get_rect(center=(x+(width/2), y+(height/2)))
        screen.blit(t,text_rect)
    
        
    #if pygame.mouse.get_pressed()[0]:
        #fun()
def songselect():
    print('run song select?')
def options():
    print('run options?')
colors=[(245, 93, 62),#Orange Soda
        (135, 142, 136),#Battleship Grey
        (247, 203, 21),#Yellow Ochre PC 942
        (255, 255, 255),#White
        (118, 190, 208)]#Dark Sky Blue
pygame.init()
wid=800
hei=600
multi=100
screen = pygame.display.set_mode((wid,hei),pygame.RESIZABLE)
image = pygame.image.load('background desuuu.jpg')
image=pygame.transform.scale(image, (wid+(multi*2), hei+(multi*2)))
running=True
st=time.time()
while running:
    elp=time.time()-st
    image=pygame.transform.scale(image, (wid+(multi*2), hei+(multi*2)))
    events=pygame.event.get()
    x, y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    parallex=offset(x,y,wid,hei,multi)
    screen.blit(image,parallex)
    bw=(200/800)*wid
    bh=(100/600)*hei
    button(((wid/2)-(bw/2)),((hei/3))+(parallex[1]*0.5),bw,bh,'Mania',colors[3],20,'DelaGothicOne-Regular.ttf',colors[1],(x,y),events,songselect)
    button(((wid/2)-(bw/2)),((hei/3)*2)+(parallex[1]*0.5),bw,bh,'Options',colors[3],20,'DelaGothicOne-Regular.ttf',colors[1],(x,y),events,options)
    for e in events:
        if e == pygame.QUIT:
            running = False
        if e.type == pygame.VIDEORESIZE:
            scrsize = e.size  # or event.w, event.h
            screen = pygame.display.set_mode(scrsize,pygame.RESIZABLE)
            wid,hei=scrsize
    
    if elp <0.5:
        fadein = pygame.Surface((wid,hei))
        fadein.set_alpha(225-(elp*450))
        fadein.fill((0, 0, 0))
        screen.blit(fadein,(0,0))
    pygame.display.flip()
    