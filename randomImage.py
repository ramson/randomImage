import sys, getopt

from PNGCreator import PNGCreator
from LineCollection import LineCollection

WIDTH = 1400
HEIGHT = 800
NUMBER_OF_POINTS = 10000
OUTPUT_FILE = 'result.png'

def main(argv):
    width = WIDTH
    height = HEIGHT
    number_of_points = NUMBER_OF_POINTS
    output_file = OUTPUT_FILE
    try:
        opts, args = getopt.getopt(argv, "ho:w:s:n:", ["help", "outfile=", "width=", "height=", "numberOfPoints="])
    except getopt.GetoptError:
        print 'randomImage.py -o <outputfile> -w <width> -h <height> -n <number of points>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'randomImage.py -o <outputfile> -w <width> -s <height> -n <number of points>'
            sys.exit()
        elif opt in ("-o", "--outfile"):
            output_file = int(arg)
        elif opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-s", "--height"):
            height = int(arg)
        elif opt in ("-n", "--numberOfPoints"):
            number_of_points = int(arg)

    png_creator = PNGCreator(width, height)

    lines = LineCollection(10, height, width)
    for i in range(number_of_points):
        lines.add_point_to_any_line()

    for line in lines.get_lines():
        png_creator.add_black_line(line)

    png_creator.write_to_file(output_file)

if __name__ == "__main__":
   main(sys.argv[1:])