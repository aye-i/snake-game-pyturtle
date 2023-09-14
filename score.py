from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("LawnGreen")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("data.txt") as score_file:
            self.high_score = int(score_file.read())
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=("Tahoma", 10, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("Red")
    #     self.write(f"Game Over!", align="center", font=("Courier", 20, "bold"))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as score_file:
                score_file.write(str(self.high_score))
        self.score = 0
        print(f"Score: {self.score} | High Score: {self.high_score}")
        self.update_score()


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.create_border()

    def create_border(self):
        self.color("Gold")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.pendown()
        for _ in range(4):
            self.forward(560)
            self.right(90)