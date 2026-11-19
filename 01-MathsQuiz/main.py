
import tkinter as tk
import random
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Maths Quiz")
root.geometry("600x500")
root.resizable(False, False)

# Store quiz information
selectedDifficulty = ""
correctAnswer = 0
attempts = 0
questionNumber = 0
score = 0

# Application heading
heading = tk.Label(
    root,
    text="MATHS QUIZ",
    font=("Arial", 24, "bold")
)
heading.pack(pady=15)

# Instructions
instruction = tk.Label(
    root,
    text="Choose your difficulty level:",
    font=("Arial", 14)
)
instruction.pack(pady=5)

# Question counter
progressLabel = tk.Label(
    root,
    text="Question: 0 / 10     Score: 0",
    font=("Arial", 12, "bold")
)
progressLabel.pack(pady=10)

# Question display
questionLabel = tk.Label(
    root,
    text="",
    font=("Arial", 20, "bold")
)
questionLabel.pack(pady=15)

# Answer input box
answerEntry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center"
)
answerEntry.pack(pady=10)


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

    global correctAnswer, attempts, questionNumber

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
    updateProgress()


# Function to check the submitted answer
def checkAnswer():

    global attempts, score

    if not selectedDifficulty:
        messagebox.showwarning(
            "Choose Difficulty",
            "Please select a difficulty level first."
        )
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

    questionLabel.config(
        text="QUIZ COMPLETED!"
    )

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

    resultLabel.pack(pady=15)
    replayButton.pack(pady=10)


# Function to restart the quiz
def replayQuiz():

    global questionNumber, score, attempts

    questionNumber = 0
    score = 0
    attempts = 0

    resultLabel.pack_forget()
    replayButton.pack_forget()

    answerEntry.pack(pady=10)
    submitButton.pack(pady=10)

    instruction.config(
        text="Choose your difficulty level:"
    )

    progressLabel.config(
        text="Question: 0 / 10     Score: 0"
    )

    questionLabel.config(text="")


# Function to select difficulty
def selectDifficulty(level):

    global selectedDifficulty
    global questionNumber
    global score

    selectedDifficulty = level
    questionNumber = 0
    score = 0

    resultLabel.pack_forget()
    replayButton.pack_forget()

    answerEntry.pack(pady=10)
    submitButton.pack(pady=10)

    instruction.config(
        text=f"You selected {level} difficulty"
    )

    displayProblem(level)


# Function to display difficulty menu
def displayMenu():

    tk.Label(
        root,
        text="DIFFICULTY LEVEL",
        font=("Arial", 16, "bold")
    ).pack(pady=5)

    tk.Button(
        root,
        text="Easy",
        width=20,
        command=lambda: selectDifficulty("Easy")
    ).pack(pady=3)

    tk.Button(
        root,
        text="Moderate",
        width=20,
        command=lambda: selectDifficulty("Moderate")
    ).pack(pady=3)

    tk.Button(
        root,
        text="Advanced",
        width=20,
        command=lambda: selectDifficulty("Advanced")
    ).pack(pady=3)


# Results label
resultLabel = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold")
)

# Replay button
replayButton = tk.Button(
    root,
    text="Play Again",
    width=20,
    command=replayQuiz
)

# Submit answer button
submitButton = tk.Button(
    root,
    text="Submit Answer",
    width=20,
    command=checkAnswer
)
submitButton.pack(pady=10)

# Display the menu
displayMenu()

# Run application
root.mainloop()
