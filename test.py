# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:53:58 2022

@author: danyz
"""
import pygame, sys
from pygame.locals import *
pygame.init()
def main():
    DISPLAY=pygame.display.set_mode((640,640))
    WHITE=(255,255,255)
    BROWN=(160,82,45)
    DISPLAY.fill(BROWN)
    queen = pygame.image.load("bQ.png")
    queen = pygame.transform.scale(queen, (70,70))
    for x in range(8):
        for y in range(8):
            if (x%2 == 0 and y%2 == 0) or (x%2 == 1 and y%2 == 1):
                pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(80*x,80*y,80,80))
    DISPLAY.blit(queen, (5, 5))
while(True):
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    main()
    pygame.display.update()
    
    
