
import sys, pygame
from pygame import mixer
from scenes import Display_Scene

#initialize game
pygame.init()
mixer.init()

class Game_Features(Display_Scene):

    def __init__(self):
        self.scene = 'A'

    def scene_manager(self):
        self.blit_screen()
        if self.scene == 'A':
            self.nodeA()
        if self.scene == 'B':
            self.nodeB()
        if self.scene == 'C':
            self.nodeC(self.click_count)
        if self.scene == 'D':
            self.nodeD(self.click_count)
        if self.scene == 'E':
            self.nodeE()
        if self.scene == 'F':
            self.nodeF(self.click_count)
        if self.scene == 'e':
            self.nodee(self.click_count)
        if self.scene == 'G':
            self.nodeG()
        if self.scene == 'H':
            self.nodeH(self.click_count)
        if self.scene == 'g':
            self.nodeg(self.click_count)
        if self.scene == 'I':
            self.nodeI(self.click_count)
        if self.scene == 'f':
            self.nodef(self.click_count)
        if self.scene == 'J':
            self.nodeJ()
        if self.scene == 'K':
            self.nodeK(self.click_count)
        if self.scene == 'L':
            self.nodeL(self.click_count)
        if self.scene == 'M':
            self.nodeM(self.click_count)
        if self.scene == 'N':
            self.nodeN(self.click_count)
        if self.scene == 'O':
            self.nodeO()
        if self.scene == 'P':
            self.nodeP(self.click_count)
        if self.scene == 'o':
            self.nodeo(self.click_count)
        if self.scene == 'Q':
            self.nodeQ(self.click_count)
        if self.scene == 'R':
            self.nodeR()
        if self.scene == 'S':
            self.nodeS(self.click_count)
        if self.scene == 'r':
            self.noder(self.click_count)
        if self.scene == 'game_over':
            self.game_over(self.go_scene)
        if self.scene == 'play_again':
            self.play_again(self.scene)
        self.user_decision(self.scene)

    def blit_screen(self):
        #resize display
        w, h = pygame.display.get_surface().get_size()
        self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
        #resize rectangles for collision detection
        if self.scene == 'A':
            self.START_BUTTON_POS = pygame.Rect(w/2.25, h/1.23, w/8.3, h/14)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.START_BUTTON_POS, 3)
        elif self.scene == 'E':
            self.LOOK_INTO_IT_POS = pygame.Rect(w/33.33, h/1.17, w/5.78, h/22.58)
            self.TELL_HIM_POS = pygame.Rect(w/1.47, h/1.17, w/3.34, h/21.88)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.TELL_HIM_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.LOOK_INTO_IT_POS, 3)
        elif self.scene == 'G':
            self.HELP_WITH_POS = pygame.Rect(w/33.33, h/1.17, w/2.88, h/22.58)
            self.MAKE_UP_POS = pygame.Rect(w/1.67, h/1.17, w/2.86, h/22.58)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.HELP_WITH_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.MAKE_UP_POS, 3)
        elif self.scene == 'J':
            self.TAKE_THE_GUN_POS = pygame.Rect(w/33.33, h/1.17, w/5.18, h/22.58)
            self.RUN_AND_HIDE_POS = pygame.Rect(w/1.28, h/1.17, w/5.38, h/22.58)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.TAKE_THE_GUN_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.RUN_AND_HIDE_POS, 3)
        elif self.scene == 'O':
            self.CONTINUE_VOYAGE_POS = pygame.Rect(w/33.33, h/1.17, w/4.18, h/22.58)
            self.JUMP_OFF_SHIP_POS = pygame.Rect(w/1.29, h/1.17, w/5.13, h/22.58)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.CONTINUE_VOYAGE_POS, 3)
            pygame.draw.rect(self.COLLISION_SCREEN, self.WHITE, self.JUMP_OFF_SHIP_POS, 3)
        elif self.scene == 'R':
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
                case 'A':
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
                                self.sceneB_blit_line1()
                                self.sceneB_blit_line2()
                                self.scene = 'B'
                        else:
                            self.START_BUTTON.set_alpha(150)
                    pygame.display.update()
                case 'B':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene C - display click count 0
                        self.screen_fader()
                        self.blit_line1('C')
                        self.blit_line2('C')
                        self.blit_line3('C')
                        self.blit_line4('C')
                        self.click_count = 1
                        self.scene = 'C'
                case 'C':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene C - display click count 1-4
                        if self.click_count <= 3:
                            self.blit_line1('C', self.click_count)
                            self.blit_line2('C', self.click_count)
                            self.blit_line3('C', self.click_count)
                            self.blit_line4('C', self.click_count)
                            self.click_count +=1
                        else:
                            #scene D - display click count 0
                            self.screen_fader()
                            self.blit_line1('D')
                            self.blit_line2('D')
                            self.blit_line3('D')
                            self.blit_line4('D')
                            self.click_count = 1
                            self.scene = 'D'
                case 'D':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene D - display click count 1-3
                        if self.click_count <= 3:
                            self.blit_line1('D', self.click_count)
                            self.blit_line2('D', self.click_count)
                            self.blit_line3('D', self.click_count)
                            self.blit_line4('D', self.click_count)
                            self.click_count+=1
                        else:
                            self.scene = 'E'
                            self.narrow_screen('E', 70)
                case 'E':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                        else:
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene F - click 0
                            self.blit_line1('F')
                            self.blit_line2('F')
                            self.blit_line3('F')
                            self.blit_line4('F')
                            self.click_count = 1
                            self.scene = 'F'
                    #if mouse move or click
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 1
                            self.x_right -= 1
                            self.clock.tick(60)
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
                                #scene F - click 0
                                self.blit_line1('F')
                                self.blit_line2('F')
                                self.blit_line3('F')
                                self.blit_line4('F')
                                self.click_count = 1
                                self.scene = 'F'
                        elif CHOICE_B:
                            #bold option
                            self.TELL_HIM.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.TELL_HIM.set_alpha(100)
                                #scene e - click 0
                                self.blit_line1('e')
                                self.blit_line2('e')
                                self.blit_line3('e')
                                self.blit_line4('e')
                                self.click_count = 1
                                self.scene = 'e'
                        else:
                            self.LOOK_INTO_IT.set_alpha(100)
                            self.TELL_HIM.set_alpha(100)
                case 'F':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene F - click 1 - 3
                        if self.click_count <= 3:
                            self.blit_line1('F', self.click_count)
                            self.blit_line2('F', self.click_count)
                            self.blit_line3('F', self.click_count)
                            self.blit_line4('F', self.click_count)
                            self.click_count +=1
                        else:
                            self.narrow_screen('G', 70)
                            self.scene = 'G'
                case 'e':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene e - click 1 - 4
                        if self.click_count <= 4:
                            self.blit_line1('e', self.click_count)
                            self.blit_line2('e', self.click_count)
                            self.blit_line3('e', self.click_count)
                            self.blit_line4('e', self.click_count)
                            self.click_count +=1
                        else:
                            self.go_scene = 'e'
                            self.game_over_fader(self.go_scene)
                            self.scene = 'game_over'
                case 'G':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                        else:
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene H - click 0
                            self.blit_line1('H')
                            self.blit_line2('H')
                            self.blit_line3('H')
                            self.blit_line4('H')
                            self.click_count = 1
                            self.scene = 'H'
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 1
                            self.x_right -= 1
                            self.clock.tick(60)
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
                                #scene H - click 0
                                self.blit_line1('H')
                                self.blit_line2('H')
                                self.blit_line3('H')
                                self.blit_line4('H')
                                self.click_count = 1
                                self.scene = 'H'
                        elif CHOICE_B:
                            #bold option
                            self.MAKE_UP.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.MAKE_UP.set_alpha(100)
                                #scene g - click 0
                                self.blit_line1('g')
                                self.blit_line2('g')
                                self.blit_line3('g')
                                self.blit_line4('g')
                                self.click_count = 1
                                self.scene = 'g'
                        else:
                            self.HELP_WITH.set_alpha(100)
                            self.MAKE_UP.set_alpha(100)
                case 'H':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.click_count <= 1:
                            #scene H - click 1
                            self.blit_line1('H', self.click_count)
                            self.blit_line2('H', self.click_count)
                            self.blit_line3('H', self.click_count)
                            self.blit_line4('H', self.click_count)
                            self.click_count+=1
                        else:
                            #scene I - click 0
                            self.screen_fader()
                            self.blit_line1('I')
                            self.blit_line2('I')
                            self.blit_line3('I')
                            self.blit_line4('I')
                            self.click_count = 1
                            self.scene = 'I'
                case 'g':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.click_count <= 1:
                            #scene g - click 1
                            self.blit_line1('g', self.click_count)
                            self.blit_line2('g', self.click_count)
                            self.blit_line3('g', self.click_count)
                            self.blit_line4('g', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene f - click 0
                            self.blit_line1('f')
                            self.blit_line2('f')
                            self.blit_line3('f')
                            self.blit_line4('f')
                            self.click_count = 1
                            self.scene = 'f'
                case 'I':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene I - click 1
                        if self.click_count <= 1:
                            self.blit_line1('I', self.click_count)
                            self.blit_line2('I', self.click_count)
                            self.blit_line3('I', self.click_count)
                            self.blit_line4('I', self.click_count)
                            self.click_count+=1
                    else:
                        self.narrow_screen('J', 70)
                        self.scene = 'J'
                case 'f':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene f - click 1
                        if self.click_count <= 1:
                            self.blit_line1('f', self.click_count)
                            self.blit_line2('f', self.click_count)
                            self.blit_line3('f', self.click_count)
                            self.blit_line4('f', self.click_count)
                            self.click_count+=1
                        else:
                            self.go_scene = 'f'
                            self.game_over_fader(self.go_scene)
                            self.scene = 'game_over'
                case 'J':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                            self.clock.tick(60)
                        else:
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene K - click 0
                            self.blit_line1('K')
                            self.blit_line2('K')
                            self.blit_line3('K')
                            self.blit_line4('K')
                            self.click_count = 1
                            self.scene = 'K'
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
                                #scene K - click 0
                                self.blit_line1('K')
                                self.blit_line2('K')
                                self.blit_line3('K')
                                self.blit_line4('K')
                                self.click_count = 1
                                self.scene = 'K'
                        elif CHOICE_B:
                            #bold option
                            self.RUN_AND_HIDE.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.RUN_AND_HIDE.set_alpha(100)
                                #scene K - click 0
                                self.blit_line1('K')
                                self.blit_line2('K')
                                self.blit_line3('K')
                                self.blit_line4('K')
                                self.click_count = 1
                                self.scene = 'K'
                        else:
                            self.TAKE_THE_GUN.set_alpha(100)
                            self.RUN_AND_HIDE.set_alpha(100)
                case 'K':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene K - click 1 - 2
                        if self.click_count <= 2:
                            self.blit_line1('K', self.click_count)
                            self.blit_line2('K', self.click_count)
                            self.blit_line3('K', self.click_count)
                            self.blit_line4('K', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene L - click 0
                            self.blit_line1('L')
                            self.blit_line2('L')
                            self.blit_line3('L')
                            self.blit_line4('L')
                            self.click_count = 1
                            self.scene = 'L'
                case 'L':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene L - click 1 - 4
                        if self.click_count <= 4:
                            self.blit_line1('L', self.click_count)
                            self.blit_line2('L', self.click_count)
                            self.blit_line3('L', self.click_count)
                            self.blit_line4('L', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene M - click 0
                            self.blit_line1('M')
                            self.blit_line2('M')
                            self.blit_line3('M')
                            self.blit_line4('M')
                            self.click_count = 1
                            self.scene = 'M'
                case 'M':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene M - click 1 - 3
                        if self.click_count <= 3:
                            self.blit_line1('M', self.click_count)
                            self.blit_line2('M', self.click_count)
                            self.blit_line3('M', self.click_count)
                            self.blit_line4('M', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene N - click 0
                            self.blit_line1('N')
                            self.blit_line2('N')
                            self.blit_line3('N')
                            self.blit_line4('N')
                            self.click_count = 1
                            self.scene = 'N'
                case 'N':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene N - click 1
                        if self.click_count <= 1:
                            self.blit_line1('N', self.click_count)
                            self.blit_line2('N', self.click_count)
                            self.blit_line3('N', self.click_count)
                            self.blit_line4('N', self.click_count)
                            self.click_count+=1
                        else:
                            self.narrow_screen('O', 70)
                            self.scene = 'O'
                case 'O':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                        else:
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene P - click 0
                            self.blit_line1('P')
                            self.blit_line2('P')
                            self.blit_line3('P')
                            self.blit_line4('P')
                            self.click_count = 1
                            self.scene = 'P'
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 1
                            self.x_right -= 1
                            self.clock.tick(60)
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
                                #scene P - click 0
                                self.blit_line1('P')
                                self.blit_line2('P')
                                self.blit_line3('P')
                                self.blit_line4('P')
                                self.click_count = 1
                                self.scene = 'P'
                        elif CHOICE_B:
                            #bold option
                            self.JUMP_OFF_SHIP.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.JUMP_OFF_SHIP.set_alpha(100)
                                #scene o - click 0
                                self.blit_line1('o')
                                self.blit_line2('o')
                                self.blit_line3('o')
                                self.blit_line4('o')
                                self.click_count = 1
                                self.scene = 'o'
                        else:
                            self.CONTINUE_VOYAGE.set_alpha(100)
                            self.JUMP_OFF_SHIP.set_alpha(100)
                case 'P':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene P - click 1
                        if self.click_count <= 1:
                            self.blit_line1('P', self.click_count)
                            self.blit_line2('P', self.click_count)
                            self.blit_line3('P', self.click_count)
                            self.blit_line4('P', self.click_count)
                            self.click_count+=1
                        else:
                            self.screen_fader()
                            #scene Q - click 0
                            self.blit_line1('Q')
                            self.blit_line2('Q')
                            self.blit_line3('Q')
                            self.blit_line4('Q')
                            self.click_count = 1
                            self.scene = 'Q'
                case 'o':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene o - click 1
                        if self.click_count <= 1:
                            self.blit_line1('o', self.click_count)
                            self.blit_line2('o', self.click_count)
                            self.blit_line3('o', self.click_count)
                            self.blit_line4('o', self.click_count)
                            self.click_count+=1
                        else:
                            self.go_scene = 'o'
                            self.game_over_fader(self.go_scene)
                            self.scene = 'game_over'
                case 'Q':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene Q - click 1 - 3
                        if self.click_count <= 3:
                            self.blit_line1('Q', self.click_count)
                            self.blit_line2('Q', self.click_count)
                            self.blit_line3('Q', self.click_count)
                            self.blit_line4('Q', self.click_count)
                            self.click_count+=1
                        else:
                            self.narrow_screen('R', 90)
                            self.scene = 'R'
                case 'R':
                    timer_interval = 50 # 0.5 sec
                    timer_event = pygame.USEREVENT
                    pygame.time.set_timer(timer_event, timer_interval)
                    if event.type == timer_event:
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 2
                            self.x_right -= 2
                        else:
                            pygame.mixer.Sound.play(self.SELECT)
                            self.screen_fader()
                            #scene S - click 0
                            self.blit_line1('S')
                            self.blit_line2('S')
                            self.blit_line3('S')
                            self.blit_line4('S')
                            self.click_count = 1
                            self.scene = 'S'
                    if (event.type == pygame.MOUSEMOTION) or (event.type == pygame.MOUSEBUTTONDOWN):
                        #stop if black lines reach white line midpoint
                        if self.x_left < 100:
                            self.x_left += 1
                            self.x_right -= 1
                            self.clock.tick(60)
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
                                #scene S - click 0
                                self.blit_line1('S')
                                self.blit_line2('S')
                                self.blit_line3('S')
                                self.blit_line4('S')
                                self.click_count = 1
                                self.scene = 'S'
                        elif CHOICE_B:
                            #bold option
                            self.RUN_AWAY.set_alpha(300)
                            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                                pygame.mixer.Sound.play(self.SELECT)
                                self.screen_fader()
                                self.RUN_AWAY.set_alpha(100)
                                #scene r - click 0
                                self.blit_line1('r')
                                self.blit_line2('r')
                                self.blit_line3('r')
                                self.blit_line4('r')
                                self.click_count = 1
                                self.scene = 'r'
                        else:
                            self.ATTACK_IT.set_alpha(100)
                            self.RUN_AWAY.set_alpha(100)
                case 'S':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene S - click 1 - 3
                        if self.click_count <= 3:
                            self.blit_line1('S', self.click_count)
                            self.blit_line2('S', self.click_count)
                            self.blit_line3('S', self.click_count)
                            self.blit_line4('S', self.click_count)
                            self.click_count+=1
                        else:
                            self.go_scene = 'S'
                            self.game_over_fader(self.go_scene)
                            self.scene = 'game_over'
                case 'r':
                    self.x_left = -290
                    self.x_right = 864
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #scene r - click 1 - 2
                        if self.click_count <= 2:
                            self.blit_line1('r', self.click_count)
                            self.blit_line2('r', self.click_count)
                            self.blit_line3('r', self.click_count)
                            self.blit_line4('r', self.click_count)
                            self.click_count+=1
                        else:
                            self.go_scene = 'r'
                            self.game_over_fader(self.go_scene)
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
                                self.scene = 'A'
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

