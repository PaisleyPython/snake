from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
screen = Screen()


# down = turtle.setheading(270)
# left = turtle.setheading(180)
# right = turtle.setheading(0)
up = turtle.setheading(90)
down = turtle.setheading(270)
left = turtle.setheading(180)
right = turtle.setheading(0)

screen.listen()
screen.onkey(turtle.up, "Up")  # Has to be Cap first letter
screen.onkey(turtle.down, "Down")
screen.onkey(turtle.left, "Left")
screen.onkey(turtle.right, "Right")

# turtle.forward("space", 20)

screen.exitonclick()
