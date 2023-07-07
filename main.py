import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Setting screen attributes
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating food and snake
my_snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

    # Define end game
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() > 280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in my_snake.segments:
        if segment == my_snake.head:
            pass
        elif my_snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()








# Exit screen once clicked
screen.exitonclick()
