from Point import Point

def get_direction(point1, point2):
    x_change = point2.get_x() - point1.get_x()
    y_change = point2.get_y() - point1.get_y()
    if x_change < 0 and y_change < 0:
        return UpLeft
    if x_change < 0 and y_change == 0:
        return Up
    if x_change < 0 and y_change > 0:
        return UpRight
    if x_change == 0 and y_change > 0:
        return Right
    if x_change > 0 and y_change > 0:
        return DownRight
    if x_change > 0 and y_change == 0:
        return Down
    if x_change > 0 and y_change < 0:
        return DownLeft
    return Left


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
