"""
Main file to put the running code (since I can't keep track of everything)
"""
import pygame
# from partner_finder_final import obj_Actor
from partner_finder_controller import obj_Actor, ai_Test
from constants import *
from partner_finder_view import map_create
from utilities import struc_Tile, com_Classmate, generate_student, com_Professor
import random

#ENDGAME = False
INTERACT_MODE = 0
Player_yes = "NO"


'''''''''
  ____
 |  _ \ _ __ __ ___      _(_)_ __   __ _
 | | | | '__/ _` \ \ /\ / / | '_ \ / _` |
 | |_| | | | (_| |\ V  V /| | | | | (_| |
 |____/|_|  \__,_| \_/\_/ |_|_| |_|\__, |
                                  |___/        '''''''''


def draw_game(ENDGAME):

    e = ENDGAME
    global SURFACE_MAIN

    # coloring background
    SURFACE_MAIN.fill(COLOR_GREY)

    # draw the map
    draw_map(GAME_MAP, e)

    # draws in all game objects in the list in an easy fashion
    for obj in GAME_OBJECTS:
        obj.draw(SURFACE_MAIN)

    e = (draw_messages() or ENDGAME)

    # update the display
    pygame.display.flip()
    return e


def draw_map(map_to_draw,ENDGAME):
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


    if ENDGAME == True:
       print("this is the endgame")
       print(ENDGAME)
       map_create()
       SURFACE_MAIN.fill(COLOR_BLACK)
      # if classmate.trait1 == PLAYER.trait1 and classmate.trait2 == PLAYER.trait2 and classmate.trait3 == PLAYER.trait3:
        #   draw_text(SURFACE_MAIN, "You made the best Softdes project Olin has ever seen, your partner must have come from Babson. Either way your cleverness and wits got you through this, congrats!", (0,15), COLOR_WHITE)
       #elif classmate.trait1 == PLAYER.trait1 and classmate.trait2 == PLAYER.trait2 or classmate.trait2 == PLAYER.trait2 and classmate.trait3 == PLAYER.trait3 or classmate.trait3 == PLAYER.trait3 and classmate.trait1 == PLAYER.trait1:
        #   draw_text(SURFACE_MAIN, "You made an okay softdes project. Everything went smoothly, but you probably could have done better. Maybe if you had just chosen someone else...?", (0,15), COLOR_WHITE)
       #else:
        #   draw_text(SURFACE_MAIN, "You created the worst softdes project ever and argued non-stop over everything. This could have been avoided, your professor expected better.", (0,15), COLOR_WHITE)

       for obj in GAME_OBJECTS:
           GAME_OBJECTS.remove(obj)
           return GAME_OBJECTS






def draw_messages():
    e = False
    if PLAYER.x == 1 and PLAYER.y == 1:
            e = False
            if INTERACT_MODE == 1:
                draw_text(SURFACE_MAIN, "Professor: Hello there, I have a question for you! What are your three traits?", (0, 0), COLOR_BLUE)
            elif INTERACT_MODE == 2:
                draw_text(SURFACE_MAIN, "Professor: Oh, so you're " + PLAYER.trait1 + ", " + PLAYER.trait2 + ', and ' + PLAYER.trait3 , (0, 0), COLOR_BLUE)
            elif INTERACT_MODE == 3:
                draw_text(SURFACE_MAIN, "Professor: Good luck finding a partner that matches your traits! Don't fail!", (0, 0), COLOR_BLUE)


    for classmate in All_CLASSMATES:
        if classmate.x == PLAYER.x and classmate.y == PLAYER.y:
                if INTERACT_MODE == 1:
                    draw_text(SURFACE_MAIN, classmate.name+ " : Hi! my name is " + classmate.name, (0, 0), COLOR_BLUE)
                elif INTERACT_MODE == 2:
                    draw_text(SURFACE_MAIN, classmate.name + ": I want you to know I am " + classmate.trait1 + ", " + classmate.trait2 + ', and ' + classmate.trait3, (0, 0), COLOR_BLUE)
                elif INTERACT_MODE == 3:
                    draw_text(SURFACE_MAIN, classmate.name + ": Do you want to be my parter?" + " " + "Yes=Y, No=N", (0,0), COLOR_BLUE)
                elif INTERACT_MODE < 0:
                    draw_text(SURFACE_MAIN, classmate.name + ": Oh okay...See you around!", (0,0), COLOR_BLUE)
                elif INTERACT_MODE > 100:
                    e = True
                    if classmate.trait1 == PLAYER.trait1 and classmate.trait2 == PLAYER.trait2 and classmate.trait3 == PLAYER.trait3:
                        draw_text(SURFACE_MAIN, classmate.name + ": Awesome! I think we'd be great teammates! See you around!", (0,0), COLOR_BLUE)
                        draw_text(SURFACE_MAIN, "You made the best Softdes project Olin has ever seen!", (0,50), COLOR_GREEN)
                        draw_text(SURFACE_MAIN, "Your partner must have been from Babson.", (0,100), COLOR_GREEN)
                        draw_text(SURFACE_MAIN, "Either way your cleverness and wits got you through this, congrats!", (0,150), COLOR_GREEN)
                        draw_text(SURFACE_MAIN, "Your professor personally gave you access to Olin College's endowment!", (0,200), COLOR_GREEN)
                    elif classmate.trait1 == PLAYER.trait1 and classmate.trait2 == PLAYER.trait2 or classmate.trait2 == PLAYER.trait2 and classmate.trait3 == PLAYER.trait3 or classmate.trait3 == PLAYER.trait3 and classmate.trait1 == PLAYER.trait1:
                        draw_text(SURFACE_MAIN, classmate.name + ": Sure. Why not, could be worse.", (0,0), COLOR_BLUE)
                        draw_text(SURFACE_MAIN, "You made an okay softdes project.", (0,50), COLOR_GREY)
                        draw_text(SURFACE_MAIN, "Everything went smoothly(?), but you probably could have done better.", (0,100), COLOR_GREY)
                        draw_text(SURFACE_MAIN, "No one walked up to your booth at the expo, and you recieved no recognition.", (0,100), COLOR_GREY)
                        draw_text(SURFACE_MAIN, "Maybe if you had chosen someone else...maybe a Babson Student?", (0,150), COLOR_GREY)
                    else:
                        draw_text(SURFACE_MAIN, classmate.name + ": Me?! Are you sure?! I have a bad feeling about this...", (0,0), COLOR_BLUE)
                        draw_text(SURFACE_MAIN, "You created the worst softdes project ever and argued non-stop over everything.", (0,50), COLOR_RED)
                        draw_text(SURFACE_MAIN, "This could have been avoided, your professor expected better.", (0,100), COLOR_RED)
                        draw_text(SURFACE_MAIN, "The product of too much olin-inbreeding...maybe mingle with Babson students?", (0,100), COLOR_RED)


    return e







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
    ENDGAME = False
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
            INTERACT_MODE = 0



        elif player_action == "conversation":
            INTERACT_MODE += 1
            print("we are in conversation mode")
            print(INTERACT_MODE)

        if player_action == "YES":
            INTERACT_MODE += 100

        elif player_action == "NO":
            INTERACT_MODE += -10


        ENDGAME = draw_game(ENDGAME)


    # Quitting the game
    pygame.quit()
    exit()


def game_initialize():
    '''This function initializes mainwindow and pygame '''
    global SURFACE_MAIN, GAME_MAP, PLAYER, CLASSMATE, GAME_OBJECTS, All_CLASSMATES, INTERACT_MODE, ENDGAME

    # important to keep everything in the initialization

    #initialize pygame
    pygame.init()



    # sets parameters from constants.py
    SURFACE_MAIN = pygame.display.set_mode( (GAME_WIDTH, GAME_HEIGHT) )
    # gives map builder a variable
    GAME_MAP = map_create()

    # Placeholder "Jason" is the name of the player character
    classmate_com1 = com_Classmate("YOU")
    PLAYER = obj_Actor(10, 0, "player", random.choice(traits1), random.choice(traits2), random.choice(traits3), S_PLAYER, classmate = classmate_com1)
    # This serves as the name and ai for an npc character, maybe make one for everyone?
    professor_com1 = com_Professor("Professor")
    PROFESSOR = obj_Actor(1,1, "professor", "no trait", "no trait", "no trait", S_PROFESSOR, professor = professor_com1)
    ai_com = ai_Test()
    # CLASSMATE = obj_Actor(15, 5, "classmate", S_CLASSMATE, ai = ai_com)





    # THESE ARE THE GAME OBJECTS BEING DRAWN IN THE DRAWING FUNCTION, EVERY STUDENT
    GAME_OBJECTS = [PLAYER, PROFESSOR]
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
            if event.key == pygame.K_y:
                return "YES"
            if event.key == pygame.K_n:
                return "NO"
    return "no-action"




if __name__ == '__main__':
    game_initialize()
    game_main_loop()
