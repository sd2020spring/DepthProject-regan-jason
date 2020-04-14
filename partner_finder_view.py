# partner_finder_view
class ClassroomView:
    '''
    Class to help visualize the classroom enviornment

    Attributes: a Classroom instance representing the room to EnvironmentView
    '''
    def __init__(self, classroom):
        self.classroom = classroom

    def draw(self):
        '''
        Draws the layout of the classroom.

        Returns:
        The current layout of the Classroom
        '''
        pass

    def add_students(self):
        '''
        Function will add x amount of students to populate the
        classroom. Each student will have their own spawn point.
        Treats students in an kind of x,y coordinate system with
        students occupying squares.
        '''
        pass

    pass
