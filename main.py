#import time, random, sys, math, pg
import entity
import scavver
#import threading
#import colored
from pg.locals import QUIT
import pygame as pg
import time
import random
#import turtle
import sys
import math
pg.init()
pg.font.init()
class text:
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   END = '\033[0m'
win = pg.display.set_mode((680, 340))
pg.display.set_caption('Scrapnel')
icon = pg.image.load("assets/download4.png")
title = pg.image.load("assets/titletxt.png")
pg.display.set_icon(icon)
#pg.display.set_caption('Hello World!')
clock = pg.time.Clock()
basicdirt = pg.image.load("assets/bestdirt2.png")
#basicdirt = pg.Surface((886,886))
while True:
  for event in pg.event.get():
    if event.type == pg.KEYDOWN:
      # or event.type == pg.KEYUP:
        print("Key: ", str(event.key))
        if event.type == pg.QUIT:
            #or esc
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == 27:
              pg.quit()
              exit()
        if event.type == pg.KEYDOWN:
            if event.key == 9:
                pg.display.toggle_fullwin()
        #timed events (spawning new entities, etc)        
        #update each entityw
        #draw win
        win.blit(basicdirt,(0,0))
        win.blit(title,(0.2,0.2))
        pg.display.update()
        clock.tick(20)
        while True:
            width=win.get_width()
            height = win.get_height()
            mouse=pg.mouse.get_pos()
    if showmousecors == True:
        smalltxt(mouse,670,570)
    global ev
    ev = pg.event.get()
    for event in ev:
        if event.type == pg.KEYDOWN:
        lastkey=event.key
        for x in range(0, 1, 1):
            if lastkey == pg.K_SPACE:
                running = True
                runtog = True
                titl("Welcome To CritterSim v0.1")
                Fsize = 32
                getpet()
        if event.key == pg.K_TAB:
            pg.display.toggle_fullwin() 
            global FStog
            FStog = True
        elif event.key == pg.K_ESCAPE:
            pg.quit()
            running = False
            exit("You Quit")
            sys.exit  
        elif event.key == pg.K_KP_PERIOD:
            print('Showing Logo ')
            logov01= ("Assets\critv0.1.png")
            window.blit(logov01, (0, 0))
        
        elif event.key == pg.K_LALT:
          print('updating')
          titl('updating...')
          time.sleep(3)
          titl('')
          update()
          srf.fill(bgclr,None,0)
        
        elif event.key == toggledevkey:
        #devmode()
          dev=true
          print("devmode+")
      elif event.type == pg.QUIT:
        pg.quit()
        running = False
        exit("You Quit")
        sys.exit()
    update()
