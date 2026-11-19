
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


def saveStudents():
    with open("studentMarks.txt", "w") as file:
        file.write(str(len(studentList)) + "\n")

        for student in studentList:
            file.write(
                f"{student['code']},{student['name']},"
                f"{student['course1']},{student['course2']},"
                f"{student['course3']},{student['exam']}\n"
            )


def displayStudentList(title, records):
    if not records:
        messagebox.showinfo("No Records", "No student records available.")
        return

    window = tk.Toplevel(root)
    window.title(title)
    window.geometry("650x500")
    window.configure(bg=LIGHT_GREY)

    heading = tk.Label(
        window, text=title, font=(FONT, 18, "bold"),
        bg=LIGHT_GREY, fg=NAVY
    )
    heading.pack(pady=15)

    textArea = tk.Text(
        window, font=(FONT, 11), bg=WHITE,
        fg=NAVY, width=65, height=22
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

    messagebox.showinfo(
        "Highest Marks",
        f"Student Name: {highestStudent['name']}\n"
        f"Student Code: {highestStudent['code']}\n"
        f"Highest Exam Marks: {highestStudent['exam']}"
    )


def lowestMarks():
    if not studentList:
        messagebox.showinfo("No Records", "No student records available.")
        return

    lowestStudent = min(studentList, key=lambda student: student["exam"])

    messagebox.showinfo(
        "Lowest Marks",
        f"Student Name: {lowestStudent['name']}\n"
        f"Student Code: {lowestStudent['code']}\n"
        f"Lowest Exam Marks: {lowestStudent['exam']}"
    )


def sortStudents():
    sortedStudents = sorted(
        studentList,
        key=lambda student: student["name"].lower()
    )
    displayStudentList("Students Sorted by Name (A-Z)", sortedStudents)


def addStudent():
    addWindow = tk.Toplevel(root)
    addWindow.title("Add New Student")
    addWindow.geometry("400x520")
    addWindow.configure(bg=LIGHT_GREY)
    addWindow.resizable(False, False)

    heading = tk.Label(
        addWindow, text="Add New Student",
        font=(FONT, 20, "bold"), bg=LIGHT_GREY, fg=NAVY
    )
    heading.pack(pady=15)

    fields = [
        ("Student Code", "code"),
        ("Student Name", "name"),
        ("Course 1 Marks", "course1"),
        ("Course 2 Marks", "course2"),
        ("Course 3 Marks", "course3"),
        ("Exam Marks", "exam")
    ]

    entries = {}

    for labelText, fieldName in fields:
        label = tk.Label(
            addWindow, text=labelText,
            font=(FONT, 10), bg=LIGHT_GREY, fg=NAVY
        )
        label.pack(pady=(5, 2))

        entry = tk.Entry(addWindow, font=(FONT, 11), width=28)
        entry.pack(pady=2)
        entries[fieldName] = entry

    def saveNewStudent():
        code = entries["code"].get().strip()
        name = entries["name"].get().strip()

        if not code or not name:
            messagebox.showwarning(
                "Missing Details",
                "Please enter the student code and name.",
                parent=addWindow
            )
            return

        for student in studentList:
            if student["code"] == code:
                messagebox.showerror(
                    "Duplicate Code",
                    "This student code already exists.",
                    parent=addWindow
                )
                return

        try:
            course1 = int(entries["course1"].get())
            course2 = int(entries["course2"].get())
            course3 = int(entries["course3"].get())
            exam = int(entries["exam"].get())
        except ValueError:
            messagebox.showerror(
                "Invalid Marks",
                "Please enter whole numbers for all marks.",
                parent=addWindow
            )
            return

        marks = [course1, course2, course3, exam]

        if any(mark < 0 or mark > 100 for mark in marks):
            messagebox.showerror(
                "Invalid Marks",
                "Marks must be between 0 and 100.",
                parent=addWindow
            )
            return

        newStudent = {
            "code": code,
            "name": name,
            "course1": course1,
            "course2": course2,
            "course3": course3,
            "exam": exam
        }

        studentList.append(newStudent)
        saveStudents()

        messagebox.showinfo(
            "Success",
            "New student added successfully!",
            parent=addWindow
        )
        addWindow.destroy()

    saveButton = tk.Button(
        addWindow, text="Save Student",
        font=(FONT, 11, "bold"), bg=NAVY,
        fg=WHITE, width=22, command=saveNewStudent
    )
    saveButton.pack(pady=20)


def deleteStudent():
    deleteWindow = tk.Toplevel(root)
    deleteWindow.title("Delete Student")
    deleteWindow.geometry("400x250")
    deleteWindow.configure(bg=LIGHT_GREY)
    deleteWindow.resizable(False, False)

    heading = tk.Label(
        deleteWindow, text="Delete Student",
        font=(FONT, 20, "bold"), bg=LIGHT_GREY, fg=NAVY
    )
    heading.pack(pady=20)

    codeLabel = tk.Label(
        deleteWindow, text="Enter Student Code:",
        font=(FONT, 11), bg=LIGHT_GREY, fg=NAVY
    )
    codeLabel.pack(pady=5)

    codeEntry = tk.Entry(deleteWindow, font=(FONT, 12), width=25)
    codeEntry.pack(pady=5)

    def confirmDelete():
        code = codeEntry.get().strip()

        if not code:
            messagebox.showwarning(
                "Missing Code", "Please enter a student code.",
                parent=deleteWindow
            )
            return

        for student in studentList:
            if student["code"] == code:
                confirm = messagebox.askyesno(
                    "Confirm Deletion",
                    f"Are you sure you want to delete {student['name']}?",
                    parent=deleteWindow
                )

                if confirm:
                    studentList.remove(student)
                    saveStudents()
                    messagebox.showinfo(
                        "Success", "Student deleted successfully!",
                        parent=deleteWindow
                    )
                    deleteWindow.destroy()
                return

        messagebox.showerror(
            "Not Found", "Student code not found.",
            parent=deleteWindow
        )

    deleteButton = tk.Button(
        deleteWindow, text="Delete Student",
        font=(FONT, 11, "bold"), bg=NAVY,
        fg=WHITE, width=22, command=confirmDelete
    )
    deleteButton.pack(pady=20)


def updateStudent():
    updateWindow = tk.Toplevel(root)
    updateWindow.title("Update Student")
    updateWindow.geometry("420x540")
    updateWindow.configure(bg=LIGHT_GREY)
    updateWindow.resizable(False, False)

    heading = tk.Label(
        updateWindow, text="Update Student Details",
        font=(FONT, 18, "bold"), bg=LIGHT_GREY, fg=NAVY
    )
    heading.pack(pady=15)

    codeLabel = tk.Label(
        updateWindow, text="Enter Student Code:",
        font=(FONT, 11), bg=LIGHT_GREY, fg=NAVY
    )
    codeLabel.pack(pady=5)

    codeEntry = tk.Entry(updateWindow, font=(FONT, 11), width=28)
    codeEntry.pack(pady=5)

    entries = {}

    fields = [
        ("Student Name", "name"),
        ("Course 1 Marks", "course1"),
        ("Course 2 Marks", "course2"),
        ("Course 3 Marks", "course3"),
        ("Exam Marks", "exam")
    ]

    for labelText, fieldName in fields:
        label = tk.Label(
            updateWindow, text=labelText,
            font=(FONT, 10), bg=LIGHT_GREY, fg=NAVY
        )
        label.pack(pady=(7, 2))

        entry = tk.Entry(updateWindow, font=(FONT, 11), width=28)
        entry.pack(pady=2)
        entries[fieldName] = entry

    selectedStudent = {"student": None}

    def findStudent():
        code = codeEntry.get().strip()

        if not code:
            messagebox.showwarning(
                "Missing Code",
                "Please enter a student code.",
                parent=updateWindow
            )
            return

        for student in studentList:
            if student["code"] == code:
                selectedStudent["student"] = student

                for fieldName in entries:
                    entries[fieldName].delete(0, tk.END)
                    entries[fieldName].insert(
                        0, str(student[fieldName])
                    )

                messagebox.showinfo(
                    "Student Found",
                    "Student details loaded. You can now edit them.",
                    parent=updateWindow
                )
                return

        messagebox.showerror(
            "Not Found",
            "Student code not found.",
            parent=updateWindow
        )

    def saveUpdatedStudent():
        student = selectedStudent["student"]

        if student is None:
            messagebox.showwarning(
                "Find Student First",
                "Please find a student before saving changes.",
                parent=updateWindow
            )
            return

        name = entries["name"].get().strip()

        if not name:
            messagebox.showwarning(
                "Missing Name",
                "Please enter the student's name.",
                parent=updateWindow
            )
            return

        try:
            course1 = int(entries["course1"].get())
            course2 = int(entries["course2"].get())
            course3 = int(entries["course3"].get())
            exam = int(entries["exam"].get())
        except ValueError:
            messagebox.showerror(
                "Invalid Marks",
                "Please enter whole numbers for all marks.",
                parent=updateWindow
            )
            return

        marks = [course1, course2, course3, exam]

        if any(mark < 0 or mark > 100 for mark in marks):
            messagebox.showerror(
                "Invalid Marks",
                "Marks must be between 0 and 100.",
                parent=updateWindow
            )
            return

        student["name"] = name
        student["course1"] = course1
        student["course2"] = course2
        student["course3"] = course3
        student["exam"] = exam

        saveStudents()

        messagebox.showinfo(
            "Success",
            "Student details updated successfully!",
            parent=updateWindow
        )
        updateWindow.destroy()

    findButton = tk.Button(
        updateWindow, text="Find Student",
        font=(FONT, 10, "bold"), bg=NAVY,
        fg=WHITE, width=22, command=findStudent
    )
    findButton.pack(pady=10)

    saveButton = tk.Button(
        updateWindow, text="Save Changes",
        font=(FONT, 10, "bold"), bg=NAVY,
        fg=WHITE, width=22, command=saveUpdatedStudent
    )
    saveButton.pack(pady=10)


# Load student records
loadStudents()

# Main window
root = tk.Tk()
root.title("Student Manager")
root.geometry("750x850")
root.resizable(True, True)
root.configure(bg=LIGHT_GREY)

heading = tk.Label(
    root, text="Student Manager",
    font=(FONT, 24, "bold"), bg=LIGHT_GREY, fg=NAVY
)
heading.pack(pady=20)

welcomeLabel = tk.Label(
    root, text="Welcome! Manage and view student records.",
    font=(FONT, 12), bg=LIGHT_GREY, fg=NAVY
)
welcomeLabel.pack(pady=5)

viewButton = tk.Button(
    root, text="View All Students",
    font=(FONT, 12, "bold"), bg=NAVY,
    fg=WHITE, width=25, command=viewAllStudents
)
viewButton.pack(pady=8)

searchLabel = tk.Label(
    root, text="Enter Student Code:",
    font=(FONT, 11), bg=LIGHT_GREY, fg=NAVY
)
searchLabel.pack(pady=5)

searchEntry = tk.Entry(root, font=(FONT, 12), width=25)
searchEntry.pack(pady=5)

searchButton = tk.Button(
    root, text="Search Student",
    font=(FONT, 12, "bold"), bg=NAVY,
    fg=WHITE, width=25, command=searchStudent
)
searchButton.pack(pady=8)

highestButton = tk.Button(
    root, text="Find Highest Marks",
    font=(FONT, 12, "bold"), bg=NAVY,
    fg=WHITE, width=25, command=highestMarks
)
highestButton.pack(pady=8)

lowestButton = tk.Button(
    root, text="Find Lowest Marks",
    font=(FONT, 12, "bold"), bg=NAVY,
    fg=WHITE, width=25, command=lowestMarks
)
lowestButton.pack(pady=8)

sortButton = tk.Button(
    root, text="Sort Students by Name (A-Z)",
    font=(FONT, 12, "bold"), bg=NAVY,
    fg=WHITE, width=25, command=sortStudents
)
sortButton.pack(pady=8)

addButton = tk.Button(
    root, text="Add New Student",
    font=(FONT, 12, "bold"), bg=NAVY,
    fg=WHITE, width=25, command=addStudent
)
addButton.pack(pady=8)

deleteButton = tk.Button(
    root, text="Delete Student",
    font=(FONT, 12, "bold"), bg=NAVY,
    fg=WHITE, width=25, command=deleteStudent
)
deleteButton.pack(pady=8)

updateButton = tk.Button(
    root, text="Update Student Details",
    font=(FONT, 12, "bold"), bg=NAVY,
    fg=WHITE, width=25, command=updateStudent
)
updateButton.pack(pady=8)

root.mainloop()
