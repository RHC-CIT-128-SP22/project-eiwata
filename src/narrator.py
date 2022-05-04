
import pygame
from initgame import Init_Game

pygame.init()
pygame.font.init()
pygame.mixer.init()

class Narrator(Init_Game):

    #create clock
    FPS = 50
    clock = pygame.time.Clock()

    #initialize font and colors
    FONT = pygame.font.SysFont('Rockwell', 19)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #initialize variables
    line1_v2 = ''
    line2_v2 = ''
    line3_v2 = ''
    line4_v2 = ''
    line1_v3 = FONT.render(line1_v2, True, WHITE)
    line2_v3 = FONT.render(line2_v2, True, WHITE)
    line3_v3 = FONT.render(line3_v2, True, WHITE)
    line4_v3 = FONT.render(line4_v2, True, WHITE)


    def blit_line1(self, scene, count = 0):
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'node3':
                    #display scene
                    self.SCREEN.fill(self.BLACK)
                    self.SCREEN.blit(self.UNIVERSITY, (0, 80))
                    match count:
                        case 0:
                            f.seek(self.char_counter(8))
                        case 1:
                            f.seek(self.char_counter(12))
                        case 2:
                            f.seek(self.char_counter(16))
                        case 3:
                            f.seek(self.char_counter(20))
                case 'node4':
                    #display scene
                    self.SCREEN.fill(self.BLACK)
                    self.SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))
                    match count:
                        case 0:
                            f.seek(self.char_counter(27))
                        case 1:
                            f.seek(self.char_counter(31))
                        case 2:
                            f.seek(self.char_counter(35))
                        case 3:
                            f.seek(self.char_counter(39))
                case 'node6':
                    #display scene
                    self.SCREEN.fill(self.BLACK)
                    self.SCREEN.blit(self.INVESTIGATION_1, (0, 70))
                    match count:
                        case 0:
                            f.seek(self.char_counter(44))
                        case 1:
                            f.seek(self.char_counter(48))
                        case 2:
                            f.seek(self.char_counter(52))
                case 'node7':
                    #display scene
                    self.SCREEN.fill(self.BLACK)
                    self.SCREEN.blit(self.HOUSE, (0, 62.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(59))
                        case 1:
                            f.seek(self.char_counter(63))
                        case 2:
                            f.seek(self.char_counter(67))
                        case 3:
                            f.seek(self.char_counter(71))
                        case 4:
                            f.seek(self.char_counter(75))
            self.SCREEN.blit(self.TENTACLE, (150, 450))
            self.SCREEN.blit(self.DIAL_BOX, (40, 430))
            line1_v1 = f.readline().rstrip('\n')
            self.line1_v2 = ''
            for letter in range(0, len(line1_v1)):
                self.clock.tick(self.FPS)
                self.SCREEN.blit(self.DIAL_BOX, (40, 430))
                self.line1_v3 = self.FONT.render(self.line1_v2+line1_v1[letter], True, self.WHITE)
                self.SCREEN.blit(self.line1_v3, (190, 510))
                self.line1_v2 += line1_v1[letter]
                pygame.display.update()

    def blit_line2(self, scene, count = 0):
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'node3':
                    match count:
                        case 0:
                            f.seek(self.char_counter(9))
                        case 1:
                            f.seek(self.char_counter(13))
                        case 2:
                            f.seek(self.char_counter(17))
                        case 3:
                            f.seek(self.char_counter(21))
                case 'node4':
                    match count:
                        case 0:
                            f.seek(self.char_counter(28))
                        case 1:
                            f.seek(self.char_counter(32))
                        case 2:
                            f.seek(self.char_counter(36))
                        case 3:
                            f.seek(self.char_counter(40))
                case 'node6':
                    match count:
                        case 0:
                            f.seek(self.char_counter(45))
                        case 1:
                            f.seek(self.char_counter(49))
                        case 2:
                            f.seek(self.char_counter(53))
                case 'node7':
                    match count:
                        case 0:
                            f.seek(self.char_counter(60))
                        case 1:
                            f.seek(self.char_counter(64))
                        case 2:
                            f.seek(self.char_counter(68))
                        case 3:
                            f.seek(self.char_counter(72))
                        case 4:
                            f.seek(self.char_counter(76))
            line2_v1 = f.readline().rstrip('\n')
            self.line2_v2 = ''
            for letter in range(0, len(line2_v1)):
                self.clock.tick(self.FPS)
                self.SCREEN.blit(self.DIAL_BOX, (40, 430))
                self.SCREEN.blit(self.line1_v3, (190, 510))
                self.line2_v3 = self.FONT.render(self.line2_v2+line2_v1[letter], True, self.WHITE)
                self.SCREEN.blit(self.line2_v3, (190, 545))
                self.line2_v2 += line2_v1[letter]
                pygame.display.update()
    
    def blit_line3(self, scene, count = 0):
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'node3':
                    match count:
                        case 0:
                            f.seek(self.char_counter(10))
                        case 1:
                            f.seek(self.char_counter(14))
                        case 2:
                            f.seek(self.char_counter(18))
                        case 3:
                            f.seek(self.char_counter(22))
                case 'node4':
                    match count:
                        case 0:
                            f.seek(self.char_counter(29))
                        case 1:
                            f.seek(self.char_counter(33))
                        case 2:
                            f.seek(self.char_counter(37))
                        case 3:
                            f.seek(self.char_counter(41))
                case 'node6':
                    match count:
                        case 0:
                            f.seek(self.char_counter(46))
                        case 1:
                            f.seek(self.char_counter(50))
                        case 2:
                            f.seek(self.char_counter(54))
                case 'node7':
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
            line3_v1 = f.readline().rstrip('\n')
            self.line3_v2 = ''
            for letter in range(0, len(line3_v1)):
                self.clock.tick(self.FPS)
                self.SCREEN.blit(self.DIAL_BOX, (40, 430))
                self.SCREEN.blit(self.line1_v3, (190, 510))
                self.SCREEN.blit(self.line2_v3, (190, 545))
                self.line3_v3 = self.FONT.render(self.line3_v2+line3_v1[letter], True, self.WHITE)
                self.SCREEN.blit(self.line3_v3, (190, 580))
                self.line3_v2 += line3_v1[letter]
                pygame.display.update()

    def blit_line4(self, scene, count = 0):
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'node3':
                    match count:
                        case 0:
                            f.seek(self.char_counter(11))
                        case 1:
                            f.seek(self.char_counter(15))
                        case 2:
                            f.seek(self.char_counter(19))
                        case 3:
                            f.seek(self.char_counter(23))
                case 'node4':
                    match count:
                        case 0:
                            f.seek(self.char_counter(30))
                        case 1:
                            f.seek(self.char_counter(34))
                        case 2:
                            f.seek(self.char_counter(38))
                        case 3:
                            f.seek(self.char_counter(42))
                case 'node6':
                    match count:
                        case 0:
                            f.seek(self.char_counter(47))
                        case 1:
                            f.seek(self.char_counter(51))
                        case 2:
                            f.seek(self.char_counter(55))
                case 'node7':
                    match count:
                        case 0:
                            f.seek(self.char_counter(62))
                        case 1:
                            f.seek(self.char_counter(66))
                        case 2:
                            f.seek(self.char_counter(70))
                        case 3:
                            f.seek(self.char_counter(74))
                        case 4:
                            f.seek(self.char_counter(78))
            line4_v1 = f.readline().rstrip('\n')
            self.line4_v2 = ''
            for letter in range(0, len(line4_v1)):
                self.clock.tick(self.FPS)
                self.SCREEN.blit(self.DIAL_BOX, (40, 430))
                self.SCREEN.blit(self.DIAL_BOX, (40, 430))
                self.SCREEN.blit(self.line1_v3, (190, 510))
                self.SCREEN.blit(self.line2_v3, (190, 545))
                self.SCREEN.blit(self.line3_v3, (190, 580))
                self.line4_v3 = self.FONT.render(self.line4_v2+line4_v1[letter], True, self.WHITE)
                self.SCREEN.blit(self.line4_v3, (190, 615))
                self.line4_v2 += line4_v1[letter]
                pygame.display.update()

    def char_counter(self, n):
        n = n - 1
        with open('dialogue.txt', 'r') as f:
            line_offset = []
            offset = 0
            for line in f:
                line_offset.append(offset)
                offset += len(line)
            f.seek(0)
        return line_offset[n]
    
    def scene2_blit_line1(self):
        with open('dialogue.txt', 'r') as f:
            #display scene
            self.SCREEN.fill(self.BLACK)

            f.seek(8)
            line1_v1 = f.readline().rstrip('\n')
            line1_v2 = ''
            for letter in range(0, len(line1_v1)):
                self.clock.tick(self.FPS)
                self.SCREEN.fill(self.BLACK)
                line1_v3 = self.FONT.render(line1_v2+line1_v1[letter], True, self.WHITE)
                self.SCREEN.blit(line1_v3, (330, 330))
                line1_v2 += line1_v1[letter]
                pygame.display.update() 

    def scene2_blit_line2(self):
        with open('dialogue.txt', 'r') as f:
            f.seek(48)
            line2_v1 = f.readline().rstrip('\n')
            line2_v2 = ''
            for letter in range(0, len(line2_v1)):
                self.clock.tick(self.FPS)
                pygame.draw.rect(self.SCREEN, self.BLACK, pygame.Rect(300, 365, 400, 35))
                line2_v3 = self.FONT.render(line2_v2+line2_v1[letter], True, self.WHITE)
                self.SCREEN.blit(line2_v3, (300, 365))
                line2_v2 += line2_v1[letter]
                pygame.display.update()