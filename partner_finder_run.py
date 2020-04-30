"""
Main file to put the running code (since I can't keep track of everything)
"""
import pygame
from partner_finder_final import Student
from partner_finder_controller import Player
from partner_finder_view import Classroom

#initialize Pygame
pygame.init()

#Screen object with params SCREEN_WIDTH and SCREEN_HEIGHT
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
while running:

    #PlayerCharacter.create_student()
    classroom = Classroom()
    classroom.HEIGHT = 800
    classroom.WIDTH = 600

    player = Player()
    player.draw()
    speedx = 0
    speedy = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            speedy += -1
            speedx = 0
        elif event.type == pygame.K_UP:
            speedy += 1
            speedx = 0
        elif event.type == pygame.K_RIGHT:
            speedx += 1
            speedy = 0
        elif event.type == pygame.K_LEFT:
            speedx += -1
            speedy = 0
        elif event.type == pygame.INTERACT:
            pass
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    player.move(speedx, speedy)
    player.draw()
