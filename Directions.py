from Point import Point

class Up:
    @staticmethod
    def move(point):
        new_x = point.get_x() - 1
        new_y = point.get_y()
        return Point(new_x, new_y)

    @staticmethod
    def next_direction():
        return UpRight
    
    @staticmethod
    def previous_direction():
        return UpLeft
    
class Down:
    @staticmethod
    def move(point):
        new_x = point.get_x() + 1
        new_y = point.get_y()
        return Point(new_x, new_y)

    @staticmethod
    def next_direction():
        return DownLeft
    
    @staticmethod
    def previous_direction():
        return DownRight

class Left:
    @staticmethod
    def move(point):
        new_x = point.get_x()
        new_y = point.get_y() - 1
        return Point(new_x, new_y)

    @staticmethod
    def next_direction():
        return UpLeft
    
    @staticmethod
    def previous_direction():
        return DownLeft

class Right:
    @staticmethod
    def move(point):
        new_x = point.get_x()
        new_y = point.get_y() + 1
        return Point(new_x, new_y)

    @staticmethod
    def next_direction():
        return DownRight
    
    @staticmethod
    def previous_direction():
        return UpRight

class UpRight:
    @staticmethod
    def move(point):
        new_x = point.get_x() - 1
        new_y = point.get_y() + 1
        return Point(new_x, new_y)

    @staticmethod
    def next_direction():
        return Right
    
    @staticmethod
    def previous_direction():
        return Up

class UpLeft:
    @staticmethod
    def move(point):
        new_x = point.get_x() - 1
        new_y = point.get_y() - 1
        return Point(new_x, new_y)

    @staticmethod
    def next_direction():
        return Up
    
    @staticmethod
    def previous_direction():
        return Left

class DownLeft:
    @staticmethod
    def move(point):
        new_x = point.get_x() + 1
        new_y = point.get_y() - 1
        return Point(new_x, new_y)

    @staticmethod
    def next_direction():
        return Left
    
    @staticmethod
    def previous_direction():
        return Down

class DownRight:
    @staticmethod
    def move(point):
        new_x = point.get_x() + 1
        new_y = point.get_y() + 1
        return Point(new_x, new_y)

    @staticmethod
    def next_direction():
        return Down
    
    @staticmethod
    def previous_direction():
        return Right
