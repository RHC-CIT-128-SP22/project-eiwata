#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame
import time
from pygame import mixer
from pygame.locals import *

#initialize game
pygame.init()
mixer.init()
clock = pygame.time.Clock()

#load display and audio
icon = pygame.image.load("pictures/icon.png")
startBG = pygame.image.load("pictures/startBG.png")
title = pygame.image.load("pictures/mainTitle.png")
startButton = pygame.image.load("pictures/startButton.png")
opening = mixer.music.load("audio/BeforeDawn.wav")

#load more display and audio
portraitScene = pygame.image.load("pictures/portrait.png")
conversation = pygame.image.load("pictures/rectangle.png")

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

class Scene:
    def __init__(self):
        self.scene = 'start_screen'

    def start_screen(self):
        screen.blit(startBG, (0, 70))
        screen.blit(title, (40, 50))
        screen.blit(startButton, (350, 470))
        startButton.set_alpha(150)

        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
            #set variables for mouse position
            mx, my = pygame.mouse.get_pos()
        
            #if mouse hovering over start button
            if mx in range(350, 450) and my in range(470, 510):
                #change start button
                startButton.set_alpha(300)

                #if left click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #pygame.mixer.Sound.play(startSound)
                    self.next_scene()
                    self.scene = 'scene_one'
        pygame.display.update()

    def scene_one(self):
        screen.fill((0,0,0))
        screen.blit(portraitScene, (0, 70))
        screen.blit(conversation, (100, 350))
        font = pygame.font.SysFont('Comic Sans MS', 20)
        text = font.render('[Insert Dialogue]', True, (0, 0, 0))
        screen.blit(text, (170, 370))
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.next_scene()
            self.scene = 'scene_two'
        
    def scene_two(self):
        screen.fill((0,0,0))
        pygame.display.update()
        
    #transition to next scene
    def next_scene(self):
        fade = pygame.Surface((800, 600))
        fade.fill((0, 0, 0))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)

    def scene_manager(self):
        if self.scene == 'start_screen':
            self.start_screen()
        if self.scene == 'scene_one':
            self.scene_one()
        if self.scene == 'scene_two':
            self.scene_two()

#################  END OF FUNCTION DEFINITIONS  ###################

#create object of class
current_game = Scene()

#########################  MAIN GAME LOOP  #########################
running = True
while running:

    #window stays open until user quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #game start
    current_game.scene_manager()
    clock.tick(60)

##########################  EXIT GAME LOOP  ########################

#stop background music
mixer.music.stop()