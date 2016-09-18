from NextPoint import NextPoint
from Directions import get_direction

class SuccessorFinderWithPredecessor:
    @staticmethod
    def find_successor(point_list, max_x, max_y):
        if len(point_list) == 1:
            point = NextPoint.move_random(point_list[-1])
            if not point.is_valid(max_x, max_y):
                point = SuccessorFinderWithPredecessor.find_successor(max_x, max_y)
            return point

        previous_direction = get_direction(point_list[-2], point_list[-1])
        return NextPoint.move_in_similar_direction(point_list[-1], previous_direction)