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
S_WALL = pygame.image.load("data/other.png")
S_FLOOR = pygame.image.load("data/floor.png")
S_PROFESSOR = pygame.image.load("data/professor.png")

# FONT
FONT_MESSAGE = pygame.font.Font('data/Roboto-Black.ttf', 20)

# Classmate properties
names = ["Sophia", "Isabella", "Emma", "Olivia", "Ava", "Emily", "Abigial", "Ella",
"Addison", "Avery", "Lillian", "Lilith", "Bella", "Charlotte", "Aubrey", "Mariah",
"Eva", "Genesis", "Scarlett", "Madelyn", "Molly", "Faith", "Harper", "Autumn", "Kaylee",
"Lauren", "Allison", "Sarah", "Jacob", "Isaac", "Andrew", "Ryan", "Zachary", "Diego",
"Jaden", "Kevin", "Xavier", "Ian", "Chase", "Ayden", "Carson", "Adam", "Thomas", "Jose",
"Robert", "Dylan", "Joseph", "Caleb", "Elijah", "Evan", "Eli", "Luis"]
gradyear = ["2020", "2021", "2022", "2023", "2024"]
traits1 = ["hardworking", "laidback", "a party animal"]
traits2 = ["knowledgable", "resourceful", "clueless"]
traits3 = ["a pancake lover", "will eat anything", "a waffle lover"]
image_base = [pygame.image.load("data/3d.png"), pygame.image.load('data/blue.png'), pygame.image.load('data/bread.png'),
pygame.image.load('data/dabbing.png'), pygame.image.load('data/deal.png'), pygame.image.load('data/doge.PNG'),
pygame.image.load('data/dogecoin.png'), pygame.image.load('data/headphone.png'), pygame.image.load('data/helmet.png'),
pygame.image.load('data/kid.png'), pygame.image.load('data/pixel.png'), pygame.image.load('data/sandwich.png'),
pygame.image.load('data/shout.png'), pygame.image.load('data/smug.png'), pygame.image.load('data/animu.png'),
pygame.image.load('data/plush.png'), pygame.image.load('data/poof.png'), pygame.image.load('data/sad.png'),
pygame.image.load('data/shibaflower.png'), pygame.image.load('data/smile.png'), pygame.image.load('data/yawn.png'),
pygame.image.load('data/pot.png')]
