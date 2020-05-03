import pygame

pygame.init()

# HERE ARE THE COLORS

GAME_WIDTH = 800
GAME_HEIGHT = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

# TEMPORARY FPS LIMIT
GAME_FPS = 60

CLASSROOM_WIDTH = 30
CLASSROOM_HEIGHT = 30

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)
COLOR_BLUE = (0, 0, 255)

#SPRITES
S_PLAYER = pygame.image.load("data/cheems.png")
S_WALL = pygame.image.load("data/table.png")
S_FLOOR = pygame.image.load("data/floor.png")
S_CLASSMATE = pygame.image.load("data/doge.png")



# FONT
FONT_MESSAGE = pygame.font.Font('data\Roboto-Black.ttf', 20)
