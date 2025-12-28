from tkinter import *
import math

WORK = 2 #work time in minutes
SHORT_BREAK = 5 #short break in minutes
LONG_BREAK = 25 #long break in minutes
BG = "light goldenrod" #BG for components
TOTAL_WORK_SESSIONS = 8 #num of work sessions
timer_id = None
break_id = None
session_counter = 0

def break_counter(seccount):
    global session_counter
    if seccount < 0:
        if session_counter > 0:
            timer_label.config(text="Timer")
            sec_counter(WORK * 60)        
        return
    minutes = math.floor((seccount) / 60)
    seconds = seccount % 60

    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes} : {seconds}")
    global break_id 
    break_id = window.after(1000, break_counter, seccount-1)
    
def sec_counter(seccount):
    global session_counter
    if seccount < 0:
        session_counter += 1
        if session_counter == TOTAL_WORK_SESSIONS:
            timer_label.config(text="Done")
            return
        ticks = tick_label["text"]
        tick_label.config(text=ticks+"✔️")
        timer_label.config(text="Break")
        
        if session_counter % 4 == 0:
            print(session_counter)
            break_counter(LONG_BREAK * 60)
        else:
            print(session_counter)
            break_counter(SHORT_BREAK * 60)   
        return

    minutes = math.floor(seccount / 60)
    seconds = seccount % 60

    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes} : {seconds}")
    global timer_id 
    timer_id = window.after(30, sec_counter, seccount-1)
    

def start_button_click():
    sec_counter(WORK * 60)
    
def reset_button_click():
    canvas.itemconfig(timer_text,text=f"{WORK} : 00")
    global timer_id, break_id, session_counter
    session_counter = 0
    tick_label.config(text="")
    timer_label.config(text="Timer")
    if timer_id:
        window.after_cancel(timer_id)
    if break_id:
        window.after_cancel(break_id)


window = Tk()
window.title("Pomodoro!")
window.config(bg=BG,padx=200,pady=100)

timer_label = Label(text=f"Timer",font=("Arial",20,"bold"),foreground="green",background=BG)
timer_label.grid(column=1,row=0)

pomodoro_img = PhotoImage(file="./pomodoro.png")

canvas = Canvas(width=200,height=223,bg=BG, highlightthickness=0)
canvas.create_image(100,110,image=pomodoro_img)

timer_text = canvas.create_text(100,125,text=f"25 : 00",font=("Arial",20,"bold"))

canvas.grid(column=1,row=1)

start_button = Button(text="Start",highlightbackground=BG,command=start_button_click)
start_button.grid(column=0,row=3)

reset_button = Button(text="Reset",highlightbackground=BG,command=reset_button_click)
reset_button.grid(column=2,row=3)

tick_label = Label(text="",font=("Arial",20,"bold"),bg=BG)
tick_label.grid(columnspan=3,rowspan=1)

window.mainloop()