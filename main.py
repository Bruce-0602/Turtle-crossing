import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

bruce = Player()
car_manager = CarManager()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(bruce.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # screen.update()
    car_manager.generate_car()
    car_manager.move()
    screen.update()

    # Finish one level
    if bruce.ycor() > 290:
        scoreboard.level_up()
        scoreboard.update_scoreboard()
        bruce.reset()
        car_manager.reset()

    # Game over
    for i in car_manager.car_list:
        if bruce.distance(i) < 15:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()