
import sys, pygame
from pygame import mixer
from scenes import Display_Scene

pygame.init()
mixer.init()

class Game_Features(Display_Scene):
    def __init__(self):
        self.scene = 'node1'
        self.WIN_RESIZED = False

    def scene_manager(self):
        if self.scene == 'node1':
            self.node1()
            self.blit_screen()
            self.user_decision('node1')
        if self.scene == 'node2':
            self.node2()
            self.blit_screen()
            self.user_decision('node2')
        if self.scene == 'node3':
            self.node3()
            self.blit_screen()
            self.user_decision('node3')
        if self.scene == 'node4':
            self.node4()
            self.blit_screen()
            self.user_decision('node4')
        if self.scene == 'node5':
            self.node5()
            self.blit_screen()
            self.user_decision('node5')
        if self.scene == 'node6':
            self.node6()
            self.blit_screen()
            self.user_decision('node6')
        if self.scene == 'node7':
            self.node7()
            self.blit_screen()
            self.user_decision('node7')
        if self.scene == 'node8':
            self.node8()
            self.blit_screen()
            self.user_decision('node8')
        if self.scene == 'node9':
            self.node9()
            self.blit_screen()
            self.user_decision('node9')
        if self.scene == 'node10':
            self.node10()
            self.blit_screen()
            self.user_decision('node10')
        if self.scene == 'node11':
            self.node11()
            self.blit_screen()
            self.user_decision('node11')
        if self.scene == 'node12':
            self.node12()
            self.blit_screen()
            self.user_decision('node12')
        if self.scene == 'node13':
            self.node13()
            self.blit_screen()
            self.user_decision('node13')
        if self.scene == 'node14':
            self.node14()
            self.blit_screen()
            self.user_decision('node14')
        if self.scene == 'node15':
            self.node15()
            self.blit_screen()
            self.user_decision('node15')
        if self.scene == 'node16':
            self.node16()
            self.blit_screen()
            self.user_decision('node16')
        if self.scene == 'node17':
            self.node17()
            self.blit_screen()
            self.user_decision('node17')
        if self.scene == 'node18':
            self.node18()
            self.blit_screen()
            self.user_decision('node18')
        if self.scene == 'node19':
            self.node19()
            self.blit_screen()
            self.user_decision('node19')
        if self.scene == 'node20':
            self.node20()
            self.blit_screen()
            self.user_decision('node20')
        if self.scene == 'node21':
            self.node21()
            self.blit_screen()
            self.user_decision('node21')
        if self.scene == 'node22':
            self.node22()
            self.blit_screen()
            self.user_decision('node22')
        if self.scene == 'node23':
            self.node23()
            self.blit_screen()
            self.user_decision('node23')
        if self.scene == 'node24':
            self.node24()
            self.blit_screen()
            self.user_decision('node24')

    def blit_screen(self):
        if self.WIN_RESIZED == False:
            self.SCREEN.blit(self.PSEUDO_SCREEN, (0, 0))
            self.SCREEN.blit(self.COLLISION_SCREEN, (0, 0))
        #if window has been resized 
        elif self.WIN_RESIZED == True:
            w, h = pygame.display.get_surface().get_size()
            self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
            if self.scene == 'node1':
                #visible screen that scales to the size of window
                self.START_BUTTON_POS = pygame.Rect(w/2.25, h/1.23, w/8.3, h/14)
                pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.START_BUTTON_POS, 3)
            if self.scene == 'node5':
                self.TELL_HIM_POS = pygame.Rect(w/1.44, h/1.17, w/3.6, h/28)
                self.LOOK_INTO_IT_POS = pygame.Rect(w/33.3, h/1.17, w/6.37, h/28)
                pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.TELL_HIM_POS, 3)
                pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.LOOK_INTO_IT_POS, 3)

    def user_decision(self, scene):
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

            #more specific actions per scene
            match scene:
                case 'node1':
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
                                self.scene = 'node2'
                        else:
                            self.START_BUTTON.set_alpha(150)
                    pygame.display.update()
                case 'node2':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen_fader()
                        self.scene = 'node3'
                case 'node3':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen_fader()
                        self.scene = 'node4'
                case 'node4':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.scene = 'node5'
                        self.narrow_screen(5, 70)
                case 'node5':
                    #if mouse move or click
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()
                        
                        CHOICE_A = self.LOOK_INTO_IT_POS.collidepoint(mx, my)
                        CHOICE_B = self.TELL_HIM_POS.collidepoint(mx, my)

                        #if hovering over option
                        if CHOICE_A:
                            #bold option
                            self.LOOK_INTO_IT.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                self.scene = 'node6'
                        if CHOICE_B:
                            #bold option
                            self.TELL_HIM.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                self.scene = 'node7'
                        else:
                            self.LOOK_INTO_IT.set_alpha(100)
                            self.TELL_HIM.set_alpha(100)

    #fade out next scene
    def screen_fader(self):
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