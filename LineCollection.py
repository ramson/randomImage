from Line import Line
from Point import Point
from random import randint

class LineCollection:
    def __init__(self, max_lines, max_x, max_y):
        self.lines = []
        self.maximum_number_of_lines = max_lines
        self.max_x = max_x
        self.max_y = max_y

    def get_lines(self):
        return self.lines

    def add_line(self, point):
        line = Line(point)
        self.lines.append(line)

    def add_point_to_any_line(self):
        size = len(self.lines)
        if size >= self.maximum_number_of_lines:
            size = size - 1
        random = randint(0, size)
        
        if random >= len(self.lines):
            # add point in new line
            self.add_line(self.generate_random_point())
            return
        
        # add point to existing line
        
        
        # maxRandomNumber = size of __lines or size of __lines-1
        # get random number between 0 and maxRandomNumber
        # if random == 0:
        #   add_line
        # lineToChange = __lines[random]
        #

    def generate_random_point(self):
        point = Point(randint(0, self.max_x), randint(0, self.max_y))
        return point
