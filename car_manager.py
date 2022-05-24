from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        helper = random.randint(1, 6)
        if helper <= 2:
            temp = Turtle()
            temp.shape("square")
            temp.penup()
            temp.color(random.choice(COLORS))
            temp.shapesize(stretch_wid=0.5, stretch_len=1)
            temp.goto(280, random.randint(-280, 280))
            self.car_list.append(temp)

    def move(self):
        for i in self.car_list:
            i.goto(i.xcor() - self.move_speed, i.ycor())
            if i.xcor() < -300:
                i.hideturtle()
                self.car_list.remove(i)

    def reset(self):
        for i in self.car_list:
            i.hideturtle()
        self.car_list = []
        self.move_speed += MOVE_INCREMENT
