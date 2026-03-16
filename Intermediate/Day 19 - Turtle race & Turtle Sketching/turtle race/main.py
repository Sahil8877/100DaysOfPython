from turtle_race import Turtle

#insert list of colors to start racing ith turtles
turtle_colors = ["red","blue","green","purple","maroon"]
turtles = Turtle(turtle_colors)
screen = turtles.screen
screen.setup(width=600,height=700)
                  
user_color_bet = turtles.color_bet(turtle_colors)
winner = turtles.start_race()
if winner == user_color_bet:
    print(f"\nCongrats! {turtles.winning_turtle_color.title()} Won.\n")
else:
    print(f"\nSorry you lose! {turtles.winning_turtle_color.title()} Won.\n")

screen.exitonclick()









