import Point
from SuccessorFinder import SuccessorFinderWithDirectionFromDirectPredecessor


class Line:
    def __init__(self, point, max_x, max_y):
        self.__points = []
        self.__points.append(point)
        self.__successor_strategy = SuccessorFinderWithDirectionFromDirectPredecessor(True, max_x, max_y)

    def get_points(self):
        return self.__points

    def add_next_point(self):
        self.__points.append(self.__successor_strategy.find_successor(self.__points))
