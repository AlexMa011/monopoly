from player import *
from cell import *
import pygame
from pygame.locals import *
from sys import exit
import random
import os
import profile

#import all the sources
background_image_filename='sources/background.jpg'
player1_image_filename='sources/1.jpg'
player2_image_filename='sources/2.jpg'
player1_person_filename='sources/1c.png'
player2_person_filename='sources/2c.png'

#initialize the game member

a=player('WuXie',player1_image_filename)
b=player('XiaoGe',player2_image_filename)
a.money,b.money=2000,8000
a.bonus,b.bonus=200,100
a.diamond,b.diamond=3,0
a.star,b.star=4,0
a.overdraft,b.overdraft=500,100
a.label,b.label=1,2
players=[a,b]



#initialize the map

zones=['0']
for i in range(0,5):
    zones.append(zone())

zones[1].money,zones[2].money,zones[3].money,zones[4].money,zones[5].money=300,600,1000,0,0
zones[1].diamond,zones[2].diamond,zones[3].diamond,zones[4].diamond,zones[5].diamond=1,3,2,4,2
zones[1].size,zones[2].size,zones[3].size,zones[4].size,zones[5].size=2,5,5,5,2
zones[1].x,zones[2].x,zones[3].x,zones[4].x,zones[5].x=320,480,80,0,80
zones[1].y,zones[2].y,zones[3].y,zones[4].y,zones[5].y=0,80,480,80,0
zones[1].direction,zones[2].direction,zones[3].direction,zones[4].direction,zones[5].direction='h','v','h','v','h'
zones[1].name,zones[2].name,zones[3].name,zones[4].name,zones[5].name='zone1','zone2','zone3','zone4','zone5'

zone1=[]
zone2=[]
zone3=[]
zone4=[]
zone5=[]

for i in range(0,5):
    zone2.append(cell(zones[2]))
    zone2[i].y+=80*i
    zone4.append(cell(zones[4]))
    zone4[i].y=zone4[i].area.y+80*(4-i)
    zone3.append(cell(zones[3]))
    zone3[i].x=zone3[i].area.x+80*(4-i)
    if(i<2):
        zone1.append(cell(zones[1]))
        zone1[i].x+=80*i
        zone5.append(cell(zones[5]))
        zone5[i].x+=80*i

bank1=bank()
s1=supermarket()
s2=supermarket()
s3=supermarket()
s4=supermarket()
s1.x=480
s1.y=0
s2.x=480
s2.y=480
s3.x=0
s3.y=480
houses=['0']
road=[bank1]+zone1+[s1]+zone2+[s2]+zone3+[s3]+zone4+[s4]+zone5

#initialize the game window
pygame.init()
screen=pygame.display.set_mode((560,560),0,32)
pygame.display.set_caption("monopoly")

font=pygame.font.SysFont("Segoe Script",16)
font_height=font.get_linesize()
font_dice=pygame.font.SysFont("arial",60)
font_dice_height=font.get_linesize()


#set the image sources
background=pygame.image.load(background_image_filename).convert()
player1=pygame.image.load(player1_image_filename).convert()
player2=pygame.image.load(player2_image_filename).convert()
a.person=pygame.image.load(player1_person_filename).convert_alpha()
b.person=pygame.image.load(player2_person_filename).convert_alpha()
for x in range(1,6):
    a.pictures['zone'+str(x)]=pygame.image.load('sources/1-'+str(x)+'.jpg').convert()
    b.pictures['zone'+str(x)]=pygame.image.load('sources/2-'+str(x)+'.jpg').convert()
for x in range(1,4):
    houses.append(pygame.image.load('sources/house'+str(x)+'.png').convert_alpha())




def show():
    screen.blit(background,(0,0))
    screen.blit(player1,(230,130))
    screen.blit(player2,(360,130))
    for zone in zones[1:]:
            if(zone.owner!=0):
                if(zone.direction=='v'):
                    y_cell=zone.y
                    for c in range(0,zone.size):
                        screen.blit(zone.owner.pictures[zone.name],(zone.x,y_cell))
                        y_cell+=80
                elif(zone.direction=='h'):
                    x_cell=zone.x
                    for c in range(0,zone.size):
                        screen.blit(zone.owner.pictures[zone.name],(x_cell,zone.y))
                        x_cell+=80
    for p in players:
        y=220
        for text in p.__dict__:
            if (text=='name' or text=='diamond' or text=='star' or text=='money' or text=='house'):
                screen.blit(font.render(text,True,(0,0,0)),(150,y))
                screen.blit(font.render(str(p.__dict__[text]),True,(0,0,0)),(230+130*(p.label-1),y))
                y+=font_height
    for q in road:
        if(q.__class__==cell):
            if(q.grade==1):
                screen.blit(houses[1],(q.x,q.y+30))
            elif(q.grade==2):
                screen.blit(houses[2],(q.x,q.y+30))
            elif(q.grade==3):
                screen.blit(houses[3],(q.x,q.y+30))


def show_pos(a):
    for p in players:
        if(p!=a):
            screen.blit(p.person,(road[p.position].x,road[p.position].y))

def input(event):
    if event.type==KEYDOWN:
        if event.key==K_y:
            return 'y'
        elif event.key==K_LEFT:
            return 'left'
        elif event.key==K_RIGHT:
            return 'right'

def easy():
    show()
    show_pos(0)
    pygame.display.update()


def main():
    speed=250
    error=1.5
    question=(150,350)
    question2=(150,350+font_height)
    question1=(110,350)
    question3=(150,350+font_height*2)

    easy()
    screen.blit(font.render("click the mouse to throw the dice",True,(0,0,0)),question)
    screen.blit(font.render("the top left will show the number ",True,(0,0,0)),question2)

    clock = pygame.time.Clock()

    change=0
    player=players[0]
#开始游戏！
    while a.money>-a.overdraft and b.money>-b.overdraft:
        for event in pygame.event.get():

            if event.type==QUIT:
                exit()
            elif event.type==MOUSEBUTTONDOWN:
                dice=random.randint(1,6)
                player=players[change]
                change=1-change



                #移动
                player.x=road[player.position].x
                player.y=road[player.position].y

                player.position+=dice
                if(player.position>23):
                    player.position-=24


                clock = pygame.time.Clock()
                #move
                while (abs(player.x-road[player.position].x)>error or abs(player.y-road[player.position].y)>error):

                    show()
                    show_pos(player)
                    screen.blit(font_dice.render(str(dice),True,(0,0,0)),(150,130))
                    screen.blit(player.person,(player.x,player.y))
                    time_passed=clock.tick()
                    time_passed_seconds=time_passed/1000.0
                    distance_moved = time_passed_seconds*speed

                    if(abs(player.y-0)<error and player.x<480):
                        player.x+=distance_moved
                    if(abs(player.x-480)<error and player.y<480):
                        player.y+=distance_moved
                    if(abs(player.y-480)<error and player.x>0):
                        player.x-=distance_moved
                    if(abs(player.x-0)<error and player.y>0):
                        player.y-=distance_moved

                    pygame.display.update()


                easy()


                if(road[player.position].__class__==supermarket):
                    screen.blit(font.render("what do you want to buy? ",True,(0,0,0)),question)
                    screen.blit(font.render("diamond <- or star ->",True,(0,0,0)),question2)
                    pygame.display.update()
                elif(road[player.position].__class__==bank):
                    player.get()

                elif(road[player.position].area.owner==0 and player.money>=road[player.position].money and player.diamond>=road[player.position].diamond):
                    screen.blit(font.render("Do you want buy the area with",True,(0,0,0)),question)
                    screen.blit(font.render('$ '+str(road[player.position].money)+" and "+str(road[player.position].diamond)+" diamonds?",True,(0,0,0)),question2)
                    screen.blit(font.render("Press Y if you would like to ",True,(0,0,0)),question3)
                    pygame.display.update()
                elif(road[player.position].area.owner!=0 and road[player.position].area.owner!=player):
                    screen.blit(font.render("You must pay "+str(road[player.position].area.owner.name)+" "+str(road[player.position].grade*100),True,(0,0,0)),question)
                    player.pay(road[player.position].area.owner,road[player.position])
                    pygame.display.update()

                elif(road[player.position].area.owner==player and road[player.position].grade==0):
                    screen.blit(font.render("Do you want build house with $200? ",True,(0,0,0)),question1)
                    screen.blit(font.render("Press Y if you would like to ",True,(0,0,0)),question2)
                    pygame.display.update()
                elif(road[player.position].area.owner==player and road[player.position].grade>0):
                    screen.blit(font.render("Do you want upgrade the house? ",True,(0,0,0)),question1)
                    screen.blit(font.render("Press Y if you would like to ",True,(0,0,0)),question2)
                    pygame.display.update()


            elif event.type==KEYDOWN:
                if(road[player.position].__class__==supermarket):
                    screen.blit(font.render("what do you want to buy? ",True,(0,0,0)),question)
                    screen.blit(font.render("diamond <- or star ->",True,(0,0,0)),question2)
                    pygame.display.update()
                    ans1=(input(event)=='left')
                    ans2=(input(event)=='right')
                    player.buy_goods(ans1,ans2)
                elif(road[player.position].__class__==bank):
                    player.get()
                elif(road[player.position].area.owner==0 and player.money>=road[player.position].money and player.diamond>=road[player.position].diamond):
                    screen.blit(font.render("Do you want buy the area with",True,(0,0,0)),question)
                    screen.blit(font.render('$ '+str(road[player.position].money)+" and "+str(road[player.position].diamond)+" diamonds?",True,(0,0,0)),question2)
                    screen.blit(font.render("Press Y if you would like to ",True,(0,0,0)),question3)
                    pygame.display.update()
                    ans=(input(event)=='y')
                    player.buy_cell(road[player.position],ans)
                elif(road[player.position].area.owner==player  and road[player.position].grade==0):
                    screen.blit(font.render("Do you want build house with $200 ? ",True,(0,0,0)),question1)
                    screen.blit(font.render("Press Y if you would like to ",True,(0,0,0)),question2)
                    ans=(input(event)=='y')
                    player.build(road[player.position],ans)
                elif(road[player.position].area.owner==player and road[player.position].grade>0):
                    screen.blit(font.render("Do you want upgrade the house? ",True,(0,0,0)),question1)
                    screen.blit(font.render("Press Y if you would like to ",True,(0,0,0)),question2)
                    ans=(input(event)=='y')
                    player.upgrade(road[player.position],ans)
                easy()


            else:
                continue

        pygame.display.update()

main()
