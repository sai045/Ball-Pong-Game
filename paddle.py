from turtle import Turtle, Screen
import time


class paddle:
    def __init__(self, y):
        self.paddle = None
        self.create_paddle(y)

    def create_paddle(self, y):
        t = Turtle("square")
        t.penup()
        t.goto(y, 0)
        t.shapesize(5, 1)
        t.speed("slowest")
        self.paddle = t

    def up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()+20)

    def down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()-20)
