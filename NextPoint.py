import random
from random import randint

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
    def move_random(point):
        direction = random.choice(NextPoint.all_directions)
        return direction.move(point)

    @staticmethod
    def move_in_similar_direction(point, direction):
        direction_change = randint(-2, 2)
        for i in range (abs(direction_change)):
            if direction_change < 0:
                direction = direction.previous_direction()
            else:
                direction = direction.next_direction()
        return direction.move(point)
