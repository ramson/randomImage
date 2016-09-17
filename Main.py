from PNGCreator import PNGCreator
from Point import Point
from LineCollection import LineCollection

WIDTH = 1400
HEIGHT = 800
NUMBER_OF_POINTS = 100

png_creator = PNGCreator(WIDTH, HEIGHT)

lines = LineCollection(10, HEIGHT, WIDTH)
for i in range(NUMBER_OF_POINTS):
    lines.add_point_to_any_line()

for line in lines.get_lines():
    png_creator.add_black_line(line)

png_creator.write_to_file('result.png')
