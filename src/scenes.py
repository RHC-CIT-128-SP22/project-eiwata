
import pygame
from pygame import mixer
from pygame.locals import *
from narrator import Narrator

pygame.init()
pygame.mixer.init()

class Display_Scene(Narrator):

    x_left = -290
    x_right = 864

    def node1(self):
        #display start screen 
        self.PSEUDO_SCREEN.blit(self.START_SCREEN, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TITLE, (50, 50))
        self.PSEUDO_SCREEN.blit(self.START_BUTTON, (self.X/2.25, self.Y/1.23))

        pygame.display.update()   

    def node2(self):
        #display scene 2
        self.PSEUDO_SCREEN.fill(self.BLACK)

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            f.seek(self.char_counter(3))
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (330, 330))
            self.PSEUDO_SCREEN.blit(line2, (300, 365))

        w, h = pygame.display.get_surface().get_size()
        self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
        pygame.display.update()

    def node3(self, count):
        count -= 1
        #display scene 3
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.UNIVERSITY, (0, 80))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f: 
            match count:
                case 0:
                    f.seek(self.char_counter(8))
                case 1:
                    f.seek(self.char_counter(12))
                case 2:
                    f.seek(self.char_counter(16))
                case 3:
                    f.seek(self.char_counter(20))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node4(self, count):
        count = count - 1
        #display scene 4
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

       #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(27))
                case 1:
                    f.seek(self.char_counter(31))
                case 2:
                    f.seek(self.char_counter(35))
                case 3:
                    f.seek(self.char_counter(39))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    #DECISION SCENE
    def node5(self):
        #display scene 5
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))

        top_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 70, 1000, 70])
        bottom_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 570, 1000, 70])

        self.PSEUDO_SCREEN.blit(self.LOOK_INTO_IT, (30, 600))
        self.PSEUDO_SCREEN.blit(self.TELL_HIM, (680, 600))
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (136.5, 665))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_left, 660))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_right, 660))

        pygame.display.update()

    def node6(self, count):
        count -= 1
        #display scene 6
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_1, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(44))
                case 1:
                    f.seek(self.char_counter(48))
                case 2:
                    f.seek(self.char_counter(52))
                case 3:
                    f.seek(self.char_counter(56))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node7(self, count):
        count -= 1
        #display scene 7
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HOUSE, (0, 62.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(61))
                case 1:
                    f.seek(self.char_counter(65))
                case 2:
                    f.seek(self.char_counter(69))
                case 3:
                    f.seek(self.char_counter(73))
                case 4:
                    f.seek(self.char_counter(77))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    #DECISION SCENE
    def node8(self):
        #display scene 8
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_1, (0, 70))

        bottom_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 570, 1000, 70])

        self.PSEUDO_SCREEN.blit(self.HELP_WITH, (30, 600))
        self.PSEUDO_SCREEN.blit(self.MAKE_UP, (600, 600))
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (136.5, 665))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_left, 660))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_right, 660))
        pygame.display.update()

    def node9(self, count):
        count-=1
        #display scene 9
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_2, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(82))
                case 1:
                    f.seek(self.char_counter(86))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node10(self, count):
        count -= 1
        #display scene 10
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.TOWN, (0, 54.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(91))
                case 1:
                    f.seek(self.char_counter(95))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node11(self, count):
        count -= 1
        #display scene 11
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(100))
                case 1:
                    f.seek(self.char_counter(104))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node12(self, count):
        count -= 1
        #display scene 12
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.ALONE, (0, 68.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(110))
                case 1:
                    f.seek(self.char_counter(114))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    #DECISION SCENE
    def node13(self):
        #display scene 13
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))

        top_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 68, 1000, 70])
        bottom_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 570, 1000, 72])

        self.PSEUDO_SCREEN.blit(self.TAKE_THE_GUN, (30, 600))
        self.PSEUDO_SCREEN.blit(self.RUN_AND_HIDE, (784, 600))
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (136.5, 665))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_left, 660))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_right, 660))

        pygame.display.update()

    def node14(self, count):
        count -= 1
        #display scene 14
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(119))
                case 1:
                    f.seek(self.char_counter(123))
                case 2:
                    f.seek(self.char_counter(127))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node15(self, count):
        count -= 1
        #display scene 15
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.STATUE, (0, 16.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(132))
                case 1:
                    f.seek(self.char_counter(136))
                case 2:
                    f.seek(self.char_counter(140))
                case 3:
                    f.seek(self.char_counter(144))
                case 4:
                    f.seek(self.char_counter(148))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node16(self, count):
        count -= 1
        #display scene 16
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.HOUSE, (0, 62.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(153))
                case 1:
                    f.seek(self.char_counter(157))
                case 2:
                    f.seek(self.char_counter(161))
                case 3:
                    f.seek(self.char_counter(165))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node17(self, count):
        count -= 1
        #display scene 17
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(170))
                case 1:
                    f.seek(self.char_counter(174))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    #DECISION SCENE
    def node18(self):
        #display scene 18
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))

        top_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 68, 1000, 70])
        bottom_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 570, 1000, 72])

        self.PSEUDO_SCREEN.blit(self.CONTINUE_VOYAGE, (30, 600))
        self.PSEUDO_SCREEN.blit(self.JUMP_OFF_SHIP, (775, 600))
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (136.5, 665))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_left, 660))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_right, 660))

        pygame.display.update()

    def node19(self, count):
        count -= 1
        #display scene 19
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(180))
                case 1:
                    f.seek(self.char_counter(184))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node20(self, count):
        count -= 1
        #display scene 20
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.SAIL, (0, 37.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(191))
                case 1:
                    f.seek(self.char_counter(195))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node21(self, count):
        count -= 1
        #display scene 21
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.RLYEH_1, (0, 90))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(201))
                case 1:
                    f.seek(self.char_counter(205))
                case 2:
                    f.seek(self.char_counter(209))
                case 3:
                    f.seek(self.char_counter(213))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    #DECISION SCENE
    def node22(self):
        #display scene 22
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.RLYEH_1, (0, 90))

        top_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 70, 1000, 70])
        bottom_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 570, 1000, 70])

        self.PSEUDO_SCREEN.blit(self.RUN_AWAY, (828, 600))
        self.PSEUDO_SCREEN.blit(self.ATTACK_IT, (30, 600))
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (136.5, 665))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_left, 660))
        self.PSEUDO_SCREEN.blit(self.BLACK_LINE, (self.x_right, 660))

        pygame.display.update()

    def node23(self, count):
        count -= 1
        #display scene 23
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.RLYEH_2, (0, 63.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(218))
                case 1:
                    f.seek(self.char_counter(222))
                case 2:
                    f.seek(self.char_counter(226))
                case 3:
                    f.seek(self.char_counter(230))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def node24(self, count):
        count -= 1
        #display scene 24
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.RLYEH_3, (0, 56))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #seek line number for every click count
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(235))
                case 1:
                    f.seek(self.char_counter(239))
                case 2:
                    f.seek(self.char_counter(243))
            #display dialogue
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    #display game over screen
    def game_over(self, scene):
        w, h = pygame.display.get_surface().get_size()
        self.PSEUDO_SCREEN.fill(self.BLACK)
        #display scene background img
        match scene:
            case 7:
                self.PSEUDO_SCREEN.blit(self.HOUSE, (0, 62.5))
            case 12:
                self.PSEUDO_SCREEN.blit(self.ALONE, (0, 68.5))
            case 20:
                self.PSEUDO_SCREEN.blit(self.SAIL, (0, 37.5))
            case 23:
                self.PSEUDO_SCREEN.blit(self.RLYEH_2, (0, 63.5))
            case 24:
                self.PSEUDO_SCREEN.blit(self.RLYEH_3, (0, 56))
        #display buttons
        self.PSEUDO_SCREEN.blit(self.GAME_OVER, (195, 200))
        self.PSEUDO_SCREEN.blit(self.CONTINUE, (150, 400))
        self.PSEUDO_SCREEN.blit(self.EXIT, (680, 400))
        self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
        pygame.display.update()

    #fade into game over screen
    def game_over_fader(self, scene):
        #initialize variables
        w, h = pygame.display.get_surface().get_size()
        go_fader = pygame.Surface((self.X, self.Y))
        go_fader.fill(self.BLACK)
        #display semi-transparent background img over black window
        match scene:
            case 7:
                self.HOUSE.set_alpha(90)
                go_fader.blit(self.HOUSE, (0, 62.5))
            case 12:
                self.ALONE.set_alpha(90)
                go_fader.blit(self.ALONE, (0, 68.5))
            case 20:
                self.SAIL.set_alpha(90)
                go_fader.blit(self.SAIL, (0, 37.5))
            case 23:
                self.RLYEH_2.set_alpha(90)
                go_fader.blit(self.RLYEH_2, (0, 63.5))
            case 24:
                self.RLYEH_3.set_alpha(90)
                go_fader.blit(self.RLYEH_3, (0, 56))
        go_fader.blit(self.GAME_OVER, (195, 200))
        go_fader.blit(self.CONTINUE, (150, 400))
        go_fader.blit(self.EXIT, (680, 400))
        #slowly fade into game over screen
        for alpha in range(0, 300):
            go_fader.set_alpha(alpha)
            self.PSEUDO_SCREEN.blit(go_fader, (0, 0))
            self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
            pygame.display.update()


    #narrows the screen before decisions
    def narrow_screen(self, scene, y):
        #initialize variables
        TOP_Y = 0
        w, h = pygame.display.get_surface().get_size()
        BOTTOM_Y = self.h - y

        match scene:
            case 5:
                #display scene 5
                self.PSEUDO_SCREEN.fill(self.BLACK)
                self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))
            case 8:
                #display scene 8
                self.PSEUDO_SCREEN.fill(self.BLACK)
                self.PSEUDO_SCREEN.blit(self.INVESTIGATION_1, (0, 70))
            case 13:
                 #display scene 13
                self.PSEUDO_SCREEN.fill(self.BLACK)
                self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))
            case 18:
                #display scene 18
                self.PSEUDO_SCREEN.fill(self.BLACK)
                self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))
            case 22:
                #display scene 22
                self.PSEUDO_SCREEN.fill(self.BLACK)
                self.PSEUDO_SCREEN.blit(self.RLYEH_1, (0, 90))
        if scene == 8:
            #increase only bottom margin (bc top margin cuts off head of inspector)
            for i in range(y):
                BOTTOM_Y -= 1
                self.clock.tick(150)
                bottom_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, BOTTOM_Y, w, h/10])
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
                pygame.display.update()
        else:
            #increase top and bottom margin
            for i in range(y):
                TOP_Y += 1
                BOTTOM_Y -= 1
                self.clock.tick(150)
                top_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, TOP_Y, w, h/10])
                bottom_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, BOTTOM_Y, w, h/10])
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
                pygame.display.update()


