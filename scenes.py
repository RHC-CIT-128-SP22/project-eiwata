
import pygame
from pygame import *

pygame.init()

class Display_Scene():
    #create game window
    X, Y = 800, 600
    SCREEN = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("The Call of Cthulhu - Survival Horror Game")
    ICON = pygame.image.load("pictures/icon.png")
    pygame.display.set_icon(ICON)

    #load buttons and icons
    TITLE = pygame.image.load("pictures/mainTitle.png")
    START_BUTTON = pygame.image.load("pictures/startButton.png")
    DIAL_BOX = pygame.image.load("pictures/rectangle.png")

    #load background images
    START_SCREEN = pygame.image.load("pictures/startBG.png")
    PORTRAIT_SCENE = pygame.image.load("pictures/portrait.png")
    HORROR_IN_CLAY = pygame.image.load("pictures/horrorInClay.jpg")
    UNIVERSITY = pygame.image.load("pictures/UNIVERSITY.jpg")

    #colors and font
    FONT = pygame.font.SysFont('Comic Sans MS', 17)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #set transparency
    DIAL_BOX.set_alpha(190)
    START_BUTTON.set_alpha(150)

    def start_screen(self):
        #display start screen
        self.SCREEN.blit(self.START_SCREEN, (0, 70))
        self.SCREEN.blit(self.TITLE, (40, 50))
        self.SCREEN.blit(self.START_BUTTON, (350, 470))

        pygame.display.update()

    def scene_one(self):   
        #display scene one 
        self.SCREEN.blit(self.PORTRAIT_SCENE, (0, 70))
        self.SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        L1 = self.FONT.render('[Insert Dialogue]', True, self.WHITE)
        L2 = self.FONT.render('[Insert More Dialogue]', True, self.WHITE)
        self.SCREEN.blit(L1, (170, 440))
        self.SCREEN.blit(L2, (170, 490))

        pygame.display.update()

    def scene_two(self):
        #display scene two
        self.SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))
        self.SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        L1 = self.FONT.render('[Insert Dialogue]', True, self.WHITE)
        L2 = self.FONT.render('[Insert More Dialogue]', True, self.WHITE)
        self.SCREEN.blit(L1, (170, 440))
        self.SCREEN.blit(L2, (170, 490))

        pygame.display.update()

    def scene_three(self):
        #display scene three
        self.SCREEN.blit(self.UNIVERSITY, (0, 90))
        self.SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        L1 = self.FONT.render('[Insert Dialogue]', True, self.WHITE)
        L2 = self.FONT.render('[Insert More Dialogue]', True, self.WHITE)
        self.SCREEN.blit(L1, (170, 440))
        self.SCREEN.blit(L2, (170, 490))

        pygame.display.update()
