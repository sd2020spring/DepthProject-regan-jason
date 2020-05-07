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
from constants import names, traits1, traits2, traits3, image_base
from partner_finder_controller import obj_Actor, ai_Test
# from partner_finder_controller import obj_Actor

white=(255,255,255)


'''
 ____ _____ ____  _   _  ____ _____ _   _ ____  _____ ____
/ ___|_   _|  _ \| | | |/ ___|_   _| | | |  _ \| ____/ ___|
\___ \ | | | |_) | | | | |     | | | | | | |_) |  _| \___ \
 ___) || | |  _ <| |_| | |___  | | | |_| |  _ <| |___ ___) |
|____/ |_| |_| \_\\___/ \____| |_|  \___/|_| \_\_____|____/  '''


class struc_Tile:
    def __init__(self, block_path):
        self.block_path = block_path

class table_Tile:
    def __init__(self, block_path):
        self.block_path = block_path


'''
  ____ ___  __  __ ____   ___  _   _ _____ _   _ _____ ____
 / ___/ _ \|  \/  |  _ \ / _ \| \ | | ____| \ | |_   _/ ___|
| |  | | | | |\/| | |_) | | | |  \| |  _| |  \| | | | \___ \
| |__| |_| | |  | |  __/| |_| | |\  | |___| |\  | | |  ___) |
 \____\___/|_|  |_|_|    \___/|_| \_|_____|_| \_| |_| |____/  '''


class com_Classmate:
    '''
    classmates can move around and be interacted with
    '''
    #GIVE AI
    def __init__(self, name_instance):

        self.name_instance = name_instance

class com_Professor:
    '''
    classmates can move around and be interacted with
    '''
    #GIVE AI
    def __init__(self, name_instance):

        self.name_instance = name_instance


    # Generates classmates with random traits and random sprites and
    #random names

def generate_student():

    students = []

    classmate_number = 20

    for n in range(classmate_number):
        students.append(obj_Actor(random.randint(1, 23), random.randint(1, 17),
                                    random.choice(names), random.choice(traits1),
                                    random.choice(traits2), random.choice(traits3),
                                    sprite = image_base.pop(random.randint(0, len(image_base)-1)), ai = ai_Test()))
    return students
