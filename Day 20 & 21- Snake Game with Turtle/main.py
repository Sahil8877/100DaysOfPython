from game_play import SnakeGame
import time

#SnakeGame class object
snake_obj = SnakeGame()

screen = snake_obj.screen
screen.setup(width=600,height=600)

moving = True
snake_obj.score_tracker()
#keep playing until collision detected
while moving:
    
    snake_obj.move() #to move all segments together
    snake_obj.check_food() # to check if the segment touches the food object
    
    time.sleep(snake_obj.DELAY) #delays the frame animation
    
    screen.update() #update the screen with all frames
    if snake_obj.check_wall_collision():
        moving = False
    if snake_obj.check_body_collision():
        moving = False
    

    screen.listen()
    
    screen.onkeypress(fun=snake_obj.right,key="Right")
    screen.onkeypress(fun=snake_obj.left,key="Left")
    screen.onkeypress(fun=snake_obj.up,key="Up")
    screen.onkeypress(fun=snake_obj.down,key="Down")
    
screen.exitonclick()



        
        

        

