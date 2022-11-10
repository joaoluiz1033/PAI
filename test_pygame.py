# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:25:33 2022

@author: joao-luiz.de-oliveir
"""

import pygame, sys
from pygame.locals import *

    pygame.init()

    DISPLAY=pygame.display.set_mode((640,640))
    running=True
    moving=False
  

    WHITE=(255,255,255)
    BLACK=(0,0,0)
    rook = pygame.image.load("rook.jpg")
    rook = pygame.transform.scale(rook, (60,60))
    for x in range(8):
        for y in range(8):
                if ((x%2==0) and (y%2==0)) or ((x%2==1) and (y%2==1)):
                    pygame.draw.rect(DISPLAY,WHITE,pygame.Rect(80*x,80*y, 80, 80))
    DISPLAY.blit(rook, (10, 10))
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
            elif event.type == MOUSEBUTTONUP:
                moving = False
 
        # Make your image move continuously
            elif event.type == MOUSEMOTION and moving:
                rect.move_ip(event.rel)
        pygame.display.update()

main()

