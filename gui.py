import pygame
import time
import os, sys, math, pygame, pygame.font, pygame.image
from pygame.locals import Rect
import utils
import random
import greedy1
import animate

#load background image
jokerImg = pygame.image.load('assets/joker1.png')
jackImg = pygame.image.load('assets/kartu.png')

#global var
lastDeck = []
lastDeckSym = []
repickShape = True

cardHover = False

#warna
red = (200,0,0)
gray = (128,128,128)
white = (255,255,255)
silver= (192,192,192)
navy =(0,0,128)
black =(0,0,0)


#text welcome 
class textWavey:
    def __init__(self, font, message, fontcolor, amount=10):
        self.base = font.render(message, 0, fontcolor)
        self.steps = range(0, self.base.get_width(), 2)
        self.amount = amount
        self.size = self.base.get_rect().inflate(0, amount).size
        self.offset = 0.0
        
    def animate(self):
        s= pygame.Surface(self.size)
        s.set_colorkey((0,0,0))
        height = self.size[1]
        self.offset += 0.5
        for step in self.steps:
            src = Rect(step, 0, 2, height)
            dst = src.move(0, math.cos(self.offset + step*.02)*self.amount)
            s.blit(self.base, dst, src)
        return s

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#layar satu
def joker(x,y):
    screen.blit(jokerImg, (x,y))

#layar dua
def jack(x,y,a,b):
    global cardHover

    screen.blit(jackImg, (x,y))  
    if cardHover:
        cardI = pygame.image.load('assets/back2.png').convert()
    else:
        cardI = pygame.image.load('assets/back1.png').convert()
        
    eks = pygame.image.load('assets/eks.png')
    score =pygame.image.load('assets/nilai.png')
    poinI = pygame.image.load('assets/poin.png')
    screen.blit(cardI,(a,b))
    screen.blit(eks,(150,550))
    screen.blit(score,(100,50))
    screen.blit(poinI,(450,50))

#ending
def ending(x,y):
    endI = animate.GIFImage("assets/end.gif")
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((255,255,255))
        endI.render(screen, (0, 0))
        pygame.display.flip()

#untuk kartu
def card (x,y,nilai,s):
    nilai=str(nilai)
    cardImg =pygame.image.load('assets/'+s+nilai+'.gif')
    screen.blit(cardImg, (x,y))

#untuk kalimat
def message_display(text,x,y):
    a = pygame.font.SysFont('Times New Roman',35)
    TextSurf, TextRect = text_objects(text,a)
    TextRect.center =(x,y)
    screen.blit(TextSurf, TextRect)

#start button atau button lain 
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

#untuk ambil kartu
def pick_Card(deck,total):
    global lastDeck

    if len(deck)>0:
            out = utils.pick4card(deck)
            poin ,ekspresi= greedy1.calculate(out[0])

            total+=poin

            lastDeck = out[0]
            
            print(out[0])
            return [False,out[1],total,ekspresi]
                
    else:
            return [True,[],total,None]


def game_intro():
    bigfont = pygame.font.SysFont(None, 60)
    renderer = textWavey(bigfont, 'Welcome..', white, 14)
    text = renderer.animate()
    intro = True
    
    while intro:   
        pygame.time.delay(40)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        x = (width*0.001)
        y = (height*0.001)
        joker(x,y)
        text = renderer.animate()
        screen.blit(text, (300, 400))
        button('Start',350,480,100,50,gray,silver,game_loop)
        pygame.display.flip()

def animateSys(prog):
    global lastDeckSym
    global repickShape
    global lastDeck

    targetPosX = [-300,-100,100,300]
    targetPosY = 200

    originPosX = 350
    originPosY = 200

    if(repickShape):
        lastDeckSym = ['S','H','D','C']
        for i in range(1,4):
            shape = ['S','H','D','C']
            s = random.choice(shape)
            lastDeckSym[i] = s
        repickShape = False

    for i in range(1,5):
        x = originPosX + (targetPosX[i-1]) * (prog/100.0)
        y = originPosY + (targetPosY) * (prog/100.0)
        card(x,y,lastDeck[i-1],lastDeckSym[i-1])

def game_loop():
    global repickShape
    global cardHover

    ekspresi = ""
    poin = 0


    x = (width*0.001)
    y = (height*0.001)
    a = 350 # x coordinate of card
    b = 200 # y coordinate of card
    jack(x,y,a,b)

    pygame.display.flip()   

    deck = utils.getNewDeck()

    gameExit = False
    poin = 0
    prog = -99
    while not gameExit:  
        jack(x,y,a,b) 
        if(prog!=-99):
            if(prog<100):
                prog+=1
            else:
                poin_s=utils.countScore(ekspresi)
                message_display(ekspresi,400,575)
                message_display(str(poin_s),500,70)
                message_display(str(poin),150,70) 
            animateSys(prog)

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            if a+50 > mouse[0] > a and b+80 > mouse[1] > b:
                cardHover = True
                
                if click[0]==1 :
                    #print('clicked on image')
                    gameExit,deck,poin,ekspresi=pick_Card(deck,poin)
                    repickShape = True
                    prog = 0

            else:
                cardHover = False
            

        pygame.display.flip()           
    if gameExit:
        ending(800,600)

if __name__ == '__main__':
    #insialisasi pywindow
    pygame.font.init()
    (width, height) = (800, 600)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    pygame.display.set_caption("24 game")
    game_intro()
