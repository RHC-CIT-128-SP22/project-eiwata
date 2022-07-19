
import pygame
from initgame import Init_Game

#initialize game
pygame.init()
pygame.font.init()
pygame.mixer.init()

class Narrator(Init_Game):

    #create clock
    FPS = 200

    #initialize font and colors
    FONT = pygame.font.SysFont('Rockwell', 19)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #initialize variables
    line1_v2 = ''
    line2_v2 = ''
    line3_v2 = ''
    line4_v2 = ''
    line1_v3 = FONT.render(line1_v2, True, WHITE)
    line2_v3 = FONT.render(line2_v2, True, WHITE)
    line3_v3 = FONT.render(line3_v2, True, WHITE)
    line4_v3 = FONT.render(line4_v2, True, WHITE)

    #display line 1
    def blit_line1(self, scene, count = 0):
        #initialize variables
        w, h = pygame.display.get_surface().get_size()

        #seek line number per scene for every click count
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'C':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.UNIVERSITY, (0, 80))
                    match count:
                        case 0:
                            f.seek(self.char_counter(8))
                        case 1:
                            f.seek(self.char_counter(12))
                        case 2:
                            f.seek(self.char_counter(16))
                        case 3:
                            f.seek(self.char_counter(20))
                case 'D':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.HORROR_IN_CLAY, (0, 70))
                    match count:
                        case 0:
                            f.seek(self.char_counter(27))
                        case 1:
                            f.seek(self.char_counter(31))
                        case 2:
                            f.seek(self.char_counter(35))
                        case 3:
                            f.seek(self.char_counter(39))
                case 'F':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.INVESTIGATION_1, (0, 70))
                    match count:
                        case 0:
                            f.seek(self.char_counter(44))
                        case 1:
                            f.seek(self.char_counter(48))
                        case 2:
                            f.seek(self.char_counter(52))
                        case 3:
                            f.seek(self.char_counter(56))
                case 'e':
                    #display scene
                    self.HOUSE.set_alpha(300)
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.HOUSE, (0, 62.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(61))
                        case 1:
                            f.seek(self.char_counter(65))
                        case 2:
                            f.seek(self.char_counter(69))
                        case 3:
                            f.seek(self.char_counter(73))
                        case 4:
                            f.seek(self.char_counter(77))
                case 'H':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.INVESTIGATION_2, (0, 70))
                    match count:
                        case 0:
                            f.seek(self.char_counter(82))
                        case 1:
                            f.seek(self.char_counter(86))
                case 'g':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.TOWN, (0, 54.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(91))
                        case 1:
                            f.seek(self.char_counter(95))
                case 'I':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(100))
                        case 1:
                            f.seek(self.char_counter(104))
                case 'f':
                    #display scene
                    self.ALONE.set_alpha(300)
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.ALONE, (0, 68.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(110))
                        case 1:
                            f.seek(self.char_counter(114))
                case 'K':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.INVESTIGATION_3, (0, 68.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(119))
                        case 1:
                            f.seek(self.char_counter(123))
                        case 2:
                            f.seek(self.char_counter(127))
                case 'L':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.STATUE, (0, 16.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(132))
                        case 1:
                            f.seek(self.char_counter(136))
                        case 2:
                            f.seek(self.char_counter(140))
                        case 3:
                            f.seek(self.char_counter(144))
                        case 4:
                            f.seek(self.char_counter(148))
                case 'M':
                    #display scene
                    self.HOUSE.set_alpha(300)
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.HOUSE, (0, 62.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(153))
                        case 1:
                            f.seek(self.char_counter(157))
                        case 2:
                            f.seek(self.char_counter(161))
                        case 3:
                            f.seek(self.char_counter(165))
                case 'N':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(170))
                        case 1:
                            f.seek(self.char_counter(174))
                case 'P':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.DOCK, (0, 68.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(180))
                        case 1:
                            f.seek(self.char_counter(184))
                case 'o':
                    #display scene
                    self.SAIL.set_alpha(300)
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.SAIL, (0, 37.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(191))
                        case 1:
                            f.seek(self.char_counter(195))
                case 'Q':
                    #display scene
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.RLYEH_1, (0, 90))
                    match count:
                        case 0:
                            f.seek(self.char_counter(201))
                        case 1:
                            f.seek(self.char_counter(205))
                        case 2:
                            f.seek(self.char_counter(209))
                        case 3:
                            f.seek(self.char_counter(213))
                case 'S':
                    #display scene
                    self.RLYEH_2.set_alpha(300)
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.RLYEH_2, (0, 63.5))
                    match count:
                        case 0:
                            f.seek(self.char_counter(218))
                        case 1:
                            f.seek(self.char_counter(222))
                        case 2:
                            f.seek(self.char_counter(226))
                        case 3:
                            f.seek(self.char_counter(230))
                case 'r':
                    #display scene
                    self.RLYEH_3.set_alpha(300)
                    self.PSEUDO_SCREEN.fill(self.BLACK)
                    self.PSEUDO_SCREEN.blit(self.RLYEH_3, (0, 56))
                    match count:
                        case 0:
                            f.seek(self.char_counter(235))
                        case 1:
                            f.seek(self.char_counter(239))
                        case 2:
                            f.seek(self.char_counter(243))
            #slowly display dialogue by adding char to different versions of line1
            line1_v1 = f.readline().rstrip('\n')
            self.line1_v2 = ''
            blip_count = 0
            for letter in range(0, len(line1_v1)):
                self.clock.tick(self.FPS)
                self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
                self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))
                self.line1_v3 = self.FONT.render(self.line1_v2+line1_v1[letter], True, self.WHITE)
                self.PSEUDO_SCREEN.blit(self.line1_v3, (190, 510))
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
                self.line1_v2 += line1_v1[letter]
                #sound fx
                blip_count += 1
                if blip_count % 5 == 0:
                    pygame.mixer.Sound.play(self.DIAL_SOUND)
                pygame.display.update()

    #display line 2
    def blit_line2(self, scene, count = 0):
        #initialize variables
        w, h = pygame.display.get_surface().get_size()

        #seek line number per scene for every click count
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'C':
                    match count:
                        case 0:
                            f.seek(self.char_counter(9))
                        case 1:
                            f.seek(self.char_counter(13))
                        case 2:
                            f.seek(self.char_counter(17))
                        case 3:
                            f.seek(self.char_counter(21))
                case 'D':
                    match count:
                        case 0:
                            f.seek(self.char_counter(28))
                        case 1:
                            f.seek(self.char_counter(32))
                        case 2:
                            f.seek(self.char_counter(36))
                        case 3:
                            f.seek(self.char_counter(40))
                case 'F':
                    match count:
                        case 0:
                            f.seek(self.char_counter(45))
                        case 1:
                            f.seek(self.char_counter(49))
                        case 2:
                            f.seek(self.char_counter(53))
                        case 3:
                            f.seek(self.char_counter(57))
                case 'e':
                    match count:
                        case 0:
                            f.seek(self.char_counter(62))
                        case 1:
                            f.seek(self.char_counter(66))
                        case 2:
                            f.seek(self.char_counter(70))
                        case 3:
                            f.seek(self.char_counter(74))
                        case 4:
                            f.seek(self.char_counter(78))
                case 'H':
                    match count:
                        case 0:
                            f.seek(self.char_counter(83))
                        case 1:
                            f.seek(self.char_counter(87))
                case 'g':
                    match count:
                        case 0:
                            f.seek(self.char_counter(92))
                        case 1:
                            f.seek(self.char_counter(96))
                case 'I':
                    match count:
                        case 0:
                            f.seek(self.char_counter(101))
                        case 1:
                            f.seek(self.char_counter(105))
                case 'f':
                    match count:
                        case 0:
                            f.seek(self.char_counter(111))
                        case 1:
                            f.seek(self.char_counter(115))
                case 'K':
                    match count:
                        case 0:
                            f.seek(self.char_counter(120))
                        case 1:
                            f.seek(self.char_counter(124))
                        case 2:
                            f.seek(self.char_counter(128))
                case 'L':
                    match count:
                        case 0:
                            f.seek(self.char_counter(133))
                        case 1:
                            f.seek(self.char_counter(137))
                        case 2:
                            f.seek(self.char_counter(141))
                        case 3:
                            f.seek(self.char_counter(145))
                        case 4:
                            f.seek(self.char_counter(149))
                case 'M':
                    match count:
                        case 0:
                            f.seek(self.char_counter(154))
                        case 1:
                            f.seek(self.char_counter(158))
                        case 2:
                            f.seek(self.char_counter(162))
                        case 3:
                            f.seek(self.char_counter(166))
                case 'N':
                    match count:
                        case 0:
                            f.seek(self.char_counter(171))
                        case 1:
                            f.seek(self.char_counter(175))
                case 'P':
                    match count:
                        case 0:
                            f.seek(self.char_counter(181))
                        case 1:
                            f.seek(self.char_counter(185))
                case 'o':
                    match count:
                        case 0:
                            f.seek(self.char_counter(192))
                        case 1:
                            f.seek(self.char_counter(196))
                case 'Q':
                    match count:
                        case 0:
                            f.seek(self.char_counter(202))
                        case 1:
                            f.seek(self.char_counter(206))
                        case 2:
                            f.seek(self.char_counter(210))
                        case 3:
                            f.seek(self.char_counter(214))
                case 'S':
                    match count:
                        case 0:
                            f.seek(self.char_counter(219))
                        case 1:
                            f.seek(self.char_counter(223))
                        case 2:
                            f.seek(self.char_counter(227))
                        case 3:
                            f.seek(self.char_counter(231))
                case 'r':
                    match count:
                        case 0:
                            f.seek(self.char_counter(236))
                        case 1:
                            f.seek(self.char_counter(240))
                        case 2:
                            f.seek(self.char_counter(244))
            #slowly display dialogue by adding char to different versions of line2
            line2_v1 = f.readline().rstrip('\n')
            self.line2_v2 = ''
            blip_count = 0
            for letter in range(0, len(line2_v1)):
                self.clock.tick(self.FPS)
                self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
                self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))
                self.PSEUDO_SCREEN.blit(self.line1_v3, (190, 510))
                self.line2_v3 = self.FONT.render(self.line2_v2+line2_v1[letter], True, self.WHITE)
                self.PSEUDO_SCREEN.blit(self.line2_v3, (190, 545))
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
                self.line2_v2 += line2_v1[letter]
                #sound fx
                blip_count += 1
                if blip_count % 5 == 0:
                    pygame.mixer.Sound.play(self.DIAL_SOUND)
                pygame.display.update()
    
    #display line 3
    def blit_line3(self, scene, count = 0):
        #initialize variables
        w, h = pygame.display.get_surface().get_size()

        #seek line number per scene for every click count
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'C':
                    match count:
                        case 0:
                            f.seek(self.char_counter(10))
                        case 1:
                            f.seek(self.char_counter(14))
                        case 2:
                            f.seek(self.char_counter(18))
                        case 3:
                            f.seek(self.char_counter(22))
                case 'D':
                    match count:
                        case 0:
                            f.seek(self.char_counter(29))
                        case 1:
                            f.seek(self.char_counter(33))
                        case 2:
                            f.seek(self.char_counter(37))
                        case 3:
                            f.seek(self.char_counter(41))
                case 'F':
                    match count:
                        case 0:
                            f.seek(self.char_counter(46))
                        case 1:
                            f.seek(self.char_counter(50))
                        case 2:
                            f.seek(self.char_counter(54))
                        case 3:
                            f.seek(self.char_counter(58))
                case 'e':
                    match count:
                        case 0:
                            f.seek(self.char_counter(63))
                        case 1:
                            f.seek(self.char_counter(67))
                        case 2:
                            f.seek(self.char_counter(71))
                        case 3:
                            f.seek(self.char_counter(75))
                        case 4:
                            f.seek(self.char_counter(79))
                case 'H':
                    match count:
                        case 0:
                            f.seek(self.char_counter(84))
                        case 1:
                            f.seek(self.char_counter(88))
                case 'g':
                    match count:
                        case 0:
                            f.seek(self.char_counter(93))
                        case 1:
                            f.seek(self.char_counter(97))
                case 'I':
                    match count:
                        case 0:
                            f.seek(self.char_counter(102))
                        case 1:
                            f.seek(self.char_counter(106))
                case 'f':
                    match count:
                        case 0:
                            f.seek(self.char_counter(112))
                        case 1:
                            f.seek(self.char_counter(116))
                case 'K':
                    match count:
                        case 0:
                            f.seek(self.char_counter(121))
                        case 1:
                            f.seek(self.char_counter(125))
                        case 2:
                            f.seek(self.char_counter(129))
                case 'L':
                    match count:
                        case 0:
                            f.seek(self.char_counter(134))
                        case 1:
                            f.seek(self.char_counter(138))
                        case 2:
                            f.seek(self.char_counter(142))
                        case 3:
                            f.seek(self.char_counter(146))
                        case 4:
                            f.seek(self.char_counter(150))
                case 'M':
                    match count:
                        case 0:
                            f.seek(self.char_counter(155))
                        case 1:
                            f.seek(self.char_counter(159))
                        case 2:
                            f.seek(self.char_counter(163))
                        case 3:
                            f.seek(self.char_counter(167))
                case 'N':
                    match count:
                        case 0:
                            f.seek(self.char_counter(172))
                        case 1:
                            f.seek(self.char_counter(176))
                case 'P':
                    match count:
                        case 0:
                            f.seek(self.char_counter(182))
                        case 1:
                            f.seek(self.char_counter(186))
                case 'o':
                    match count:
                        case 0:
                            f.seek(self.char_counter(193))
                        case 1:
                            f.seek(self.char_counter(197))
                case 'Q':
                    match count:
                        case 0:
                            f.seek(self.char_counter(203))
                        case 1:
                            f.seek(self.char_counter(207))
                        case 2:
                            f.seek(self.char_counter(211))
                        case 3:
                            f.seek(self.char_counter(215))
                case 'S':
                    match count:
                        case 0:
                            f.seek(self.char_counter(220))
                        case 1:
                            f.seek(self.char_counter(224))
                        case 2:
                            f.seek(self.char_counter(228))
                        case 3:
                            f.seek(self.char_counter(232))
                case 'r':
                    match count:
                        case 0:
                            f.seek(self.char_counter(237))
                        case 1:
                            f.seek(self.char_counter(241))
                        case 2:
                            f.seek(self.char_counter(245))
            #slowly display dialogue by adding char to different versions of line3
            line3_v1 = f.readline().rstrip('\n')
            self.line3_v2 = ''
            blip_count = 0
            for letter in range(0, len(line3_v1)):
                self.clock.tick(self.FPS)
                self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
                self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))
                self.PSEUDO_SCREEN.blit(self.line1_v3, (190, 510))
                self.PSEUDO_SCREEN.blit(self.line2_v3, (190, 545))
                self.line3_v3 = self.FONT.render(self.line3_v2+line3_v1[letter], True, self.WHITE)
                self.PSEUDO_SCREEN.blit(self.line3_v3, (190, 580))
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
                self.line3_v2 += line3_v1[letter]
                #sound fx
                blip_count += 1
                if blip_count % 5 == 0:
                    pygame.mixer.Sound.play(self.DIAL_SOUND)
                pygame.display.update()

    #display line 4
    def blit_line4(self, scene, count = 0):
        #initialize variables
        w, h = pygame.display.get_surface().get_size()

        #seek line number per scene for every click count
        with open('dialogue.txt', 'r') as f:
            match scene:
                case 'C':
                    match count:
                        case 0:
                            f.seek(self.char_counter(11))
                        case 1:
                            f.seek(self.char_counter(15))
                        case 2:
                            f.seek(self.char_counter(19))
                        case 3:
                            f.seek(self.char_counter(23))
                case 'D':
                    match count:
                        case 0:
                            f.seek(self.char_counter(30))
                        case 1:
                            f.seek(self.char_counter(34))
                        case 2:
                            f.seek(self.char_counter(38))
                        case 3:
                            f.seek(self.char_counter(42))
                case 'F':
                    match count:
                        case 0:
                            f.seek(self.char_counter(47))
                        case 1:
                            f.seek(self.char_counter(51))
                        case 2:
                            f.seek(self.char_counter(55))
                        case 3:
                            f.seek(self.char_counter(59))
                case 'e':
                    match count:
                        case 0:
                            f.seek(self.char_counter(64))
                        case 1:
                            f.seek(self.char_counter(68))
                        case 2:
                            f.seek(self.char_counter(72))
                        case 3:
                            f.seek(self.char_counter(76))
                        case 4:
                            f.seek(self.char_counter(80))
                case 'H':
                    match count:
                        case 0:
                            f.seek(self.char_counter(85))
                        case 1:
                            f.seek(self.char_counter(89))
                case 'g':
                    match count:
                        case 0:
                            f.seek(self.char_counter(94))
                        case 1:
                            f.seek(self.char_counter(98))
                case 'I':
                    match count:
                        case 0:
                            f.seek(self.char_counter(103))
                        case 1:
                            f.seek(self.char_counter(107))
                case 'f':
                    match count:
                        case 0:
                            f.seek(self.char_counter(113))
                        case 1:
                            f.seek(self.char_counter(117))
                case 'K':
                    match count:
                        case 0:
                            f.seek(self.char_counter(122))
                        case 1:
                            f.seek(self.char_counter(126))
                        case 2:
                            f.seek(self.char_counter(130))
                case 'L':
                    match count:
                        case 0:
                            f.seek(self.char_counter(135))
                        case 1:
                            f.seek(self.char_counter(139))
                        case 2:
                            f.seek(self.char_counter(143))
                        case 3:
                            f.seek(self.char_counter(147))
                        case 4:
                            f.seek(self.char_counter(151))
                case 'M':
                    match count:
                        case 0:
                            f.seek(self.char_counter(156))
                        case 1:
                            f.seek(self.char_counter(160))
                        case 2:
                            f.seek(self.char_counter(164))
                        case 3:
                            f.seek(self.char_counter(168))
                case 'N':
                    match count:
                        case 0:
                            f.seek(self.char_counter(173))
                        case 1:
                            f.seek(self.char_counter(177))
                case 'P':
                    match count:
                        case 0:
                            f.seek(self.char_counter(183))
                        case 1:
                            f.seek(self.char_counter(187))
                case 'o':
                    match count:
                        case 0:
                            f.seek(self.char_counter(194))
                        case 1:
                            f.seek(self.char_counter(198))
                case 'Q':
                    match count:
                        case 0:
                            f.seek(self.char_counter(204))
                        case 1:
                            f.seek(self.char_counter(208))
                        case 2:
                            f.seek(self.char_counter(212))
                        case 3:
                            f.seek(self.char_counter(216))
                case 'S':
                    match count:
                        case 0:
                            f.seek(self.char_counter(221))
                        case 1:
                            f.seek(self.char_counter(225))
                        case 2:
                            f.seek(self.char_counter(229))
                        case 3:
                            f.seek(self.char_counter(233))
                case 'r':
                    match count:
                        case 0:
                            f.seek(self.char_counter(238))
                        case 1:
                            f.seek(self.char_counter(242))
                        case 2:
                            f.seek(self.char_counter(246))
            #slowly display dialogue by adding char to different versions of line4
            line4_v1 = f.readline().rstrip('\n')
            self.line4_v2 = ''
            blip_count = 0
            for letter in range(0, len(line4_v1)):
                self.clock.tick(self.FPS)
                self.PSEUDO_SCREEN.blit(self.TENTACLE, (150, 450))
                self.PSEUDO_SCREEN.blit(self.DIAL_BOX, (40, 430))
                self.PSEUDO_SCREEN.blit(self.line1_v3, (190, 510))
                self.PSEUDO_SCREEN.blit(self.line2_v3, (190, 545))
                self.PSEUDO_SCREEN.blit(self.line3_v3, (190, 580))
                self.line4_v3 = self.FONT.render(self.line4_v2+line4_v1[letter], True, self.WHITE)
                self.PSEUDO_SCREEN.blit(self.line4_v3, (190, 615))
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
                self.line4_v2 += line4_v1[letter]
                #sound fx
                blip_count += 1
                if blip_count % 5 == 0:
                    pygame.mixer.Sound.play(self.DIAL_SOUND)
                pygame.display.update()

    #takes line number and returns char count up to that point
    def char_counter(self, n):
        n = n - 1
        with open('dialogue.txt', 'r') as f:
            line_offset = []
            offset = 0
            for line in f:
                line_offset.append(offset)
                offset += len(line)
            f.seek(0)
        return line_offset[n]
    
    #display line 1 for node B
    def sceneB_blit_line1(self):
        #initialize variables
        w, h = pygame.display.get_surface().get_size()
        blip_count = 0
        with open('dialogue.txt', 'r') as f:
            self.PSEUDO_SCREEN.fill(self.BLACK)
            f.seek(8)
            #slowly display dialogue by adding char to different versions of line1
            line1_v1 = f.readline().rstrip('\n')
            line1_v2 = ''
            for letter in range(0, len(line1_v1)):
                self.clock.tick(70)
                self.PSEUDO_SCREEN.fill(self.BLACK)
                line1_v3 = self.FONT.render(line1_v2+line1_v1[letter], True, self.WHITE)
                self.PSEUDO_SCREEN.blit(line1_v3, (330, 330))
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
                line1_v2 += line1_v1[letter]
                #sound fx
                blip_count += 1
                if blip_count % 5 == 0:
                    pygame.mixer.Sound.play(self.DIAL_SOUND)
                pygame.display.update() 

    #display line 2 for node B
    def sceneB_blit_line2(self):
        #initialize variables
        w, h = pygame.display.get_surface().get_size()
        blip_count = 0
        with open('dialogue.txt', 'r') as f:
            f.seek(48)
            #slowly display dialogue by adding char to different versions of line2
            line2_v1 = f.readline().rstrip('\n')
            line2_v2 = ''
            for letter in range(0, len(line2_v1)):
                self.clock.tick(70)
                pygame.draw.rect(self.PSEUDO_SCREEN, self.BLACK, pygame.Rect(300, 365, 400, 35))
                line2_v3 = self.FONT.render(line2_v2+line2_v1[letter], True, self.WHITE)
                self.PSEUDO_SCREEN.blit(line2_v3, (300, 365))
                self.SCREEN.blit(pygame.transform.scale(self.PSEUDO_SCREEN, (w, h)), (0, 0))
                line2_v2 += line2_v1[letter]
                #sound fx
                blip_count += 1
                if blip_count % 5 == 0:
                    pygame.mixer.Sound.play(self.DIAL_SOUND)
                pygame.display.update()
