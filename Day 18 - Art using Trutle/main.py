import turtle as t
import random

turtle = t.Turtle()
turtle.shape("classic")
turtle.shapesize(1)
window = t.Screen()
window.canvheight = 1


def random_colors():
    """
    random color generator using r,g,b scales and then returning a tuple
    """
    t.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

def shapes(sides):
    """
    draw different shapes with sides from 3 to 10
    """
    angle = 360/sides
    for _ in range(sides):
        turtle.color(random_colors())
        turtle.forward(100)
        turtle.left(angle)
def start_drawing_shapes():
    """
    start drawing shapes using `shapes(sides)` function
    """
    for _ in range (3,11):
        shapes(_)


def random_walk(step):
    """
    random walk simulation which selects a random heading/direction and moves towards it in a fixed length
    """
    directions = [0, 90, 180, 270] 
    turtle.speed(0)
    for i in range(200):
        turtle.pencolor(random_colors())
        pos = random.choice(directions)
        turtle.setheading(pos)
        turtle.pensize(10)
        turtle.forward(step)

def circle(tilt):
    """
    draws circle on a fixed point until it completes a 360 loop
    """
    turtle.speed(0)
    for i in range(int(360/tilt)):
        turtle.pensize(2)
        turtle.pencolor(random_colors())
        turtle.circle(100)
        turtle.left(tilt)
       
        
def art():
    """
    creates a art using dots
    """
    window.colormode(255)
    #colours list with r,g,b values
    rgb_colors = [ (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-240,240)
    for _ in range(10):
        for i in range(10):
            turtle.pendown()
            turtle.pencolor(random.choice(rgb_colors))
            turtle.dot(20)
            turtle.penup()
            turtle.forward(50)
            turtle.pendown()
        turtle.penup()
        
        turtle.goto(-240,turtle.ycor()-50)

##uncomment any function to draw using Turtle

# art()
# start_drawing_shapes()
# random_walk(20)

window.exitonclick()