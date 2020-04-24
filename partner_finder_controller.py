#partner_finder_controller
import Pygame

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    INTERACT
)

class Player:
    '''
    A controller that allows the input of the user to change
    the view on the board.

    Attributes:
        classroom: model of classroom
        view:
    '''
    def __init__(self):
        self.x = x
        self.y = y
        self.image = image

    def move(self, speedx, speedy):
        '''
        Moves player character depending on the key input
        given by the player. Movement will be given as such:
        Move Right = Right arrow
        Move Left = Left arrow
        Move Up = Up arrow
        Move Down = Down arrow
        '''
        self.x += speedx
        self.y += speedy

    def draw(self):
        window.blit(self.image(self.x, self.y))
