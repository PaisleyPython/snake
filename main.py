# Main runs file
# snake game consists of main, snake, food, scoreboard and data.txt for the storage of the high-score.


from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()
turtle = Turtle()

screen.setup(width=610, height=610)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)  # computer doesnt like this.


screen.listen()
screen.onkey(snake.up, "Up")  # Has to be Cap first letter
screen.onkey(snake.down, "Down")  # snake.method
screen.onkey(snake.left, "Left")  # method is defined within the snake class
screen.onkey(snake.right, "Right")

# TODO, Think of a way to turn these into methods within the Snake() class
# Think of using setheading to get the angles right.

FONT = ("courier", 35, "normal")
game_is_on = True
while game_is_on:
    # This is needed in order to get rid of the turn the arrow off from the centre of the screen.
    turtle.hideturtle()
    screen.update()  # my computer really doesnt like this
    time.sleep(0.1)
    snake.movement()
# Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment_score()


# Detect collison with wall.
# Perhaps the game over code could be made into a function.
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        score.update_scoreboard
        snake.reset()

        # game_is_on = False
        # score.game_over()
        # print("GAME OVER")

# Detect collision with tail.
# DONE Using slicing, eliminate the first if statement.

    for segment in snake.segments[1:]:  # remember the head is at the back.
        if segment == snake.head:
            pass

        # This is whats going to determine there's been a collision
        elif snake.head.distance(segment) < 10:
            score.update_scoreboard
            snake.reset()
            score.reset()

            # game_is_on = False
            # score.game_over()

    # print(segment)


# If head collides with any segment in the tail: trigger game_over

screen.exitonclick()
