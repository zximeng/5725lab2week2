import pygame
from pygame.locals import *   # for event MOUSE variables
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)   
# os.putenv('SDL_VIDEODRIVER', 'fbcon')   # Display on piTFT
# os.putenv('SDL_FBDEV', '/dev/fb1')     
# os.putenv('SDL_MOUSEDRV', 'TSLIB')     # Track mouse clicks on piTFT
# os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
pygame.init()
pygame.mouse.set_visible(True)
WHITE = 255, 255, 255
BLACK = 0,0,0
green = (0, 255, 0) 
blue = (0, 0, 128) 
screen = pygame.display.set_mode((320, 240))
my_font= pygame.font.Font(None, 50)
my_buttons= { 'quit':(80,180)}
screen.fill(BLACK)               # Erase the Work space     
for my_text, text_pos in my_buttons.items():    
    text_surface = my_font.render(my_text, True, WHITE)    
    rect = text_surface.get_rect(center=text_pos)
    screen.blit(text_surface, rect)
pygame.display.flip()
start = time.time()

flag = True
while flag:       
    for event in pygame.event.get():        
        if(event.type is MOUSEBUTTONDOWN):            
            pos = pygame.mouse.get_pos()           
        elif(event.type is MOUSEBUTTONUP):            
            pos = pygame.mouse.get_pos() 
            x,y = pos
            toprint = str(x) + ',' + str(y)
            text = my_font.render(toprint, True, WHITE)
            textRect = text.get_rect(center=(160,120))  
            screen.blit(text, textRect)
            pygame.display.flip()
            print(toprint)          
            if y > 120:                
                if x < 160:    
                    print ('quit button pressed')
                    flag = False

    if(not time.time() - start < 30):
		flag = False
    if(not GPIO.input(27)):
		flag = False