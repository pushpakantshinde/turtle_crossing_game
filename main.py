from turtle import Screen, Turtle
from player import Player
from cars import Cars
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("white")
my_screen.title("Turtle-crossing Game")
my_screen.tracer(0)

player = Player()
car_manager = Cars()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(player.move_player, "Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    my_screen.update()

    car_manager.create_cars()
    car_manager.move_car()
    # scoreboard.update_scoreboard()

    # Detect when turtle reaches to other side
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.level_up()

    # Detect collision with the car
    for car in car_manager.cars_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            player.clear_player()           # Clear the player on screen
            car_manager.clear_cars()        # Clear the cars on the screen
            my_screen.update()              # Need to update the screen otherwise we cant see clearing of player & cars
            is_game_on = False

my_screen.exitonclick()