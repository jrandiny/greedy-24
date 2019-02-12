import pygame
import time
import os, sys, math, pygame, pygame.font, pygame.image
from pygame.locals import Rect
import utils
import random
import greedy1
#import animate
import abc

#load background image

jackImg = pygame.image.load('assets/kartu.png')

#global var
lastDeck = []
lastDeckSym = []
repickShape = True

state = 1

#warna

gray = (128,128,128)
white = (255,255,255)
silver= (192,192,192)
navy =(0,0,128)
black =(0,0,0)
cyan=(0,255,255)
aqua =(127,255,212)


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
        self.offset += 0.1
        for step in self.steps:
            src = Rect(step, 0, 2, height)
            dst = src.move(0, math.cos(self.offset + step*.02)*self.amount)
            s.blit(self.base, dst, src)
        return s

class screen(abc.ABC):
    @abc.abstractmethod
    def loop(self):
        pass

class introScreen(screen):
    def __init__(self):
        bigfont = pygame.font.SysFont(None, 60)
        self.renderer = textWavey(bigfont, 'Welcome..', white, 14)

    def switchToMain(self):
        global state
        state = 2

    def loop(self):
        x = (width*0.001)
        y = (height*0.001)
        jokerImg = pygame.image.load('assets/joker1.png')
        screen.blit(jokerImg, (x,y))
        text = self.renderer.animate()
        
        screen.blit(text, (300, 400))
        button('Start',350,480,100,50,gray,silver,self.switchToMain)

class mainScreen(screen):
    def __init__(self,deck):
        self.prog = -99
        self.cardHover = False
        self.repickShape = True
        self.lastDeck = deck
        self.lastDeckSym = []
        self.ekspresi = ""
        self.poin = 0

        self.cardX = 350
        self.cardY = 200

        self.eks = pygame.image.load('assets/eks.png')
        self.score =pygame.image.load('assets/nilai.png')
        self.poinI = pygame.image.load('assets/poin.png')

        self.cardIBack1 = pygame.image.load('assets/back1.png').convert()
        self.cardIBack2 = pygame.image.load('assets/back2.png').convert()

        self.endI = pygame.image.load("assets/end.gif")

    def switchToEnd(self):
        global state
        state = 3

    def updateParam(self,deck,poin, ekspresi):
        self.poin = poin
        self.ekspresi = ekspresi
        self.lastDeck = deck
        self.repickShape = True
        self.prog = 0

    def animateSys(self,prog):
        targetPosX = [-300,-100,100,300]
        targetPosY = 200

        originPosX = 350
        originPosY = 200
        if (len(self.lastDeck)>0):
            if(self.repickShape):
                self.lastDeckSym = ['S','H','D','C']
                for i in range(1,4):
                    shape = ['S','H','D','C']
                    s = random.choice(shape)
                    self.lastDeckSym[i] = s
                self.repickShape = False
        
            for i in range(1,5):
                x = originPosX + (targetPosX[i-1]) * (prog/100.0)
                y = originPosY + (targetPosY) * (prog/100.0)
                card(x,y,self.lastDeck[i-1],self.lastDeckSym[i-1])
        else:
            x = (width*0.001)
            y = (height*0.001)
            screen.blit(jackImg, (x,y))
            button('Reshuffle',350,300,100,50,cyan,aqua,game_loop)
            button('Exit ?',350,500,100,50,cyan,aqua,self.switchToEnd)
            


            


    def loop(self):
        x = (width*0.001)
        y = (height*0.001)
        cardX = 350 # x coordinate of card
        cardY = 200 # y coordinate of card

        screen.blit(jackImg, (x,y))  
        if self.cardHover:
            cardI = self.cardIBack2
        else:
            cardI = self.cardIBack1

        screen.blit(cardI,(cardX,cardY))
        screen.blit(self.eks,(150,550))
        screen.blit(self.score,(100,50))
        screen.blit(self.poinI,(450,50))

        poin_s=utils.countScore(self.ekspresi)
        message_display(self.ekspresi,400,575)
        message_display(str(round(poin_s,2)),500,70)
        message_display(str(round(self.poin,2)),150,70) 

        if(self.prog!=-99):
            if(self.prog<100):
                self.prog+=1
                
            self.animateSys(self.prog)
       
            

    def eventLoop(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.cardX+50 > mouse[0] > self.cardX and self.cardY+80 > mouse[1] > self.cardY:
            self.cardHover = True
            
            if click[0]==1 :
                _,deck,poin,ekspresi=pick_Card(self.lastDeck,self.poin)
                self.updateParam(deck,poin,ekspresi)
        else:
            self.cardHover = False

class endingScreen(screen):
    def __init__(self):
        self.endI = pygame.image.load("assets/end.gif")

    def switchToM(self):
        global state
        state = 2

    def loop(self):
        x = (width*0.001)
        y = (height*0.001)
        screen.blit(self.endI, (x,y))       
        button('Bye',150,330,100,50,navy,cyan,quit)
        button('Play again',450,330,100,50,navy,cyan,self.switchToM)
        
    
        

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

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

def game_loop():
    global state
    
    deck = utils.getNewDeck()

    intro = introScreen()
    main = mainScreen(deck)
    end = endingScreen()
    
    while 1:  
        if(state == 1):
            intro.loop()
        elif(state == 2):
            main.loop()
        elif(state == 3):
            end.loop()
           

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if(state == 2):
                main.eventLoop()
            
           
            
            
                
                
            
        pygame.display.flip()           

if __name__ == '__main__':
    #insialisasi pywindow
    pygame.font.init()
    (width, height) = (800, 600)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    pygame.display.set_caption("24 game")
    game_loop()
    
