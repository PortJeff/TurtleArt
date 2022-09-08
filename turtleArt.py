import turtle




#tree
#og length of branch, lenth to stop at, turning angle
def tree(len,minlen, ang):
	turtle.penup()
	turtle.goto(0,-500)
	turtle.pendown()
	turtle.left(90)
	if len > minlen:
		turtle.forward(len)
		turtle.left(ang)
		tree(len*.7, minlen,  ang)
		turtle.right(ang*2)
		tree(len*.7, minlen,  ang)
		turtle.left(ang)
		turtle.backward(len)


#dragon
#iterations of fractal(resolution), length of each line
def dragon(iterations, len):
	turtle.screensize(10000,10000)
	turtle.tracer(0,0)
	#turtle.speed(10000)
	og = "r"
	while iterations!=0:
		ogg = og[::-1]
		f = ""
		for element in ogg:
			if element == "r":
				f = f + "l"
			else:
				f = f + "r"
		og = og + "r" + f
		i-=1
	print('beginning fractal')

	for element in og:
		turtle.forward(len)
		if element == "r":
				turtle.right(90)
		else:
			turtle.left(90)


def drawTriangle(length):
	for i in range(3):
		turtle.forward(length)
		turtle.right(120)


def sierpinskiTriangle(length, it, speed):
	turtle.speed(speed)
	pos=[-500,-500]
	turtle.penup()
	turtle.goto(-500,-500)
	turtle.pendown()
	turtle.left(60)
	def draw(length, it):
		if(it > 0):
			drawTriangle(length)
			draw(length/2, it-1)
			turtle.forward(length)
			drawTriangle(length)
			draw(length/2, it-1)
			turtle.right(120)
			turtle.forward(length)
			turtle.left(120)
			drawTriangle(length)
			draw(length/2, it-1)
			turtle.left(120)
			turtle.forward(length)
			turtle.right(120)
	draw(length, it)


#sierpinskiTriangle(500, 6, 20)
#dragon(16, 1)
#tree(15, 3, 30)

turtle.done()
