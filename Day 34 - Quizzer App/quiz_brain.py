import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = 0
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question_object = self.question_list[self.question_number]
        
        self.question_number += 1
        self.current_question = question_object
        print("q :",self.current_question.text)
        return html.unescape(question_object.text)

    
    def total_score(self,check):
        if check:
            self.score += 1
            res = self.score
        return res


    def check_answer(self, user_answer):

        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.total_score(True)
            print("You got it right!")
            return True
        else:
            print("That's wrong.")
            return False