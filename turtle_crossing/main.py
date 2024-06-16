import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if car_manager.move_cars(turtle.pos()):
        game_is_on = False
        score_board.game_over()
    if turtle.is_at_finishline():
        score_board.level_up()
        car_manager.speed_up()
        turtle.back_to_start()
    screen.update()

screen.exitonclick()
