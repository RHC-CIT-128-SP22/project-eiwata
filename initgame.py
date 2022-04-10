
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

    #load buttons and icons
    TITLE = pygame.image.load("assets/title.png")
    START_BUTTON = pygame.image.load("assets/startButton.png")
    DIAL_BOX = pygame.image.load("assets/rectangle.png")

    #load background images
    START_SCREEN = pygame.image.load("assets/startBG.png")
    PORTRAIT_SCENE = pygame.image.load("assets/portrait.png")
    HORROR_IN_CLAY = pygame.image.load("assets/horrorInClay.png")
    UNIVERSITY = pygame.image.load("assets/university.png")

    #declare colors and font
    FONT = pygame.font.SysFont('Rockwell', 19)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #set item transparency
    DIAL_BOX.set_alpha(220)
    START_BUTTON.set_alpha(150)

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

