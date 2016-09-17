from random import randint

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    @staticmethod
    def generate_random_point(max_x, max_y):
        point = Point(randint(0, max_x), randint(0, max_y))
        return point
