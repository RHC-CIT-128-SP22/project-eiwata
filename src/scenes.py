
import pygame
from pygame import mixer
from pygame.locals import *
from initgame import Init_Game

pygame.init()
pygame.mixer.init()

class Display_Scene(Init_Game):

    def narrow_screen(self, scene, y):
        #initialize variables
        TOP_Y = 0
        BOTTOM_Y = 700 - y

        match scene:
            case 5:
                #display scene 5
                self.PSEUDO_SCREEN.fill(self.BLACK)
                self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))

                for i in range(y):
                    TOP_Y += 1
                    BOTTOM_Y -= 1
                    top_margin = pygame.draw.rect(self.SCREEN, self.BLACK, [0, TOP_Y, 1000, 70])
                    bottom_margin = pygame.draw.rect(self.SCREEN, self.BLACK, [0, BOTTOM_Y, 1000, 70])
                    pygame.display.update()

    def node1(self):
        #display start screen 
        self.PSEUDO_SCREEN.blit(self.START_SCREEN, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TITLE, (50, 50))
        self.PSEUDO_SCREEN.blit(self.START_BUTTON, (self.X/2.25, self.Y/1.23))

        pygame.display.update()   

    def node2(self):
        #display scene 2
        self.PSEUDO_SCREEN.fill(self.BLACK)

        pygame.display.update()

    def node3(self):
        #display scene 3
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
        #display scene 4
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

    #DECISION SCENE
    def node5(self):
        #display scene 5
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))

        top_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 70, 1000, 70])
        bottom_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 570, 1000, 70])

        self.PSEUDO_SCREEN.blit(self.LOOK_INTO_IT, (30, 600))
        self.PSEUDO_SCREEN.blit(self.TELL_HIM, (695, 600))
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (100, 270))

        pygame.display.update()

    def node6(self):
        #display scene 6
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_1, (0, 70))
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

    def node7(self):
        #display scene 7
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HOUSE, (0, 37.5))
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

    #DECISION SCENE
    def node8(self):
        #display scene 8
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_1, (0, 70))

        pygame.display.update()

    def node9(self):
        #display scene 9
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_2, (0, 70))
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

    def node10(self):
        #display scene 10
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.TOWN, (0, 54.5))
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

    def node11(self):
        #display scene 11
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))
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

    def node12(self):
        #display scene 12
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.ALONE, (0, 68.5))
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

    #DECISION SCENE
    def node13(self):
        #display scene 13
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))

        pygame.display.update()

    def node14(self):
        #display scene 14
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))
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

    def node15(self):
        #display scene 15
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.STATUE, (0, 16.5))
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

    def node16(self):
        #display scene 16
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HOUSE, (0, 37.5))
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

    def node17(self):
        #display scene 17
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))
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

    #DECISION SCENE
    def node18(self):
        #display scene 18
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))

        pygame.display.update()

    def node19(self):
        #display scene 19
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))
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

    def node20(self):
        #display scene 20
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.SAIL, (0, 37.5))
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

    def node21(self):
        #display scene 21
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.RLYEH_1, (0, 90))
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

    #DECISION SCENE
    def node22(self):
        #display scene 22
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.RLYEH_1, (0, 90))

        pygame.display.update()

    def node23(self):
        #display scene 23
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.RLYEH_2, (0, 63.5))
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

    def node24(self):
        #display scene 24
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.RLYEH_3, (0, 56))
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

        