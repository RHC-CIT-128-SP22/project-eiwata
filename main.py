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

#Game Loop
running = True
while running:

    #window stays open until user quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #black rgb background
    screen.fill((0, 0, 0))
    pygame.display.update()
