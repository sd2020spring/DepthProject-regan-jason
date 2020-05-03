# partner_finder_view
import pygame
from partner_finder_final import struc_Tile, com_Classmate
from constants import *
from partner_finder_controller import *
from partner_finder_run import *
import partner_finder_run


'''
.___  ___.      ___      .______
|   \/   |     /   \     |   _  \
|  \  /  |    /  ^  \    |  |_)  |
|  |\/|  |   /  /_\  \   |   ___/
|  |  |  |  /  _____  \  |  |
|__|  |__| /__/     \__\ | _|      '''


''' the 0 to 30 represents that there are 30 tiles'''

def map_create():
    '''
    Class to help visualize the classroom enviornment

    Attributes: a Classroom instance representing the room to EnvironmentView
    '''
    new_map = [[ struc_Tile(False) for y in range(0, CELL_HEIGHT)] for x in range(0, CELL_WIDTH) ]

    new_map[10][10].block_path = True
    new_map[10][15].block_path = True

    return new_map


'''''''''
  ____
 |  _ \ _ __ __ ___      _(_)_ __   __ _
 | | | | '__/ _` \ \ /\ / / | '_ \ / _` |
 | |_| | | | (_| |\ V  V /| | | | | (_| |
 |____/|_|  \__,_| \_/\_/ |_|_| |_|\__, |
                                  |___/        '''''''''









def add_students(self):
    '''
    Function will add x amount of students to populate the
    classroom. Each student will have their own spawn point.
    Treats students in an kind of x,y coordinate system with
    students occupying squares.
    '''
    for object in students:
        self.x = random.choice(xposition)
        self.y = random.choice(yposition)
