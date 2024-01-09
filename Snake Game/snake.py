from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)
            

    def add_segment(self, position):
        reptile = Turtle(shape= 'square')
        reptile.penup()
        reptile.color('white')
        reptile.goto(position)
        self.snake_list.append(reptile)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for s in range(len(self.snake_list)-1, 0, -1):
            new_x = self.snake_list[s-1].xcor()
            new_y = self.snake_list[s-1].ycor()
            self.snake_list[s].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def right(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)

    def left(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].setheading(LEFT) 