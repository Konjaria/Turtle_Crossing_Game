from turtle import Turtle
from random import choice
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
VELOCITY = [1, 3, 6, 10, 0]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
      self.all_cars = []
      self.velocity = 1
      self.car_speed = MOVE_INCREMENT

    def Create_cars(self):
        random_number = randint(1,2 )
        random_number = randint(1, 6)
        if random_number == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=1,stretch_len=2)
            self.random_y = randint(-250, 280)
            car.goto(300, self.random_y)
            self.all_cars.append(car)


    def Move(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def Collision_to_the_Lside(self):
        for car in self.all_cars:
            if car.xcor()== -250:
                car.goto(280, self.random_y)

    def Level_Upgraded(self):
        self.car_speed += MOVE_INCREMENT



