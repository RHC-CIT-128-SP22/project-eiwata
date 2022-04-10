
import pygame
from pygame import mixer
from pygame.locals import *
from initgame import Init_Game

pygame.init()
pygame.mixer.init()

class Display_Scene(Init_Game):

    def start_screen(self):
        #display start screen
        self.PSEUDO_SCREEN.blit(self.START_SCREEN, (0, 0))
        self.PSEUDO_SCREEN.blit(self.START_BUTTON, (350, 470))

        pygame.display.update()

    def scene_one(self):   
        #display scene one 
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.PORTRAIT_SCENE, (0, 0))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        line1 = self.FONT.render('[Insert Dialogue]', True, self.WHITE)
        line2 = self.FONT.render('[Insert More Dialogue]', True, self.WHITE)
        self.PSEUDO_SCREEN.blit(line1, (170, 450))
        self.PSEUDO_SCREEN.blit(line2, (170, 500))

        pygame.display.update()

    def scene_two(self):
        #display scene two
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 0))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        line1 = self.FONT.render('[Insert Dialogue]', True, self.WHITE)
        line2 = self.FONT.render('[Insert More Dialogue]', True, self.WHITE)
        self.PSEUDO_SCREEN.blit(line1, (170, 450))
        self.PSEUDO_SCREEN.blit(line2, (170, 500))

        pygame.display.update()

    def scene_three(self):
        #display scene three
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.UNIVERSITY, (0, 0))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        line1 = self.FONT.render('[Insert Dialogue]', True, self.WHITE)
        line2 = self.FONT.render('[Insert More Dialogue]', True, self.WHITE)
        self.PSEUDO_SCREEN.blit(line1, (170, 450))
        self.PSEUDO_SCREEN.blit(line2, (170, 500))

        pygame.display.update()

