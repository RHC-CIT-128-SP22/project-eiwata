
import sys, pygame
from pygame import mixer
from scenes import Display_Scene

pygame.init()
mixer.init()

class Game_Features(Display_Scene):
    def __init__(self):
        self.scene = 'node1'
        self.WIN_RESIZED = False
        self.scene3_count = 0
        self.scene4_count = 0
        self.scene6_count = 0
        self.scene7_count = 0
        self.scene9_count = 0
        self.scene10_count = 0
        self.scene11_count = 0
        self.scene12_count = 0
        self.scene14_count = 0
        self.scene15_count = 0
        self.scene16_count = 0
        self.scene17_count = 0
        self.scene19_count = 0
        self.scene20_count = 0
        self.scene21_count = 0
        self.scene23_count = 0
        self.scene24_count = 0

    def scene_manager(self):
        self.blit_screen()
        if self.scene == 'node1':
            self.node1()
            self.user_decision('node1')
        if self.scene == 'node2':
            self.node2()
            self.user_decision('node2')
        if self.scene == 'node3':
            self.node3(self.scene3_count)
            self.user_decision('node3')
        if self.scene == 'node4':
            self.node4(self.scene4_count)
            self.user_decision('node4')
        if self.scene == 'node5':
            self.node5()
            self.user_decision('node5')
        if self.scene == 'node6':
            self.node6(self.scene6_count)
            self.user_decision('node6')
        if self.scene == 'node7':
            self.node7(self.scene7_count)
            self.user_decision('node7')
        if self.scene == 'node8':
            self.node8()
            self.user_decision('node8')
        if self.scene == 'node9':
            self.node9(self.scene9_count)
            self.user_decision('node9')
        if self.scene == 'node10':
            self.node10(self.scene10_count)
            self.user_decision('node10')
        if self.scene == 'node11':
            self.node11(self.scene11_count)
            self.user_decision('node11')
        if self.scene == 'node12':
            self.node12(self.scene12_count)
            self.user_decision('node12')
        if self.scene == 'node13':
            self.node13()
            self.user_decision('node13')
        if self.scene == 'node14':
            self.node14(self.scene14_count)
            self.user_decision('node14')
        if self.scene == 'node15':
            self.node15(self.scene15_count)
            self.user_decision('node15')
        if self.scene == 'node16':
            self.node16(self.scene16_count)
            self.user_decision('node16')
        if self.scene == 'node17':
            self.node17(self.scene17_count)
            self.user_decision('node17')
        if self.scene == 'node18':
            self.node18()
            self.user_decision('node18')
        if self.scene == 'node19':
            self.node19(self.scene19_count)
            self.user_decision('node19')
        if self.scene == 'node20':
            self.node20(self.scene20_count)
            self.user_decision('node20')
        if self.scene == 'node21':
            self.node21(self.scene21_count)
            self.user_decision('node21')
        if self.scene == 'node22':
            self.node22()
            self.user_decision('node22')
        if self.scene == 'node23':
            self.node23(self.scene23_count)
            self.user_decision('node23')
        if self.scene == 'node24':
            self.node24(self.scene24_count)
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
                self.TELL_HIM_POS = pygame.Rect(w/1.47, h/1.17, w/3.34, h/21.88)
                self.LOOK_INTO_IT_POS = pygame.Rect(w/33.33, h/1.17, w/5.78, h/22.58)
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
                                self.scene2_blit_line1()
                                self.scene2_blit_line2()
                                self.scene = 'node2'
                        else:
                            self.START_BUTTON.set_alpha(150)
                    pygame.display.update()
                case 'node2':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 3 - display click count 0
                        self.screen_fader()
                        self.blit_line1('node3', self.scene3_count)
                        self.blit_line2('node3', self.scene3_count)
                        self.blit_line3('node3', self.scene3_count)
                        self.blit_line4('node3', self.scene3_count)
                        self.scene3_count+=1
                        self.scene = 'node3'
                case 'node3':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 3 - display click count 1-4
                        if self.scene3_count <= 3:
                            self.blit_line1('node3', self.scene3_count)
                            self.blit_line2('node3', self.scene3_count)
                            self.blit_line3('node3', self.scene3_count)
                            self.blit_line4('node3', self.scene3_count)
                            self.scene3_count+=1
                        else:
                            #scene 4 - display click count 0
                            self.screen_fader()
                            self.blit_line1('node4', self.scene4_count)
                            self.blit_line2('node4', self.scene4_count)
                            self.blit_line3('node4', self.scene4_count)
                            self.blit_line4('node4', self.scene4_count)
                            self.scene4_count+=1
                            self.scene = 'node4'
                case 'node4':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 4 - display click count 1-3
                        if self.scene4_count <= 3:
                            self.blit_line1('node4', self.scene4_count)
                            self.blit_line2('node4', self.scene4_count)
                            self.blit_line3('node4', self.scene4_count)
                            self.blit_line4('node4', self.scene4_count)
                            self.scene4_count+=1
                        else:
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
                                self.screen_fader()
                                #scene 6 - click 0
                                self.blit_line1('node6', self.scene6_count)
                                self.blit_line2('node6', self.scene6_count)
                                self.blit_line3('node6', self.scene6_count)
                                self.blit_line4('node6', self.scene6_count)
                                self.scene6_count+=1
                                self.scene = 'node6'
                        elif CHOICE_B:
                            #bold option
                            self.TELL_HIM.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                self.screen_fader()
                                #scene 7 - click 0
                                self.blit_line1('node7', self.scene7_count)
                                self.blit_line2('node7', self.scene7_count)
                                self.blit_line3('node7', self.scene7_count)
                                self.blit_line4('node7', self.scene7_count)
                                self.scene7_count+=1
                                self.scene = 'node7'
                        else:
                            self.LOOK_INTO_IT.set_alpha(100)
                            self.TELL_HIM.set_alpha(100)
                case 'node6':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 6 - click 1 - 3
                        if self.scene6_count <= 3:
                            self.blit_line1('node6', self.scene6_count)
                            self.blit_line2('node6', self.scene6_count)
                            self.blit_line3('node6', self.scene6_count)
                            self.blit_line4('node6', self.scene6_count)
                            self.scene6_count+=1
                        else:
                            self.narrow_screen(8, 70)
                            self.scene = 'node8'
                case 'node7':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 7 - click 1 - 4
                        if self.scene7_count <= 4:
                            self.blit_line1('node7', self.scene7_count)
                            self.blit_line2('node7', self.scene7_count)
                            self.blit_line3('node7', self.scene7_count)
                            self.blit_line4('node7', self.scene7_count)
                            self.scene7_count+=1
                        else:
                            pygame.quit()
                            sys.exit('QUIT GAME')
                case 'node8':
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()
                        
                        CHOICE_A = self.HELP_WITH_POS.collidepoint(mx, my)
                        CHOICE_B = self.MAKE_UP_POS.collidepoint(mx, my)
                        #if hovering over option
                        if CHOICE_A:
                            #bold option
                            self.HELP_WITH.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                self.screen_fader()
                                #scene 9 - click 0
                                self.blit_line1('node9', self.scene9_count)
                                self.blit_line2('node9', self.scene9_count)
                                self.blit_line3('node9', self.scene9_count)
                                self.blit_line4('node9', self.scene9_count)
                                self.scene9_count+=1
                                self.scene = 'node9'
                        elif CHOICE_B:
                            #bold option
                            self.MAKE_UP.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                self.screen_fader()
                                #scene 10 - click 0
                                self.blit_line1('node10', self.scene10_count)
                                self.blit_line2('node10', self.scene10_count)
                                self.blit_line3('node10', self.scene10_count)
                                self.blit_line4('node10', self.scene10_count)
                                self.scene10_count+=1
                                self.scene = 'node10'
                        else:
                            self.HELP_WITH.set_alpha(100)
                            self.MAKE_UP.set_alpha(100)
                case 'node9':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.scene9_count <= 1:
                            #scene 9 - click 1
                            self.blit_line1('node9', self.scene9_count)
                            self.blit_line2('node9', self.scene9_count)
                            self.blit_line3('node9', self.scene9_count)
                            self.blit_line4('node9', self.scene9_count)
                            self.scene9_count+=1
                        else:
                            self.screen_fader()
                            self.blit_line1('node11', self.scene11_count)
                            self.blit_line2('node11', self.scene11_count)
                            self.blit_line3('node11', self.scene11_count)
                            self.blit_line4('node11', self.scene11_count)
                            self.scene11_count+=1
                            self.scene = 'node11'
                case 'node10':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.scene10_count <= 1:
                            #scene 10 - click 1
                            self.blit_line1('node10', self.scene10_count)
                            self.blit_line2('node10', self.scene10_count)
                            self.blit_line3('node10', self.scene10_count)
                            self.blit_line4('node10', self.scene10_count)
                            self.scene10_count+=1
                        else:
                            self.screen_fader()
                            self.blit_line1('node12', self.scene12_count)
                            self.blit_line2('node12', self.scene12_count)
                            self.blit_line3('node12', self.scene12_count)
                            self.blit_line4('node12', self.scene12_count)
                            self.scene12_count+=1
                            self.scene = 'node12'
                case 'node11':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.scene11_count <= 1:
                            self.blit_line1('node11', self.scene11_count)
                            self.blit_line2('node11', self.scene11_count)
                            self.blit_line3('node11', self.scene11_count)
                            self.blit_line4('node11', self.scene11_count)
                            self.scene11_count+=1
                    else:
                        self.narrow_screen(13, 70)
                        self.scene = 'node13'
                case 'node12':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.scene12_count <= 1:
                            self.blit_line1('node12', self.scene12_count)
                            self.blit_line2('node12', self.scene12_count)
                            self.blit_line3('node12', self.scene12_count)
                            self.blit_line4('node12', self.scene12_count)
                            self.scene12_count+=1
                        else:
                            pygame.quit()
                            sys.exit('QUIT GAME')
                case 'node13':
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()

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