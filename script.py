# -*- coding: utf-8 -*-


# turtle.shape('triangle')
# turtle.color('blue', 'orange')
# turtle.shape('square')
# turtle.shape('triangle')
# turtle.shapesize(5,8,10)

# >>> turtle.shapesize(8,8,10)
# >>> turtle.stamp()
# 5
# >>> turtle.shape('triangle')
# >>> turtle.shapesize(5,5,6)

# import turtle

# def divide_three( length_line ):
# 	return int(length_line / 3)

# def tringle_interior(len_imterion):



# def create_tringle(length_line, ):


# turtle.shape('triangle')
# turtle.forward(600)
# turtle.stamp()

# turtle.left(120)
# turtle.forward(600)
# turtle.stamp()

# turtle.left(120)
# turtle.forward(600)
# turtle.stamp()

# turtle.left(180)
# turtle.forward(200)
# turtle.stamp()

# turtle.right(60)
# turtle.forward(200)
# turtle.stamp()

# turtle.right(120)
# turtle.forward(200)
# turtle.stamp()

# turtle.right(120)
# turtle.forward(200)
# turtle.stamp()

# turtle.right(120)
# turtle.forward(400)
# turtle.stamp()

# turtle.right(120)
# turtle.forward(200)
# turtle.stamp()

# turtle.right(120)
# turtle.forward(200)
# turtle.stamp()

# turtle.forward(200)
# turtle.stamp()

# turtle.right(120)
# turtle.forward(200)
# turtle.stamp()

# turtle.right(120)
# turtle.forward(200)
# turtle.stamp()



# turtle.stamp()
# turtle.right(90)

# turtle.forward(300)
# turtle.stamp()
# turtle.left(135)
# turtle.forward(410)

# turtle.end_fill()
# turtle.exitonclick()




# def divide_three( length_line ):
# 	return int(length_line / 3)

# def next_step(len_imterion, line_radius):
# 	turtle.right(line_radius)
# 	turtle.forward(len_imterion)
# 	turtle.stamp()

# def next_step_left(length_line, line_radius):
# 	turtle.left(line_radius)
# 	turtle.forward(length_line)
# 	turtle.stamp()



# def tringle_interior(len_imterion, line_radius):
# 	next_step(len_imterion, line_radius)

# 	next_step(len_imterion, line_radius)

# 	turtle.right(line_radius)
# 	turtle.forward(400)
# 	turtle.stamp()

# 	next_step(len_imterion, line_radius)

# 	next_step(len_imterion, line_radius)

# 	turtle.forward(len_imterion)
# 	turtle.stamp()

# 	next_step(len_imterion, line_radius)

# 	next_step(len_imterion, line_radius)


# def create_tringle(length_line, line_radius):
# 	interior = divide_three( length_line )

# 	turtle.shape('triangle')
# 	turtle.forward(length_line)
# 	turtle.stamp()

# 	next_step_left(length_line, line_radius)
# 	next_step_left(length_line, line_radius)

# 	turtle.left(180)
# 	turtle.forward(interior)
# 	turtle.stamp()

# 	turtle.right(60)
# 	turtle.forward(interior)
# 	turtle.stamp()

# 	tringle_interior(interior, line_radius)
# 	turtle.end_fill()
# 	turtle.exitonclick()


# create_tringle(600, 120)







"""Triangle"""

# def draw_sierpinski(length,depth):
#     if depth==0:
#         turtle.forward(length)
#         turtle.left(120)

#         turtle.forward(length)
#         turtle.left(120)

#         turtle.forward(length)
#         turtle.left(120)
#     else:
#         draw_sierpinski(length/2,depth-1)
#         turtle.forward(length/2)
#         draw_sierpinski(length/2,depth-1)

#         turtle.backward(length/2)
#         turtle.left(60)
#         turtle.forward(length/2)
#         turtle.right(60)

#         draw_sierpinski(length/2,depth-1)
#         turtle.left(60)
#         turtle.backward(length/2)
#         turtle.right(60)


# draw_sierpinski(500,2)
# turtle.exitonclick()


# list_num = 'vasa ivan'.split()


# print(list_num)

	# for i in range(len(st) - len(sub)):
	# 	count += 1
	# 	count_w[sub] = count
	# return count_w

"""Turtle Graphics"""

# import re
# from turtle import *

# turtle = Turtle()

# def search(st):
# 	document_text = st
# 	text_string = document_text.lower()
# 	match_pattern = re.findall(  r'\w*', text_string)
# 	frequency = { }
# 	word_ret = {}
# 	for word in match_pattern:
# 		count = frequency.get(word,0)
# 		frequency[word] = count + 1

# 	frequency_list = frequency.keys()

# 	for words in frequency_list:
# 		word_ret[words] = frequency[words] 
	
# 	return word_ret


# res = search('hello hell hell  12')


# # (7/ 14) * 1 = 0.5

# per = []

# for item in res:
# 	if item != '':
# 		per.append(res[item])

# sum_str = sum(per)

# def cal_list( x, y ):
# 	new_l = []
# 	for i in x:
# 		my_r = i / y * 1
# 		new_l.append(my_r)
# 	return new_l

# percentages = cal_list(per, sum_str)

# radius = 200

# color_num = ['blue','red','green','white','yellow', 'violet','orange']

# penup()
# forward(radius)
# left(90)
# pendown()
# # color('palegreen')
# begin_fill()
# circle(radius)
# end_fill()
# home()
# right(90)
# # color('yellow')
# def segment(percentages, radius):
# 	rollingPercent = 0
# 	for percent in percentages:
# 		segment = percent * 360
# 		rollingPercent += segment
# 		color('yellow')
# 		setheading(rollingPercent)
# 		# color(clr[int_cl])
# 		pendown()
# 		forward(radius)
# 		penup()
# 		home()

# segment(percentages,radius)

# exitonclick()

"""Gold pyramid """

# def golden_pyramid_d(triangle):
# 	tr = [0, 1, 2, 3, 4, 5, 6] # copy
# 	for i in range(len(tr) - 2, -1, -1):
# 		for j in range(i + 1):
# 			tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
# 	return tr

# print(golden_pyramid_d(range(7)))



# def fib1(n):
# 	assert n >= 0
# 	return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

# n = [1, 4, 7, 2, 5]

# n.sort(reverse=True)

# print(n)

# print(fib1(5))

"""Fractal flame"""

from turtle import *
import random



ob = Turtle()



class FracFl:
	def __init__(self, x= 0, y = 0):
		self.x = x
		self.y = y

	def __mul__(self, other):
		if isinstance( other, (int, float) ):
			return FracFl(self.x * other, self.y * other)
		elif isinstance(other, __class__):
			return FracFl(self.x * other.x, self.y * other.y)

v = FracFl(2, 5)
v1 = FracFl(3, 6)

v2 = v * v1

print(v2.x)


ob.speed(3)

cl = ['red', 'green', 'blue']

def draw_fractal(length, angle, x, y):
	ob.up()
	ob.goto(x, y)
	ob.down()


	c = 0
	ob.begin_fill()
	for i in range(5):

		x = random.randint(-100, -1)
		y = random.randint(1, 100)

		x = (x ** 2 + y ** 2) // x
		y = (x ** 2 + y ** 2) // x



		print(x)
		print(y)

		ob.fillcolor(cl[c])
		ob.goto(x, y)
		# x += 1
		# y += 1
		c += 1
		if c >2:
			c = 0
	ob.end_fill()




draw_fractal(200, 120, -30, 40)

exitonclick()