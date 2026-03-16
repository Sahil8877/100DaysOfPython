import pandas as pd
from tkinter import *
from tkmacosx import Button
import random

window = Tk()
window.minsize(width=500,height=500)
window.title("Flashcards")
window.config(bg="black",padx=50,pady=50)

load_quiz_data = pd.read_csv('questions.csv')
load_quiz_data = load_quiz_data.sample(frac=1).reset_index(drop=True)

class QuizBrain:
    def __init__(self):
        self.card = Canvas(window,width=500,height=300,bg='orange',highlightthickness=0)   
        self.card.grid(row=0,column=0)
        self.quiz_bank = list(zip(load_quiz_data.q,load_quiz_data.a))
        self.incorrect_q_tracker = []
        self.disp_answer = False
        self.quiz_over = False
        self.shuffler(self.quiz_bank)
        self.q_generator()
        self.q_card()
           
    def shuffler(self,quiz_bank):
        random.shuffle(quiz_bank)

    def q_generator(self):
        if len(self.quiz_bank) != 0:
            self.random_set = self.quiz_bank.pop()
            
        elif len(self.incorrect_q_tracker) != 0:
            self.shuffler(self.incorrect_q_tracker)
            self.random_set = self.incorrect_q_tracker.pop()
        else:
            self.quiz_over = True
            return
        self.random_q = self.random_set[0]

    def show_answer(self):

        if self.quiz_over:
            exit()

        if not self.disp_answer:
            self.card.delete("all")
            self.disp_answer = True
            show_answer_btn.configure(text="SHOW QUESTION")
            self.card.config(bg="green")
            self.card.create_text(250,150,text=f"{self.random_set[1]}",font=("helvetica",30,"bold")) 
        else:
            show_answer_btn.configure(text="SHOW ANSWER")
            self.disp_answer = False
            self.q_card()

    def correct_btn(self):
        if self.disp_answer:
            show_answer_btn.configure(text="SHOW ANSWER")
            self.q_generator()
            self.q_card()
            self.disp_answer = False

    def q_card(self):
        self.card.delete("all")
        if not self.quiz_over:
            self.card.config(bg="orange")
            self.card.create_text(250,125,text=f"Python Quiz",font=("courier",15,"italic"),fill="black")
            self.card.create_text(250,150,text=f"{self.random_q}",font=("helvetica",15,"bold"),fill="black")
        else:
            show_answer_btn.configure(text="Exit Now")
            self.card.create_text(250,150,text=f"You have finished all the cards.",font=("helvetica",20,"bold"),fill="white")            

    def incorrect_btn(self):
        if self.disp_answer:
            show_answer_btn.configure(text="SHOW ANSWER")
            self.incorrect_q_tracker.append(self.random_set)
            self.q_generator()
            self.q_card()
            self.disp_answer = False

quiz = QuizBrain()

#--------------------buttons--------------------#

correct_btn_img = PhotoImage(file='./correct_btn.png')
incorrect_btn_img = PhotoImage(file='./incorrect_btn.png')

show_answer_btn = Button(font=("helvetica",15,),text="SHOW ANSWER",command=quiz.show_answer,width=255,height=40,bg="white")
show_answer_btn.grid(column=0,row=3,sticky="ew")

correct_btn = Button(command=quiz.correct_btn,image=correct_btn_img,height=55,width=250,highlightthickness=0,borderwidth=0,relief='flat',bg="white")
correct_btn.grid(column=0,row=1,sticky="e")

incorrect_btn = Button(command=quiz.incorrect_btn,image=incorrect_btn_img,height=55,width=250,highlightthickness = 0,borderwidth=0,relief = 'flat',bg="white")
incorrect_btn.grid(column=0,row = 1, sticky="w")

window.mainloop()