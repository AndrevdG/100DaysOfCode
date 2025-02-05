from turtle import Turtle

MOVEMENT = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.__init_ball()
        self.movespeed = 0.1
        self.x_movement = MOVEMENT
        self.y_movement = MOVEMENT

    def __init_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto((0, 0))

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1
        self.movespeed *= 0.9

    def reset_position(self):
        self.goto((0, 0))
        self.movespeed = 0.1
        self.bounce_x()
