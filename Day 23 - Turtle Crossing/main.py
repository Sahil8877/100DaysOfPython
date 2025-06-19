from turtle import Screen
import time
from car_manager import Car_Manager
from player import Player

screen = Screen()
#set bg color for window
screen.bgcolor("black")
#set color mode to r,g,b 
screen.colormode(255)
screen.setup(width=600,height=600)
screen.title("Turtle Crossing")
#turn off animations                          
screen.tracer(0)
#car_manager class instance
cars = Car_Manager()
#player class instance
player = Player(screen)

is_game_over = False

#generate cars by calling car_generator method
cars.car_generator()

#listening to events
screen.listen()
#key events to control the turtle
screen.onkeypress(fun=player.player_move_up,key="Up")
screen.onkeypress(fun=player.player_move_down,key="Down")

while not is_game_over:
    time.sleep(0.5 * player.GAME_SPEED)

    if player.check_collision(cars.list_of_cars):
        #if collision detected then game ends
        is_game_over = True
        
    else:
        cars.car_moving()

    screen.update()

    

    
        
