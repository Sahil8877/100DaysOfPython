from turtle import Turtle,Screen
import random

class SnakeGame:
    def __init__(self):
        
        self.screen = Screen()
        self.screen.title("Snake Island!")
        self.screen.bgcolor("black")
        #turn animation off
        self.screen.tracer(0)
        #set innitial size,speed,time
        self.INITIAL_SIZE = 2
        self.INITIAL_SPEED = 10
        self.DELAY = 0.1
        self.current_speed = self.INITIAL_SPEED        
        self.snake_body = []
        self.score_obj = Turtle()
        self.high_score_obj = Turtle()
        self.score = 0
        # high_score = 0


        # with open("Day 20 & 21- Snake Game with Turtle/high_scores.txt", "w") as high_score_file:
   
        #     high_score_file.write(str(high_score))
        with open("Day 20 & 21- Snake Game with Turtle/high_scores.txt", "r") as high_score_file:
            high_score = high_score_file.read()
        
        #create high score turtle object
        self.high_score = int(high_score)
        self.high_score_obj.clear()
        self.high_score_obj.hideturtle()
        self.high_score_obj.pencolor("white")
        self.high_score_obj.penup()
        self.high_score_obj.setpos(200,270)
        self.high_score_obj.pendown()

        self.update_high_score()
        
        #create turtle object for food
        self.curr_food = Turtle("circle")
        self.food_colors = ["red","green","blue","maroon","orange","yellow","brown","purple","white","magenta"]
        self.curr_food.shapesize(0.5,0.5)
        self.curr_food.color(random.choice(self.food_colors))
        self.curr_food.penup()
        self.curr_food.goto(random.randint(-260,260),random.randint(-260,260))
    
    def create_snake(self):
        xcor_for_head = 0

        #create the initial snake body objects
        for _ in range(self.INITIAL_SIZE):
            snake = Turtle("square")
            snake.penup()
            snake.hideturtle()
            snake.color("white")
            snake.goto(xcor_for_head,0)
            snake.showturtle()
            self.snake_body.append(snake)
            xcor_for_head -= 20

    def add_snake_body(self):
        """
        To add new segments behind previous segments of snake body
        """
        self.screen.tracer(0)
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(self.snake_body[-1].xcor(),self.snake_body[-1].ycor())
        self.snake_body.append(new_body)


    def move(self):
        """
        To move all body segments forward
        """
        for idx in range(len(self.snake_body)-1,0,-1):
            self.snake_body[idx].goto(self.snake_body[idx-1].xcor(),self.snake_body[idx-1].ycor())
        self.snake_body[0].forward(self.current_speed)
    
    
   
    def right(self):
        """
        Function to go right
        """
        if self.snake_body[0].heading() == 90 or self.snake_body[0].heading() == 270:
            self.snake_body[0].setheading(0)


    def left(self):
        """
        Function to go left
        """
        if self.snake_body[0].heading() == 90 or self.snake_body[0].heading() == 270:
            self.snake_body[0].setheading(180)


    def up(self):
        """
        Function to go up
        """
        if self.snake_body[0].heading() == 0 or self.snake_body[0].heading() == 180:
            self.snake_body[0].setheading(90)
    

    def down(self):
        """
        Function to go down
        """
        if self.snake_body[0].heading() == 0 or self.snake_body[0].heading() == 180:
            self.snake_body[0].setheading(270)


    def random_food_pos(self):
        """
        To randomly set position of food object
        """
        self.curr_food.hideturtle()
        self.curr_food.color(random.choice(self.food_colors))
        self.curr_food.goto(random.randint(-260,260),random.randint(-260,260))
        self.curr_food.showturtle()


    def check_food(self):
        """
        Function to check if the first segment of snake has touched the food object
        """
        if self.curr_food and self.curr_food.distance(self.snake_body[0]) < 15:
            print("reached")
            self.score+=1
            self.INITIAL_SIZE+=1
            self.DELAY *= 0.95
            self.add_snake_body()
            self.random_food_pos()
            self.score_tracker()
            
    def reset_snake(self):
        for body in self.snake_body:
            body.hideturtle()
        self.snake_body.clear()
        self.INITIAL_SPEED = 10
        self.INITIAL_SIZE = 2
        self.DELAY = 0.1
        
        self.create_snake()

    def check_body_collision(self):
        """
        Function to check collision between segments
        return True if collision detected
        """
        head = self.snake_body[0]
        if len(self.snake_body) > 3:
            for body in self.snake_body[1:]:
                if head.distance(body) < 5:
                    print("Collision detected")
                    self.score = 0
                    self.high_score_tracker()
                    self.score_tracker()

                    return True
        return False
    
    def check_wall_collision(self):
        """
        Fucntion to check if segments within the window 
        return True if collision detected
        """
        head = self.snake_body[0]
        # print(head.xcor())
        # print(head.ycor())
        if (head.xcor() < -280 or head.xcor() >= 280) or (head.ycor() <= -280 or head.ycor() >= 290) :
            print("Wall collision")
            self.score = 0
            self.high_score_tracker()
            self.score_tracker()
            return True
        return False
        
    def update_high_score(self):
        
        self.high_score_obj.clear()
        self.high_score_obj.write(f"High Score : {self.high_score}", align="center",font=("Courier", 16, "bold"))

    def high_score_tracker(self):
        """
        Function to display Game over text if segments collide with eachother or the window
        """
        if self.score > self.high_score:
            print('in')
            self.high_score = self.score
            with open("Day 20 & 21- Snake Game with Turtle/high_scores.txt",mode="w") as high_score_file:
                high_score_file.write(str(self.high_score))
    
            self.update_high_score()
        

    def score_tracker(self):
        """
        Function to display the score
        """
        self.score_obj.clear()
        self.score_obj.hideturtle()
        self.score_obj.pencolor("white")
        self.score_obj.penup()
        self.score_obj.setpos(-240,270)
        self.score_obj.pendown()
        self.score_obj.write(f"Score : {self.score}", align="center",font=("Courier", 16, "bold"))
        
    
    
        
        
        




    




        
        

        

