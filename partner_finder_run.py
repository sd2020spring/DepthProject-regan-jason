"""
Main file to put the running code (since I can't keep track of everything)
"""
from partner_finder_final import Player, Student
import partner_finder_controller
import partner_finder_view


#Define constants for window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Screen object with params SCREEN_WIDTH and SCREEN_HEIGHT
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
while running:

    #PlayerCharacter.create_student()

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
