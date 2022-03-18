from turtle import Turtle


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x = 3
        self.y = 3

    def move(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)

    def bounce(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
