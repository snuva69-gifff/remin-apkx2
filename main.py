import pygame as py 
import random as r
import time

py.init()
run = True
flag_event=False
flagkey = False
flag_end=False
flag_jump=False
flag_start = False
size_x,size_y = 800,600
speed = 100
clock = py.time.Clock()
screen = py.display.set_mode((size_x,size_y))
color_screen = (255,255,255)
color_circle =(0,0,0)
x_circle,y_circle = 0,390
flagtarget =0
speed_y =-4

point = 0

x1,y1 =1000,350
r1,t1=7,50
rn1=r.randint(20,50)

x2,y2 =2000,350
r2,t2=10,50
rn2=r.randint(100,150)

font1=py.font.Font(None,100)
font2=py.font.Font(None,40)
font3=py.font.Font(None,150)
font4_youlost =py.font.Font(None,200)
font5 = py.font.Font(None,70)

color=(r.randint(0,250),r.randint(0,250),r.randint(0,250))
py.display.set_caption("Remin")

while run:
    screen.fill((color_screen))
    if point < 250:
        color_screen = (255-(point*2),255-(point*2),255-(point*2))

    for event in py.event.get():
        if event.type==py.QUIT:
            run = False
        if event.type==py.MOUSEBUTTONDOWN:
            flag_event =True
            if flag_start==False:
                flag_start=True

    key = py.key.get_pressed()
    if flag_start==True:
        flagkey = True

    if flag_start==False:
        text = font1.render("start Game !",True,(10,10,25),(220,220,220))
        text2=font2.render("click",True,(25,30,25),(240,240,240))
        screen.blit(text,(190,260))
        screen.blit(text2,(330,330))

    if flag_start==True:
        text3 =font3.render(f"{point}",True,(50,240,50),(250,250,250))
        screen.blit(text3,(330,150))

    if flagkey==True:
        ############################################################
        py.draw.circle(screen,(color_circle),(x_circle,y_circle),10)
        py.draw.line(screen,(0,0,0),(0,400),(800,400),2)
        flagtarget+=1
        if flagtarget < 200:
            x_circle+=1
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  
        target1=py.draw.rect(screen,(color),py.Rect(x1+rn1,y1,r1,t1))
        x1-=1.5
        if x1+rn1 < -50:
            x1=800
            rn1=r.randint(1,1000)
            y1=r.randint(330,380)
            r1=r.randint(2,9)
            t1=abs(y1-400)
            color=(r.randint(0,200),r.randint(0,200),r.randint(0,200))
            point+=1

        target2=py.draw.rect(screen,(color),py.Rect(x2+rn2,y2,r2,t2))
        x2-=1.5
        if x2+rn2 < -50:
            x2=800
            rn2=r.randint(2000,2500)
            y2=r.randint(330,380)
            r2=r.randint(2,10)
            t2=abs(y2-400)
            color=(r.randint(50,250),r.randint(50,250),r.randint(50,250))
            point+=1
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
        if flag_event==True:
                if flag_jump==False and flag_end==False:
                    flag_jump=True
                if flag_jump==True:
                    if y_circle > 220 :
                        y_circle+=speed_y
                        if y_circle==230:
                            flag_jump=False
                            flag_end=True
                if flag_end==True:
                    print(flag_end,y_circle)
                    y_circle+=4
                    if y_circle > 387:
                        flag_end=False
                        flag_event=False
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ball1 = py.Rect(x_circle-10,y_circle-10,20,20)
        
        if ball1.colliderect(target1) or ball1.colliderect(target2):
            time.sleep(0.5)
            textyoulost = font4_youlost.render("YOU LOST",True , (250,20,100),(40,40,40))
            textend = font5.render("-_-",True,(0,0,0))
            screen.fill((150,150,150))
            screen.blit(textyoulost,(50,250))
            screen.blit(textend,(350,400))
            point=0
               
    py.display.flip() 
    clock.tick(((point)*4)+200)
py.quit()
