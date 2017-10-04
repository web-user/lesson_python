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

	def sinus(self, x, y):
		self.x = math.sin(x) * self.amp
		self.y = math.sin(y) * self.amp
		self.draw_m(self.x, self.y)
		# print("This func sin")

	def heart(self, x, y):
		self.x = (math.sqrt(x * x + y * y) * math.sin(math.sqrt(x * x + y * y) * math.atan(y/x))) * self.amp
		self.y = (-math.sqrt(x * x + y * y) * math.cos(math.sqrt(x * x + y * y) * math.atan(y/x))) * self.amp
		self.draw_m(self.x, self.y)
		# print("This func heart")

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

XMIN= 1.777
XMAX = 1.777
YMIN = -1
YMAX = 1
# calculations for drawing
def calculate(win, my_turtle, f_type, iter_num, points_count):
	cal = MainCalculate(my_turtle)



def main():

	# parse arguments and set values for vars
	args = parser.parse_args()



if __name__ == '__main__':
	main()