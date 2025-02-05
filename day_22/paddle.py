from turtle import Turtle

PADDLE_HEIGHT = 5
PADDLE_WIDTH = 1


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.__init_paddle(position)

    def __init_paddle(self, position):
        self.shape('square')
        self.color('white')
        self.resizemode('user')
        self.setheading(90)
        self.shapesize(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.penup()
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
