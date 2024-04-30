from tkinter import *
from quiz_brain import QuizBrain

# Constants
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("350x550+500+200") # width x height + x_offset + y_offset
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score} / {self.quiz.question_number}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic")) # With width=280, the text will wrap at the edge of the canvas
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.canvas.config(bg="white")

    def true_pressed(self):
        self.update_score(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.update_score(self.quiz.check_answer("False"))

    def update_score(self, question_result: bool):
        if question_result:
            self.canvas.config(bg="#66CC33")
        else:
            self.canvas.config(bg="#FF3300")

        self.score_label.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number}")
        self.window.after(1000, self.get_next_question)