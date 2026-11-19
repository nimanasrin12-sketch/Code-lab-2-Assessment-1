
import tkinter as tk
import random

# AI assistance acknowledgement:
# Tool: ChatGPT (OpenAI)
# Purpose: Assistance with developing a Tkinter joke application,
# including loading and displaying random jokes.

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
currentJoke = None


# Function to display a random joke
def displayJoke():

    global currentJoke

    currentJoke = random.choice(jokeList)

    jokeLabel.config(text=currentJoke[0])


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

# Joke display
jokeLabel = tk.Label(
    root,
    text="Click the button to hear a joke!",
    font=(FONT, 16, "bold"),
    bg=WHITE,
    fg=NAVY,
    wraplength=500,
    height=3
)
jokeLabel.pack(pady=25)

# Tell me a joke button
jokeButton = tk.Button(
    root,
    text="Tell Me a Joke",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    command=displayJoke
)
jokeButton.pack(pady=15)

# Run application
root.mainloop()
