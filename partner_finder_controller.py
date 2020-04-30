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


class Player(pygame.sprite.Sprite):
    '''
    This will be the sprite/model for the current player
    '''
    def __init__(self):

        distance = 2

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((2,2)) #We'll decide on sizing
        self.image.fill() # Character is a black square sized 2,2 for now
        self.rect = self.image.get_rect(WHITE)
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def move(self, speedx, speedy):
        self.rect.x += speedx
        self.rect.y += speedy

    def draw(self):
        window.blit(self.image.get_rect(self.rect.x, self.rect.y))
