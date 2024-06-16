from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
MAX_CARS = 40
MAX_CARS_PER_TURN = 2
NEW_CARS_THIS_TURN = [0, 0, 0, 0, 1, 1, 1, 1, 2]
CHANCE_OF_NEW_CAR = 6


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_cars((0, -300))
        self.move_distance = STARTING_MOVE_DISTANCE

    def __init_car(self):
        if randint(1, CHANCE_OF_NEW_CAR) == 1:
            car = Turtle("square")
            car.color(choice(COLORS))
            car.penup()
            car.setheading(180)
            car.resizemode("user")
            car.turtlesize(1, 2)
            y_cord = randint(-12, 12) * 20
            car.goto(300, y_cord)
            self.cars.append(car)

    def __move_cars_forward(self, t_position):
        # move cars forward
        for car in self.cars:
            car.forward(self.move_distance)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)
            # if car is close to t_position, we have collision with turtle
            if car.distance(t_position) < 25:
                return True
        return False

    def move_cars(self, t_position):
        self.__init_car()
        return self.__move_cars_forward(t_position)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
