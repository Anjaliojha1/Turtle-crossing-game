import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoeboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()

screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 6) == 1:
        car_manager.car_struct()
    car_manager.move_car()

    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

        if player.ycor() > 280:
            player.reset_position()
            score.increase_score()
            car_manager.level_up()



screen.exitonclick()