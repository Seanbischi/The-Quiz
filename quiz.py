import json


def init():
    with open("questions.json", "r") as f:
        questions = json.load(f)
    score = 0


def ask_questions():
    pass


def final():
    pass


if __name__ == "__main__":
    init()
    ask_questions()
    final()
