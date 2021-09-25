import turtle
from random import randint

screen = turtle.Screen()
screen.bgcolor('light green')

turtle.up()
turtle.setpos(-170, 250)
turtle.down()
turtle.pencolor('indigo')
turtle.write("Turtle Racing Competition", font=("Ariel", 20, "bold"))
turtle.hideturtle()


cross_line = turtle.Turtle()
cross_line.up()
cross_line.setpos(250, 200)
cross_line.down()
cross_line.pencolor('red')
cross_line.pensize(4)
cross_line.right(90)
cross_line.forward(250)
cross_line.hideturtle()


racer1 = turtle.Turtle()
racer1.pencolor('purple')
racer1.pensize(2)
racer1.up()
racer1.setpos(-200, 145)
racer1.down()
racer1.write("Turtle1", font=("Ariel", 12, "bold"))
racer1.up()
racer1.setpos(-100,150)
racer1.shape('turtle')
racer1.down()


racer2 = turtle.Turtle()
racer2.pencolor('green')
racer2.pensize(2)
racer2.up()
racer2.setpos(-200, 95)
racer2.down()
racer2.write("Turtle2", font=("Ariel", 12, "bold"))
racer2.up()
racer2.setpos(-100,100)
racer2.shape('turtle')
racer2.down()


racer3 = turtle.Turtle()
racer3.pencolor('blue')
racer3.pensize(2)
racer3.up()
racer3.setpos(-200, 45)
racer3.down()
racer3.write("Turtle3", font=("Ariel", 12, "bold"))
racer3.up()
racer3.setpos(-100,50)
racer3.shape('turtle')
racer3.down()


racer4 = turtle.Turtle()
racer4.pencolor('maroon')
racer4.pensize(2)
racer4.up()
racer4.setpos(-200, -5)
racer4.down()
racer4.write("Turtle4", font=("Ariel", 12, "bold"))
racer4.up()
racer4.setpos(-100,0)
racer4.shape('turtle')
racer4.down()


racer1_dist = 0
racer2_dist = 0
racer3_dist = 0
racer4_dist = 0



while True:
	
	move = randint(0, 3)
	racer1.forward(randint(0,3))
	racer1_dist += move
	if racer1.pos() >= (260.0, 150):
		winner = "Turtle1"
		break
	
	move = randint(0, 3)
	racer2.forward(randint(0,3))
	racer2_dist += move
	if racer2.pos() >= (260.0, 100):
		winner = "Turtle2"
		break
	
	move = randint(0, 3)
	racer3.forward(randint(0,3))
	racer3_dist += move
	if racer3.pos() >= (260.0, 50):
		winner = "Turtle3"
		break
	
	move = randint(0, 3)
	racer4.forward(randint(0,3))
	racer4_dist += move
	if racer4.pos() >= (260.0, 0):
		winner = "Turtle4"
		break


turtle.up()
turtle.setpos(-125, -150)
turtle.down()
turtle.pencolor("crimson")
turtle.write(winner+" won the race!", font=("Ariel", 18, "bold"))

screen.exitonclick()
