from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.goto(-270,250)
        self.update()
    def write1(self):
        self.write(f"Level : {self.score}",align="left",font=("Courier", 24, "normal"))
        self.color("white")
    def update(self):
        self.score+=1
        self.clear()
        self.write1()
    def game_over(self):
        self.goto(0,0)
        self.write("Game over",align="center",font=("Courier", 24, "normal"))




