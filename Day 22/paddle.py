from turtle import Turtle

class Paddles:
    """
    Paddles class to define the paddle controls - Up and Down 
    """
    def __init__(self, position):
        #turtle object for paddle creation
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(position)
        self.paddle.shapesize(stretch_wid=1, stretch_len=6)  # Vertical paddle
        self.paddle.setheading(270)  # Point upward

    def paddle_control_up(self):
        """
        Paddle control function to go UP
        """
        if self.paddle.ycor() < 220:
            self.paddle.sety(self.paddle.ycor() + 30)

    def paddle_control_down(self):
        """
        Paddle control function to go DOWN
        """
        if self.paddle.ycor() > -220:
            self.paddle.sety(self.paddle.ycor() - 30)