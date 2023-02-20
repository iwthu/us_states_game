import turtle

ALIGNMENT = "center"
FONT = ("Ariel", 8, "normal")


class TextOnScreen(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def write_down_guess(self, state_data, states_cords):
        self.goto(states_cords)
        self.write(align=ALIGNMENT, font=FONT, arg=state_data)
