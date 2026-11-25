
import tkinter as tk
import random
from PIL import Image, ImageTk

# Code Lab 2 - Assessment 1
# Project 2: Alexa Tell Me a Joke

NAVY = "#172554"
LIGHT_GREY = "#F0F4F8"
WHITE = "#FFFFFF"

FONT = "Segoe UI"

def loadJokes():
    jokes = []

    with open("randomJokes.txt", "r") as file:
        for line in file:
            line = line.strip()

            if "?" in line:
                setup, punchline = line.split("?", 1)
                jokes.append((setup + "?", punchline))

    return jokes

jokeList = loadJokes()
currentJoke = None

def displayJoke():
    global currentJoke

    currentJoke = random.choice(jokeList)
    jokeLabel.config(text=currentJoke[0])

def showPunchline():
    if currentJoke is not None:
        jokeLabel.config(text=currentJoke[1])

def nextJoke():
    displayJoke()

root = tk.Tk()
root.title("Alexa Tell Me a Joke")
root.geometry("650x550")
root.resizable(False, False)

# Background image
backgroundImage = Image.open("joke_background.png")
backgroundImage = backgroundImage.resize((650, 550), Image.Resampling.LANCZOS)
backgroundPhoto = ImageTk.PhotoImage(backgroundImage)

backgroundLabel = tk.Label(root, image=backgroundPhoto)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

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
welcomeLabel.pack(pady=25)

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
jokeLabel.pack(pady=20)

# Tell me a joke button
jokeButton = tk.Button(
    root,
    text="Tell Me a Joke",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    command=displayJoke
)
jokeButton.pack(pady=8)

# Show punchline button
punchlineButton = tk.Button(
    root,
    text="Show Punchline",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    command=showPunchline
)
punchlineButton.pack(pady=8)

# Next joke button
nextButton = tk.Button(
    root,
    text="Next Joke",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    command=nextJoke
)
nextButton.pack(pady=8)

# Quit button
quitButton = tk.Button(
    root,
    text="Quit",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    command=root.destroy
)
quitButton.pack(pady=8)

root.mainloop()
