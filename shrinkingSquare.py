import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")


def shrinkgSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkgSquare(150)
shrinkgSquare(130)
shrinkgSquare(110)
shrinkgSquare(90)
shrinkgSquare(70)
shrinkgSquare(50)
shrinkgSquare(30)
shrinkgSquare(10)

turtle.done()