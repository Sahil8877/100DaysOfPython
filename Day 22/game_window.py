from turtle import Turtle, Screen

class GameWindow():
    """
    Game window class to initialise the configurations for the turtle window
    """
    def __init__(self):
        #turtle object to draw screen  divider
        self.divider = Turtle("classic")
        self.screen = Screen()
        self.screen.title("Ping Pong!")
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.setup(width=800,height=600)
        self.divider.pencolor("white")
        self.divider.penup()
        self.divider.goto(0,350)
        self.divider.setheading(270)
        #for loop to draw dashed lines
        for _ in range(35):
            self.divider.pendown()
            self.divider.forward(10)
            self.divider.penup()
            self.divider.forward(10)

       
        


