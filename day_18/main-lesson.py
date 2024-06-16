import turtle as t
import random

tim = t.Turtle()

# for _ in range(25):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
screen = t.Screen()
screen.colormode(255)

# def draw_shape(num_sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)

# screen.colormode(255)
# for sides in range(3, 11):
#     tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     draw_shape(sides)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# angles = [0, 90, 180, 270]

# tim.pensize(10)
# tim.speed(10)
# for _ in range(200):
#     tim.setheading(random.choice(angles))
#     tim.pencolor(random_color())
#     tim.forward(30)


tim.speed("fastest")
for i in range(72):
    tim.pencolor(random_color())
    tim.circle(150)
    tim.right(5)

screen.exitonclick()
