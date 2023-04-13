import time, random, sys, math, pygame, turtle
import entity
#import threading
#import colored

from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((680,340))
pygame.display.set_caption('Scrapnel')
icon = pygame.image.load("assets/download4.png")
title = pygame.image.load("assets/titletxt.png")

pygame.display.set_icon(icon)
#pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
basicdirt =  pygame.image.load("assets/bestdirt2.png")
#basicdirt = pygame.Surface((886,886))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
        # or event.type == pygame.KEYUP:
            print("Key: ",str(event.key))
        if event.type == pygame.QUIT:
            #or esc
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                pygame.quit()
                exit()
        if event.type == pygame.KEYDOWN:
            if event.key == 9:
                pygame.display.toggle_fullscreen()
    screen.blit(basicdirt,(0,0))
    screen.blit(title,(0.2,0.2))
    pygame.display.update()
    clock.tick(20)
    