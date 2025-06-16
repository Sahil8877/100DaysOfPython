from turtle import Turtle
import random

class Car_Manager():
    def __init__(self):
        """
        list_of_cars: list to store the turtle (car) objects
        Y_CORDS: Y cordinates to define strict lanes for objects to move
        NUM_OF_CARS: Setting num of car objects to create
        """
        self.list_of_cars = []
        self.Y_CORDS = [200,150,100,50,20,-20,-50,-100,-150,-200]
        self.NUM_OF_CARS = 30

    def random_colors(self):
        """
        return random r,g,b values (30 to 235) as a tuple
        """
        r=random.randint(30,235)
        g=random.randint(30,235)
        b=random.randint(30,235)
        return r,g,b
    
    def car_generator(self):
        """
        Generates car objects and stores it in a list called list_of_cars
        """
        #stores previous distance between turtle object to spread objects evenly on x axis
        self.distance_between_objects = 0 
        for _ in range(self.NUM_OF_CARS):
            car = Turtle()
            
            car.shape("square")
        
            #random colors for ech turtle object
            car.color(self.random_colors())
        
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.penup()
            # selecting fixed random lanes for each object to avoid overlapping
            random_lane = random.choice(self.Y_CORDS)
            #set turtle object position using distance from previous object - 60
            car.goto(self.distance_between_objects - 60,random_lane)
            self.list_of_cars.append(car)
            #storing current object x cordinate to use as a distance 
            self.distance_between_objects = car.xcor()
                

    def car_moving(self):
        """
        method to move turtle objects from left to right with 10 steps
        """
        for cars in self.list_of_cars:
            cars.forward(10)           
            if cars.xcor() > 250:
                # if all turtle objects move beyond 250 on x cordinate then 
                # reverse their x cordinates to positives for reusing the turtle objects
                # by setting their x axis back to previous positions with random y cordinates

                #generate random lane from fixed y cordinates
                random_lane = random.choice(self.Y_CORDS)
                #reset object positions on random lanes
                cars.goto(self.distance_between_objects,random_lane)
                cars.color(self.random_colors())
                
                    
            

        



    
