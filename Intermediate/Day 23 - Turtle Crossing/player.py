from turtle import Turtle
import time
from scoreboard import Scoreboard

class Player():
    def __init__(self,screen):
        """
        Player inherits from scoreboard
        defines game speed and turtle object as player
        """
        self.scoreboard = Scoreboard(screen)
        self.player = Turtle(shape="turtle")
        self.player.setheading(90)
        self.player.penup()
        self.player.color("white")
        self.player.goto(0,-250)
        self.GAME_SPEED = 0.1
        
    
    def player_move_up(self):
        """
        method to move the player up 10 steps
        """
        if self.player.ycor() < 250:
            self.player.forward(20)
    
    def player_move_down(self):
        """
        method to move the player down 10 steps
        """
        if self.player.ycor() > -250:
            self.player.backward(20)

    def check_collision(self,cars):
        """
        method to track object and player collisions
        if collision is detected display GAME OVER and return True 
        else if the player crosses 250 on y axis, reset player position, 
        increment game speed and return none
        """
        for car in cars:
            if car.distance(self.player) <= 25:
                
                print("collision detected")
                self.scoreboard.game_over()
                time.sleep(2)
                return True
            if self.player.ycor() == 250: 
                self.scoreboard.add_score()
                self.player.goto(0,-250)
                self.GAME_SPEED -= 0.005
                return None
    
    
        