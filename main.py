from turtle import Screen, Turtle
from player import Player
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("white")
my_screen.title("Turtle-crossing Game")
my_screen.tracer(0)

player = Player()

my_screen.listen()
my_screen.onkey(player.move_player, "Up")

is_game_on = True

while is_game_on:
    pass


my_screen.exitonclick()
