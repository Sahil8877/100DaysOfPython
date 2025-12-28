
import turtle as t
import random
class Turtle:
    def __init__(self,turtle_colors):
        """
        creates multiple turtle objects by iterating over the user defined colors list
        """
        self.winning_turtle = ""
        self.turtle_colors = turtle_colors
        self.turtle_dict = {}
        for color_of_turtle in self.turtle_colors:
            turtle_obj = t.Turtle(shape="turtle")
            turtle_obj.color(f"{color_of_turtle}")
            self.turtle_dict[color_of_turtle] = turtle_obj
        self.screen = t.Screen()
        self.screen.listen()  
        
    def color_bet(self,turtle_colors):
        """
        keeps prompting user to bet on a color from the turtles list,
        returns the color user has bet on
        """
        while True:
            self.user_bet = self.screen.textinput(title="Bet on a your fav turtle",prompt="Enter the turtle color here :").lower()
            if self.user_bet in turtle_colors:
                return self.user_bet 
            else:
                print("Sorry! incorrect color input!")
                pass

    def winner_bg_color(self):
        """
        change the wining turtles color as bg
        """
        self.screen.bgcolor(self.winning_turtle_color)

    def start_race(self):
        """
        creates a turtle_obj list and randomly selectes one turtle_obj from list to move forward,
        returns the color of the turtle_obj
        """
        ycor = 10*len(self.turtle_dict)
        self.turtle_list = []
        for color,turtle_obj in self.turtle_dict.items():
            turtle_obj.penup()
            turtle_obj.goto(-290,ycor)
            ycor -= 30
            self.turtle_list.append(turtle_obj)

        while self.winning_turtle == "":            
            self.random_turtle_from_list = random.choice(self.turtle_list)            
            self.turtle_currently_moving = self.random_turtle_from_list.forward(random.randint(1,6))
            self.turtle_xcor = self.random_turtle_from_list.xcor()
            if self.turtle_xcor > 285:
                self.winning_turtle_color = ""
                for color, turtle_obj in self.turtle_dict.items():
                    if self.random_turtle_from_list == turtle_obj:
                        self.winning_turtle_color = color
                        break

                self.winner_bg_color()
                return self.winning_turtle_color

                
  