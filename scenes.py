
import pygame
from pygame import mixer
from pygame.locals import *
from initgame import Init_Game

pygame.init()
pygame.mixer.init()

class Display_Scene(Init_Game):

    def node1(self):
        #display start screen 
        self.PSEUDO_SCREEN.blit(self.START_SCREEN, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TITLE, (50, 50))
        self.PSEUDO_SCREEN.blit(self.START_BUTTON, (self.X/2.25, self.Y/1.23))

        pygame.display.update()   

    def node2(self):
        #display scene two
        self.PSEUDO_SCREEN.fill(self.BLACK)

        pygame.display.update()

    def node3(self):
        #display scene three
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.UNIVERSITY, (0, 80))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (60, 430))
        self.PSEUDO_SCREEN.blit(self.BORDER, (375, 485))

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 540))
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line2, (190, 575))
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line3, (190, 610))
        pygame.display.update()

    def node4(self):
        #display scene four
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (60, 430))
        self.PSEUDO_SCREEN.blit(self.BORDER, (375, 485))

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 540))
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line2, (190, 575))
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line3, (190, 610))
        pygame.display.update()

    def node5(self):
        #display scene five
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))

        pygame.display.update()

