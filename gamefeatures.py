
import sys
import pygame
from pygame import mixer
from scenes import Display_Scene

#initialize game
pygame.init()
mixer.init()

#set audio
OPENING = mixer.music.load("audio/BeforeDawn.wav")
START_SOUND = pygame.mixer.Sound("audio/wildBeastRoar.wav")
mixer.music.set_volume(0)

class Game_Features(Display_Scene):
    def __init__(self):
        self.scene = 'start_screen'

    def scene_manager(self):
        if self.scene == 'start_screen':
            self.start_screen()
            self.user_decision(0)
        if self.scene == 'scene_one':
            self.scene_one()
            self.user_decision(1)
        if self.scene == 'scene_two':
            self.scene_two()
            self.user_decision(2)
        if self.scene == 'scene_three':
            self.scene_three()
            self.user_decision(3)

    def user_decision(self, scene):
        match scene:
            case 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit('QUIT GAME')
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()
        
                        #if hovering over start button
                        if (mx in range(350, 450)) and (my in range(470, 510)):
                            #bold start button
                            self.START_BUTTON.set_alpha(300)

                            #if click start button
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                #pygame.mixer.Sound.play(startSound)
                                self.fade_scene()
                                self.scene = 'scene_one'
                        else:
                            self.START_BUTTON.set_alpha(150)
                pygame.display.update()
            case 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit('QUIT GAME')
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.fade_scene()
                        self.scene = 'scene_two'
            case 2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit('QUIT GAME')
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.fade_scene()
                        self.scene = 'scene_three'
            case 3:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit('QUIT GAME')
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()

    #fade to next scene
    def fade_scene(self):
        fade = pygame.Surface((self.X, self.Y))
        fade.fill(self.BLACK)
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            self.SCREEN.blit(fade, (0, 0))
            pygame.display.update()

