import json
import tkinter as tk
from tkinter import messagebox as msg

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.questions, self.score = self.init()
        self.index = 0
        self.correct_answer = None

        # Creating GUI components
        self.question_label = tk.Label(master, text="")
        self.question_label.pack()
        self.var = tk.IntVar()
        self.option_buttons = []
        for i in range(3):
            button = tk.Radiobutton(master, text="", variable=self.var, value=i)
            button.pack()
            self.option_buttons.append(button)
        self.check_button = tk.Button(master, text="Check", command=self.check_answer)
        self.check_button.pack()
        self.score_label = tk.Label(master, text=f'Score: {self.score}')
        self.score_label.pack()

        # Display the first question
        self.display_question()

    def init(self):
        with open("questions.json", "r") as f:
            questions = json.load(f)
        score = 0
        return questions, score

    def display_question(self):
        q = self.questions[self.index]
        self.question_label.config(text=q["question"])
        for i, opt in enumerate(q["options"]):
            self.option_buttons[i].config(text=opt["text"])
            if opt["correct"]:
                self.correct_answer = i
        self.var.set(-1)

    def check_answer(self):
        if self.var.get() == self.correct_answer:
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
            msg.showinfo("Correct", "Die gegebene antowort ist Korekt !")
        else:
            msg.showerror("Incorrect", "Die gegebene antwort ist falsch!")

        self.index += 1
        if self.index < len(self.questions):
            self.display_question()
        else:
            msg.showinfo("End", "The quiz has ended!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz App")
    app = QuizApp(root)
    root.mainloop()

