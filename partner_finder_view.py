# partner_finder_view
import pygame
import partner_finder_final



class Classroom:
    '''
    Class to help visualize the classroom enviornment

    Attributes: a Classroom instance representing the room to EnvironmentView
    '''
    def __init__(self, HEIGHT, WIDTH):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH


    def draw(self):
        '''
        Draws the layout of the classroom.
        with tables/people
        Returns: The current layout of the Classroom
        '''
        screen.blit(self.image.get_rect(self.HEIGHT, self.WIDTH))

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
