import turtle

# Set up the turtle screen
turtle.setup(400,400)
turtle.title("Turtle Spiral")
turtle.bgcolor("white")

# Define the turtle's pen color and width
#turtle.pencolor("blue")
turtle.pensize(3)

# Draw the spiral
for i in range(100):
    for colors in ["", "olive", "black"]:
        turtle.pencolor(colors)
        turtle.forward(i * 5)
        turtle.right(144)

# Keep the turtle window open until the user closes it
turtle.done()
