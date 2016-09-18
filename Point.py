from random import randint

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def is_valid(self, max_x, max_y):
        if self.__x < 0:
            return False
        if self.__x >= max_x:
            return False
        if self.__y < 0:
            return False
        if self.__y >= max_y:
            return False
        return True
    
    @staticmethod
    def generate_random_point(max_x, max_y):
        point = Point(randint(0, max_x), randint(0, max_y))
        if not point.is_valid(max_x, max_y):
            print "Point(" + str(point.get_x()) + "/" + str(point.get_y()) + ") is out of range."
        return point
