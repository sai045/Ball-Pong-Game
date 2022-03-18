from turtle import Turtle, Screen
import time
from main_screen import main_screen
from score import score
from paddle import paddle
from ball import ball

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.tracer(0)
screen.listen()

SCREEN = main_screen()
player_one_score = score(-40, 250)
player_two_score = score(40, 250)
player_one = paddle(350)
player_two = paddle(-350)
Ball = ball()

screen.onkey(player_one.up, "Up")
screen.onkey(player_one.down, "Down")

screen.onkey(player_two.up, "w")
screen.onkey(player_two.down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.01)
    screen.update()
    Ball.move()

    if Ball.ycor() > 280 or Ball.ycor() < -280:
        Ball.bounce()

    if Ball.distance(player_one.paddle) < 50 and Ball.xcor() > 320:
        Ball.bounce_x()

    if Ball.distance(player_two.paddle) < 50 and Ball.xcor() < -320:
        Ball.bounce_x()

    if Ball.xcor() > 380:
        player_two_score.score_increment()
        Ball.bounce_x()

    if Ball.xcor() < -380:
        player_one_score.score_increment()
        Ball.bounce_x()


screen.exitonclick()
