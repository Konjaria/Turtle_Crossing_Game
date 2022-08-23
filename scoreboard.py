from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.Level = 1
        self.goto(-280, 260)
        self.write(f"Level: {self.Level}",False,"Left",FONT)

    def Update_Scoreboard(self):
        self.write(f"Level: {self.Level}", False, "Left", FONT)

    def Increase_the_Level(self):
        self.clear()
        self.Level += 1
        self.Update_Scoreboard()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "Center", FONT)

