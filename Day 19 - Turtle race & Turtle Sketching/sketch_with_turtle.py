import turtle as t
turtle = t.Turtle()
screen = t.Screen()
screen.listen()

def forward():
    turtle.forward(20)

def backward():
    turtle.backward(20)

def right():
    turtle.right(15)

def left():
    turtle.left(15)

def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

#press W to go forward
screen.onkeypress(forward,"w")
#press S to go backward
screen.onkeypress(backward,"s")
#press A to go left
screen.onkeypress(left,"a")
#press D to go right
screen.onkeypress(right,"d")
#press C to clear drawing and go to starting position
screen.onkeypress(clear_screen,"c")

screen.exitonclick()