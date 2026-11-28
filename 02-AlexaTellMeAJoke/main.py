
import tkinter as tk
import random
from PIL import Image, ImageTk, ImageOps

# Define colours and font styles used throughout the application
FONT = "Georgia"
GOLD = "#FFD36A"
WHITE = "#FFFFFF"
GREEN = "#078A24"
ORANGE = "#E68A00"
RED = "#B51220"
DARK = "#292929"


# Read jokes from the external text file and separate questions from punchlines
def loadJokes():
    jokes = []

    with open("randomJokes.txt", "r", encoding="utf-8") as file:
        for line in file:
            if "?" in line:
                setup, punchline = line.strip().split("?", 1)
                jokes.append((setup + "?", punchline.strip()))

    return jokes


# Store all jokes and track the currently selected joke
jokeList = loadJokes()
currentJoke = None


# Create and configure the main application window
root = tk.Tk()
root.title("Alexa Tell Me a Joke")
root.geometry("1100x700")
root.minsize(800, 550)


# Set the custom application icon in the window title bar
logoImage = Image.open("joke_logo.png")
logo = ImageTk.PhotoImage(logoImage)
root.iconphoto(True, logo)


# Create a canvas to display the background and page elements
canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)


# Load the theatre background image
background = Image.open("joke_background.png")
backgroundPhoto = None
currentPage = "home"


# Create a reusable rounded button using a polygon shape and clickable text
def roundedButton(x, y, width, height, text, colour, command):
    points = [
        x + 20, y, x + width - 20, y,
        x + width, y + 20, x + width, y + height - 20,
        x + width - 20, y + height, x + 20, y + height,
        x, y + height - 20, x, y + 20
    ]

    shape = canvas.create_polygon(
        points, smooth=True, fill=colour,
        outline=GOLD, width=3
    )

    label = canvas.create_text(
        x + width / 2, y + height / 2,
        text=text, fill=WHITE,
        font=("Segoe UI", 17, "bold")
    )

    # Bind mouse clicks to both the button shape and its text
    canvas.tag_bind(shape, "<Button-1>", lambda event: command())
    canvas.tag_bind(label, "<Button-1>", lambda event: command())


# Change the active page to the home screen
def showHome():
    global currentPage
    currentPage = "home"
    drawPage()


# Change the active page to the joke screen
def showJokePage():
    global currentPage
    currentPage = "joke"
    drawPage()


# Select a random joke from the loaded joke collection
def tellJoke():
    global currentJoke

    if jokeList:
        currentJoke = random.choice(jokeList)
        drawPage()


# Display the punchline for the currently selected joke
def showPunchline():
    if currentJoke:
        drawPage(showAnswer=True)


# Draw the background, headings, text and buttons for each page
def drawPage(showAnswer=False):
    global backgroundPhoto

    canvas.delete("all")

    width = canvas.winfo_width()
    height = canvas.winfo_height()

    if width < 2 or height < 2:
        return

    # Resize the background image to cover the entire application window
    resized = ImageOps.fit(
        background, (width, height),
        method=Image.Resampling.LANCZOS
    )

    backgroundPhoto = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=backgroundPhoto, anchor="nw")

    # Calculate the horizontal position of the page content
    centre = width * 0.55

    if currentPage == "home":

        # Display the main heading on the home page
        canvas.create_text(
            centre, height * 0.19,
            text="ALEXA, TELL ME A JOKE!",
            fill=WHITE,
            font=(FONT, max(20, int(height * 0.055)), "bold")
        )

        # Add a gold underline below the heading
        canvas.create_line(
            centre - width * 0.19,
            height * 0.26,
            centre + width * 0.19,
            height * 0.26,
            fill=GOLD,
            width=4
        )

        # Display the welcome message and instructions
        canvas.create_text(
            centre, height * 0.38,
            text="WELCOME TO THE JOKE SHOW",
            fill=GOLD,
            font=(FONT, max(15, int(height * 0.035)), "bold")
        )

        canvas.create_text(
            centre, height * 0.47,
            text="Get ready for some laughs!",
            fill=WHITE,
            font=(FONT, max(12, int(height * 0.025)))
        )

        canvas.create_text(
            centre, height * 0.53,
            text="Click below to discover a random joke.",
            fill=WHITE,
            font=(FONT, max(11, int(height * 0.022)))
        )

        # Create the button that opens the joke page
        roundedButton(
            centre - 110, height * 0.63,
            220, 65,
            "START THE JOKE",
            GREEN,
            showJokePage
        )

    else:

        # Display the heading on the joke page
        canvas.create_text(
            centre, height * 0.12,
            text="THE JOKE SHOW",
            fill=WHITE,
            font=(FONT, max(20, int(height * 0.05)), "bold")
        )

        # Add a decorative gold underline
        canvas.create_line(
            centre - width * 0.15,
            height * 0.19,
            centre + width * 0.15,
            height * 0.19,
            fill=GOLD,
            width=4
        )

        # Display the question and, when requested, its punchline
        if currentJoke:

            canvas.create_text(
                centre, height * 0.32,
                text=currentJoke[0],
                fill=WHITE,
                font=(FONT, max(14, int(height * 0.03)), "bold"),
                width=width * 0.65,
                justify="center"
            )

            if showAnswer:
                canvas.create_text(
                    centre, height * 0.43,
                    text=currentJoke[1],
                    fill=GOLD,
                    font=(FONT, max(13, int(height * 0.027)), "bold"),
                    width=width * 0.65,
                    justify="center"
                )

        else:
            # Show a message before the first joke is selected
            canvas.create_text(
                centre, height * 0.34,
                text="Ready for your first joke?",
                fill=WHITE,
                font=(FONT, max(14, int(height * 0.03)), "bold")
            )

        # Create the buttons for the joke activities
        roundedButton(
            centre - 125, height * 0.55,
            250, 55,
            "TELL ME A JOKE",
            GREEN,
            tellJoke
        )

        roundedButton(
            centre - 125, height * 0.65,
            250, 55,
            "SHOW PUNCHLINE",
            ORANGE,
            showPunchline
        )

        roundedButton(
            centre - 125, height * 0.75,
            250, 55,
            "NEXT JOKE",
            RED,
            tellJoke
        )

        # Create navigation buttons for the home page and application exit
        roundedButton(
            centre - 230, height * 0.88,
            140, 45,
            "HOME",
            DARK,
            showHome
        )

        roundedButton(
            centre - 65, height * 0.88,
            140, 45,
            "EXIT",
            DARK,
            root.destroy
        )


# Redraw all page elements when the application window is resized
canvas.bind("<Configure>", lambda event: drawPage())


# Start the Tkinter event loop and keep the application running
root.mainloop()
