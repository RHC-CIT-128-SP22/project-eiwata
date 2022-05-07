#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame
from pygame import mixer
from gamefeatures import Game_Features

#initialize game
pygame.init()
pygame.mixer.init()

def main():
    #initialize variables
    curr_game = Game_Features()

    #set audio
    OPENING = mixer.music.load("assets/Beginning.mp3")
    mixer.music.set_volume(0.7)

    #play bgm
    mixer.music.play(-1)

 ########  MAIN GAME LOOP ########
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        curr_game.scene_manager()

 ####### END OF GAME LOOP ########

if __name__ == '__main__':
    main()
