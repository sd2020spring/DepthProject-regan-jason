# partner_finder_view
import pygame
from utilities import struc_Tile, com_Classmate
from constants import *



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

    for i in range(20):
        new_map[0][i].block_path = True
    for i in range(25):
        new_map[i][0].block_path = True
    for i in range(20):
        new_map[24][i].block_path = True
    for i in range(25):
        new_map[i][18].block_path = True

    #ne
    return new_map
