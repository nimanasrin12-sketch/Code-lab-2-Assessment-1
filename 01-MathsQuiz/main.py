
# Import Tkinter for creating the graphical user interface
import tkinter as tk

# Import messagebox to display warning messages
from tkinter import messagebox

# Import Pillow tools for loading and resizing images
from PIL import Image, ImageTk, ImageOps

# Import random to generate different maths questions
import random


# ---------------- COLOURS AND FONT ----------------

# Define colours used throughout the application
WHITE = "#FFFFFF"
GREEN = "#239B56"
ORANGE = "#E67E22"
RED = "#C0392B"
GOLD = "#FFD700"
CYAN = "#00D9E8"
GREY = "#F0F4F8"

# Set the font style used in the application
FONT = "Times New Roman"


# ---------------- MAIN WINDOW ----------------

# Create the main application window
root = tk.Tk()

# Set the title displayed on the window
root.title("Maths Quiz")

# Set the starting window size
root.geometry("900x600")

# Set the minimum window size
root.minsize(750, 500)

# Load the background image
background = Image.open("maths_background.png")

# Load the application logo
logo = Image.open("maths_logo.png")

# Resize the logo for the application icon
logoPhoto = ImageTk.PhotoImage(logo.resize((65, 65)))

# Display the logo in the window title bar
root.iconphoto(True, logoPhoto)


# ---------------- CREATE FOUR PAGES ----------------

# Create dictionaries to store pages, canvases and images
pages = {}
canvases = {}
photos = {}

# Create the four application pages
for name in ("home", "difficulty", "quiz", "result"):

    # Create a separate frame for each page
    pages[name] = tk.Frame(root)

    # Make each frame fill the main window
    pages[name].place(relwidth=1, relheight=1)

    # Create a canvas to display backgrounds and text
    canvases[name] = tk.Canvas(pages[name], highlightthickness=0)

    # Make the canvas fill its frame
    canvases[name].pack(fill="both", expand=True)

    # Add a background image placeholder
    canvases[name].bgItem = canvases[name].create_image(
        0, 0, anchor="nw"
    )


# Function to display the selected page
def showPage(name):
    pages[name].tkraise()


# ---------------- REUSABLE FUNCTIONS ----------------

# Function to create text on a canvas
def addText(canvas, x, y, text, size, color=WHITE, bold=False):

    # Create and return a text item with the selected font
    return canvas.create_text(
        x, y, text=text,
        font=(FONT, size, "bold" if bold else "normal"),
        fill=color
    )


# Function to create reusable buttons
def addButton(canvas, text, color, command, width=16):

    # Return a customised Tkinter button
    return tk.Button(
        canvas, text=text,
        font=(FONT, 16, "bold"),
        bg=color,
        fg=WHITE if color != GREY else "#172554",
        width=width, cursor="hand2", command=command
    )


# ---------------- HOME PAGE ----------------

# Select the Home Page canvas
home = canvases["home"]

# Display the main heading
homeTitle = addText(home, 45, 65, "MATHS QUIZ", 30, WHITE, True)

# Align the heading to the left
home.itemconfig(homeTitle, anchor="w")

# Add a long yellow divider below the heading
homeLine = home.create_line(
    45, 105, 855, 105, fill=GOLD, width=4
)

# Display the welcome heading and introduction
homeMain = addText(home, 450, 200, "UNLOCK YOUR POTENTIAL", 32, WHITE, True)
homeWelcome = addText(home, 450, 270, "Welcome to Maths Quiz!", 23, WHITE, True)
homeTagline = addText(home, 450, 325, "Think. Solve. Achieve.", 18)
homeInfo = addText(home, 450, 370, "Are you ready for a fun maths challenge?", 15)

# Create the Start Quiz button
startButton = addButton(
    home, "START QUIZ", GREEN, lambda: showPage("difficulty")
)

# Position the Start Quiz button
startItem = home.create_window(450, 470, window=startButton)


# ---------------- DIFFICULTY PAGE ----------------

# Select the Difficulty Page canvas
difficulty = canvases["difficulty"]

# Display the difficulty selection heading and instruction
difficultyTitle = addText(
    difficulty, 450, 130, "CHOOSE YOUR DIFFICULTY", 29, WHITE, True
)
difficultyInfo = addText(
    difficulty, 450, 190, "Select a level to start your challenge", 18
)

# Create buttons for the three difficulty levels
easyButton = addButton(
    difficulty, "EASY", GREEN, lambda: startQuiz("Easy")
)
hardButton = addButton(
    difficulty, "HARD", ORANGE, lambda: startQuiz("Hard")
)
extremeButton = addButton(
    difficulty, "EXTREME", RED, lambda: startQuiz("Extreme")
)

# Create a Back button to return to the Home Page
difficultyBack = addButton(
    difficulty, "BACK", GREY, lambda: showPage("home"), 12
)

# Position all difficulty buttons
easyItem = difficulty.create_window(450, 285, window=easyButton)
hardItem = difficulty.create_window(450, 365, window=hardButton)
extremeItem = difficulty.create_window(450, 445, window=extremeButton)
difficultyBackItem = difficulty.create_window(450, 530, window=difficultyBack)


# ---------------- QUIZ PAGE ----------------

# Select the Quiz Page canvas
quiz = canvases["quiz"]

# Display the Quiz Page heading
quizTitle = addText(quiz, 450, 65, "MATHS QUIZ", 28, WHITE, True)

# Add a long yellow divider across the Quiz Page
quizLine = quiz.create_line(
    45, 90, 855, 90, fill=GOLD, width=4
)

# Display the question number and current score
questionItem = addText(quiz, 450, 130, "Question 1 of 10", 16, WHITE, True)
scoreItem = addText(quiz, 450, 185, "Score: 0", 17, WHITE, True)

# Create the area where maths questions will appear
mathsQuestion = addText(quiz, 450, 270, "", 28, WHITE, True)

# Create an Entry widget for the user's answer
answerEntry = tk.Entry(
    quiz, font=(FONT, 20), justify="center", width=15
)

# Position the answer entry box
answerItem = quiz.create_window(450, 355, window=answerEntry)

# Create a text area for answer feedback
feedbackItem = addText(quiz, 450, 415, "", 15, GOLD, True)


# ---------------- PROGRESS CIRCLE ----------------

# Create the background ring of the progress circle
ringBackground = quiz.create_arc(
    0, 0, 150, 150, start=90, extent=359.9,
    style="arc", outline="#263747", width=14
)

# Create the coloured ring that displays progress
progressRing = quiz.create_arc(
    0, 0, 150, 150, start=90, extent=0,
    style="arc", outline=CYAN, width=14
)

# Display the progress percentage in the centre
progressPercent = addText(quiz, 0, 0, "0%", 30, CYAN, True)

# Display the progress heading
progressLabel = addText(quiz, 0, 0, "PROGRESS", 13, WHITE, True)


# ---------------- QUIZ BUTTONS ----------------

# Create the Submit Answer button
submitButton = addButton(
    quiz, "SUBMIT ANSWER", GREEN, lambda: checkAnswer(), 18
)

# Position the Submit Answer button
submitItem = quiz.create_window(450, 490, window=submitButton)

# Create the Back button
quizBack = addButton(
    quiz, "BACK", GREY, lambda: backToDifficulty(), 10
)

# Position the Back button
quizBackItem = quiz.create_window(450, 560, window=quizBack)


# ---------------- RESULT PAGE ----------------

# Select the Result Page canvas
result = canvases["result"]

# Display the result heading and score
resultTitle = addText(result, 450, 145, "QUIZ COMPLETED!", 30, WHITE, True)
finalScore = addText(result, 450, 235, "Your Score: 0 / 100", 23, WHITE, True)

# Display the grade and feedback
gradeItem = addText(result, 450, 300, "Grade: F", 21, WHITE, True)
resultMessage = addText(result, 450, 360, "Keep practising!", 18)

# Create Play Again and Home buttons
playButton = addButton(
    result, "PLAY AGAIN", GREEN, lambda: showPage("difficulty")
)
homeButton = addButton(
    result, "HOME", GREY, lambda: showPage("home"), 12
)

# Position the result page buttons
playItem = result.create_window(450, 440, window=playButton)
homeItem = result.create_window(450, 510, window=homeButton)


# ---------------- QUIZ VARIABLES ----------------

# Store the generated questions
questions = []

# Track the current question number
questionNumber = 0

# Store the user's total score
score = 0

# Count the number of attempts for each question
attempts = 0

# Store the scheduled next-question callback
nextJob = None


# ---------------- GENERATE QUESTIONS ----------------

# Function to generate ten random questions
def createQuestions(level):

    # Set number ranges according to difficulty
    if level == "Easy":
        low, high = 1, 9

    elif level == "Hard":
        low, high = 10, 99

    else:
        low, high = 1000, 9999

    # Create an empty list for the questions
    newQuestions = []

    # Generate ten questions using a loop
    for i in range(10):

        # Generate two random numbers
        a = random.randint(low, high)
        b = random.randint(low, high)

        # Randomly select addition or subtraction
        operation = random.choice(["+", "-"])

        # Calculate the correct answer
        answer = a + b if operation == "+" else a - b

        # Store the question and answer as a tuple
        newQuestions.append((a, operation, b, answer))

    # Return all generated questions
    return newQuestions


# ---------------- UPDATE PROGRESS ----------------

# Function to update the progress circle
def updateProgress(completed):

    # Calculate the percentage of completed questions
    percentage = int(completed / 10 * 100)

    # Update the circular progress indicator
    quiz.itemconfig(
        progressRing, extent=-(percentage / 100) * 360
    )

    # Display the updated percentage
    quiz.itemconfig(progressPercent, text=f"{percentage}%")


# ---------------- START QUIZ ----------------

# Function to start a new quiz at the selected difficulty
def startQuiz(level):

    # Allow these global variables to be updated
    global questions, questionNumber, score, attempts, nextJob

    # Cancel any previously scheduled question
    if nextJob is not None:
        root.after_cancel(nextJob)
        nextJob = None

    # Generate questions for the selected difficulty
    questions = createQuestions(level)

    # Reset the quiz variables
    questionNumber = 0
    score = 0
    attempts = 0

    # Enable the Submit Answer button
    submitButton.config(state="normal")

    # Reset the progress circle
    updateProgress(0)

    # Display the first question
    showQuestion()

    # Open the Quiz Page
    showPage("quiz")


# ---------------- DISPLAY QUESTION ----------------

# Function to display the current question
def showQuestion():

    # Reset the attempts for the new question
    global attempts
    attempts = 0

    # Get the question details from the question list
    a, operation, b, answer = questions[questionNumber]

    # Update the question number, score and maths question
    quiz.itemconfig(
        questionItem, text=f"Question {questionNumber + 1} of 10"
    )
    quiz.itemconfig(scoreItem, text=f"Score: {score}")
    quiz.itemconfig(mathsQuestion, text=f"{a} {operation} {b} = ?")

    # Clear previous feedback
    quiz.itemconfig(feedbackItem, text="")

    # Clear the answer box
    answerEntry.delete(0, tk.END)

    # Enable the Submit Answer button
    submitButton.config(state="normal")

    # Place the cursor inside the answer box
    answerEntry.focus_set()


# ---------------- NEXT QUESTION ----------------

# Function to move to the next question
def nextQuestion():

    # Update the current question number
    global questionNumber, nextJob
    nextJob = None
    questionNumber += 1

    # Display the next question if questions remain
    if questionNumber < 10:
        showQuestion()

    # Otherwise, display the final result
    else:
        showResults()


# ---------------- CHECK ANSWER ----------------

# Function to check the user's submitted answer
def checkAnswer():

    # Allow the score, attempts and scheduled callback to be updated
    global score, attempts, nextJob

    # Prevent multiple submissions while waiting for the next question
    if submitButton["state"] == "disabled":
        return

    # Read the answer entered by the user
    userAnswer = answerEntry.get().strip()

    # Check whether the answer box is empty
    if not userAnswer:
        messagebox.showwarning(
            "Missing Answer", "Please enter your answer."
        )
        return

    # Convert the entered answer into an integer
    try:
        userAnswer = int(userAnswer)

    # Display a warning if the answer is not a whole number
    except ValueError:
        messagebox.showwarning(
            "Invalid Answer", "Please enter a whole number."
        )
        answerEntry.delete(0, tk.END)
        return

    # Get the correct answer for the current question
    correctAnswer = questions[questionNumber][3]

    # Increase the attempt count
    attempts += 1

    # Check whether the submitted answer is correct
    if userAnswer == correctAnswer:

        # Award ten points on the first attempt and five on the second
        points = 10 if attempts == 1 else 5
        score += points

        # Display correct-answer feedback and update the score
        quiz.itemconfig(
            feedbackItem, text=f"Correct! You earned {points} points."
        )
        quiz.itemconfig(scoreItem, text=f"Score: {score}")

        # Update progress and disable further submissions
        updateProgress(questionNumber + 1)
        submitButton.config(state="disabled")

        # Automatically move to the next question after one second
        nextJob = root.after(1000, nextQuestion)

    # Give the user another attempt after an incorrect first answer
    elif attempts == 1:
        quiz.itemconfig(
            feedbackItem, text="Try again! One more attempt."
        )
        answerEntry.delete(0, tk.END)

    # Display the correct answer after two incorrect attempts
    else:
        quiz.itemconfig(
            feedbackItem,
            text=f"Incorrect! The answer was {correctAnswer}."
        )

        # Update progress and disable further submissions
        updateProgress(questionNumber + 1)
        submitButton.config(state="disabled")

        # Move to the next question after a short delay
        nextJob = root.after(1800, nextQuestion)


# ---------------- DISPLAY RESULTS ----------------

# Function to calculate and display the final result
def showResults():

    # Display the final score out of 100
    result.itemconfig(finalScore, text=f"Your Score: {score} / 100")

    # Assign a grade and feedback according to the score
    if score >= 90:
        grade, feedback = "A+", "Excellent work!"

    elif score >= 80:
        grade, feedback = "A", "Very good!"

    elif score >= 70:
        grade, feedback = "B", "Good job!"

    elif score >= 60:
        grade, feedback = "C", "You are improving!"

    elif score >= 50:
        grade, feedback = "D", "You passed!"

    else:
        grade, feedback = "F", "Keep practising!"

    # Update the grade and feedback on the Result Page
    result.itemconfig(gradeItem, text=f"Grade: {grade}")
    result.itemconfig(resultMessage, text=feedback)

    # Display the Result Page
    showPage("result")


# ---------------- BACK TO DIFFICULTY ----------------

# Function to return to the difficulty selection page
def backToDifficulty():

    # Allow the scheduled callback to be updated
    global nextJob

    # Cancel a scheduled question if one exists
    if nextJob is not None:
        root.after_cancel(nextJob)
        nextJob = None

    # Enable the Submit Answer button
    submitButton.config(state="normal")

    # Clear the answer entry
    answerEntry.delete(0, tk.END)

    # Display the Difficulty Page
    showPage("difficulty")


# Allow the Enter key to submit an answer
answerEntry.bind("<Return>", lambda event: checkAnswer())


# ---------------- RESPONSIVE PAGE SIZING ----------------

# Function to resize page elements when the window changes size
def resizePage(name, event):

    # Get the current canvas width and height
    width, height = event.width, event.height

    # Avoid resizing when the canvas is too small
    if width < 2 or height < 2:
        return

    # Calculate the scaling factor for the current window
    scale = min(width / 900, height / 600)

    # Limit the scaling factor to keep elements readable
    scale = max(0.8, min(scale, 1.85))

    # Function to calculate scaled font sizes
    def fontSize(size):
        return max(8, int(size * scale))

    # Resize the background image to fit the canvas
    image = ImageOps.fit(
        background, (width, height),
        method=Image.Resampling.LANCZOS
    )

    # Keep a reference to the resized image
    photos[name] = ImageTk.PhotoImage(image)

    # Get the canvas for the selected page
    canvas = canvases[name]

    # Display the resized background
    canvas.itemconfig(canvas.bgItem, image=photos[name])

    # Function to position elements using relative coordinates
    def move(item, x, y):
        canvas.coords(item, width * x, height * y)


    # ---------------- HOME PAGE RESPONSIVE LAYOUT ----------------

    if name == "home":

        # Position the heading and yellow divider
        move(homeTitle, 0.05, 0.12)

        canvas.coords(
            homeLine,
            width * 0.05, height * 0.18,
            width * 0.95, height * 0.18
        )

        # Position the welcome text and button
        move(homeMain, 0.5, 0.34)
        move(homeWelcome, 0.5, 0.45)
        move(homeTagline, 0.5, 0.54)
        move(homeInfo, 0.5, 0.62)
        move(startItem, 0.5, 0.79)

        # Resize Home Page text and button fonts
        canvas.itemconfig(homeTitle, font=(FONT, fontSize(30), "bold"))
        canvas.itemconfig(homeMain, font=(FONT, fontSize(32), "bold"))
        canvas.itemconfig(homeWelcome, font=(FONT, fontSize(23), "bold"))
        canvas.itemconfig(homeTagline, font=(FONT, fontSize(18)))
        canvas.itemconfig(homeInfo, font=(FONT, fontSize(15)))
        startButton.config(font=(FONT, fontSize(18), "bold"))


    # ---------------- DIFFICULTY PAGE RESPONSIVE LAYOUT ----------------

    elif name == "difficulty":

        # Position all difficulty page elements
        for item, y in [
            (difficultyTitle, 0.22),
            (difficultyInfo, 0.32),
            (easyItem, 0.47),
            (hardItem, 0.61),
            (extremeItem, 0.75),
            (difficultyBackItem, 0.90)
        ]:
            move(item, 0.5, y)

        # Resize the heading and instruction fonts
        canvas.itemconfig(
            difficultyTitle, font=(FONT, fontSize(29), "bold")
        )
        canvas.itemconfig(
            difficultyInfo, font=(FONT, fontSize(18))
        )

        # Resize all difficulty buttons
        for button in (easyButton, hardButton, extremeButton):
            button.config(font=(FONT, fontSize(18), "bold"))

        # Resize the Back button
        difficultyBack.config(font=(FONT, fontSize(13), "bold"))


    # ---------------- QUIZ PAGE RESPONSIVE LAYOUT ----------------

    elif name == "quiz":

        # Position the quiz heading, question, score and answer area
        for item, y in [
            (quizTitle, 0.10),
            (questionItem, 0.22),
            (scoreItem, 0.31),
            (mathsQuestion, 0.45),
            (answerItem, 0.59),
            (feedbackItem, 0.68),
            (submitItem, 0.79),
            (quizBackItem, 0.91)
        ]:
            move(item, 0.5, y)

        # Keep the yellow divider long across the Quiz Page
        canvas.coords(
            quizLine,
            width * 0.05, height * 0.15,
            width * 0.95, height * 0.15
        )
        canvas.itemconfig(quizLine, width=4)

        # Set the progress circle size and position
        ringSize = min(210, width * 0.22, height * 0.32)
        ringX = width * 0.84
        ringY = height * 0.35

        # Calculate the circle boundaries
        left = ringX - ringSize / 2
        top = ringY - ringSize / 2
        right = ringX + ringSize / 2
        bottom = ringY + ringSize / 2

        # Resize the progress circle rings
        for item in (ringBackground, progressRing):
            canvas.coords(item, left, top, right, bottom)
            canvas.itemconfig(
                item, width=max(10, int(ringSize * 0.095))
            )

        # Position the progress percentage and heading
        canvas.coords(progressPercent, ringX, ringY)
        canvas.coords(progressLabel, ringX, top - fontSize(18))

        # Resize the progress circle text
        canvas.itemconfig(
            progressPercent,
            font=(FONT, int(ringSize * 0.25), "bold")
        )
        canvas.itemconfig(
            progressLabel,
            font=(FONT, fontSize(13), "bold")
        )

        # Resize the Quiz Page text
        canvas.itemconfig(quizTitle, font=(FONT, fontSize(28), "bold"))
        canvas.itemconfig(questionItem, font=(FONT, fontSize(16), "bold"))
        canvas.itemconfig(scoreItem, font=(FONT, fontSize(17), "bold"))
        canvas.itemconfig(mathsQuestion, font=(FONT, fontSize(28), "bold"))
        canvas.itemconfig(feedbackItem, font=(FONT, fontSize(15), "bold"))

        # Resize the answer box and quiz buttons
        answerEntry.config(font=(FONT, fontSize(20)))
        submitButton.config(font=(FONT, fontSize(16), "bold"))
        quizBack.config(font=(FONT, fontSize(13), "bold"))


    # ---------------- RESULT PAGE RESPONSIVE LAYOUT ----------------

    elif name == "result":

        # Position all result page elements
        for item, y in [
            (resultTitle, 0.24),
            (finalScore, 0.39),
            (gradeItem, 0.50),
            (resultMessage, 0.60),
            (playItem, 0.75),
            (homeItem, 0.87)
        ]:
            move(item, 0.5, y)

        # Resize the result text
        canvas.itemconfig(resultTitle, font=(FONT, fontSize(30), "bold"))
        canvas.itemconfig(finalScore, font=(FONT, fontSize(23), "bold"))
        canvas.itemconfig(gradeItem, font=(FONT, fontSize(21), "bold"))
        canvas.itemconfig(resultMessage, font=(FONT, fontSize(18)))

        # Resize the result buttons
        playButton.config(font=(FONT, fontSize(16), "bold"))
        homeButton.config(font=(FONT, fontSize(14), "bold"))


# ---------------- APPLY RESPONSIVE SIZING ----------------

# Bind the Configure event to each canvas
# This automatically resizes the page when the window changes size
for page in canvases:

    # Pass the current page name to the resize function
    canvases[page].bind(
        "<Configure>",
        lambda event, name=page: resizePage(name, event)
    )


# ---------------- RUN APPLICATION ----------------

# Display the Home Page when the application starts
showPage("home")

# Keep the application running and respond to user actions
root.mainloop()
