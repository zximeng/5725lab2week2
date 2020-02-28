import pygame
from pygame.locals import *   # for event MOUSE variables
import os
import time
import RPi.GPIO as GPIO
def displaycollide():
    size = width, height = 320, 240 
    speed = [2,2]
    speed1 = [-1,-1] 
    inits = [0,10]
    inits1 = [200,10]
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("magic_ball.png")
    ballrect = ball.get_rect()

    ballrect = ballrect.move(inits)
    ball1 = pygame.image.load("soccer_ball.png")
    ballrect1 = ball1.get_rect()
    ballrect1 = ballrect1.move(inits1)

    start = time.time()
    flag1 = True  # global flag
    ballrect1.move(inits1)

    while (flag1):    
        ballrect = ballrect.move(speed)    
        if ballrect.left < 0 or ballrect.right > width:       
            speed[0] = -speed[0]    
        if ballrect.top < 0 or ballrect.bottom > height:     
            speed[1] = -speed[1]
        ballrect1 = ballrect1.move(speed1)    
        if ballrect1.left < 0 or ballrect1.right > width:       
            speed1[0] = -speed1[0]    
        if ballrect1.top < 0 or ballrect1.bottom > height:     
            speed1[1] = -speed1[1]
        if (ballrect.colliderect(ballrect1) == True):
            tmp,tmp1 = speed1[0],speed1[1]
            speed1[0] = speed[0]
            speed1[1] = speed[1]
            speed[0] = tmp
            speed[1] = tmp1
        time.sleep(0.01)
        screen.fill(black)               # Erase the Work space   
        screen.blit(ball, ballrect)   # Combine Ball surface with workspace 
        screen.blit(ball1, ballrect1)

        if(not time.time() - start < 10):
            flag1 = False
        if(not GPIO.input(27)):
            flag1 = False
        pygame.display.flip()
        for event in pygame.event.get():
            if(event.type is MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos() 
                x,y = pos
                if y > 120:                
                    if x < 160:    
                        print ('quit button pressed')
                        flag1 = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)   
os.putenv('SDL_VIDEODRIVER', 'fbcon')   # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1')     
os.putenv('SDL_MOUSEDRV', 'TSLIB')     # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
pygame.init()
pygame.mouse.set_visible(False)
WHITE = 255, 255, 255
BLACK = 0,0,0
green = (0, 255, 0) 
blue = (0, 0, 128) 
screen = pygame.display.set_mode((320, 240))
my_font= pygame.font.Font(None, 50)
my_buttons= { 'quit':(80,180), 'start':(240,180)}


start = time.time()

flag = True
while flag:       
    for event in pygame.event.get():        
        if(event.type is MOUSEBUTTONDOWN):            
            pos = pygame.mouse.get_pos()           
        elif(event.type is MOUSEBUTTONUP):
            screen.fill(BLACK)               # Erase the Work space     
            for my_text, text_pos in my_buttons.items():    
                text_surface = my_font.render(my_text, True, WHITE)    
                rect = text_surface.get_rect(center=text_pos)
                screen.blit(text_surface, rect)            
            pos = pygame.mouse.get_pos() 
            x,y = pos
            toprint = str(x) + ',' + str(y)
            text = my_font.render(toprint, True, WHITE)
            textRect = text.get_rect(center=(160,120))  
            screen.blit(text, textRect)
            pygame.display.flip()
            print(toprint)
            os.system("scrot")          
            if y > 120:                
                if x < 160:    
                    print ('quit button pressed')
                    flag = False
                else:
                    displaycollide()
                    

                    

    if(not time.time() - start < 30):
		flag = False
    if(not GPIO.input(27)):
		flag = False


