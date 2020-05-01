#partner_finder_controller
import pygame
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


blue = (0,0,225)

class Player(pygame.sprite.Sprite):
    '''
    This will be the sprite/model for the current player
    '''
    def __init__(self, x, y):

        distance = 2

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((2,2)) #We'll decide on sizing
        self.image.fill(blue) # Character is a black square sized 2,2 for now
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (distance / 2, distance / 2)

    def move(self, speedx, speedy):
        self.rect.x += speedx
        self.rect.y += speedy

    def draw(self):
        screen.blit(self.image.get_rect(self.rect.x, self.rect.y)
