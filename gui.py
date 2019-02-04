import pygame
import time
import os, sys, math, pygame, pygame.font, pygame.image
from pygame.locals import *
import utils
import random
import greedy1
import animate

#insialisasi pywindow
pygame.font.init()
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption("24 gamee")

#load background image
jokerImg = pygame.image.load('assets/joker1.png')
jackImg = pygame.image.load('assets/kartu.png')


#warna
red = (200,0,0)
gray = (128,128,128)
white = (255,255,255)
silver= (192,192,192)
navy =[0,0,128]
black =[0,0,0]


#text welcome 
class textWavey:
    def __init__(self, font, message, fontcolor, amount=10):
        self.base = font.render(message, 0, fontcolor)
        self.steps = range(0, self.base.get_width(), 2)
        self.amount = amount
        self.size = self.base.get_rect().inflate(0, amount).size
        self.offset = 0.0
        
    def animate(self):
        s = pygame.Surface(self.size)
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
    pygame.display.flip()

#layar dua
def jack(x,y,a,b):
    screen.blit(jackImg, (x,y))  
    cardI = pygame.image.load('assets/back1.png').convert()
    eks = pygame.image.load('assets/eks.png')
    score =pygame.image.load('assets/nilai.png')
    poinI = pygame.image.load('assets/poin.png')
    screen.blit(cardI,(a,b))
    screen.blit(eks,(150,550))
    screen.blit(score,(100,50))
    screen.blit(poinI,(450,50))
    pygame.display.flip() 

#ending
def ending(x,y):
    endI = animate.GIFImage("assets/end.gif")
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        screen.fill((255,255,255))
        endI.render(screen, (0, 0))
        pygame.display.flip()

#untuk kartu
def card (x,nilai):
    shape = ['S','H','D','C']
    s = random.choice(shape)
    nilai=str(nilai)
    cardImg =pygame.image.load('assets/'+s+nilai+'.gif')
    screen.blit(cardImg, (x,400))
    pygame.display.flip()

#untuk kalimat
def message_display(text,x,y):
    a = pygame.font.SysFont('Times New Roman',35)
    TextSurf, TextRect = text_objects(text,a)
    TextRect.center =(x,y)
    screen.blit(TextSurf, TextRect)
    pygame.display.flip()

#def score (text):
    


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
    if len(deck)>0:
            out = utils.pick4card(deck)
            poin ,ekspresi= greedy1.calculate(out[0])
           
            total+=poin
            deck = out[1]
            x= 100
            for i in range(4):
                card(x,out[0][i])
                x+=200
            print(out[0])
            return [False,out[1],total,ekspresi]
                
    else:
            return [True,[],total,None]


def game_intro():
    bigfont = pygame.font.SysFont(None, 60)
    renderer = textWavey(bigfont, entry_info, white, 14)
    text = renderer.animate()
    intro = True
    
    while intro:   
        pygame.time.delay(40)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        x = (width*0.001)
        y = (height*0.001)
        joker(x,y)
        text = renderer.animate()
        screen.blit(text, (300, 400))
        button('Start',350,480,100,50,gray,silver,game_loop)
        pygame.display.flip()


def game_loop():
    x = (width*0.001)
    y = (height*0.001)
    a = 350 # x coordinate of card
    b = 200 # y coordinate of card
   
    jack(x,y,a,b)
   
    cardI = pygame.image.load('assets/back1.png').convert()
    screen.blit(cardI,(a,b))
    pygame.display.flip()   

    deck = utils.getNewDeck()

    gameExit = False
    poin = 0
    while not gameExit:       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if a+50 > mouse[0] > a and b+80 > mouse[1] > b:
                cardI = pygame.image.load('assets/back2.png').convert()
                screen.blit(cardI,(a,b))
                pygame.display.flip()  
                if click[0]==1 :
                    #print('clicked on image')
                    gameExit,deck,poin,ekspresi=pick_Card(deck,poin)
                    if(not gameExit):''
                        poin_s=utils.countScore(ekspresi)
                        message_display(ekspresi,400,575)
                        message_display(str(poin_s),500,70)
                        #print("poin : %d" % poin)
                        message_display(str(poin),150,70) 
                        pygame.time.delay(1000)        
                
            jack(x,y,a,b)            
    if gameExit:
        ending(800,600)
       

       

entry_info = 'Welcome..'

if __name__ == '__main__':
    game_intro()
