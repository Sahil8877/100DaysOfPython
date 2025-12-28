from turtle import Turtle,Screen

class Scoreboard():
    def __init__(self,screen):
        """
        score board class to display player scores as level and game over text
        """

        self.screen = screen
        self.score = 0
        self.score_display = Turtle()
        self.score_display.goto(-50,260)
        self.score_display.hideturtle()
        self.score_display.pencolor("white")
        # print initial score as level 0
        self.update_score()

        self.game_over_disp = Turtle()
     
    def update_score(self):
        """
        method to display the score as level 
        """
        self.score_display.clear()
        self.score_display.write(f"LEVEL : {self.score}",font=("Arial",20,"normal"))
    
    def game_over(self):     
        """
        method to display game over text when collision is detected
        """
        
        self.game_over_disp.penup()
        self.game_over_disp.goto(0,0)
        self.game_over_disp.pencolor("red")
        self.game_over_disp.hideturtle()
        self.game_over_disp.write("GAME OVER!",align="center",font=("Arial",20,"normal"))
        #update the screen window to show the text before game quits
        self.screen.update()

    def add_score(self):
        """
        method to add new score and call update score method to display the changes
        """
        self.score += 1
        self.update_score()

        

    
    
    
    


