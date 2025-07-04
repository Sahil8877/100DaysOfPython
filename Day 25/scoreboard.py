from turtle import Turtle

class Score:
    #score class to keep track of user score
    def __init__(self):
        #initialize turtle object to write the score on the screen
        self.score = 0
        self.score_obj = Turtle()
        self.score_obj.hideturtle()
        self.score_obj.penup()
        self.score_obj.goto(180,255)
        self.score_obj.write(f"Your Score : {self.score}/50",align='left',font=("roboto", 18, "normal"))

    def update_current_score(self):
        #func to update the score and write it on the screen
        self.score_obj.clear()
        self.score += 1
        self.score_obj.write(f"Your Score : {self.score}/50",align='left',font=("roboto", 18, "normal"))
        
    