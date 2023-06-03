import json


def init():
    with open("questions.json", "r") as f:
        questions = json.load(f)
    score = 0
    return questions, score


def ask_questions():
    pass


def final():
    pass


if __name__ == "__main__":
    my_questions, my_score = init()
    ask_questions()
    final()
