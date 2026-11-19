
import tkinter as tk

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


# Function to select difficulty
def selectDifficulty(level):
    instruction.config(
        text=f"You selected {level} difficulty!"
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
