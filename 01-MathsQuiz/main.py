
import tkinter as tk
import random

# Create the main application window
root = tk.Tk()
root.title("Maths Quiz")
root.geometry("600x450")
root.resizable(False, False)

# Application heading
heading = tk.Label(
    root,
    text="MATHS QUIZ",
    font=("Arial", 24, "bold")
)
heading.pack(pady=30)

# Instructions
instruction = tk.Label(
    root,
    text="Choose your difficulty level:",
    font=("Arial", 14)
)
instruction.pack(pady=15)


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


# Function to select difficulty
def selectDifficulty(level):

    number1, number2 = randomInt(level)

    instruction.config(
        text=f"{level}: Example numbers: {number1} and {number2}"
    )


# Function to display difficulty menu
def displayMenu():

    tk.Label(
        root,
        text="DIFFICULTY LEVEL",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Button(
        root,
        text="Easy",
        width=20,
        command=lambda: selectDifficulty("Easy")
    ).pack(pady=5)

    tk.Button(
        root,
        text="Moderate",
        width=20,
        command=lambda: selectDifficulty("Moderate")
    ).pack(pady=5)

    tk.Button(
        root,
        text="Advanced",
        width=20,
        command=lambda: selectDifficulty("Advanced")
    ).pack(pady=5)


# Display the menu
displayMenu()

# Run application
root.mainloop()
