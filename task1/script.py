import turtle


def draw_sierpinski(length,depth):
	if depth==0:
		for i in range(3):
			turtle.forward(length)
			turtle.left(120)
	else:
		draw_sierpinski(length/2,depth-1)
		turtle.forward(length/2)
		draw_sierpinski(length/2,depth-1)

		turtle.backward(length/2)
		turtle.left(60)
		turtle.forward(length/2)
		turtle.right(60)

		draw_sierpinski(length/2,depth-1)
		turtle.left(60)
		turtle.backward(length/2)
		turtle.right(60)


if __name__ == "__main__":
	draw_sierpinski(500,2)
	turtle.exitonclick()
