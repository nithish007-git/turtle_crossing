COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle


class CarManager(Turtle):
    def __init__(self):
        self.allcars=[]
    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.allcars.append(car)



    def move_cars(self):
        for i  in self.allcars:
            i.backward(STARTING_MOVE_DISTANCE)

    def speed1(self):
        STARTING_MOVE_DISTANCE=random.randint(9,20)
        self.move_cars()
        print(STARTING_MOVE_DISTANCE)
