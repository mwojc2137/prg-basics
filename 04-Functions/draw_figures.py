import turtle


def draw_square(len):
# Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

# Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

# Draw a square
    for i in range(4):
        pen.forward(len)
        pen.right(90)

# Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()