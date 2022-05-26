
import pygame

#initialize game
pygame.init()
pygame.mixer.init()

class Init_Game():

    #create game window
    X, Y = 1000, 700
    SCREEN = pygame.display.set_mode((X, Y), pygame.RESIZABLE)
    pygame.display.set_caption("The Call of Cthulhu - Interactive Horror Game")
    ICON = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(ICON)
    clock = pygame.time.Clock()

    #load buttons and icons
    TITLE = pygame.image.load("assets/title.png")
    START_BUTTON = pygame.image.load("assets/startButton.png")
    DIAL_BOX = pygame.image.load("assets/rectangle.png")
    BORDER = pygame.image.load("assets/red border.png")
    WHITE_LINE = pygame.image.load("assets/white line.png")
    BLACK_LINE = pygame.image.load("assets/black line.png")
    TENTACLE = pygame.image.load("assets/tentacle-art-invertebrate-tenticles-5a8a929ad57a7d9fc498da38c662a6fc.png")
    GAME_OVER = pygame.image.load("assets/Game Over.png")

    #load decision choices
    LOOK_INTO_IT = pygame.image.load("assets/Look into it.png")
    TELL_HIM = pygame.image.load("assets/Tell him it's nothing.png")
    MAKE_UP = pygame.image.load("assets/Make up excuse to leave.png")
    HELP_WITH = pygame.image.load("assets/Help with investigation.png")
    TAKE_THE_GUN = pygame.image.load("assets/Take the gun.png")
    RUN_AND_HIDE = pygame.image.load("assets/Run and hide.png")
    CONTINUE_VOYAGE = pygame.image.load("assets/Continue voyage.png")
    JUMP_OFF_SHIP = pygame.image.load("assets/Jump off ship.png")
    RUN_AWAY = pygame.image.load("assets/Run away.png")
    ATTACK_IT = pygame.image.load("assets/Attack it.png")
    CONTINUE = pygame.image.load("assets/Continue.png")
    EXIT = pygame.image.load("assets/Exit.png")

    #load background images
    START_SCREEN = pygame.image.load("assets/startBG.png")
    HORROR_IN_CLAY = pygame.image.load("assets/horrorInClay.png")
    UNIVERSITY = pygame.image.load("assets/university.png")
    HOUSE = pygame.image.load("assets/cthulhu wallpaper 171.png")
    INVESTIGATION_1 = pygame.image.load("assets/video-game-call-of-cthulhu-cthulhu-h-p-lovecraft-wallpaper-thumb.png")
    INVESTIGATION_2 = pygame.image.load("assets/l2bh9dglc7f41.png")
    TOWN = pygame.image.load("assets/01f9c651478436ed8ff940ea5591620f_550485.png")
    INVESTIGATION_3 = pygame.image.load("assets/666e378141b7824060579ce896d783c098d5c5db37584015aee1c22cc9133364.png")
    ALONE = pygame.image.load("assets/call-of-cthulhu-review-523506-32.png")
    STATUE = pygame.image.load("assets/38-389668_star-on-the-shore-cthulhu.png")
    DOCK = pygame.image.load("assets/20181026120602_1.png")
    SAIL = pygame.image.load("assets/coc-boat.png")
    RLYEH_1 = pygame.image.load("assets/rlyeh-1.png")
    RLYEH_2 = pygame.image.load("assets/YChlAcTe.png")
    RLYEH_3 = pygame.image.load("assets/timo-peter-cthulhu-hd-wallpaper-preview.png")

    #set colors and font
    FONT = pygame.font.SysFont('Rockwell', 19)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #set item transparency
    DIAL_BOX.set_alpha(210)
    BORDER.set_alpha(210)
    TENTACLE.set_alpha(210)
    START_BUTTON.set_alpha(150)
    LOOK_INTO_IT.set_alpha(100)
    TELL_HIM.set_alpha(100)
    MAKE_UP.set_alpha(100)
    HELP_WITH.set_alpha(100)
    TAKE_THE_GUN.set_alpha(100)
    RUN_AND_HIDE.set_alpha(100)
    CONTINUE_VOYAGE.set_alpha(100)
    JUMP_OFF_SHIP.set_alpha(100)
    RUN_AWAY.set_alpha(100)
    ATTACK_IT.set_alpha(100)
    CONTINUE.set_alpha(90)
    EXIT.set_alpha(90)
    GAME_OVER.set_alpha(210)

    #set sfx
    START_SOUND = pygame.mixer.Sound("assets/wildBeastRoar.wav")
    DIAL_SOUND = pygame.mixer.Sound("assets/blip5.wav")
    SELECT = pygame.mixer.Sound("assets/long pop.wav")
    START_SOUND.set_volume(0.8)
    DIAL_SOUND.set_volume(0.6)

    #screen that scales to the size of the window
    PSEUDO_SCREEN = pygame.Surface((X, Y))

    #invisible screen for collision detection
    COLLISION_SCREEN = pygame.Surface((X, Y))

    #collision items
    w, h = pygame.display.get_surface().get_size()
    START_BUTTON_POS = pygame.Rect(w/2.25, h/1.23, w/8.3, h/14)
    TELL_HIM_POS = pygame.Rect(w/1.47, h/1.17, w/3.34, h/21.88)
    LOOK_INTO_IT_POS = pygame.Rect(w/33.33, h/1.17, w/5.78, h/22.58)
    HELP_WITH_POS = pygame.Rect(w/33.33, h/1.17, w/2.88, h/22.58)
    MAKE_UP_POS = pygame.Rect(w/1.67, h/1.17, w/2.86, h/22.58)
    TAKE_THE_GUN_POS = pygame.Rect(w/33.33, h/1.17, w/5.18, h/22.58)
    RUN_AND_HIDE_POS = pygame.Rect(w/1.28, h/1.17, w/5.38, h/22.58)
    CONTINUE_VOYAGE_POS = pygame.Rect(w/33.33, h/1.17, w/4.18, h/22.58)
    JUMP_OFF_SHIP_POS = pygame.Rect(w/1.29, h/1.17, w/5.13, h/22.58)
    ATTACK_IT_POS = pygame.Rect(w/33.33, h/1.17, w/7.41, h/22.58)
    RUN_AWAY_POS = pygame.Rect(w/1.21, h/1.17, w/7.04, h/22.58)
    CONTINUE_POS = pygame.Rect(w/6.67, h/1.75, w/4.15, h/14.58)
    EXIT_POS = pygame.Rect(w/1.47, h/1.75, w/9.62, h/14.89)

