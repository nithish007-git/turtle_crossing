from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
     def __init__(self):
         super().__init__()
         self.shape("turtle")
         self.color("white")
         self.penup()
         self.goto(0,-250)
         self.left(90)

     def up(self):
        self.forward(10)
     def down(self):
        self.back(10)
     def reset1(self):
         self.goto(0,-250)
