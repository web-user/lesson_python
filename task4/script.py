import turtle
import random
import math
import argparse

# parse args for run program
parser = argparse.ArgumentParser(description="For this you can use only this arguments")
parser.add_argument('-t', '--type', help='Type of nonlinear transformation.Available types:\n'
                                         'sinus, heart, spherical, polar, disk', required=True)
parser.add_argument('-i', '--iter_num', type=int, help='Number of iterations. Default value is: 7')
parser.add_argument('-p', '--points_count', type=int,
                    help="Number of points for 1 iteration. More points - best picture. Default value is: 150")

class MainCalculate:

    amp = 120  # scaling factor
    def __init__(self, turtle, x = 0, y = 0):
        self.turtle = turtle
        self.x = x
        self.y = y
    

    def draw_m(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.fd(5)

    def get_color(self):
        return random.randint(0, 150), random.randint(0, 150), random.randint(0, 150)

    def sinus(self, x, y):
        self.x = math.sin(x) * self.amp
        self.y = math.sin(y) * self.amp
        self.draw_m(self.x, self.y)

    def heart(self, x, y):
        self.x = (math.sqrt(x * x + y * y) * math.sin(math.sqrt(x * x + y * y) * math.atan(y/x))) * self.amp
        self.y = (-math.sqrt(x * x + y * y) * math.cos(math.sqrt(x * x + y * y) * math.atan(y/x))) * self.amp
        self.draw_m(self.x, self.y)

    def spherical(self, x, y):
        self.x =  (x / (x*x + y*y)) * self.amp
        self.y = (y / (x*x + y*y)) * self.amp
        self.draw_m(self.x, self.y)

    def polar(self, x, y):
        self.x = (math.atan(y/x)/math.pi) * self.amp
        self.y = (math.sqrt(x*x + y*y) - 1) * self.amp
        self.draw_m(self.x, self.y)

    def disk(self, x, y):
        self.x = ((1/math.pi) * math.atan(y/x) * math.sin(math.pi * math.sqrt(x*x + y*y))) * self.amp
        self.y = ((1/math.pi) * math.atan(y/x) * math.cos(math.pi * math.sqrt(x*x + y*y))) * self.amp
        self.draw_m(self.x, self.y)

    def all_cal(self, f_type, x, y):
        param = [self.sinus, self.heart]
        getattr(self, f_type)(x, y)

XMIN= -1.777
XMAX = 1.777
YMIN = -1
YMAX = 1
# calculations for drawing
def calculate(win, my_turtle, f_type, iter_num, points_count):
    calculate = MainCalculate(my_turtle)
    win.bgcolor("#c5f079")
    
    for i in range(iter_num):
        # generate coefficients for affine transformation
        a = random.random()
        d = random.uniform(a * a, 1.0)
        b = random.random()
        e = random.uniform(b * b, 1.0)
        c = random.uniform(-1.5, 1.5)
        f = random.uniform(-1.5, 1.5)

        # run calculations and drawing
        for j in range(points_count):
            # generate x & y for nonlinear transformation
            newx = random.uniform(XMIN, XMAX)
            newy = random.uniform(YMIN, YMAX)
            x = a * newx + b * newy + c
            y = d * newx + e * newy + f
            # apply random color
            my_turtle.pencolor(calculate.get_color())
            # get type of nonlinear transformation
            calculate.all_cal(f_type, x, y)


def main():

    # parse arguments and set values for vars
    args = parser.parse_args()
    f_type = args.type  # set type of nonlinear transformation

    # set number of iterations
    if args.iter_num is not None:
        iter_num = args.iter_num
    else:
        iter_num = 7

    # set points count for 1 iteration
    if args.points_count is not None:
        points_count = args.points_count
    else:
        points_count = 150

    # check type of nonlinear transformation
    if f_type in ("sinus", "heart", "spherical", "polar", "disk"):
        win = turtle.Screen()
        my_turtle = turtle.Turtle()
        my_turtle.screen.colormode(255)
        my_turtle.speed(0)

        # call function for draw fractal flame
        calculate(win, my_turtle, f_type, iter_num, points_count)
        win.exitonclick()
    else:
        print("Please set correct type of nonlinear transformation\nFor get help run this scripts with parameter -h")


if __name__ == '__main__':
    main()
