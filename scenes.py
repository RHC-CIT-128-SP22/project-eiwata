
import pygame
from pygame import mixer
from pygame.locals import *
from initgame import Init_Game

pygame.init()
pygame.mixer.init()

class Display_Scene(Init_Game):

    def start_screen(self):
        #display start screen 
        self.PSEUDO_SCREEN.blit(self.START_SCREEN, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TITLE, (50, 50))
        self.PSEUDO_SCREEN.blit(self.START_BUTTON, (self.X/2.25, self.Y/1.23))

        pygame.display.update()

    def scene_one(self):   
        #display scene one 
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.PORTRAIT_SCENE, (0, 70))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (60, 430))

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            line1 = self.FONT.render(f.read(17), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            f.seek(18)
            line2 = self.FONT.render(f.read(22), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line2, (190, 560))
        pygame.display.update()
    

    def scene_two(self):
        #display scene two
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 60))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (60, 430))

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            line1 = self.FONT.render(f.read(17), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            f.seek(18)
            line2 = self.FONT.render(f.read(22), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line2, (190, 560))

        pygame.display.update()

    def scene_three(self):
        #display scene three
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.UNIVERSITY, (0, 80))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (60, 430))

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            line1 = self.FONT.render(f.read(17), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            f.seek(18)
            line2 = self.FONT.render(f.read(22), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line2, (190, 560))

        pygame.display.update()

