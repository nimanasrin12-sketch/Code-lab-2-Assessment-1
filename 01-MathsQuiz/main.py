
import tkinter as tk
import random

# Create the main application window
root = tk.Tk()
root.title("Maths Quiz")
root.geometry("600x450")
root.resizable(False, False)

# Store quiz information
selectedDifficulty = ""
correctAnswer = 0

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


# Function to check the correct answer
def isCorrect(number1, number2, operation):

    if operation == "+":
        return number1 + number2

    else:
        return number1 - number2


# Function to display a question
def displayProblem(level):

    global correctAnswer

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


# Function to select difficulty
def selectDifficulty(level):

    global selectedDifficulty

    selectedDifficulty = level

    instruction.config(
        text=f"You selected {level} difficulty"
    )

    displayProblem(level)


# Function to check the submitted answer
def checkAnswer():

    try:
        userAnswer = int(answerEntry.get())

        if userAnswer == correctAnswer:
            questionLabel.config(text="Correct answer!")

        else:
            questionLabel.config(text="Incorrect! Try again.")

    except ValueError:
        questionLabel.config(
            text="Please enter a valid number."
        )


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
