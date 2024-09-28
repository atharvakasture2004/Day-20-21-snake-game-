from turtle import Turtle,Screen
import random,time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

snake=Snake()
food = Food()
score=ScoreBoard()
game_on=True 

Screen=Screen()
Screen.setup(height=615,width=615)
Screen.bgcolor("black")
Screen.title("Snake Game")
Screen.tracer(0)
Screen.listen()
Screen.onkey(snake.up,"Up")
Screen.onkey(snake.down,"Down")
Screen.onkey(snake.left,"Left")
Screen.onkey(snake.right,"Right")



while game_on:
    Screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        score.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset() 
            snake.reset() 

    
        
        
Screen.exitonclick()