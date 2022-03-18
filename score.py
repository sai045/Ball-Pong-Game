from turtle import Turtle


class score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x, y)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", False,
                   "center", ("Arial", 32, "normal"))

    def score_increment(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False,
                   "center", ("Arial", 24, "normal"))
