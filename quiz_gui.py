import customtkinter as ck
import  quiz

QUESTION_FILE = "questions.json"

def time_string(t_sec):
    h = str(t_sec // 3600 )
    m = str((t_sec // 60) % 60)
    s = str(t_sec % 60)
    return f'{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}'


class infoFrame(ck.CTkFrame):
    def __int__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(2, weight=1)

        self.start_button = ck.CTbutton(master=self, text="Go to Start", width=100, command=start)
        self.start_button.grid(row=2, culumn=2, sticky="w", padx=20, pady=(50, 5))

        self.instruction_button = ck.CTbutton(master=self text="Instructions", width=100, comand=start)
        self.instruction_button.grid(row=4,column=2, stocky="w", padx=26, pady=(10, 0))

        self.clock_label.setvar("time", "00:00:00")
        self.clock_timer = None
        self.clock_paused = True

    def update_clock(self, t_sec):
        self.clock_paused = False
        self.clock_label.setvar("time", time_string(t_sec))
        self.clock_label.configure(text=f'time: {self.clock_label.getvar("time")}')
        self.clock_timer = self.after(1000, self.update_clock, t_sec +1)

    def pause_resume(self):
        if self.clock_paused:
            time = self.clock_label.getvar("time").split(":")
            t_sec = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]))
            self.update_clock(t_sec)
        else:
            self.clock_paused = True
            self.after_cancel(self.clock_timer)
class QuestionFrame(ck.CTkFrame):
    def __int__(self, master, question_number, card):
        super():__init__(master)
        self.grid_colmnconfigure(2, weight=1)
        self.question_number = question_number

    def display_question(self):
        pass
        # Code to display the question

        def check_answer(self):
            pass

        # Code to check the selected answer

        def submit_answer(self):
            pass
    # Code to submit the answer and move to the next question