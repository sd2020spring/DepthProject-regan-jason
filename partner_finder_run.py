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
window = (800,600)

#Set screen up
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

screen.blit(background,(0,0))

pygame.display.flip()

running = True
while running:

    #PlayerCharacter.create_student()
    classroom = Classroom(800, 600)

    player = Player(0,0)
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
