
import pygame
from initgame import Init_Game

pygame.init()
pygame.mixer.init()

class Narrator(Init_Game):

    #create clock
    FPS = 50
    clock = pygame.time.Clock()

    def blit_line1(self, scene, count = 0):
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'node3':
                    #display scene
                    self.SCREEN.fill(self.BLACK)
                    self.SCREEN.blit(self.UNIVERSITY, (0, 80))
                    self.SCREEN.blit(self.TENTACLE, (150, 450))
                    self.SCREEN.blit(self.DIAL_BOX, (40, 430))
                    match count:
                        case 0:
                            f.seek(self.char_counter(8))
                        case 1:
                            f.seek(self.char_counter(12))
                        case 2:
                            f.seek(self.char_counter(16))
                        case 3:
                            f.seek(self.char_counter(20))
                        case 4:
                            f.seek(self.char_counter(24))
            line1_v1 = f.readline().rstrip('\n')
            line1_v2 = ''
            for letter in range(0, len(line1_v1)):
                self.clock.tick(self.FPS)
                line1_v3 = self.FONT.render(line1_v2+line1_v1[letter], True, self.WHITE)
                self.SCREEN.blit(line1_v3, (190, 510))
                line1_v2 += line1_v1[letter]
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
                        case 4:
                            f.seek(self.char_counter(25))
            line2_v1 = f.readline().rstrip('\n')
            line2_v2 = ''
            for letter in range(0, len(line2_v1)):
                self.clock.tick(self.FPS)
                line2_v3 = self.FONT.render(line2_v2+line2_v1[letter], True, self.WHITE)
                self.SCREEN.blit(line2_v3, (190, 545))
                line2_v2 += line2_v1[letter]
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
                        case 4:
                            f.seek(self.char_counter(26))
            line3_v1 = f.readline().rstrip('\n')
            line3_v2 = ''
            for letter in range(0, len(line3_v1)):
                self.clock.tick(self.FPS)
                line3_v3 = self.FONT.render(line3_v2+line3_v1[letter], True, self.WHITE)
                self.SCREEN.blit(line3_v3, (190, 580))
                line3_v2 += line3_v1[letter]
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
                        case 4:
                            f.seek(self.char_counter(27))
            line4_v1 = f.readline().rstrip('\n')
            line4_v2 = ''
            for letter in range(0, len(line4_v1)):
                self.clock.tick(self.FPS)
                line4_v3 = self.FONT.render(line4_v2+line4_v1[letter], True, self.WHITE)
                self.SCREEN.blit(line4_v3, (190, 615))
                line4_v2 += line4_v1[letter]
                pygame.display.update()

    def char_counter(self, n):
        n = n - 1
        with open('dialogue.txt', 'r') as f:
            # Read in the file once and build a list of line offsets
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
                line1_v3 = self.FONT.render(line1_v2+line1_v1[letter], True, self.WHITE)
                self.SCREEN.blit(line1_v3, (325, 330))
                line1_v2 += line1_v1[letter]
                pygame.display.update() 

    def scene2_blit_line2(self):
        with open('dialogue.txt', 'r') as f:
            f.seek(48)
            line2_v1 = f.readline().rstrip('\n')
            line2_v2 = ''
            for letter in range(0, len(line2_v1)):
                self.clock.tick(self.FPS)
                line2_v3 = self.FONT.render(line2_v2+line2_v1[letter], True, self.WHITE)
                self.SCREEN.blit(line2_v3, (300, 365))
                line2_v2 += line2_v1[letter]
                pygame.display.update()