from game_window import GameWindow
from turtle import Turtle
from score import Score

class Ball():
    """
    Ball class, defines the ball movements, collision detection
    """
    def __init__(self):
        #turtle object to show ball
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.shapesize(stretch_len=2,stretch_wid=2)
        self.ball.penup()
        self.ball.speed(1)
        #initital ball x,y position
        self.ball_x_move = 9
        self.ball_y_move = 9
        #initial ball moving speed 
        self.ball_move_speed = 0.08
        #initializing the score class object
        self.score = Score()
        #initial scores for left and right player 
        self.r_score = 0
        self.l_score = 0
        

    def move(self):
        """
        move method the move the ball in x,y direction using initial positions `self.ball_x_move` and ``self.ball_y_move
        """
        self.move_x_to = self.ball.xcor() + self.ball_x_move
        self.move_y_to = self.ball.ycor() + self.ball_y_move

        self.ball.goto(self.move_x_to,self.move_y_to)  

    def check_collision(self, paddle_r,paddle_l):
        """
        function to check the different collisions like top/bottom wall and paddle hit
        parameters: 
        paddle_r : to get right paddle position from main.py
        paddle_l : to get left paddle position from main.py
        """
        if self.ball.distance(paddle_r) < 50 and self.ball.xcor() == 360 or self.ball.distance(paddle_l) < 50 and self.ball.xcor() == -360:
            """
            to check if the distance between the ball and right/left paddles < 50 and x/y coordinates of ball == 360(right) and -360(left)
            If both are true then ball had hit the paddles and we move the ball in opp direction to bounce back.
            and increase the relative speed of the ball
            """
            print("Paddle hit!")
            self.ball_x_move *= -1
            self.ball_move_speed*=0.9

        # Wall collision (top/bottom)
        if self.ball.ycor() > 290 or self.ball.ycor() < -290:
            """
            if the ball y_cor(TOP) > 290 and y_cor(BOTTOM) < -290 is true ball had hit a wall 
            if tru we move the ball opp direction of y_cor to bounce back
            """
            self.ball_y_move *= -1

        # Right/Left wall (missed paddle)
        if self.ball.xcor() > 380 or self.ball.xcor() < -380:
            """
            If the ball x_cor(right) > 380 and x_cor(left) < -380 the ball had missed the paddles
            if true we reset the ball speed to 0.08
            """
            print("Missed paddle game over or reset!")
            self.ball_move_speed=0.08

            #condition checks for score increment
            if self.ball.xcor() > 300:
                #if ball x_cor(right) > 300 left player gets +1 score
                self.l_score += 1
                #calling left score method to increase the score
                self.score.l_scores(self.l_score)
            elif self.ball.xcor() < -300:
                #if ball x_cor(left) < -300 right player gets +1 score
                self.r_score += 1
                #callinf right score method to increase the score
                self.score.r_scores(self.r_score)

            #resetting the initial ball position to center when ball misses the paddles
            self.ball.goto(0, 0)
            #to bounce ball into opposite direction when either of the paddles were missed
            self.ball_x_move *= -1



        

