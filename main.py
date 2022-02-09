import time
from turtle import Turtle,Screen
from car import CarManager
from player import Player
from scoreboard import Scoreboard
import time

player1=Player()
score=Scoreboard()
screen=Screen()
car=CarManager()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("turtle crossing")
screen.bgcolor("black")

screen.listen()
screen.onkey(player1.up,"a")
screen.onkey(player1.down,"s")









game=True
while game:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    #collison with car
    for i in car.allcars:
        if  i.distance(player1) < 20:
            game=False
            score.game_over()
    #top bar
    if player1.ycor()>=250:
        player1.reset1()
        car.speed1()
        score.update()






screen.exitonclick()

