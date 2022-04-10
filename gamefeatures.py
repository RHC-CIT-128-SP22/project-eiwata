
import sys, pygame
from pygame import mixer
from scenes import Display_Scene

pygame.init()
mixer.init()

class Game_Features(Display_Scene):
    def __init__(self):
        self.scene = 'start_screen'
        self.WIN_RESIZED = False

    def scene_manager(self):
        if self.scene == 'start_screen':
            self.start_screen()
            self.user_decision('start_screen')
        if self.scene == 'scene_one':
            self.scene_one()
            self.user_decision('scene_one')
        if self.scene == 'scene_two':
            self.scene_two()
            self.user_decision('scene_two')
        if self.scene == 'scene_three':
            self.scene_three()
            self.user_decision('scene_three')

    def user_decision(self, scene):
        if self.WIN_RESIZED == False:
            self.SCREEN.blit(self.PSEUDO_SCREEN, (0, 0))
            self.SCREEN.blit(self.COLLISION_SCREEN, (0, 0))
        for event in pygame.event.get():
            #if user quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('QUIT GAME')
            #if window is being resized
            if (event.type == pygame.VIDEORESIZE):
                self.WIN_RESIZED = True
                self.SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (event.w, event.h)), (0, 0))
                if scene == 'start_screen':
                    self.START_BUTTON_POS = pygame.Rect(event.w/2.25, event.h/1.23, event.w/8.3, event.h/14)
                    pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.START_BUTTON_POS, 3)
                    #self.SCREEN.blit(pygame.transform.scale(self.COLLISION_SCREEN, (event.w, event.h)), (0, 0))
            #if window has been resized 
            elif self.WIN_RESIZED == True:
                w, h = pygame.display.get_surface().get_size()
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
                if scene == 'start_screen':
                    #visible screen that scales to the size of window
                    self.START_BUTTON_POS = pygame.Rect(w/2.25, h/1.23, w/8.3, h/14)
                    pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.START_BUTTON_POS, 3)
                    #self.SCREEN.blit(pygame.transform.scale(self.COLLISION_SCREEN, (w, h)), (0, 0))
            #more specific actions per scene
            match scene:
                case 'start_screen':
                    #if mouse move or click
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()
        
                        #if hovering over start button
                        collision = self.START_BUTTON_POS.collidepoint(mx, my)
                        if collision:
                            #bold start button
                            self.START_BUTTON.set_alpha(300)

                            #if click start button
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.START_SOUND)
                                self.fade_out()
                                self.scene = 'scene_one'
                        else:
                            self.START_BUTTON.set_alpha(150)

                    pygame.display.update()
                case 'scene_one':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.fade_out()
                        self.scene = 'scene_two'
                case 'scene_two':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.fade_out()
                        self.scene = 'scene_three'
                case 'scene_three':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()

    #fade out next scene
    def fade_out(self):
        #default window size
        if self.WIN_RESIZED == False:
            fade = pygame.Surface((self.X, self.Y))
            self.PSEUDO_SCREEN.fill(self.BLACK)
            self.SCREEN.blit(self.PSEUDO_SCREEN, (0, 0))
            for alpha in range(0, 300):
                self.PSEUDO_SCREEN.set_alpha(alpha)
                self.PSEUDO_SCREEN.blit(fade, (0, 0))
                pygame.display.update()
        #custom window size
        else:
            fade = pygame.Surface((self.X, self.Y))
            w, h = pygame.display.get_surface().get_size()
            self.PSEUDO_SCREEN.fill(self.BLACK)
            self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
            for alpha in range(0, 300):
                self.PSEUDO_SCREEN.set_alpha(alpha)
                self.PSEUDO_SCREEN.blit(fade, (0, 0))
                pygame.display.update()