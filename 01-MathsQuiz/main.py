
import tkinter as tk
import random
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Maths Quiz")
root.geometry("600x450")
root.resizable(False, False)

# Store quiz information
selectedDifficulty = ""
correctAnswer = 0
attempts = 0

# Application heading
heading = tk.Label(
    root,
    text="MATHS QUIZ",
    font=("Arial", 24, "bold")
)
heading.pack(pady=20)

# Instructions
instruction = tk.Label(
    root,
    text="Choose your difficulty level:",
    font=("Arial", 14)
)
instruction.pack(pady=10)

# Question display
questionLabel = tk.Label(
    root,
    text="",
    font=("Arial", 20, "bold")
)
questionLabel.pack(pady=20)

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


# Function to display a question
def displayProblem(level):

    global correctAnswer, attempts

    attempts = 0

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


# Function to check the submitted answer
def checkAnswer():

    global attempts

    try:
        userAnswer = int(answerEntry.get())

        if userAnswer == correctAnswer:

            messagebox.showinfo(
                "Result",
                "Correct answer!"
            )

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
                    "Result",
                    f"Incorrect! The correct answer is {correctAnswer}."
                )

                displayProblem(selectedDifficulty)

    except ValueError:

        messagebox.showwarning(
            "Invalid Input",
            "Please enter a whole number."
        )


# Function to select difficulty
def selectDifficulty(level):

    global selectedDifficulty

    selectedDifficulty = level

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
