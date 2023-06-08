import json


def init():
    with open("questions.json", "r") as f:
        questions = json.load(f)
    score = 0
    return questions, score


def ask_questions(questions, score):
    for q_index in range(len(questions)):
        print(questions[q_index]["question"])
        for o_index in range(len(questions[q_index]["options"])):
            print(f'{o_index + 1}: {questions[q_index]["options"][o_index]["text"]}')
        answer = int(input(f'Bitte geben sie eine korekte antwort.'))
        if questions[q_index]["options"][answer - 1]["correct"]:
            score += 1
        print(f'\n')
        print(f'Ihren momentan Punkteanzahl ist : {score}\n')








def final():
    pass


if __name__ == "__main__":
    my_questions, my_score = init()
    ask_questions(my_questions, my_score)
    final()
