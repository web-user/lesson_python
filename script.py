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

import turtle

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
#         # turtle.backward(length/2)
#         # turtle.left(60)
#         # turtle.forward(length/2)
#         # turtle.right(60)
#         # draw_sierpinski(length/2,depth-1)


# draw_sierpinski(500,1)
# turtle.exitonclick()

# def element_triangle(length_line):
# 	for n in range(0,3):
# 		turtle.forward(length_line/2)
# 		turtle.left(120)

# def create_tirngle(length_line):
# 	element_triangle(length_line)
# 	turtle.forward(length_line/2)
# 	element_triangle(length_line)
# 	turtle.left(60)
# 	turtle.forward(length_line/2)
# 	turtle.left(60)
# 	element_triangle(length_line)


# create_tirngle(600)
# turtle.exitonclick()

# list_num = 'vasa ivan'.split()


# print(list_num)

	# for i in range(len(st) - len(sub)):
	# 	count += 1
	# 	count_w[sub] = count
	# return count_w
import re

def search(st):
	document_text = st
	text_string = document_text.lower()
	match_pattern = re.findall(  r'\w*', text_string)
	frequency = { }
	word_ret = {}
	for word in match_pattern:
		count = frequency.get(word,0)
		frequency[word] = count + 1

	frequency_list = frequency.keys()

	for words in frequency_list:
		word_ret[words] = frequency[words] 
	
	return word_ret

	# return count_w

res = search('hello hell hell 12 12 wo e worl del')



print(res)


# def drawTriangle(points,color,myTurtle):
# 	myTurtle.color(color)
# 	myTurtle.up()
# 	myTurtle.goto(points[0][0],points[0][1])
# 	myTurtle.down()
# 	myTurtle.begin_fill()
# 	myTurtle.goto(points[1][0],points[1][1])
# 	myTurtle.goto(points[2][0],points[2][1])
# 	myTurtle.goto(points[0][0],points[0][1])
# 	myTurtle.end_fill()

# def getMid(p1,p2):
# 	return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

# def sierpinski(points,degree,myTurtle):
# 	colormap = ['blue','red','green','white','yellow', 'violet','orange']
# 	drawTriangle(points,colormap[degree],myTurtle)
# 	if degree > 0:
# 		sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
# 		sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree-1, myTurtle)
# 		sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)

# def main():
# 	myTurtle = turtle.Turtle()
# 	myWin = turtle.Screen()
# 	myPoints = [[-100,-50],[0,100],[100,-50]]
# 	sierpinski(myPoints,2,myTurtle)
# 	myWin.exitonclick()

# main()
