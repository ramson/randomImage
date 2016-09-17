import random

from Directions import Up
from Directions import UpRight
from Directions import Right
from Directions import DownRight
from Directions import Down
from Directions import DownLeft
from Directions import Left
from Directions import UpLeft

from Point import Point

class NextPoint:
    all_directions = [Up, UpRight, Right, DownRight, Down, DownLeft, Left, UpLeft]

    @staticmethod
    def moveRandom(point):
        direction = random.choice(NextPoint.all_directions)
        return direction.move(point)
