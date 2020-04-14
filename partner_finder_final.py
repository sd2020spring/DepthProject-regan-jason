# Partner_finder_final.py
"""
The Softdes Partner Finder
- Players create a character, and then will talk to other characters
in the classroom to find their perfect softdes partner.
- Each character will be saved into a database that will then use
those characters as the students in subsequent playthroughs.

Created by: Jason Lin and Regan Mah
"""
import pygame
import random

# import some controls
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#initialize Pygame
pygame.init()

#Define constants for window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Screen object with params SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Prof(Menu):
    """
    Prof will basically be like a save point/ends game when you
    select your Partner.
    Not sure if this falls under the menu class or not
    """

    def end_result():
        '''
        When character chooses a partner, a final result will
        be posted stating the outcome of the game.
        '''
        pass
    pass

class Student:

    def __init__(self, name, gradyear, trait1, trait2, trait3):
        self.name = name
        self.gradyear = gradyear
        self.trait1 = trait1
        self.trait2 = trait2
        self.trait3 = trait3

    def generate_student():
        """
        This function will generate a student using the random.choice
        function. It will choose a random name, a random gradyear, and
        random traits.
        Note: Will only generate enough students to fill the classroom,
        and the more player characters stored, the less random students
        will be generated.
        """
        pass


class PlayerCharacter(Student):

    def create_student(name, gradyear):
        """
        Takes player input to create a character with a name
        and their gradyear
        """
        name = input("What is your name?")
        year = input("What year are you in?")

        return name, year

    def define_traits():
        """
        Asks the player several questions that will define the traits
        of the player character. These traits will then be used to
        see if the player character and their parter are compatible.
        """

        question1 = input("How would you describe your working style?\nA) If it needs to be done, it better be done well\nB) Meh it'll happen one way or another\nC) Work? What's work?")
        question2 = input("Coding experience?\nA) I know everything I need to know\nB) I know enough to get by\nC) Coding? What's coding?")
        question3 = input("Do you like pancakes?\nA) I eat pancakes and nothing else\nB) Meh I'll eat them if they're put in front of me\nC) I will only eat waffles and nothing else")

        if question1 == 'A' or question1 == 'a':
            trait1 = hardworking
            return trait1
        elif question1 == 'B' or question1 == 'b':
            trait1 = laidback
            return trait1
        elif question1 == 'C' or question1 == 'c':
            trait1 = useless
            return trait1

        if question2 == 'A' or question2 == 'a':
            trait2 = knowledgable
            return trait2
        elif question2 == 'B' or question2 == 'b':
            trait2 = resourceful
            return trait2
        elif question2 == 'C' or question2 == 'c':
            trait2 = clueless
            return trait2

        if question3 == 'A' or question3 == 'a':
            trait3 = pancake_lover
            return trait3
        elif question3 == 'B' or question3 == 'b':
            trait3 = eats_anything
            return trait3
        if question3 == 'C' or question3 == 'c':
            trait3 = waffle_lover
            return trait3

        return trait1, trait2, trait3

    def store_student():
        """
        Stores student in a list that will be used to select
        which students populate the class at random.
        """
        pass

class Menu:
    """
    A class used for the startup menus and the endgame menus, as
    well as the teacher menu (?)
    """
    pass

class Player(pygame.sprite.Sprite):
    '''
    This will be the sprite/model for the current player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((2,2)) #We'll decide on sizing
        self.image.fill(WHITE) # Character is a black square sized 2,2 for now
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 2

class Table:
    '''
    Serves as an obstacle around the classroom to resemble
    a real classroom as it isnt just empty space
    Note: Players will not be able to walk into them
    '''

    def __init__(self)
