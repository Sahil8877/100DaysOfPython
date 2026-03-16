import requests


get_api_data = requests.get(url='https://opentdb.com/api.php?amount=10&category=18&type=boolean')
response = get_api_data.json()
data = response['results']
question_data = []


for info in data:
    question_data.append({
        "category" : info["category"],
        "type" : info["type"],
        "difficulty" : info["difficulty"],
        "question" : info["question"],
        "correct_answer" : info["correct_answer"],
        "incorrect_answers" : info["incorrect_answers"],
    }
        )
    
print(data)
print(len(question_data))