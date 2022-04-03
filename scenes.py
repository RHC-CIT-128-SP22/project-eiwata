
import sys
import pygame
from pygame import mixer

#initialize game
pygame.init()
mixer.init()
CLOCK = pygame.time.Clock

#create game window
X, Y = 800, 600
SCREEN = pygame.display.set_mode((X, Y))
pygame.display.set_caption("The Call of Cthulhu - Survival Horror Game")
ICON = pygame.image.load("pictures/icon.png")
pygame.display.set_icon(ICON)

#set audio
OPENING = mixer.music.load("audio/BeforeDawn.wav")
START_SOUND = pygame.mixer.Sound("audio/wildBeastRoar.wav")
mixer.music.set_volume(0)

#colors and font
FONT = pygame.font.SysFont('Comic Sans MS', 17)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Display_Scene:
    #load buttons and audio
    TITLE = pygame.image.load("pictures/mainTitle.png")
    START_BUTTON = pygame.image.load("pictures/startButton.png")
    DIAL_BOX = pygame.image.load("pictures/rectangle.png")

    #load background images
    START_SCREEN = pygame.image.load("pictures/startBG.png")
    PORTRAIT_SCENE = pygame.image.load("pictures/portrait.png")
    HORROR_IN_CLAY = pygame.image.load("pictures/horrorInClay.jpg")
    UNIVERSITY = pygame.image.load("pictures/UNIVERSITY.jpg")

    #set transparency
    DIAL_BOX.set_alpha(190)

    def __init__(self):
        self.scene = 'start_screen'

    def start_screen(self):
        #display start screen
        SCREEN.blit(self.START_SCREEN, (0, 70))
        SCREEN.blit(self.TITLE, (40, 50))
        SCREEN.blit(self.START_BUTTON, (350, 470))
        self.START_BUTTON.set_alpha(150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('QUIT GAME')
            if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                #get mouse position
                mx, my = pygame.mouse.get_pos()
        
                #if hovering over start button
                if mx in range(350, 450) and my in range(470, 510):
                    #bold start button
                    self.START_BUTTON.set_alpha(300)

                    #if click start button
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #pygame.mixer.Sound.play(startSound)
                        self.fade_scene()
                        self.scene = 'scene_one'
        pygame.display.update()

    def scene_one(self):   
        #display scene one 
        SCREEN.blit(self.PORTRAIT_SCENE, (0, 70))
        SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        L1 = FONT.render('[Insert Dialogue]', True, WHITE)
        L2 = FONT.render('[Insert More Dialogue]', True, WHITE)
        SCREEN.blit(L1, (170, 440))
        SCREEN.blit(L2, (170, 490))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('QUIT GAME')
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.fade_scene()
                self.scene = 'scene_two'

    def scene_two(self):
        #display scene two
        SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))
        SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        L1 = FONT.render('[Insert Dialogue]', True, WHITE)
        L2 = FONT.render('[Insert More Dialogue]', True, WHITE)
        SCREEN.blit(L1, (170, 440))
        SCREEN.blit(L2, (170, 490))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('QUIT GAME')
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.fade_scene()
                self.scene = 'scene_three'

    def scene_three(self):
        #display scene three
        SCREEN.blit(self.UNIVERSITY, (0, 90))
        SCREEN.blit(self.DIAL_BOX, (30, 380))

        #display dialogue
        L1 = FONT.render('[Insert Dialogue]', True, WHITE)
        L2 = FONT.render('[Insert More Dialogue]', True, WHITE)
        SCREEN.blit(L1, (170, 440))
        SCREEN.blit(L2, (170, 490))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('QUIT GAME')
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()

    #fade to next scene
    def fade_scene(self):
        fade = pygame.Surface((X, Y))
        fade.fill(BLACK)
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            SCREEN.blit(fade, (0, 0))
            pygame.display.update()

    def scene_manager(self):
        if self.scene == 'start_screen':
            self.start_screen()
        if self.scene == 'scene_one':
            self.scene_one()
        if self.scene == 'scene_two':
            self.scene_two()
        if self.scene == 'scene_three':
            self.scene_three()
