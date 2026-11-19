
import tkinter as tk
import random

# AI assistance acknowledgement:
# Tool: ChatGPT (OpenAI)
# Purpose: Assistance with developing a Tkinter joke application.

# Colour theme
NAVY = "#172554"
LIGHT_GREY = "#F0F4F8"
WHITE = "#FFFFFF"

# Font settings
FONT = "Segoe UI"


# Function to load jokes from the text file
def loadJokes():

    jokes = []

    with open("randomJokes.txt", "r") as file:

        for line in file:
            line = line.strip()

            if "?" in line:
                setup, punchline = line.split("?", 1)
                jokes.append((setup + "?", punchline))

    return jokes


# Load all jokes
jokeList = loadJokes()


# Create the main application window
root = tk.Tk()
root.title("Alexa Tell Me a Joke")
root.geometry("650x500")
root.resizable(False, False)
root.config(bg=LIGHT_GREY)

# Application heading
heading = tk.Label(
    root,
    text="ALEXA, TELL ME A JOKE!",
    font=(FONT, 25, "bold"),
    bg=NAVY,
    fg=WHITE,
    pady=25
)
heading.pack(fill="x")

# Welcome message
welcomeLabel = tk.Label(
    root,
    text="Ready for a little laughter?",
    font=(FONT, 14),
    bg=LIGHT_GREY,
    fg=NAVY
)
welcomeLabel.pack(pady=30)

# Run application
root.mainloop()
