from turtle import Screen
# https://trinket.io/docs/colors
# https://docs.python.org/3/library/turtle.html#module-turtle
from snake import Snake
from food import Food
from score import Score, Border

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game 🐍")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
border = Border()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.075)

    snake.move()
    # detect food collision
    if snake.head.distance(food) < 20:
        food.more_food()
        snake.extend_body()
        score.increase_score()

    # wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        # game_on = False
        # score.game_over()
        score.reset_game()
        snake.reset_snake()

    # self collision
    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            # game_on = False
            # score.game_over()
            score.reset_game()
            snake.reset_snake()

screen.exitonclick()

