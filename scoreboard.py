from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.Level = 1
        self.write(f"Level: {self.Level}",False,"Left",FONT)

    def Update_Scoreboard(self):
        self.write(f"Level: {self.Level}", False, "Left", FONT)

    def Increase_the_Level(self):
        self.clear()
        self.Level += 1
        self.Update_Scoreboard()
    def game_over(self):
        self.clear()
        self.write(f"Game Over", False, "Center", FONT)

