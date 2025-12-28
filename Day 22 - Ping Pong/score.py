from turtle import Turtle

class Score:
    def __init__(self):
        #scoreboard list to score multiple turtle objects for displaying the scores
        self.scoreboard = []
        #initial right and left score set to 0 when game starts
        self.r_score = 0
        self.l_score = 0

        # Create separate Turtle objects
        self.r_score_turtle = Turtle()
        self.l_score_turtle = Turtle()

        for turtle in [self.r_score_turtle, self.l_score_turtle]:
            #hide the turtles and set the color to white for both the turtle objects
            turtle.hideturtle()
            turtle.pencolor("white")
            turtle.penup()
        #set the score diplay position on screen
        self.r_score_turtle.goto(180, 230)
        self.l_score_turtle.goto(-220, 230)
        #store the right and left player scorre objects into the scoreboard list for easy access
        self.scoreboard.append(self.r_score_turtle)
        self.scoreboard.append(self.l_score_turtle)

        #initial scores to display when game begins set to 0 by default 
        self.scoreboard[0].write(f"{self.r_score}", font=("Arial", 50, "normal"))
        self.scoreboard[1].write(f"{self.l_score}", font=("Arial", 50, "normal"))

    def r_scores(self, r_score):
        """
        Writes the scores for right player using the first turtle object from the scoreboard list
        """
        self.r_score = r_score
        #clears the previous score on screen
        self.scoreboard[0].clear()
        self.scoreboard[0].write(f"{self.r_score}", font=("Arial", 50, "normal"))

    def l_scores(self, l_score):
        """
        Writes the scores for the left player using the second turtle object from the scoreboard list
        """
        self.l_score = l_score
        #clears the previous score on screen
        self.scoreboard[1].clear()
        self.scoreboard[1].write(f"{self.l_score}", font=("Arial", 50, "normal"))
