
import tkinter as tk
from tkinter import messagebox

# AI assistance acknowledgement:
# Tool: ChatGPT (OpenAI)
# Purpose: Assistance with developing the Student Manager application.

# Colour theme
NAVY = "#172554"
LIGHT_GREY = "#F0F4F8"
WHITE = "#FFFFFF"
FONT = "Segoe UI"

studentList = []


def loadStudents():
    global studentList

    studentList = []

    with open("studentMarks.txt", "r") as file:
        numberOfStudents = int(file.readline().strip())

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

                studentList.append(student)


def displayStudentList(title, records):
    if not records:
        messagebox.showinfo("No Records", "No student records available.")
        return

    window = tk.Toplevel(root)
    window.title(title)
    window.geometry("650x500")
    window.configure(bg=LIGHT_GREY)

    heading = tk.Label(
        window,
        text=title,
        font=(FONT, 18, "bold"),
        bg=LIGHT_GREY,
        fg=NAVY
    )
    heading.pack(pady=15)

    textArea = tk.Text(
        window,
        font=(FONT, 11),
        bg=WHITE,
        fg=NAVY,
        width=65,
        height=22
    )
    textArea.pack(padx=15, pady=10)

    for student in records:
        details = (
            f"Code: {student['code']}\n"
            f"Name: {student['name']}\n"
            f"Course 1: {student['course1']}\n"
            f"Course 2: {student['course2']}\n"
            f"Course 3: {student['course3']}\n"
            f"Exam Marks: {student['exam']}\n"
            "------------------------------\n"
        )
        textArea.insert(tk.END, details)

    textArea.config(state=tk.DISABLED)


def viewAllStudents():
    displayStudentList("All Student Records", studentList)


def searchStudent():
    code = searchEntry.get().strip()

    if not code:
        messagebox.showwarning("Missing Code", "Please enter a student code.")
        return

    for student in studentList:
        if student["code"] == code:
            details = (
                f"Student Code: {student['code']}\n"
                f"Student Name: {student['name']}\n"
                f"Course 1: {student['course1']}\n"
                f"Course 2: {student['course2']}\n"
                f"Course 3: {student['course3']}\n"
                f"Exam Marks: {student['exam']}"
            )

            messagebox.showinfo("Student Details", details)
            return

    messagebox.showerror("Not Found", "Student code not found.")


def highestMarks():
    if not studentList:
        messagebox.showinfo("No Records", "No student records available.")
        return

    highestStudent = max(studentList, key=lambda student: student["exam"])

    details = (
        f"Student Name: {highestStudent['name']}\n"
        f"Student Code: {highestStudent['code']}\n"
        f"Highest Exam Marks: {highestStudent['exam']}"
    )

    messagebox.showinfo("Highest Marks", details)


def lowestMarks():
    if not studentList:
        messagebox.showinfo("No Records", "No student records available.")
        return

    lowestStudent = min(studentList, key=lambda student: student["exam"])

    details = (
        f"Student Name: {lowestStudent['name']}\n"
        f"Student Code: {lowestStudent['code']}\n"
        f"Lowest Exam Marks: {lowestStudent['exam']}"
    )

    messagebox.showinfo("Lowest Marks", details)


def sortStudents():
    sortedStudents = sorted(
        studentList,
        key=lambda student: student["name"].lower()
    )

    displayStudentList("Students Sorted by Name (A-Z)", sortedStudents)


# Load student records
loadStudents()

# Main window
root = tk.Tk()
root.title("Student Manager")
root.geometry("750x700")
root.resizable(True, True)
root.configure(bg=LIGHT_GREY)

heading = tk.Label(
    root,
    text="Student Manager",
    font=(FONT, 24, "bold"),
    bg=LIGHT_GREY,
    fg=NAVY
)
heading.pack(pady=20)

welcomeLabel = tk.Label(
    root,
    text="Welcome! Manage and view student records.",
    font=(FONT, 12),
    bg=LIGHT_GREY,
    fg=NAVY
)
welcomeLabel.pack(pady=5)

viewButton = tk.Button(
    root,
    text="View All Students",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=25,
    command=viewAllStudents
)
viewButton.pack(pady=10)

searchLabel = tk.Label(
    root,
    text="Enter Student Code:",
    font=(FONT, 11),
    bg=LIGHT_GREY,
    fg=NAVY
)
searchLabel.pack(pady=5)

searchEntry = tk.Entry(root, font=(FONT, 12), width=25)
searchEntry.pack(pady=5)

searchButton = tk.Button(
    root,
    text="Search Student",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=25,
    command=searchStudent
)
searchButton.pack(pady=8)

highestButton = tk.Button(
    root,
    text="Find Highest Marks",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=25,
    command=highestMarks
)
highestButton.pack(pady=8)

lowestButton = tk.Button(
    root,
    text="Find Lowest Marks",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=25,
    command=lowestMarks
)
lowestButton.pack(pady=8)

sortButton = tk.Button(
    root,
    text="Sort Students by Name (A-Z)",
    font=(FONT, 12, "bold"),
    bg=NAVY,
    fg=WHITE,
    width=25,
    command=sortStudents
)
sortButton.pack(pady=8)

root.mainloop()
