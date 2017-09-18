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

turtle.shape('triangle')
turtle.forward(300)
turtle.stamp()
turtle.backward(300)
turtle.left(180)

turtle.stamp()
turtle.backward(300)


turtle.stamp()
turtle.right(90)

turtle.forward(300)
turtle.stamp()
turtle.left(135)
turtle.forward(410)

turtle.end_fill()
turtle.exitonclick()


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
