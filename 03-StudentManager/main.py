
import tkinter as tk

# AI assistance acknowledgement:
# Tool: ChatGPT (OpenAI)
# Purpose: Assistance with developing a Tkinter Student Manager application.
# Prompt: Help me read student records from a text file using Python.

# Colour theme
NAVY = "#172554"
LIGHT_GREY = "#F0F4F8"
WHITE = "#FFFFFF"

# Font settings
FONT = "Segoe UI"


# Function to load student records
def loadStudents():

    students = []

    with open("studentMarks.txt", "r") as file:

        numberOfStudents = int(file.readline())

        for line in file:
            data = line.strip().split(",")

            student = {
                "code": data[0],
                "name": data[1],
                "course1": int(data[2]),
                "course2": int(data[3]),
                "course3": int(data[4]),
                "exam": int(data[5])
            }

            students.append(student)

    return students


# Load student records
studentList = loadStudents()

print("Student records loaded successfully!")
print("Number of students:", len(studentList))


# Create the main application window
root = tk.Tk()
root.title("Student Manager")
root.geometry("750x550")
root.resizable(False, False)
root.config(bg=LIGHT_GREY)

# Application heading
heading = tk.Label(
    root,
    text="STUDENT MANAGER",
    font=(FONT, 26, "bold"),
    bg=NAVY,
    fg=WHITE,
    pady=25
)
heading.pack(fill="x")

# Welcome message
welcomeLabel = tk.Label(
    root,
    text="Student Records Management System",
    font=(FONT, 14),
    bg=LIGHT_GREY,
    fg=NAVY
)
welcomeLabel.pack(pady=30)

# Run application
root.mainloop()
