from turtle import Turtle

class StateMapper():
    #state mapping class to position state names on the map
    def __init__(self):
        #intitializing the turtle object
        self.obj = Turtle()
        self.obj.hideturtle()
        self.obj.color("black")
        self.obj.penup()

    def state_coordinates(self,user_guess,state_data):
        #func to get the x,y coordinates of a particular US state and return a tuple(x,y)
        row = state_data[state_data["state"] == user_guess].iloc[0]
        return row['x'],row['y']
    
    def map_state_position(self,coordinates,user_guess):
        #func to place the US state on the map using x,y coordinates
        self.obj.goto(coordinates)
        self.obj.write(f"{user_guess}",font=("roboto", 10, "normal"))



    
    
    