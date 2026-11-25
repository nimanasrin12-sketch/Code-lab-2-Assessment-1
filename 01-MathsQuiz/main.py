import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Code Lab 2 - Assessment 1
# Project 1: Maths Quiz

NAVY = "#172554"
LIGHT_GREY = "#F0F4F8"
WHITE = "#FFFFFF"
GREEN = "#239B56"
ORANGE = "#E67E22"
RED = "#C0392B"
FONT = "Times New Roman"

root = tk.Tk()
root.title("MATHS QUIZ")
root.geometry("650x700")
root.resizable(True, True)

backgroundOriginal = Image.open("maths_background.png")
backgroundLabel = tk.Label(root)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

backgroundPhoto = None

def resizeBackground(event=None):
    global backgroundPhoto

    width = root.winfo_width()
    height = root.winfo_height()

    if width > 1 and height > 1:
        image = backgroundOriginal.resize(
            (width, height), Image.Resampling.LANCZOS
        )
        backgroundPhoto = ImageTk.PhotoImage(image)
        backgroundLabel.config(image=backgroundPhoto)
        backgroundLabel.lower()

root.bind("<Configure>", resizeBackground)
root.after(100, resizeBackground)

questionNumber = 0
score = 0
attempts = 0
correctAnswer = 0
selectedDifficulty = ""
quizFinished = False

def showPage(page):
    for frame in [homeFrame, difficultyFrame, quizFrame, resultFrame]:
        frame.place_forget()

    page.place(relx=0.5, rely=0.5, anchor="center")

def startQuiz():
    showPage(difficultyFrame)

def selectDifficulty(level):
    global selectedDifficulty, questionNumber, score, attempts, quizFinished

    selectedDifficulty = level
    questionNumber = 0
    score = 0
    attempts = 0
    quizFinished = False

    showPage(quizFrame)
    displayProblem()

def backToDifficulty():
    global questionNumber, score, attempts, quizFinished

    questionNumber = 0
    score = 0
    attempts = 0
    quizFinished = True
    answerEntry.delete(0, tk.END)

    showPage(difficultyFrame)

def getNumberRange():
    if selectedDifficulty == "Easy":
        return 1, 9
    elif selectedDifficulty == "Hard":
        return 10, 99
    return 1000, 9999

def updateProgress():
    progressLabel.config(
        text=f"QUESTION {questionNumber} OF 10     |     SCORE: {score}/100"
    )

def displayProblem():
    global questionNumber, attempts, correctAnswer

    if questionNumber == 10:
        displayResults()
        return

    questionNumber += 1
    attempts = 0

    minimum, maximum = getNumberRange()

    number1 = random.randint(minimum, maximum)
    number2 = random.randint(minimum, maximum)
    operation = random.choice(["+", "-"])

    if operation == "+":
        correctAnswer = number1 + number2
    else:
        correctAnswer = number1 - number2

    questionLabel.config(
        text=f"{number1} {operation} {number2} = ?"
    )

    answerEntry.delete(0, tk.END)
    feedbackLabel.config(text="")
    updateProgress()
    answerEntry.focus_set()

def checkAnswer():
    global score, attempts

    if quizFinished:
        return

    answer = answerEntry.get().strip()

    try:
        userAnswer = int(answer)
    except ValueError:
        messagebox.showwarning(
            "Invalid Answer",
            "Please enter a whole number."
        )
        return

    attempts += 1

    if userAnswer == correctAnswer:
        if attempts == 1:
            score += 10
            feedbackLabel.config(text="Correct! +10 marks", fg=GREEN)
        else:
            score += 5
            feedbackLabel.config(text="Correct! +5 marks", fg=GREEN)

        root.after(700, displayProblem)

    elif attempts < 2:
        feedbackLabel.config(
            text="Incorrect! Try one more time.",
            fg=ORANGE
        )
        answerEntry.delete(0, tk.END)
        answerEntry.focus_set()
    else:
        feedbackLabel.config(
            text=f"Incorrect! The answer was {correctAnswer}.",
            fg=RED
        )
        root.after(1200, displayProblem)

def displayResults():
    global quizFinished

    quizFinished = True

    if score >= 90:
        grade = "A+"
        comment = "Excellent!"
    elif score >= 80:
        grade = "A"
        comment = "Very Good!"
    elif score >= 70:
        grade = "B"
        comment = "Good!"
    elif score >= 60:
        grade = "C"
        comment = "Average"
    elif score >= 50:
        grade = "D"
        comment = "Pass"
    else:
        grade = "F"
        comment = "Needs Improvement"

    resultScoreLabel.config(text=f"Your Score: {score}/100")
    gradeLabel.config(text=f"Grade: {grade}")
    commentLabel.config(text=comment)

    showPage(resultFrame)

def replayQuiz():
    showPage(difficultyFrame)

# Home Page

homeFrame = tk.Frame(root, bg=LIGHT_GREY, padx=45, pady=50)

tk.Label(
    homeFrame,
    text="MATHS QUIZ",
    font=(FONT, 32, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
).pack(pady=(10, 25))

tk.Label(
    homeFrame,
    text="WELCOME!",
    font=(FONT, 23, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
).pack(pady=10)

tk.Label(
    homeFrame,
    text="Challenge yourself and test your maths skills!",
    font=(FONT, 12),
    bg=LIGHT_GREY,
    fg=NAVY
).pack(pady=(5, 30))

tk.Button(
    homeFrame,
    text="START QUIZ",
    font=(FONT, 14, "bold"),
    bg=GREEN,
    fg=WHITE,
    activebackground="#1E8449",
    activeforeground=WHITE,
    width=18,
    pady=12,
    relief="flat",
    cursor="hand2",
    command=startQuiz
).pack(pady=15)

# Difficulty Page

difficultyFrame = tk.Frame(root, bg=LIGHT_GREY, padx=55, pady=40)

tk.Label(
    difficultyFrame,
    text="CHOOSE YOUR DIFFICULTY",
    font=(FONT, 22, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
).pack(pady=(10, 30))

for level, colour in [
    ("Easy", GREEN),
    ("Hard", ORANGE),
    ("Extreme", RED)
]:
    tk.Button(
        difficultyFrame,
        text=level.upper(),
        font=(FONT, 14, "bold"),
        bg=colour,
        fg=WHITE,
        width=18,
        pady=10,
        relief="flat",
        cursor="hand2",
        command=lambda choice=level: selectDifficulty(choice)
    ).pack(pady=10)

tk.Button(
    difficultyFrame,
    text="BACK",
    font=(FONT, 11, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=12,
    pady=8,
    relief="flat",
    cursor="hand2",
    command=lambda: showPage(homeFrame)
).pack(pady=(25, 5))

# Quiz Page

quizFrame = tk.Frame(root, bg=LIGHT_GREY, padx=45, pady=35)

tk.Label(
    quizFrame,
    text="MATHS QUIZ",
    font=(FONT, 25, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
).pack(pady=(5, 20))

progressLabel = tk.Label(
    quizFrame,
    text="QUESTION 0 OF 10",
    font=(FONT, 12, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
)
progressLabel.pack(pady=10)

questionLabel = tk.Label(
    quizFrame,
    text="",
    font=(FONT, 28, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
)
questionLabel.pack(pady=30)

answerEntry = tk.Entry(
    quizFrame,
    font=(FONT, 18),
    justify="center",
    width=15
)
answerEntry.pack(pady=10)

feedbackLabel = tk.Label(
    quizFrame,
    text="",
    font=(FONT, 12, "bold"),
    bg=LIGHT_GREY
)
feedbackLabel.pack(pady=15)

tk.Button(
    quizFrame,
    text="SUBMIT ANSWER",
    font=(FONT, 12, "bold"),
    bg=GREEN,
    fg=WHITE,
    width=18,
    pady=10,
    relief="flat",
    cursor="hand2",
    command=checkAnswer
).pack(pady=10)

tk.Button(
    quizFrame,
    text="BACK",
    font=(FONT, 11, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=12,
    pady=8,
    relief="flat",
    cursor="hand2",
    command=backToDifficulty
).pack(pady=15)

# Results Page

resultFrame = tk.Frame(root, bg=LIGHT_GREY, padx=55, pady=45)

tk.Label(
    resultFrame,
    text="QUIZ COMPLETED!",
    font=(FONT, 25, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
).pack(pady=20)

resultScoreLabel = tk.Label(
    resultFrame,
    text="",
    font=(FONT, 20, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
)
resultScoreLabel.pack(pady=15)

gradeLabel = tk.Label(
    resultFrame,
    text="",
    font=(FONT, 18, "bold"),
    bg=LIGHT_GREY,
    fg=GREEN
)
gradeLabel.pack(pady=10)

commentLabel = tk.Label(
    resultFrame,
    text="",
    font=(FONT, 16),
    bg=LIGHT_GREY,
    fg=NAVY
)
commentLabel.pack(pady=10)

tk.Button(
    resultFrame,
    text="PLAY AGAIN",
    font=(FONT, 13, "bold"),
    bg=GREEN,
    fg=WHITE,
    width=18,
    pady=10,
    relief="flat",
    cursor="hand2",
    command=replayQuiz
).pack(pady=25)

tk.Button(
    resultFrame,
    text="HOME",
    font=(FONT, 11, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=12,
    pady=8,
    relief="flat",
    cursor="hand2",
    command=lambda: showPage(homeFrame)
).pack(pady=5)

showPage(homeFrame)

root.mainloop()