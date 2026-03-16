from game_window import GameWindow
from paddle import Paddles
from ball import Ball
import time

#object for game window class 
game_window = GameWindow()
#object for setting right paddles using initial positions as parameters
r_paddle = Paddles((380,0))
#object for setting left paddles using initial positions as parameters
l_paddle = Paddles((-380,0))
#ball class object
ball = Ball()

game_window.screen.listen()
#key press event handlinng for right and left paddle movement - UP,DOWN
game_window.screen.onkeypress(fun=r_paddle.paddle_control_up,key="Up")
game_window.screen.onkeypress(fun=r_paddle.paddle_control_down,key="Down")
game_window.screen.onkeypress(fun=l_paddle.paddle_control_up,key="w")
game_window.screen.onkeypress(fun=l_paddle.paddle_control_down,key="s")

#while loop to keep playing
while True:
    time.sleep(ball.ball_move_speed)  # animation speed
    game_window.screen.update() # Refresh screen
    #function to check for collisions by passing right and left paddle positions
    ball.check_collision(r_paddle.paddle,l_paddle.paddle) 
    #calling move function from ball class to keep moving the ball 
    ball.move() 
    

