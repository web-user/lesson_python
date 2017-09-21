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




def divide_three( length_line ):
	return int(length_line / 3)

def next_step(len_imterion, line_radius):
	turtle.right(line_radius)
	turtle.forward(len_imterion)
	turtle.stamp()

def next_step_left(length_line, line_radius):
	turtle.left(line_radius)
	turtle.forward(length_line)
	turtle.stamp()



def tringle_interior(len_imterion, line_radius):
	next_step(len_imterion, line_radius)

	next_step(len_imterion, line_radius)

	turtle.right(line_radius)
	turtle.forward(400)
	turtle.stamp()

	next_step(len_imterion, line_radius)

	next_step(len_imterion, line_radius)

	turtle.forward(len_imterion)
	turtle.stamp()

	next_step(len_imterion, line_radius)

	next_step(len_imterion, line_radius)


def create_tringle(length_line, line_radius):
	interior = divide_three( length_line )

	turtle.shape('triangle')
	turtle.forward(length_line)
	turtle.stamp()

	next_step_left(length_line, line_radius)
	next_step_left(length_line, line_radius)

	turtle.left(180)
	turtle.forward(interior)
	turtle.stamp()

	turtle.right(60)
	turtle.forward(interior)
	turtle.stamp()

	tringle_interior(interior, line_radius)
	turtle.end_fill()
	turtle.exitonclick()


create_tringle(600, 120)

















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
# 	sierpinski(myPoints,3,myTurtle)
# 	myWin.exitonclick()

# main()
