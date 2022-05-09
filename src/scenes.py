
import pygame
from pygame import mixer
from pygame.locals import *
from narrator import Narrator

pygame.init()
pygame.mixer.init()

class Display_Scene(Narrator):

    def node1(self):
        #display start screen 
        self.PSEUDO_SCREEN.blit(self.START_SCREEN, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TITLE, (50, 50))
        self.PSEUDO_SCREEN.blit(self.START_BUTTON, (self.X/2.25, self.Y/1.23))

        pygame.display.update()   

    def node2(self):
        #display scene 2
        self.PSEUDO_SCREEN.fill(self.BLACK)

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

        #display dialogue
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

        #display dialogue
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
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (100, 270))

        pygame.display.update()

    def node6(self, count):
        count -= 1
        #display scene 6
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_1, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #display dialogue
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

        #display dialogue
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

        top_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 70, 1000, 70])
        bottom_margin = pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, [0, 570, 1000, 70])

        self.PSEUDO_SCREEN.blit(self.HELP_WITH, (30, 600))
        self.PSEUDO_SCREEN.blit(self.MAKE_UP, (600, 600))
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (100, 270))
        pygame.display.update()

    def node9(self, count):
        count-=1
        #display scene 9
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_2, (0, 70))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(82))
                case 1:
                    f.seek(self.char_counter(86))
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

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(91))
                case 1:
                    f.seek(self.char_counter(95))
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

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(100))
                case 1:
                    f.seek(self.char_counter(104))
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

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(110))
                case 1:
                    f.seek(self.char_counter(114))
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
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (100, 270))

        pygame.display.update()

    def node14(self, count):
        count -= 1
        #display scene 14
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(119))
                case 1:
                    f.seek(self.char_counter(123))
                case 2:
                    f.seek(self.char_counter(127))
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

        #display dialogue
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

        #display dialogue
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

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(170))
                case 1:
                    f.seek(self.char_counter(174))
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
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (100, 270))

        pygame.display.update()

    def node19(self, count):
        count -= 1
        #display scene 19
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(181))
                case 1:
                    f.seek(self.char_counter(185))
                case 2:
                    f.seek(self.char_counter(189))
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

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(194))
                case 1:
                    f.seek(self.char_counter(198))
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

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(204))
                case 1:
                    f.seek(self.char_counter(208))
                case 2:
                    f.seek(self.char_counter(212))
                case 3:
                    f.seek(self.char_counter(216))
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

        self.PSEUDO_SCREEN.blit(self.RUN_AWAY, (30, 600))
        self.PSEUDO_SCREEN.blit(self.CHARGE_SHIP, (419, 600))
        self.PSEUDO_SCREEN.blit(self.WHITE_LINE, (100, 270))

        pygame.display.update()

    def node23(self, count):
        count -= 1
        #display scene 23
        self.PSEUDO_SCREEN.fill(self.BLACK)
        self.PSEUDO_SCREEN.blit(self.RLYEH_2, (0, 63.5))
        self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
        self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(221))
                case 1:
                    f.seek(self.char_counter(225))
                case 2:
                    f.seek(self.char_counter(229))
                case 3:
                    f.seek(self.char_counter(233))
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

        #display dialogue
        with open('dialogue.txt', 'r') as f:
            match count:
                case 0:
                    f.seek(self.char_counter(238))
                case 1:
                    f.seek(self.char_counter(242))
                case 2:
                    f.seek(self.char_counter(246))
            line1 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line2 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line3 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            line4 = self.FONT.render(f.readline().rstrip('\n'), True, self.WHITE)
            self.PSEUDO_SCREEN.blit(line1, (190, 510))
            self.PSEUDO_SCREEN.blit(line2, (190, 545))
            self.PSEUDO_SCREEN.blit(line3, (190, 580))
            self.PSEUDO_SCREEN.blit(line4, (190, 615))
        pygame.display.update()

    def game_over(self, scene):
        fade = pygame.Surface((self.X, self.Y))
        fade.fill(self.BLACK)
        fade.set_alpha(20)
        self.PSEUDO_SCREEN.blit(fade, (0, 0))
        match scene:
            case 7:
                self.HOUSE.set_alpha(30)
                self.PSEUDO_SCREEN.blit(self.HOUSE, (0, 62.5))
            case 12:
                self.ALONE.set_alpha(30)
                self.PSEUDO_SCREEN.blit(self.ALONE, (0, 68.5))
            case 20:
                self.SAIL.set_alpha(30)
                self.PSEUDO_SCREEN.blit(self.SAIL, (0, 37.5))
            case 23:
                self.RLYEH_2.set_alpha(30)
                self.PSEUDO_SCREEN.blit(self.RLYEH_2, (0, 63.5))
            case 24:
                self.RLYEH_3.set_alpha(30)
                self.PSEUDO_SCREEN.blit(self.RLYEH_3, (0, 56))
        self.PSEUDO_SCREEN.blit(self.GAME_OVER, (277, 100))
        self.PSEUDO_SCREEN.blit(self.CONTINUE, (150, 350))
        self.PSEUDO_SCREEN.blit(self.EXIT, (700, 350))
        
        #446, 128

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

        for i in range(y):
            TOP_Y += 1
            BOTTOM_Y -= 1
            top_margin = pygame.draw.rect(self.SCREEN, self.BLACK, [0, TOP_Y, w, h/10])
            bottom_margin = pygame.draw.rect(self.SCREEN, self.BLACK, [0, BOTTOM_Y, w, h/10])
            pygame.display.update()
    


