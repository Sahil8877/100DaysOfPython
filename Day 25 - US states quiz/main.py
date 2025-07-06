from turtle import Turtle, Screen
import pandas as pd
from map import StateMapper
from data_checker import DataChecker
from scoreboard import Score

#file paths for bg image an state data
bg_image_path = "./Day 25/blank_states_img.gif"
US_state_df = pd.read_csv("./Day 25/50_states.csv")

#writer turtle object for writing in game intructions
writer_obj = Turtle()
writer_obj.hideturtle()
writer_obj.penup()
writer_obj.pencolor("red")

#intialize classes 
score = Score()
state_mapper = StateMapper()
verify_user_guess = DataChecker()

#intialize the screen class with title, and bg image
screen = Screen()
screen.title("US states quiz")
screen.setup(710,580)
screen.addshape(bg_image_path)

#intialize turtle object for the bg image on screen
turtle_obj = Turtle()
turtle_obj.shape(bg_image_path)

#list to store correct guesses
guessed_states = []

playing = True

while playing:
    #user input
    user_guess = screen.textinput("Can you guess all the states in US ?","Type your answers below :").title().strip()

    if verify_user_guess.check_user_guess(user_guess,US_state_df):
        #check if user input exists in the US state names df
        if user_guess not in guessed_states and len(guessed_states) < 51:
            #check if the US state isn't already guessed and the guessed states list is < 51
            writer_obj.clear()
            #get x,y coordinates from the state_mapper class
            coordinates = state_mapper.state_coordinates(user_guess,US_state_df)
            #set the US state name position onto the map using the coordinates
            state_mapper.map_state_position(coordinates,user_guess)
            #update the current user score
            score.update_current_score()
            #store the new US state into the guessed state list
            guessed_states.append(user_guess)

        elif user_guess in guessed_states:
            #if the US state was already guessed show error message
            writer_obj.clear()
            writer_obj.goto(0,-270)
            writer_obj.write(f"Sorry! You already guessed {user_guess}.",align='center',font=("roboto", 15, "normal"))

        elif len(guessed_states) == 50:
            #if the user has guessed all the states show message in green
            writer_obj.clear()
            writer_obj.goto(0,-270)
            writer_obj.pencolor('green')
            writer_obj.write(f"Congrats! You guessed it all.",align='center',font=("roboto", 20, "normal"))
    else:
        #if the input is not in the US state df show error
        writer_obj.clear()
        writer_obj.goto(0,-274)
        writer_obj.write(f"Sorry! Looks like an invalid input : '{user_guess}'.",align='center',font=("roboto", 15, "normal"))

screen.exitonclick()