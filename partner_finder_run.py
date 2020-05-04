"""
Main file to put the running code (since I can't keep track of everything)
"""
import pygame
# from partner_finder_final import obj_Actor
from partner_finder_controller import obj_Actor, ai_Test
from constants import *
from partner_finder_view import map_create
from utilities import struc_Tile, com_Classmate, generate_student


INTERACT_MODE = False

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
        obj.draw(SURFACE_MAIN)

    draw_messages()

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

def draw_messages():


    for classmate in All_CLASSMATES:
        if classmate.x == PLAYER.x and classmate.y == PLAYER.y:
                print(INTERACT_MODE)
                if INTERACT_MODE == False:
                    draw_text(SURFACE_MAIN, classmate.name+ " : Hi! my name is " + classmate.name, (0, 0), COLOR_BLUE)
                else:
                    draw_text(SURFACE_MAIN, classmate.name+ " We are now interacting! ", (0, 0), COLOR_BLUE)




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

    global INTERACT_MODE

    running = True

    # player action definition
    player_action = "no-action"


    while running:


        # Takes in player key inputs in game controls if you quit, it'll change player_action
        player_action = game_controls()

        if player_action == "QUIT":
            running = False


        # if you aren't at your normal status, ai of npcs will take effect
        elif player_action == "player-moved":
            for obj in GAME_OBJECTS:
                if obj.ai:
                    obj.ai.take_turn(GAME_MAP)
            INTERACT_MODE = False



        elif player_action == "conversation":
            INTERACT_MODE = True
            print("we are in conversation mode")
            print(INTERACT_MODE)


        # Drawing the game
        draw_game()



    # Quitting the game
    pygame.quit()
    exit()


def game_initialize():
    '''This function initializes mainwindow and pygame '''
    global SURFACE_MAIN, GAME_MAP, PLAYER, CLASSMATE, GAME_OBJECTS, All_CLASSMATES, INTERACT_MODE

    # important to keep everything in the initialization

    #initialize pygame
    pygame.init()



    # sets parameters from constants.py
    SURFACE_MAIN = pygame.display.set_mode( (GAME_WIDTH, GAME_HEIGHT) )
    # gives map builder a variable
    GAME_MAP = map_create()

    # Placeholder "Jason" is the name of the player character
    classmate_com1 = com_Classmate("YOU")
    PLAYER = obj_Actor(10, 0, "player", "trait1", "trait2", "trait3", S_PLAYER, classmate = classmate_com1)
    # This serves as the name and ai for an npc character, maybe make one for everyone?
    # classmate_com2 = com_Classmate("Tony")
    ai_com = ai_Test()
    # CLASSMATE = obj_Actor(15, 5, "classmate", S_CLASSMATE, ai = ai_com)





    # THESE ARE THE GAME OBJECTS BEING DRAWN IN THE DRAWING FUNCTION, EVERY STUDENT
    GAME_OBJECTS = [PLAYER]
    # use extend possibly (read documentation)

    All_CLASSMATES = generate_student()

    GAME_OBJECTS.extend(All_CLASSMATES)


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
                PLAYER.move(0, -1, GAME_MAP)
                return "player-moved"
            if event.key == pygame.K_DOWN:
                PLAYER.move(0, 1, GAME_MAP)
                return "player-moved"
            if event.key == pygame.K_LEFT:
                PLAYER.move(-1, 0, GAME_MAP)
                return "player-moved"
            if event.key == pygame.K_RIGHT:
                PLAYER.move(1, 0, GAME_MAP)
                return "player-moved"
            if event.key == pygame.K_SPACE:
                return "conversation"

    return "no-action"




if __name__ == '__main__':
    game_initialize()
    game_main_loop()
