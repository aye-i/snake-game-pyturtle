from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("Crimson")
        self.speed("fastest")
        self.more_food()

    def more_food(self):
        r_position = (random.randint(-270, 270), random.randint(-270, 270))
        self.goto(r_position)


