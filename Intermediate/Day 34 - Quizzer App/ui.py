THEME_COLOR = "#375362"
from tkinter import *

class QuizUI:

    def __init__(self, quiz):

        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.minsize(width=400, height=700)
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.total_score_counter = 0
        self.total_score_counter_label = Label(text=f"Your Score : {self.total_score_counter}/{self.quiz.question_number}",highlightthickness=0,bg=THEME_COLOR,font=("Arial", 20, "italic"))
        self.total_score_counter_label.grid(row=0,column=1)
        # Canvas
        self.canvas = Canvas(width=400, height=400, bg="white", highlightthickness=0)
        self.q_text = self.canvas.create_text(
            200,
            200,
            width=350,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1,column=1,pady=50)

        self.wrong_btn_img = PhotoImage(file='Day 34 - Quizzer App/images/false.png')
        self.correct_btn_img = PhotoImage(file='Day 34 - Quizzer App/images/true.png')

        # Buttons
        self.wrong_btn = Button(
            image=self.wrong_btn_img,
            highlightthickness=0,
            command=self.wrong_btn_pressed
        )
        self.wrong_btn.grid(row=2,column=1,sticky="w")

        self.correct_btn = Button(
            image=self.correct_btn_img,
            highlightthickness=0,
            command=self.correct_btn_pressed
        )
        self.correct_btn.grid(row=2,column=1,sticky="e")

        self.get_next_question()

        self.window.mainloop()

    # ---------------------------- BUTTONS ---------------------------- #

    def wrong_btn_pressed(self):
        result = self.quiz.check_answer("False")
        if result:
            self.total_score_counter += 1
        self.total_score_counter_label.config(text=f"Your Score : {self.total_score_counter}/{self.quiz.question_number}",highlightcolor="white",font=("Arial", 20, "italic"))
        self.give_feedback(result)

    def correct_btn_pressed(self):
        result = self.quiz.check_answer("True")
        if result:
            self.total_score_counter += 1
        self.total_score_counter_label.config(text=f"Your Score : {self.total_score_counter}/{self.quiz.question_number}",highlightcolor="white",font=("Arial", 20, "italic"))
        self.give_feedback(result)

    # ---------------------------- LOGIC ---------------------------- #

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


    def get_next_question(self):
        self.canvas.config(bg="white")
        self.window.after_cancel(self.window)
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=question_text)
        else:
            self.canvas.itemconfig(self.q_text, text=f"You've completed the quiz!\nYou got : {self.total_score_counter}/{self.quiz.question_number} correct!")
            self.wrong_btn.config(state="disabled")
            self.correct_btn.config(state="disabled")
