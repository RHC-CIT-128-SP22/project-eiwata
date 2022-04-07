#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame
from pygame import mixer
from gamefeatures import Game_Features

def main():
    #initialize variables
    pygame.init()
    mixer.init()
    curr_game = Game_Features()

 ########  MAIN GAME LOOP ########
    running = True
    while running:

        mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        curr_game.scene_manager()

 ####### END OF GAME LOOP ########

if __name__ == '__main__':
    main()
