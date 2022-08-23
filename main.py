import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#Create object of the Player Class
player_acc = Player()

#Screen Tools
screen.listen()
screen.onkeypress(player_acc.move_player, "Up")

# User_Level
Level = Scoreboard()
game_is_on = True
level_passed = False
carmanager = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player_acc.ycor() == 280:
        Level.Increase_the_Level()
        carmanager.Level_Upgraded()
        player_acc.reset_the_position()
    carmanager.Create_cars()
    carmanager.Move()
    carmanager.Collision_to_the_Lside()
    for car in carmanager.all_cars:
       if  car.distance(player_acc) < 20:
            game_is_on = False
            Level.game_over()
screen.exitonclick()