#partner_finder_controller
import pygame
from constants import *
from partner_finder_view import *
from partner_finder_run import *



class obj_Actor:
    def __init__(self, x, y, name_object, sprite, classmate = None, ai = None):
        self.x = x  # map address
        self.y = y  # map address
        self.sprite = sprite

        self.classmate = classmate
        if classmate:
            self.classmate = classmate
            classmate.owner = self

        self.ai = ai
        if ai:
            self.ai = ai
            ai.owner = self


    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x*CELL_WIDTH, self.y*CELL_HEIGHT))

    def move(self, dx, dy):
        if GAME_MAP[self.x + dx][self.y + dy].block_path == False:
            self.x += dx
            self.y += dy


'''
    _    ___
   / \  |_ _|
  / _ \  | |
 / ___ \ | |
/_/   \_\___|
'''

class ai_Test:
    '''
    Every turn classmates move
    '''
    def take_turn(self):
        self.owner.move(-1, 0)
