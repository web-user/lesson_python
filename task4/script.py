import turtle
import random
import math
import argparse

"""
parse args for run program
"""
parser = argparse.ArgumentParser(description="For this you can use only this arguments")
parser.add_argument('-t', '--type', help='Type of nonlinear transformation.Available types:\n'
                                         'sinus, heart, spherical, polar, disk', required=True)
parser.add_argument('-i', '--iter_num', type=int, help='Number of iterations. Default value is: 7')
parser.add_argument('-p', '--points_count', type=int,
                    help="Number of points for 1 iteration. More points - best picture. Default value is: 150")

XMIN = -1.777
XMAX = 1.777
YMIN = -1
YMAX = 1

class MainCalculate:

    def __init__(self, turtle, x=0, y=0):
        self.turtle = turtle
        self.x = x
        self.y = y
        self.amp = 120

    def draw_m(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.fd(5)

    def get_color(self, rr, gg, bb):
        return self.turtle.pencolor(rr, gg, bb)

    def sinus(self, x, y):
        self.x = math.sin(x) * self.amp
        self.y = math.sin(y) * self.amp
        self.draw_m(self.x, self.y)

    def heart(self, x, y):
        self.x = (math.sqrt(x*x + y*y) * math.sin(math.sqrt(x*x + y*y) * math.atan(y/x))) * self.amp
        self.y = (-math.sqrt(x*x + y*y) * math.cos(math.sqrt(x*x + y*y) * math.atan(y/x))) * self.amp
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

    def call_draw(self, f_type, x, y, rr, gg, bb):
        self.get_color(rr, gg, bb)
        getattr(self, f_type)(x, y)


class Figure:
    def __init__(self):
        self.a = random.random()
        self.d = random.uniform(self.a * self.a, 1.0)
        self.b = random.random()
        self.e = random.uniform(self.b * self.b, 1.0)
        self.c = random.uniform(-1.5, 1.5)
        self.f = random.uniform(-1.5, 1.5)
        self.rr = random.randint(0, 150)
        self.gg = random.randint(0, 150)
        self.bb = random.randint(0, 150)


class Coordiate(MainCalculate):
    def __init__(self, fig, f_type, turtle):
        self.turtle = turtle
        self.f_type = f_type
        self.fig = fig
        self.new_x = random.uniform(XMIN, XMAX)
        self.new_y = random.uniform(YMIN, YMAX)
        super().__init__(self.turtle)

    def get_x(self):
        return self.fig.a*self.new_x + self.fig.b*self.new_y + self.fig.c

    def get_y(self):
        return  self.fig.d*self.new_x + self.fig.e*self.new_y + self.fig.f

    def get(self):
        return super(Coordiate, self).call_draw(self.f_type,  self.get_x(), self.get_y(), self.fig.rr, self.fig.gg, self.fig.bb)

def calculate(win, my_turtle, f_type, iter_num, points_count):

    win.bgcolor("#f7ffea")

    for i in range(iter_num):
        """
        generate coefficients for affine transformation
        """
        fig = Figure()

        # run calculations and drawing
        for j in range(points_count):
            """
            generate x & y for nonlinear transformation
            """
            Coordiate(fig, f_type, my_turtle).get()


def main():
    """
    parse arguments and set values for vars
    """
    args = parser.parse_args()
    f_type = args.type  # set type of nonlinear transformation

    # set number of iterations
    if args.iter_num:
        iter_num = args.iter_num
    else:
        iter_num = 7

    # set points count for 1 iteration
    if args.points_count:
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
