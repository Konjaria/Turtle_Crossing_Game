from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.fillcolor("green")
        self.goto(STARTING_POSITION)
        self.left(90)
        self.sety(-FINISH_LINE_Y)

    def move_player(self):
        temp = self.ycor()
        self.sety(temp + MOVE_DISTANCE)

    def reset_the_position(self):
        self.goto(STARTING_POSITION)