
import tkinter as tk
from tkinter import messagebox

# AI assistance acknowledgement:
# Tool: ChatGPT (OpenAI)
# Purpose: Assistance with developing a Tkinter Student Manager application.
# Prompt: Help me create a Student Manager with student records, viewing all students and searching for individual students.

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

            if len(data) == 6:
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


# Function to view all students
def viewAllStudents():

    studentWindow = tk.Toplevel(root)
    studentWindow.title("All Students")
    studentWindow.geometry("700x450")
    studentWindow.config(bg=LIGHT_GREY)

    title = tk.Label(
        studentWindow,
        text="ALL STUDENT RECORDS",
        font=(FONT, 20, "bold"),
        bg=NAVY,
        fg=WHITE,
        pady=15
    )
    title.pack(fill="x")

    records = tk.Text(
        studentWindow,
        font=(FONT, 11),
        bg=WHITE,
        fg=NAVY,
        width=80,
        height=18
    )
    records.pack(padx=15, pady=15)

    records.insert(
        tk.END,
        f"{'Code':<10}{'Name':<22}{'C1':<7}{'C2':<7}{'C3':<7}{'Exam':<7}\n"
    )

    records.insert(tk.END, "-" * 65 + "\n")

    for student in studentList:

        records.insert(
            tk.END,
            f"{student['code']:<10}"
            f"{student['name']:<22}"
            f"{student['course1']:<7}"
            f"{student['course2']:<7}"
            f"{student['course3']:<7}"
            f"{student['exam']:<7}\n"
        )

    records.config(state="disabled")


# Function to search for an individual student
def searchStudent():

    studentCode = searchEntry.get().strip()

    if studentCode == "":
        messagebox.showwarning(
            "Missing Code",
            "Please enter a student code."
        )
        return

    for student in studentList:

        if student["code"] == studentCode:

            details = (
                f"Student Code: {student['code']}\n"
                f"Student Name: {student['name']}\n\n"
                f"Course 1: {student['course1']}\n"
                f"Course 2: {student['course2']}\n"
                f"Course 3: {student['course3']}\n"
                f"Exam Marks: {student['exam']}"
            )

            messagebox.showinfo("Student Details", details)
            return

    messagebox.showerror(
        "Student Not Found",
        "No student found with that code."
    )


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
welcomeLabel.pack(pady=20)

# View all students button
viewButton = tk.Button(
    root,
    text="View All Students",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=22,
    command=viewAllStudents
)
viewButton.pack(pady=10)

# Search section heading
searchLabel = tk.Label(
    root,
    text="Search Individual Student",
    font=(FONT, 14, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
)
searchLabel.pack(pady=12)

# Student code input
searchEntry = tk.Entry(
    root,
    font=(FONT, 13),
    justify="center"
)
searchEntry.pack(pady=8, ipady=5)

# Search button
searchButton = tk.Button(
    root,
    text="Search Student",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=22,
    command=searchStudent
)
searchButton.pack(pady=10)

# Run application
root.mainloop()
