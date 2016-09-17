from NextPoint import NextPoint

class SuccessorFinderWithPredecessor:
    @staticmethod
    def findSuccessor(point_list):
        return NextPoint.moveRandom(point_list[-1])
