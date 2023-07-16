# Python program to
# demonstrate printing HELLO
# using turtle
 
# Here frame is initialized with
# background colour as "White"
import turtle
frame = turtle.Screen().bgcolor("White")
draw = turtle.Turtle()
 
# The colour, width and speed of the pen is initialized
draw.color("Green")
draw.width(3)

 
# Now lets get started with actual code
# printing letter H
draw.left(90)
draw.forward(70)
draw.penup()
draw.goto(0, 35)
draw.pendown()
draw.right(90)
draw.forward(30)
draw.penup()
draw.goto(30, 70)
draw.pendown()
draw.right(90)
draw.forward(70)
 
# printing letter E
draw.penup()
draw.goto(40, 0)
draw.pendown()
draw.right(180)
draw.forward(70)
draw.right(90)
draw.forward(35)
draw.penup()
draw.goto(40, 35)
draw.pendown()
draw.forward(35)
draw.penup()
draw.goto(40, 0)
draw.pendown()
draw.forward(35)
 
# printing letter L
draw.penup()
draw.goto(90, 70)
draw.pendown()
draw.right(90)
draw.forward(70)
draw.left(90)
draw.forward(35)
 
# printing letter L
draw.penup()
draw.goto(135, 70)
draw.pendown()
draw.right(90)
draw.forward(70)
draw.left(90)
draw.forward(35)
 
# printing letter O
draw.penup()
draw.goto(210, 70)
draw.pendown()
for i in range(25):
    draw.right(15)
    draw.forward(10)
turtle.exitonclick()

""" import turtle

turtle.shape("turtle")
turtle.left(45)
turtle.forward(50)
turtle.right(65)
turtle.circle(150,350)
turtle.home()
big=("Arial", 36, "normal")
turtle.penup()
turtle.goto(-40,150)
turtle.write("Hello World!", font=big)
turtle.home()
turtle.back(20)
turtle.exitonclick() """