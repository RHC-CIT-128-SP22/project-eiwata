#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame
from pygame import mixer
from pygame.locals import *

#initialize game
pygame.init()
mixer.init()

#load display and audio
icon = pygame.image.load("pictures/icon.png")
startBG = pygame.image.load("pictures/startBG.png")
title = pygame.image.load("pictures/mainTitle.png")
startButtonWhite = pygame.image.load("pictures/startButtonWhite.png")
startButton = pygame.image.load("pictures/startButton.png")
opening = mixer.music.load("audio/BeforeDawn.wav")

#set display and audio
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The Call of Cthulhu - Survival Horror Game")
pygame.display.set_icon(icon)
mixer.music.set_volume(0.1)

#sound effects
startSound = pygame.mixer.Sound("audio/wildBeastRoar.wav")

#play background music
mixer.music.play(-1)


#####################  FUNCTION DEFINITIONS  #####################
def game_intro():
    screen.blit(startBG, (0,70))
    screen.blit(title, (40, 50))
    screen.blit(startButtonWhite, (350, 470))
     
def start_selection():

    if event.type == pygame.MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
        #set variables for mouse position
        mx, my = pygame.mouse.get_pos()
        
        #if mouse hovering over start button position
        if mx in range(350, 450) and my in range(470, 510):
            #change start button
            screen.blit(startButton, (350, 470))

            #if left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(startSound)

            
#################  END OF FUNCTION DEFINITIONS  ###################


#########################  MAIN GAME LOOP  #########################
running = True
while running:

    #window stays open until user quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game_intro()
    start_selection()

    pygame.display.update()

##########################  EXIT GAME LOOP  ########################

#stop background music
mixer.music.stop()