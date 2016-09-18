from Line import Line
from Point import Point
from random import randint

class LineCollection:
    def __init__(self, max_lines, max_x, max_y):
        self.__lines = []
        self.__maximum_number_of_lines = max_lines
        self.__max_x = max_x
        self.__max_y = max_y

    def get_lines(self):
        return self.__lines

    def add_line(self, point):
        line = Line(point, self.__max_x, self.__max_y)
        self.__lines.append(line)

    def add_point_to_any_line(self):
        size = len(self.__lines)
        if size >= self.__maximum_number_of_lines:
            size = size - 1
        random = randint(0, size)
        
        if random >= len(self.__lines):
            # add point in new line
            self.add_line(self.generate_random_point())
            return
        
        # add point to existing line
        self.__lines[random].add_next_point()
        
    def generate_random_point(self):
        return Point.generate_random_point(self.__max_x, self.__max_y)
