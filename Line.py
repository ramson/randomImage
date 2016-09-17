import Point
from SuccessorFinderWithPredecessor import SuccessorFinderWithPredecessor

class Line:
    def __init__(self, point):
        self.__points = []
        self.__points.append(point)

    def get_points(self):
        return self.__points

    def add_next_point(self, max_x, max_y):
        self.__points.append(SuccessorFinderWithPredecessor.find_successor(self.__points, max_x, max_y))
