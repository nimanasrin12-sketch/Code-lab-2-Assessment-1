
import tkinter as tk
import random
from tkinter import messagebox

# AI assistance acknowledgement:
# Tool: ChatGPT (OpenAI)
# Purpose: Assistance with developing and styling a Tkinter maths quiz.

# Colour theme
NAVY = "#172554"
LIGHT_GREY = "#F0F4F8"
WHITE = "#FFFFFF"

# Font settings
FONT = "Segoe UI"

# Create the main application window
root = tk.Tk()
root.title("Maths Quiz")
root.geometry("650x700")
root.resizable(True, True)
root.config(bg=LIGHT_GREY)

# Store quiz information
selectedDifficulty = ""
correctAnswer = 0
attempts = 0
questionNumber = 0
score = 0
quizFinished = True

# Application heading
heading = tk.Label(
    root,
    text="MATHS QUIZ",
    font=(FONT, 28, "bold"),
    bg=NAVY,
    fg=WHITE,
    pady=20
)
heading.pack(fill="x")

# Subtitle
subtitle = tk.Label(
    root,
    text="Test Your Mathematical Skills",
    font=(FONT, 12),
    bg=LIGHT_GREY,
    fg=NAVY
)
subtitle.pack(pady=12)

# Instructions
instruction = tk.Label(
    root,
    text="Choose Your Difficulty",
    font=(FONT, 14, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
)
instruction.pack(pady=8)

# Question counter
progressLabel = tk.Label(
    root,
    text="Question: 0 / 10     Score: 0",
    font=(FONT, 12, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
)
progressLabel.pack(pady=12)

# Question display
questionLabel = tk.Label(
    root,
    text="",
    font=(FONT, 24, "bold"),
    bg=WHITE,
    fg=NAVY,
    width=25,
    height=2
)
questionLabel.pack(pady=12)

# Answer input box
answerEntry = tk.Entry(
    root,
    font=(FONT, 18),
    justify="center",
    bg=WHITE,
    fg=NAVY,
    relief="solid",
    bd=1
)
answerEntry.pack(pady=12, ipadx=20, ipady=5)


# Function to generate random numbers
def randomInt(difficulty):

    if difficulty == "Easy":
        minimum = 1
        maximum = 9

    elif difficulty == "Moderate":
        minimum = 10
        maximum = 99

    else:
        minimum = 1000
        maximum = 9999

    number1 = random.randint(minimum, maximum)
    number2 = random.randint(minimum, maximum)

    return number1, number2


# Function to choose addition or subtraction
def decideOperation():

    return random.choice(["+", "-"])


# Function to calculate the correct answer
def isCorrect(number1, number2, operation):

    if operation == "+":
        return number1 + number2

    else:
        return number1 - number2


# Function to update the progress display
def updateProgress():

    progressLabel.config(
        text=f"Question: {questionNumber} / 10     Score: {score}"
    )


# Function to display a question
def displayProblem(level):

    global correctAnswer, attempts
    global questionNumber, quizFinished

    if questionNumber == 10:
        displayResults()
        return

    attempts = 0
    questionNumber += 1

    number1, number2 = randomInt(level)
    operation = decideOperation()

    correctAnswer = isCorrect(
        number1,
        number2,
        operation
    )

    questionLabel.config(
        text=f"{number1} {operation} {number2} = ?"
    )

    answerEntry.delete(0, tk.END)
    answerEntry.focus()

    updateProgress()


# Function to check the submitted answer
def checkAnswer():

    global attempts, score

    if quizFinished:
        return

    try:
        userAnswer = int(answerEntry.get())

        if userAnswer == correctAnswer:

            if attempts == 0:
                score += 10
                message = "Correct! You earned 10 marks."

            else:
                score += 5
                message = "Correct on your second attempt! You earned 5 marks."

            messagebox.showinfo("Correct Answer", message)

            updateProgress()
            displayProblem(selectedDifficulty)

        else:

            attempts += 1

            if attempts == 1:

                messagebox.showwarning(
                    "Try Again",
                    "Incorrect answer. You have one more attempt."
                )

                answerEntry.delete(0, tk.END)

            else:

                messagebox.showinfo(
                    "Incorrect Answer",
                    f"The correct answer is {correctAnswer}. You earned 0 marks."
                )

                displayProblem(selectedDifficulty)

    except ValueError:

        messagebox.showwarning(
            "Invalid Input",
            "Please enter a whole number."
        )


# Function to display final results
def displayResults():

    global quizFinished

    quizFinished = True

    questionLabel.config(text="QUIZ COMPLETED!")

    answerEntry.pack_forget()
    submitButton.pack_forget()

    if score >= 90:
        grade = "A+"
        rank = "Excellent"

    elif score >= 80:
        grade = "A"
        rank = "Very Good"

    elif score >= 70:
        grade = "B"
        rank = "Good"

    elif score >= 60:
        grade = "C"
        rank = "Average"

    elif score >= 50:
        grade = "D"
        rank = "Pass"

    else:
        grade = "F"
        rank = "Needs Improvement"

    resultLabel.config(
        text=f"Final Score: {score}/100\nGrade: {grade}\nRank: {rank}"
    )

    resultLabel.pack(pady=20)
    replayButton.pack(pady=12)


# Function to restart the quiz
def replayQuiz():

    global questionNumber, score, attempts
    global quizFinished

    questionNumber = 0
    score = 0
    attempts = 0
    quizFinished = True

    resultLabel.pack_forget()
    replayButton.pack_forget()

    answerEntry.pack(pady=12, ipadx=20, ipady=5)
    submitButton.pack(pady=12)

    instruction.config(
        text="Choose Your Difficulty"
    )

    progressLabel.config(
        text="Question: 0 / 10     Score: 0"
    )

    questionLabel.config(text="")


# Function to select difficulty
def selectDifficulty(level):

    global selectedDifficulty
    global questionNumber, score, quizFinished

    selectedDifficulty = level
    questionNumber = 0
    score = 0
    quizFinished = False

    resultLabel.pack_forget()
    replayButton.pack_forget()

    answerEntry.pack(pady=12, ipadx=20, ipady=5)
    submitButton.pack(pady=12)

    instruction.config(
        text=f"You selected {level} difficulty"
    )

    displayProblem(level)


# Function to create styled buttons
def createButton(parent, text, command):

    return tk.Button(
        parent,
        text=text,
        font=(FONT, 11, "bold"),
        bg=NAVY,
        fg=WHITE,
        activebackground="#263B75",
        activeforeground=WHITE,
        width=20,
        relief="flat",
        cursor="hand2",
        command=command
    )


# Function to display difficulty menu
def displayMenu():

    tk.Label(
        root,
        text="DIFFICULTY LEVEL",
        font=(FONT, 15, "bold"),
        bg=LIGHT_GREY,
        fg=NAVY
    ).pack(pady=8)

    createButton(
        root, "Easy",
        lambda: selectDifficulty("Easy")
    ).pack(pady=4)

    createButton(
        root, "Moderate",
        lambda: selectDifficulty("Moderate")
    ).pack(pady=4)

    createButton(
        root, "Advanced",
        lambda: selectDifficulty("Advanced")
    ).pack(pady=4)


# Results label
resultLabel = tk.Label(
    root,
    text="",
    font=(FONT, 18, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
)

# Replay button
replayButton = createButton(
    root,
    "Play Again",
    replayQuiz
)

# Submit answer button
submitButton = createButton(
    root,
    "Submit Answer",
    checkAnswer
)
submitButton.pack(pady=12)

# Display the menu
displayMenu()

# Run application
root.mainloop()
