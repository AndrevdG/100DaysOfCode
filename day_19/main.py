from turtle import Turtle, Screen
from random import randint


def create_turtle(t_color, t_ypos):
    tort = Turtle(shape="turtle")
    tort.color(t_color)
    tort.penup()
    tort.goto(x=-230, y=t_ypos)
    return tort


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will run the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y = -100
for color in colors:
    turtles.append(create_turtle(t_color=color, t_ypos=y))
    y += 40


if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(6):
        turtles[i].forward(randint(0, 10))
        if turtles[i].xcor() >= 230:
            is_race_on = False
            winner = colors[i]

if user_bet == winner:
    print(f"The {winner} turtle won the race and so did you!!")
else:
    print(f"The {winner} turtle won the race. You, however, did not :(")

# screen.exitonclick()
