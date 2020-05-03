"""
Main file to put the running code (since I can't keep track of everything)
"""
import pygame
# from partner_finder_final import obj_Actor
from partner_finder_controller import *
from constants import *
from partner_finder_view import *
from partner_finder_final import *



class obj_Actor:
    ''' This Class serves as all characters including players
        and classmates '''
    def __init__(self, x, y, name_object, sprite, classmate = None, ai = None):
        self.x = x  # map address
        self.y = y  # map address
        self.sprite = sprite

        self.classmate = classmate
        if classmate:
            self.classmate = classmate
            classmate.owner = self
        # This represents the ai for classmate npcs
        self.ai = ai
        if ai:
            self.ai = ai
            ai.owner = self


    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x*CELL_WIDTH, self.y*CELL_HEIGHT))
        # Draws all character sprites in a 32x32 pixel size

    # The player character can move as long as nothing (a desk) is blocking their path
    def move(self, dx, dy):
        if GAME_MAP[self.x + dx][self.y + dy].block_path == False:
            self.x += dx
            self.y += dy

'''''''''
  ____
 |  _ \ _ __ __ ___      _(_)_ __   __ _
 | | | | '__/ _` \ \ /\ / / | '_ \ / _` |
 | |_| | | | (_| |\ V  V /| | | | | (_| |
 |____/|_|  \__,_| \_/\_/ |_|_| |_|\__, |
                                  |___/        '''''''''


def draw_game():


    global SURFACE_MAIN

    # coloring background
    SURFACE_MAIN.fill(COLOR_GREY)

    # draw the map
    draw_map(GAME_MAP)

    # draws in all game objects in the list in an easy fashion
    for obj in GAME_OBJECTS:
        obj.draw()

    draw_debug()

    # update the display
    pygame.display.flip()


def draw_map(map_to_draw):
    '''
    Draws the layout of the classroom.
    with tables/people
    Returns: The current layout of the Classroom
    '''
    for x in range(0, CLASSROOM_WIDTH):
        for y in range(0, CLASSROOM_HEIGHT):
            if map_to_draw[x][y].block_path == True:
                #draw wall if the path is "blocked"
                SURFACE_MAIN.blit(S_WALL, (x*CELL_WIDTH, y*CELL_HEIGHT))

            else:
                #draw floor if its traversable
                SURFACE_MAIN.blit(S_FLOOR, ( x*CELL_WIDTH, y*CELL_HEIGHT))

def draw_debug():

    draw_text(SURFACE_MAIN, "FPS: " + str(int(CLOCK.get_fps())), (0, 0), COLOR_BLUE)

def draw_text(display_surface, text_to_display, T_coords, text_color):
    ''' this function takes text, and displays it on the referenced surface. '''

    text_surf, text_rect = helper_text_objects(text_to_display, text_color)

    text_rect.topleft = T_coords

    display_surface.blit(text_surf, text_rect)



'''
 _   _ _____ _     ____  _____ ____  ____
| | | | ____| |   |  _ \| ____|  _ \/ ___|
| |_| |  _| | |   | |_) |  _| | |_) \___ \
|  _  | |___| |___|  __/| |___|  _ < ___) |
|_| |_|_____|_____|_|   |_____|_| \_\____/   '''


def helper_text_objects(incoming_text, incoming_color):

    Text_surface = FONT_MESSAGE.render(incoming_text, False, incoming_color)

    return Text_surface, Text_surface.get_rect()


'''
  ____    _    __  __ _____
 / ___|  / \  |  \/  | ____|
| |  _  / _ \ | |\/| |  _|
| |_| |/ ___ \| |  | | |___
 \____/_/   \_\_|  |_|_____|  '''


def game_main_loop():

    '''In this function, we loop the main game'''

    running = True

    # player action definition
    player_action = "no-action"

    while running:


        # Takes in player key inputs in game controls if you quit, it'll change player_action
        player_action = game_controls()

        if player_action == "QUIT":
            running = False

        # if you aren't at your normal status, ai of npcs will take effect
        elif player_action != "no-action":
            for obj in GAME_OBJECTS:
                if obj.ai:
                    obj.ai.take_turn()

        # Drawing the game
        draw_game()

        # TEMPORARY FPS CLOCK
        CLOCK.tick(GAME_FPS)

    # Quitting the game
    pygame.quit()
    exit()


def game_initialize():
    '''This function initializes mainwindow and pygame '''         # v temporary
    global SURFACE_MAIN, GAME_MAP, PLAYER, CLASSMATE, GAME_OBJECTS, CLOCK #temporary
    # important to keep everything in the initialization

    #initialize pygame
    pygame.init()

    CLOCK = pygame.time.Clock()

    # sets parameters from constants.py
    SURFACE_MAIN = pygame.display.set_mode( (GAME_WIDTH, GAME_HEIGHT) )
    # gives map builder a variable
    GAME_MAP = map_create()
    # Placeholder "Jason" is the name of the player character
    classmate_com1 = com_Classmate("Jason")
    PLAYER = obj_Actor(0, 0, "player", S_PLAYER, classmate = classmate_com1)
    # This serves as the name and ai for an npc character, maybe make one for everyone?
    classmate_com2 = com_Classmate("Tony")
    ai_com = ai_Test()
    CLASSMATE = obj_Actor(15, 5, "classmate", S_CLASSMATE, ai = ai_com)
    # THESE ARE THE GAME OBJECTS BEING DRAWN IN THE DRAWING FUNCTION
    GAME_OBJECTS = [PLAYER, CLASSMATE]



def game_controls():
    ''' these are the game controls '''
    events_list = pygame.event.get()

    #process input
    for event in events_list:
        if event.type == pygame.QUIT:
            return "QUIT"

        # Keyboard controls if a player moves, player_action in game main loop changes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PLAYER.move(0, -1)
                return "player-moved"
            if event.key == pygame.K_DOWN:
                PLAYER.move(0, 1)
                return "player-moved"
            if event.key == pygame.K_LEFT:
                PLAYER.move(-1, 0)
                return "player-moved"
            if event.key == pygame.K_RIGHT:
                PLAYER.move(1, 0)
                return "player-moved"

    return "no-action"




if __name__ == '__main__':
    game_initialize()
    game_main_loop()
