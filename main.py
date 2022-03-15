#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

#modules
import pygame
from pygame import mixer

#initialize the pygame
pygame.init()
mixer.init()

#create the screen and set volume
screen = pygame.display.set_mode((800, 600))
mixer.music.set_volume(0.8)

#set title and icon (for window)
pygame.display.set_caption("The Call of Cthulhu - Survival Horror Game")
icon = pygame.image.load("pictures/icon.png")
pygame.display.set_icon(icon)

#load audio and pictures
startBG = pygame.image.load("pictures/startBG.png")
title = pygame.image.load("pictures/mainTitle.png")
startButton = pygame.image.load("pictures/startButton.png")
opening = mixer.music.load("audio/BeforeDawn.wav")

#play background music
mixer.music.play(-1)

###############  MAIN GAME LOOP  ################
running = True
while running:

    #window stays open until user quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #start game display
    screen.blit(startBG, (0,70))
    screen.blit(title, (40, 50))
    screen.blit(startButton, (350, 470))

    pygame.display.update()

################  EXIT GAME LOOP ################

#stop background music
mixer.music.stop()