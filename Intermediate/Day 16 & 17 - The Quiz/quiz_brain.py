from data_bank import questions,messages
from random import choice
from question import Question

class Quiz:
    def __init__(self):
        self.score = 0
        self.total_questions = len(questions)
        self.messages = choice(messages)
        print("\nThis is QuizTrivia! 🌏 🌴\n")

    def get_question(self,question_num):
        
        self.question_answer = Question(questions[question_num]["question"],questions[question_num]["ans"])
        return self.question_answer.question
    
    def answer_checker(self,ans,user_ans):
        if str(ans).lower() == user_ans.lower():
            self.score += 1
            return True
        return False


        

