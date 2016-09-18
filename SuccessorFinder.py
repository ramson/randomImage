from NextPoint import NextPoint
from Directions import get_direction


class SuccessorFinderWithDirectionFromDirectPredecessor:
    def __init__(self, prefer_same_direction, max_x, max_y):
        self.__prefer_same_direction = prefer_same_direction
        self.__max_x = max_x
        self.__max_y = max_y

    def find_successor(self, point_list):
        if len(point_list) == 1:
            point = NextPoint.move_random(point_list[-1])
            if not point.is_valid(self.__max_x, self.__max_y):
                point = SuccessorFinderWithDirectionFromDirectPredecessor.find_successor(self.__max_x, self.__max_y)
            return point

        previous_direction = get_direction(point_list[-2], point_list[-1])
        return NextPoint.move_in_similar_direction(point_list[-1], previous_direction, self.__prefer_same_direction)
