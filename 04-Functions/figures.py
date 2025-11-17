import turtle

pen = turtle.Turtle()
pen.speed(5)

def draw_square(len):
# Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

# Draw a square
    for i in range(4):
        pen.forward(len)
        pen.right(90)


def draw_triangle(len):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    # Draw a triangle
    for i in range(3):
        pen.forward(len)
        pen.right(120)
    

def draw_rectangle(len_a, len_b):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

# Draw a square
    for i in range(4):
        if i%2 == 0:
            pen.forward(len_a)
            pen.right(90)
        else:
            pen.forward(len_b)
            pen.right(90)


