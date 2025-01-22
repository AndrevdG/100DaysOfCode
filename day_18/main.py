# import colorgram

# def rgb_tuple(color):
#     rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
#     return rgb


# extract_colors = colorgram.extract('spots.png', 30)
# colors = []
# for color in extract_colors:
#     colors.append(rgb_tuple(color))

# print(colors)

import turtle as t
from random import choice

color_list = [
    (195, 160, 120),
    (72, 92, 125),
    (143, 86, 59),
    (216, 209, 121),
    (140, 160, 188),
    (183, 146, 162),
    (29, 33, 46),
    (175, 159, 43),
    (57, 35, 26),
    (120, 73, 93),
    (140, 174, 154),
    (61, 30, 39),
    (78, 116, 80),
    (138, 28, 19),
    (117, 29, 41),
    (182, 100, 86),
    (48, 59, 91),
    (174, 99, 116),
    (101, 120, 168),
    (33, 51, 45),
    (102, 155, 88),
    (213, 176, 190),
    (217, 180, 173),
    (164, 207, 188),
    (66, 84, 27),
    (179, 187, 213),
]

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)

tim.pensize(20)
tim.penup()
tim.hideturtle()
for y in range(0, 10):
    for x in range(0, 10):
        tim.setposition(x * 50, y * 50)
        tim.dot(20, choice(color_list))


screen.exitonclick()
