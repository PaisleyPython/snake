from turtle import Turtle, Screen

# Named as a constant. USING CAPITAL LETTERS
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """This is the snake class which contains the body and movement of the snake."""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(Self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        Self.segments.append(new_segment)

    def extend(Self):
        """Adds a new segment to the snake"""
        Self.add_segment(
            Self.segments[-1].position())  # dont forget position() is a method and we call is with ()

    def movement(self):
        """moves each segment of the snake forwards"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(Self):
        for seg in Self.segments:
            seg.goto(1000, 1000)
        Self.segments.clear()  # Removes all snake segements from the list.
        Self.create_snake()  # Same attributes as the __init__ method
        Self.head = Self.segments[0]

# Because we're using the segment line often, it would make sense
# to create a new attribute. We can call this 'head'. So..:
        # self.segments[0].setheading(90); becomes:
        # self.head.setheading(UP)

# DONE Change the code so that the snake isn't able to go back on itself.

    def up(self):
        """Moves the snake up but not back on itself"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """moves the snake down but not back on itself"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """moves the snake left but not back on itself"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """moves the snake right but not back on itself"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


# Had a type error with line 25.. TypeError: 'list' object is not callable:
# This was because i was trying to call a list that had prens around it instead of brackets

# up = 90, down = 270, left = 180, right = 0
