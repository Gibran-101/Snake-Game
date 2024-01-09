from turtle import Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

to_continue = True
while to_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_scoreboard()
    if snake.snake_list[0].xcor() < -290 or snake.snake_list[0].xcor() > 290 or snake.snake_list[0].ycor() < -290 or snake.snake_list[0].ycor() > 290:
        scoreboard.game_over()
        to_continue = False
    for block in snake.snake_list[1::]:
        if snake.snake_list[0].distance(block) < 10:
            to_continue = False
            scoreboard.game_over()        

screen.exitonclick()