from turtle import Turtle
SHIFT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FWD = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.color("OliveDrab")

    def create_snake(self):
        for position in SHIFT:
           self.add_new_part(position)

    def add_new_part(self, position):
        new_part = Turtle(shape="square")
        new_part.color("LawnGreen")
        new_part.penup()
        new_part.goto(position)
        self.snake_body.append(new_part)

    def extend_body(self):
        self.add_new_part(self.snake_body[-1].position())

    def move(self):
        for body_num in range(len(self.snake_body)-1, 0, -1):
            prev_pos = self.snake_body[body_num-1].pos()
            self.snake_body[body_num].goto(prev_pos)
        self.head.forward(MOVE_FWD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for part in self.snake_body:
            part.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.color("OliveDrab")
