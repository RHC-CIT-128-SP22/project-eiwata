
import pygame
from initgame import Init_Game

pygame.init()
pygame.mixer.init()


class Narrator(Init_Game):
    def blit_line1(self, scene, count = 0):
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'node2':
                    f.seek(8)
                    line1_v1 = f.readline().rstrip('\n')
                    line1_v2 = ''
                    for letter in range(0, len(line1_v1)):
                        line1_v3 = self.FONT.render(line1_v2+line1_v1[letter], True, self.WHITE)
                        self.SCREEN.blit(line1_v3, (325, 330))
                        line1_v2 += line1_v1[letter]
                        self.clock.tick(20)
                        pygame.display.update()

    def blit_line2(self, scene, count = 0):
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'node2':
                    f.seek(48)
                    line2_v1 = f.readline().rstrip('\n')
                    line2_v2 = ''
                    for letter in range(0, len(line2_v1)):
                        line2_v3 = self.FONT.render(line2_v2+line2_v1[letter], True, self.WHITE)
                        self.SCREEN.blit(line2_v3, (300, 365))
                        line2_v2 += line2_v1[letter]
                        self.clock.tick(20)
                        pygame.display.update()