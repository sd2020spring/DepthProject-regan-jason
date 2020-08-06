#partner_finder_controller
import pygame
from constants import *
import random



class struc_Tile:
    def __init__(self, block_path):
        self.block_path = block_path

class obj_Actor:
    def __init__(self, x, y, name_object, trait1, trait2, trait3, sprite, classmate = None, professor = None, ai = None):
        self.x = x  # map address
        self.y = y  # map address
        self.sprite = sprite
        self.name = name_object

        self.classmate = classmate
        if classmate:
            self.classmate = classmate
            classmate.owner = self
        elif professor:
            self.professor = professor
            professor.owner = self



        self.trait1 = trait1

        self.trait2 = trait2

        self.trait3 = trait3

        self.ai = ai
        if ai:
            self.ai = ai
            ai.owner = self


    def draw(self, surface):
        surface.blit(self.sprite, (self.x*CELL_WIDTH, self.y*CELL_HEIGHT))

    def move(self, dx, dy, game_map):
        if game_map[self.x + dx][self.y + dy].block_path == False:
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
    def take_turn(self, game_map):
        change_value = random.randint(-1,1)
        check = random.randint(0,2)

        if check == 0:
            dx = change_value
            dy = 0
        elif check == 1:
            dy = change_value
            dx = 0
        elif check == 2:
            dy = 0
            dx = 0
        self.owner.move(dx, dy, game_map)
