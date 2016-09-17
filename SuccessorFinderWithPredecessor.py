from NextPoint import NextPoint

class SuccessorFinderWithPredecessor:
    @staticmethod
    def find_successor(point_list, max_x, max_y):
        point = NextPoint.moveRandom(point_list[-1])
        if not point.is_valid(max_x, max_y):
            point = SuccessorFinderWithPredecessor.find_successor(max_x, max_y)

        return point
