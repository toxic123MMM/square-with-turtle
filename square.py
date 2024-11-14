import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(400,300)
square=turtle.Turtle()
num_sides=4
angle=360/num_sides
side_length=100
for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)

turtle.done()