from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreBoard=ScoreBoard()

def end_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(end_game, "c")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()
        scoreBoard.l_point()
    
    if ball.xcor()<-380:
        ball.reset_position()
        scoreBoard.r_point()

screen.exitonclick()
