from turtle import Turtle, Screen


class main_screen():
    def __init__(self):
        self.create_middle()

    def create_middle(self):
        for i in range(600//10):
            t = Turtle("square")
            t.speed("fastest")
            t.shapesize(1, 0.1)
            t.penup()
            t.goto(0, -300+(10*i))
            if i % 2 != 0:
                t.color("white")
