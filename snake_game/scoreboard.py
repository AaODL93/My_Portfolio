from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}     Record: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.penup()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}     Record: {self.high_score}", align=ALIGNMENT, font=FONT)

    def restart_game(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write(f"Score: {self.score}     Record: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
