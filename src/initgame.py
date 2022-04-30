
import pygame

pygame.init()
pygame.mixer.init()

class Init_Game():
    #create game window
    X, Y = 1000, 700
    SCREEN = pygame.display.set_mode((X, Y), pygame.RESIZABLE)
    pygame.display.set_caption("The Call of Cthulhu - Interactive Horror Game")
    ICON = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(ICON)

    #create clock
    clock = pygame.time.Clock()

    #load buttons and icons
    TITLE = pygame.image.load("assets/title.png")
    START_BUTTON = pygame.image.load("assets/startButton.png")
    DIAL_BOX = pygame.image.load("assets/rectangle.png")
    BORDER = pygame.image.load("assets/red border.png")
    WHITE_LINE = pygame.image.load("assets/white line.png")
    TENTACLE = pygame.image.load("assets/tentacle-art-invertebrate-tenticles-5a8a929ad57a7d9fc498da38c662a6fc.png")

    #decision choices
    LOOK_INTO_IT = pygame.image.load("assets/Look into it.png")
    TELL_HIM = pygame.image.load("assets/Tell him it's nothing.png")

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

    #declare colors and font
    FONT = pygame.font.SysFont('Rockwell', 19)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #set item transparency
    DIAL_BOX.set_alpha(220)
    BORDER.set_alpha(200)
    TENTACLE.set_alpha(200)
    START_BUTTON.set_alpha(150)
    LOOK_INTO_IT.set_alpha(100)
    TELL_HIM.set_alpha(100)

    #set sound fx
    START_SOUND = pygame.mixer.Sound("assets/wildBeastRoar.wav")

    #screen that scales to the size of the window
    PSEUDO_SCREEN = pygame.Surface((X, Y))

    #invisible screen for collision detection
    COLLISION_SCREEN = pygame.Surface((X, Y))
    COLLISION_SCREEN.set_alpha(0)

    #collision items
    w, h = pygame.display.get_surface().get_size()
    START_BUTTON_POS = pygame.Rect(w/2.25, h/1.23, w/8.3, h/14)
    TELL_HIM_POS = pygame.Rect(w/1.47, h/1.17, w/3.34, h/21.88)
    LOOK_INTO_IT_POS = pygame.Rect(w/33.33, h/1.17, w/5.78, h/22.58)

