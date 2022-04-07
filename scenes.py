
import pygame
from initgame import Init_Game

#initialize game
pygame.init()

class Display_Scene(Init_Game):

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
        line1 = self.FONT.render('[Insert Dialogue]', True, self.WHITE)
        line2 = self.FONT.render('[Insert More Dialogue]', True, self.WHITE)
        self.SCREEN.blit(line1, (170, 440))
        self.SCREEN.blit(line2, (170, 490))

        pygame.display.update()

    def scene_two(self):
        #display scene two
        self.SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))
        self.SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        line1 = self.FONT.render('[Insert Dialogue]', True, self.WHITE)
        line2 = self.FONT.render('[Insert More Dialogue]', True, self.WHITE)
        self.SCREEN.blit(line1, (170, 440))
        self.SCREEN.blit(line2, (170, 490))

        pygame.display.update()

    def scene_three(self):
        #display scene three
        self.SCREEN.blit(self.UNIVERSITY, (0, 90))
        self.SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        line1 = self.FONT.render('[Insert Dialogue]', True, self.WHITE)
        line2 = self.FONT.render('[Insert More Dialogue]', True, self.WHITE)
        self.SCREEN.blit(line1, (170, 440))
        self.SCREEN.blit(line2, (170, 490))

        pygame.display.update()

