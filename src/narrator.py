
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

                    f.seek(100)
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
                    f.seek(162)
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
                    f.seek(223)
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
                    f.seek(280)
            line4_v1 = f.readline().rstrip('\n')
            line4_v2 = ''
            for letter in range(0, len(line4_v1)):
                self.clock.tick(self.FPS)
                line4_v3 = self.FONT.render(line4_v2+line4_v1[letter], True, self.WHITE)
                self.SCREEN.blit(line4_v3, (190, 615))
                line4_v2 += line4_v1[letter]
                pygame.display.update()
    
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