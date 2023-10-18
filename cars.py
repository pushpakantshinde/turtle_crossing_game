from turtle import Turtle
import random

INITIAL_DISTANCE = 5
INCREMENT_DISTANCE = 5

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Cars:
    def __init__(self):
        self.cars_list = []
        self.move_distance = INITIAL_DISTANCE

    def move_car(self):
        for car in self.cars_list:
            car.forward(self.move_distance)

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            y_position = random.randint(-280, 280)
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(280, y_position)
            new_car.setheading(180)
            self.cars_list.append(new_car)

    def level_up(self):
        self.move_distance += INCREMENT_DISTANCE

    def clear_cars(self):
        for car in self.cars_list:
            car.hideturtle()



