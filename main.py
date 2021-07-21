from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

l_paddle = Paddle((-350, 0))
# Will NOT work if the Caps Lock is On
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    # Detect Collision with Edge of the Screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting Right Paddle Misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # Detecting Left Paddle Misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
