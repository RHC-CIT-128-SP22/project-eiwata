#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''


import pygame
from pygame import mixer
#import time

#initialize game
pygame.init()
mixer.init()

#load display and audio
icon = pygame.image.load("pictures/icon.png")
startBG = pygame.image.load("pictures/startBG.png")
title = pygame.image.load("pictures/mainTitle.png")
startButton = pygame.image.load("pictures/startButton.png")
opening = mixer.music.load("audio/BeforeDawn.wav")

#set display and audio
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The Call of Cthulhu - Survival Horror Game")
pygame.display.set_icon(icon)
mixer.music.set_volume(0.7)

#sound effects
startSound = pygame.mixer.Sound("audio/wildBeastRoar.wav")

#play background music
mixer.music.play(-1)

def game_intro():
    #start game display
    screen.blit(startBG, (0,70))
    screen.blit(title, (40, 50))
    screen.blit(startButton, (350, 470))
     

###############  MAIN GAME LOOP  ################
running = True
while running:

    #window stays open until user quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game_intro()

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        pygame.mixer.Sound.play(startSound)

    pygame.display.update()

################  EXIT GAME LOOP ################


#stop background music
mixer.music.stop()