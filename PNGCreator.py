import png

from Point import Point
from Line import Line

class PNGCreator:
    def __init__(self, width, height):
        self.png = [[0 for x in range(width)] for y in range(height)]
        

    def write_to_file(self, file_name):
        f = open(file_name, 'wb')
        palette=[(255,255,255), (0,0,0)]
        w = png.Writer(len(self.png[0]), len(self.png), palette=palette, bitdepth=1)
        w.write(f, self.png)
        f.close()

    def add_black_pixel(self, point):
        self.png[point.get_x()][point.get_y()] = 1

    def add_black_line(self, line):
        for point in line.get_points():
            self.add_black_pixel(point)
