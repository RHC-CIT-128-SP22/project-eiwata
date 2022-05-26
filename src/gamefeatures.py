
import sys, pygame
from pygame import mixer
from scenes import Display_Scene

#initialize game
pygame.init()
mixer.init()

class Game_Features(Display_Scene):

    def __init__(self):
        self.scene = 'node1'

    def scene_manager(self):
        self.blit_screen()
        if self.scene == 'node1':
            self.node1()
        if self.scene == 'node2':
            self.node2()
        if self.scene == 'node3':
            self.node3(self.click_count)
        if self.scene == 'node4':
            self.node4(self.click_count)
        if self.scene == 'node5':
            self.node5()
        if self.scene == 'node6':
            self.node6(self.click_count)
        if self.scene == 'node7':
            self.node7(self.click_count)
        if self.scene == 'node8':
            self.node8()
        if self.scene == 'node9':
            self.node9(self.click_count)
        if self.scene == 'node10':
            self.node10(self.click_count)
        if self.scene == 'node11':
            self.node11(self.click_count)
        if self.scene == 'node12':
            self.node12(self.click_count)
        if self.scene == 'node13':
            self.node13()
        if self.scene == 'node14':
            self.node14(self.click_count)
        if self.scene == 'node15':
            self.node15(self.click_count)
        if self.scene == 'node16':
            self.node16(self.click_count)
        if self.scene == 'node17':
            self.node17(self.click_count)
        if self.scene == 'node18':
            self.node18()
        if self.scene == 'node19':
            self.node19(self.click_count)
        if self.scene == 'node20':
            self.node20(self.click_count)
        if self.scene == 'node21':
            self.node21(self.click_count)
        if self.scene == 'node22':
            self.node22()
        if self.scene == 'node23':
            self.node23(self.click_count)
        if self.scene == 'node24':
            self.node24(self.click_count)
        if self.scene == 'game_over':
            self.game_over(self.game_over_scene)
        self.user_decision(self.scene)

    def blit_screen(self):
        #resize display
        w, h = pygame.display.get_surface().get_size()
        self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
        #resize rectangles for collision detection
        if self.scene == 'node1':
            self.START_BUTTON_POS = pygame.Rect(w/2.25, h/1.23, w/8.3, h/14)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.START_BUTTON_POS, 3)
        elif self.scene == 'node5':
            self.LOOK_INTO_IT_POS = pygame.Rect(w/33.33, h/1.17, w/5.78, h/22.58)
            self.TELL_HIM_POS = pygame.Rect(w/1.47, h/1.17, w/3.34, h/21.88)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.TELL_HIM_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.LOOK_INTO_IT_POS, 3)
        elif self.scene == 'node8':
            self.HELP_WITH_POS = pygame.Rect(w/33.33, h/1.17, w/2.88, h/22.58)
            self.MAKE_UP_POS = pygame.Rect(w/1.67, h/1.17, w/2.86, h/22.58)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.HELP_WITH_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.MAKE_UP_POS, 3)
        elif self.scene == 'node13':
            self.TAKE_THE_GUN_POS = pygame.Rect(w/33.33, h/1.17, w/5.18, h/22.58)
            self.RUN_AND_HIDE_POS = pygame.Rect(w/1.28, h/1.17, w/5.38, h/22.58)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.TAKE_THE_GUN_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.RUN_AND_HIDE_POS, 3)
        elif self.scene == 'node18':
            self.CONTINUE_VOYAGE_POS = pygame.Rect(w/33.33, h/1.17, w/4.18, h/22.58)
            self.JUMP_OFF_SHIP_POS = pygame.Rect(w/1.29, h/1.17, w/5.13, h/22.58)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.CONTINUE_VOYAGE_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.JUMP_OFF_SHIP_POS, 3)
        elif self.scene == 'node22':
            self.ATTACK_IT_POS = pygame.Rect(w/33.33, h/1.17, w/7.41, h/22.58)
            self.RUN_AWAY_POS = pygame.Rect(w/1.21, h/1.17, w/7.04, h/22.58)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.ATTACK_IT_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.RUN_AWAY_POS, 3)
        elif self.scene == 'game_over':
            self.CONTINUE_POS = pygame.Rect(w/6.67, h/1.75, w/4.15, h/14.58)
            self.EXIT_POS = pygame.Rect(w/1.47, h/1.75, w/9.62, h/14.89)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.CONTINUE_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.EXIT_POS, 3)

    def user_decision(self, scene):
        for event in pygame.event.get():
            #if user quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('QUIT GAME')
            #if window is being resized
            if (event.type == pygame.VIDEORESIZE):
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
                                self.screen_fader()
                                self.START_BUTTON.set_alpha(120)
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
                        self.blit_line1('node3')
                        self.blit_line2('node3')
                        self.blit_line3('node3')
                        self.blit_line4('node3')
                        self.click_count = 1
                        self.scene = 'node3'
                case 'node3':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 3 - display click count 1-4
                        if self.click_count <= 3:
                            self.blit_line1('node3', self.click_count)
                            self.blit_line2('node3', self.click_count)
                            self.blit_line3('node3', self.click_count)
                            self.blit_line4('node3', self.click_count)
                            self.click_count +=1
                        else:
                            #scene 4 - display click count 0
                            self.screen_fader()
                            self.blit_line1('node4')
                            self.blit_line2('node4')
                            self.blit_line3('node4')
                            self.blit_line4('node4')
                            self.click_count = 1
                            self.scene = 'node4'
                case 'node4':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 4 - display click count 1-3
                        if self.click_count <= 3:
                            self.blit_line1('node4', self.click_count)
                            self.blit_line2('node4', self.click_count)
                            self.blit_line3('node4', self.click_count)
                            self.blit_line4('node4', self.click_count)
                            self.click_count+=1
                        else:
                            self.scene = 'node5'
                            self.narrow_screen(5, 70)
                case 'node5':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                        else:
                            self.LOOK_INTO_IT.set_alpha(300)
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene 6 - click 0
                            self.blit_line1('node6')
                            self.blit_line2('node6')
                            self.blit_line3('node6')
                            self.blit_line4('node6')
                            self.click_count = 1
                            self.scene = 'node6'
                    #if mouse move or click
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 1
                            self.x_right -= 1
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()
                        
                        CHOICE_A = self.LOOK_INTO_IT_POS.collidepoint(mx, my)
                        CHOICE_B = self.TELL_HIM_POS.collidepoint(mx, my)

                        #if hovering over option
                        if CHOICE_A:
                            #bold option
                            self.LOOK_INTO_IT.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.LOOK_INTO_IT.set_alpha(100)
                                #scene 6 - click 0
                                self.blit_line1('node6')
                                self.blit_line2('node6')
                                self.blit_line3('node6')
                                self.blit_line4('node6')
                                self.click_count = 1
                                self.scene = 'node6'
                        elif CHOICE_B:
                            #bold option
                            self.TELL_HIM.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.TELL_HIM.set_alpha(100)
                                #scene 7 - click 0
                                self.blit_line1('node7')
                                self.blit_line2('node7')
                                self.blit_line3('node7')
                                self.blit_line4('node7')
                                self.click_count = 1
                                self.scene = 'node7'
                        else:
                            self.LOOK_INTO_IT.set_alpha(100)
                            self.TELL_HIM.set_alpha(100)
                case 'node6':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 6 - click 1 - 3
                        if self.click_count <= 3:
                            self.blit_line1('node6', self.click_count)
                            self.blit_line2('node6', self.click_count)
                            self.blit_line3('node6', self.click_count)
                            self.blit_line4('node6', self.click_count)
                            self.click_count +=1
                        else:
                            self.narrow_screen(8, 70)
                            self.scene = 'node8'
                case 'node7':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 7 - click 1 - 4
                        if self.click_count <= 4:
                            self.blit_line1('node7', self.click_count)
                            self.blit_line2('node7', self.click_count)
                            self.blit_line3('node7', self.click_count)
                            self.blit_line4('node7', self.click_count)
                            self.click_count +=1
                        else:
                            self.game_over_scene = 7
                            self.game_over_fader(self.game_over_scene)
                            self.scene = 'game_over'
                case 'node8':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                        else:
                            self.HELP_WITH.set_alpha(300)
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene 9 - click 0
                            self.blit_line1('node9')
                            self.blit_line2('node9')
                            self.blit_line3('node9')
                            self.blit_line4('node9')
                            self.click_count = 1
                            self.scene = 'node9'
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 1
                            self.x_right -= 1
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()
                        
                        CHOICE_A = self.HELP_WITH_POS.collidepoint(mx, my)
                        CHOICE_B = self.MAKE_UP_POS.collidepoint(mx, my)
                        #if hovering over option
                        if CHOICE_A:
                            #bold option
                            self.HELP_WITH.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.HELP_WITH.set_alpha(100)
                                #scene 9 - click 0
                                self.blit_line1('node9')
                                self.blit_line2('node9')
                                self.blit_line3('node9')
                                self.blit_line4('node9')
                                self.click_count = 1
                                self.scene = 'node9'
                        elif CHOICE_B:
                            #bold option
                            self.MAKE_UP.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.MAKE_UP.set_alpha(100)
                                #scene 10 - click 0
                                self.blit_line1('node10')
                                self.blit_line2('node10')
                                self.blit_line3('node10')
                                self.blit_line4('node10')
                                self.click_count = 1
                                self.scene = 'node10'
                        else:
                            self.HELP_WITH.set_alpha(100)
                            self.MAKE_UP.set_alpha(100)
                case 'node9':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.click_count <= 1:
                            #scene 9 - click 1
                            self.blit_line1('node9', self.click_count)
                            self.blit_line2('node9', self.click_count)
                            self.blit_line3('node9', self.click_count)
                            self.blit_line4('node9', self.click_count)
                            self.click_count+=1
                        else:
                            #scene 11 - click 0
                            self.screen_fader()
                            self.blit_line1('node11')
                            self.blit_line2('node11')
                            self.blit_line3('node11')
                            self.blit_line4('node11')
                            self.click_count = 1
                            self.scene = 'node11'
                case 'node10':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.click_count <= 1:
                            #scene 10 - click 1
                            self.blit_line1('node10', self.click_count)
                            self.blit_line2('node10', self.click_count)
                            self.blit_line3('node10', self.click_count)
                            self.blit_line4('node10', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene 12 - click 0
                            self.blit_line1('node12')
                            self.blit_line2('node12')
                            self.blit_line3('node12')
                            self.blit_line4('node12')
                            self.click_count = 1
                            self.scene = 'node12'
                case 'node11':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 11 - click 1
                        if self.click_count <= 1:
                            self.blit_line1('node11', self.click_count)
                            self.blit_line2('node11', self.click_count)
                            self.blit_line3('node11', self.click_count)
                            self.blit_line4('node11', self.click_count)
                            self.click_count+=1
                    else:
                        self.narrow_screen(13, 70)
                        self.scene = 'node13'
                case 'node12':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 12 - click 1
                        if self.click_count <= 1:
                            self.blit_line1('node12', self.click_count)
                            self.blit_line2('node12', self.click_count)
                            self.blit_line3('node12', self.click_count)
                            self.blit_line4('node12', self.click_count)
                            self.click_count+=1
                        else:
                            self.game_over_scene = 12
                            self.game_over_fader(self.game_over_scene)
                            self.scene = 'game_over'
                case 'node13':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                        else:
                            self.TAKE_THE_GUN.set_alpha(300)
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene 14 - click 0
                            self.blit_line1('node14')
                            self.blit_line2('node14')
                            self.blit_line3('node14')
                            self.blit_line4('node14')
                            self.click_count = 1
                            self.scene = 'node14'
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 1
                            self.x_right -= 1
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()

                        CHOICE_A = self.TAKE_THE_GUN_POS.collidepoint(mx, my)
                        CHOICE_B = self.RUN_AND_HIDE_POS.collidepoint(mx, my)
                        #if hovering over option
                        if CHOICE_A:
                            #bold option
                            self.TAKE_THE_GUN.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.TAKE_THE_GUN.set_alpha(100)
                                #scene 14 - click 0
                                self.blit_line1('node14')
                                self.blit_line2('node14')
                                self.blit_line3('node14')
                                self.blit_line4('node14')
                                self.click_count = 1
                                self.scene = 'node14'
                        elif CHOICE_B:
                            #bold option
                            self.RUN_AND_HIDE.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.RUN_AND_HIDE.set_alpha(100)
                                #scene 14 - click 0
                                self.blit_line1('node14')
                                self.blit_line2('node14')
                                self.blit_line3('node14')
                                self.blit_line4('node14')
                                self.click_count = 1
                                self.scene = 'node14'
                        else:
                            self.TAKE_THE_GUN.set_alpha(100)
                            self.RUN_AND_HIDE.set_alpha(100)
                case 'node14':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 14 - click 1 - 2
                        if self.click_count <= 2:
                            self.blit_line1('node14', self.click_count)
                            self.blit_line2('node14', self.click_count)
                            self.blit_line3('node14', self.click_count)
                            self.blit_line4('node14', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene 15 - click 0
                            self.blit_line1('node15')
                            self.blit_line2('node15')
                            self.blit_line3('node15')
                            self.blit_line4('node15')
                            self.click_count = 1
                            self.scene = 'node15'
                case 'node15':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 15 - click 1 - 4
                        if self.click_count <= 4:
                            self.blit_line1('node15', self.click_count)
                            self.blit_line2('node15', self.click_count)
                            self.blit_line3('node15', self.click_count)
                            self.blit_line4('node15', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene 16 - click 0
                            self.blit_line1('node16')
                            self.blit_line2('node16')
                            self.blit_line3('node16')
                            self.blit_line4('node16')
                            self.click_count = 1
                            self.scene = 'node16'
                case 'node16':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 16 - click 1 - 3
                        if self.click_count <= 3:
                            self.blit_line1('node16', self.click_count)
                            self.blit_line2('node16', self.click_count)
                            self.blit_line3('node16', self.click_count)
                            self.blit_line4('node16', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene 17 - click 0
                            self.blit_line1('node17')
                            self.blit_line2('node17')
                            self.blit_line3('node17')
                            self.blit_line4('node17')
                            self.click_count = 1
                            self.scene = 'node17'
                case 'node17':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 17 - click 1
                        if self.click_count <= 1:
                            self.blit_line1('node17', self.click_count)
                            self.blit_line2('node17', self.click_count)
                            self.blit_line3('node17', self.click_count)
                            self.blit_line4('node17', self.click_count)
                            self.click_count+=1
                        else:
                            self.narrow_screen('node18', 70)
                            self.scene = 'node18'
                case 'node18':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                        else:
                            self.CONTINUE_VOYAGE.set_alpha(300)
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene 19 - click 0
                            self.blit_line1('node19')
                            self.blit_line2('node19')
                            self.blit_line3('node19')
                            self.blit_line4('node19')
                            self.click_count = 1
                            self.scene = 'node19'
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 1
                            self.x_right -= 1
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()

                        CHOICE_A = self.CONTINUE_VOYAGE_POS.collidepoint(mx, my)
                        CHOICE_B = self.JUMP_OFF_SHIP_POS.collidepoint(mx, my)
                        #if hovering over option
                        if CHOICE_A:
                            #bold option
                            self.CONTINUE_VOYAGE.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.CONTINUE_VOYAGE.set_alpha(100)
                                #scene 19 - click 0
                                self.blit_line1('node19')
                                self.blit_line2('node19')
                                self.blit_line3('node19')
                                self.blit_line4('node19')
                                self.click_count = 1
                                self.scene = 'node19'
                        elif CHOICE_B:
                            #bold option
                            self.JUMP_OFF_SHIP.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.JUMP_OFF_SHIP.set_alpha(100)
                                #scene 20 - click 0
                                self.blit_line1('node20')
                                self.blit_line2('node20')
                                self.blit_line3('node20')
                                self.blit_line4('node20')
                                self.click_count = 1
                                self.scene = 'node20'
                        else:
                            self.CONTINUE_VOYAGE.set_alpha(100)
                            self.JUMP_OFF_SHIP.set_alpha(100)
                case 'node19':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 19 - click 1
                        if self.click_count <= 1:
                            self.blit_line1('node19', self.click_count)
                            self.blit_line2('node19', self.click_count)
                            self.blit_line3('node19', self.click_count)
                            self.blit_line4('node19', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene 21 - click 0
                            self.blit_line1('node21')
                            self.blit_line2('node21')
                            self.blit_line3('node21')
                            self.blit_line4('node21')
                            self.click_count = 1
                            self.scene = 'node21'
                case 'node20':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 20 - click 1
                        if self.click_count <= 1:
                            self.blit_line1('node20', self.click_count)
                            self.blit_line2('node20', self.click_count)
                            self.blit_line3('node20', self.click_count)
                            self.blit_line4('node20', self.click_count)
                            self.click_count+=1
                        else:
                            self.game_over_scene = 20
                            self.game_over_fader(self.game_over_scene)
                            self.scene = 'game_over'
                case 'node21':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 21 - click 1 - 3
                        if self.click_count <= 3:
                            self.blit_line1('node21', self.click_count)
                            self.blit_line2('node21', self.click_count)
                            self.blit_line3('node21', self.click_count)
                            self.blit_line4('node21', self.click_count)
                            self.click_count+=1
                        else:
                            self.narrow_screen('node22', 90)
                            self.scene = 'node22'
                case 'node22':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                        else:
                            self.ATTACK_IT.set_alpha(300)
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene 23 - click 0
                            self.blit_line1('node23')
                            self.blit_line2('node23')
                            self.blit_line3('node23')
                            self.blit_line4('node23')
                            self.click_count = 1
                            self.scene = 'node23'
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 1
                            self.x_right -= 1
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()

                        CHOICE_A = self.ATTACK_IT_POS.collidepoint(mx, my)
                        CHOICE_B = self.RUN_AWAY_POS.collidepoint(mx, my)
                        #if hovering over option
                        if CHOICE_A:
                            #bold option
                            self.ATTACK_IT.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.ATTACK_IT.set_alpha(100)
                                #scene 23 - click 0
                                self.blit_line1('node23')
                                self.blit_line2('node23')
                                self.blit_line3('node23')
                                self.blit_line4('node23')
                                self.click_count = 1
                                self.scene = 'node23'
                        elif CHOICE_B:
                            #bold option
                            self.RUN_AWAY.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.RUN_AWAY.set_alpha(100)
                                #scene 24 - click 0
                                self.blit_line1('node24')
                                self.blit_line2('node24')
                                self.blit_line3('node24')
                                self.blit_line4('node24')
                                self.click_count = 1
                                self.scene = 'node24'
                        else:
                            self.ATTACK_IT.set_alpha(100)
                            self.RUN_AWAY.set_alpha(100)
                case 'node23':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 23 - click 1 - 3
                        if self.click_count <= 3:
                            self.blit_line1('node23', self.click_count)
                            self.blit_line2('node23', self.click_count)
                            self.blit_line3('node23', self.click_count)
                            self.blit_line4('node23', self.click_count)
                            self.click_count+=1
                        else:
                            self.game_over_scene = 23
                            self.game_over_fader(self.game_over_scene)
                            self.scene = 'game_over'
                case 'node24':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene 24 - click 1 - 2
                        if self.click_count <= 2:
                            self.blit_line1('node24', self.click_count)
                            self.blit_line2('node24', self.click_count)
                            self.blit_line3('node24', self.click_count)
                            self.blit_line4('node24', self.click_count)
                            self.click_count+=1
                        else:
                            self.game_over_scene = 24
                            self.game_over_fader(self.game_over_scene)
                            self.scene = 'game_over'
                case 'game_over':
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #get mouse position
                        mx, my = pygame.mouse.get_pos()

                        CHOICE_A = self.CONTINUE_POS.collidepoint(mx, my)
                        CHOICE_B = self.EXIT_POS.collidepoint(mx, my)
                        #if hovering over option
                        if CHOICE_A:
                            #bold option
                            self.CONTINUE.set_alpha(300)
                        elif CHOICE_B:
                            #bold option
                            self.EXIT.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.EXIT.set_alpha(120)
                                self.scene = 'node1'
                        else:
                            self.CONTINUE.set_alpha(90)
                            self.EXIT.set_alpha(90)

    #fade to next scene
    def screen_fader(self):
        w, h = pygame.display.get_surface().get_size()
        fade = pygame.Surface((self.X, self.Y))
        fade.fill(self.BLACK)
        for alpha in range(0, 300):
            self.PSEUDO_SCREEN.set_alpha(alpha)
            self.PSEUDO_SCREEN.blit(fade, (0, 0))
            self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
            pygame.display.update()

