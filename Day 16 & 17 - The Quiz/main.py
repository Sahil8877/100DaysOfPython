from quiz_brain import Quiz

quiz = Quiz()

question_counter = 1

while question_counter <= quiz.total_questions:
    question = quiz.get_question(question_counter)
    user_ans = input(f"Q.{question_counter}: {question} (True or False) ? :").lower()
    if user_ans not in ["true","false"]:
        print("❌ Please type true or false. Try again.\n")

    elif quiz.answer_checker(quiz.question_answer.answer,user_ans):
        question_counter+=1
        print(f"\n{quiz.messages}")
    else:
        question_counter+=1
        print("\n🙈 You'r wrong!")
    print(f"👀 Your score is : {quiz.score}/{question_counter}\n")
    
print("\n🎉 You reached the end of the quiz!")
print(f"Your final score is : {quiz.score}/{quiz.total_questions}")
    
        