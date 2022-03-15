#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

#modules
import pygame

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("The Call of Cthulhu - Survival Horror Game")
icon = pygame.image.load('cthulhu.png')
pygame.display.set_icon(icon)

#background image and title
background = pygame.image.load("cthulhuBackground.png")
title = pygame.image.load("title.png")
startButton = pygame.image.load("start.png")

#Game Loop
running = True
while running:

    #window stays open until user quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #beginnging game display
    screen.blit(background, (0,70))
    screen.blit(title, (40, 50))
    screen.blit(startButton, (350, 470))
    pygame.display.update()
