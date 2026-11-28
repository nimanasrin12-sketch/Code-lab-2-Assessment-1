
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Student Manager - Exercise 3

# Application colours and font
NAVY = "#172554"
GOLD = "#D6A642"
WHITE = "#FFFFFF"
LIGHT = "#F4F7FC"
FONT = "Segoe UI"

DATA_FILE = "studentMarks.txt"


# Load student records from the text file
def loadStudents():
    students = []

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            file.write("0\n")
        return students

    with open(DATA_FILE, "r") as file:
        lines = file.readlines()

    if lines and lines[0].strip().isdigit():
        lines = lines[1:]

    for line in lines:
        parts = line.strip().split(",")

        if len(parts) == 6:
            try:
                students.append({
                    "code": parts[0],
                    "name": parts[1],
                    "c1": int(parts[2]),
                    "c2": int(parts[3]),
                    "c3": int(parts[4]),
                    "exam": int(parts[5])
                })
            except ValueError:
                continue

    return students


# Save all student records into the file
def saveStudents():
    with open(DATA_FILE, "w") as file:
        file.write(str(len(students)) + "\n")

        for s in students:
            file.write(
                f"{s['code']},{s['name']},{s['c1']},"
                f"{s['c2']},{s['c3']},{s['exam']}\n"
            )


# Calculate student marks and grades
def getTotal(s):
    return s["c1"] + s["c2"] + s["c3"] + s["exam"]


def getPercentage(s):
    return getTotal(s) / 160 * 100


def getGrade(s):
    percentage = getPercentage(s)

    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    return "F"


students = loadStudents()


# Create the main application window
root = tk.Tk()
root.title("Student Manager")
root.geometry("1100x620")
root.minsize(850, 500)
root.resizable(True, True)


# Set the application logo
if os.path.exists("student_logo.png"):
    logoImage = Image.open("student_logo.png")
    logo = ImageTk.PhotoImage(logoImage)
    root.iconphoto(True, logo)


# Load the original background image
backgroundOriginal = Image.open("student_background.png").convert("RGB")

canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

backgroundPhoto = None
backgroundItem = canvas.create_image(0, 0, anchor="nw")


# Main application heading
headingItem = canvas.create_text(
    550, 55,
    text="STUDENT MANAGER",
    font=(FONT, 25, "bold"),
    fill=WHITE
)

# Left-side menu heading
menuHeadingItem = canvas.create_text(
    145, 151,
    text="STUDENT OPERATIONS",
    font=(FONT, 12, "bold"),
    fill=WHITE
)


# Create the right-side display panel
content = tk.Frame(canvas, bg=LIGHT)

contentWindow = canvas.create_window(
    680, 350,
    window=content,
    width=780,
    height=420
)


# Remove previous widgets from the display panel
def clearPanel():
    for widget in content.winfo_children():
        widget.destroy()


# Display a heading on each operation page
def panelTitle(title):
    tk.Label(
        content,
        text=title,
        font=(FONT, 19, "bold"),
        bg=LIGHT,
        fg=NAVY
    ).pack(pady=(12, 15))


# Create reusable buttons for different operations
def actionButton(parent, text, command, colour=NAVY):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=(FONT, 10, "bold"),
        bg=colour,
        fg=WHITE,
        activebackground=GOLD,
        activeforeground=NAVY,
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=7
    )


# Display student records using a Treeview table
def showTable(records):
    columns = (
        "code", "name", "c1", "c2", "c3",
        "exam", "total", "percentage", "grade"
    )

    tableFrame = tk.Frame(content, bg=LIGHT)
    tableFrame.pack(fill="both", expand=True, padx=12, pady=5)

    table = ttk.Treeview(
        tableFrame,
        columns=columns,
        show="headings",
        height=12
    )

    headings = {
        "code": "Code",
        "name": "Student Name",
        "c1": "C1",
        "c2": "C2",
        "c3": "C3",
        "exam": "Exam",
        "total": "Total",
        "percentage": "%",
        "grade": "Grade"
    }

    widths = {
        "code": 65,
        "name": 145,
        "c1": 42,
        "c2": 42,
        "c3": 42,
        "exam": 55,
        "total": 55,
        "percentage": 65,
        "grade": 50
    }

    for col in columns:
        table.heading(col, text=headings[col])
        table.column(col, width=widths[col], anchor="center")

    for s in records:
        table.insert("", "end", values=(
            s["code"],
            s["name"],
            s["c1"],
            s["c2"],
            s["c3"],
            s["exam"],
            getTotal(s),
            f"{getPercentage(s):.1f}%",
            getGrade(s)
        ))

    scrollbar = ttk.Scrollbar(
        tableFrame,
        orient="vertical",
        command=table.yview
    )

    table.configure(yscrollcommand=scrollbar.set)

    table.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


# View all saved students
def viewAll():
    clearPanel()
    panelTitle("ALL STUDENTS")
    showTable(students)


# Search for one student using their code
def checkStudent():
    clearPanel()
    panelTitle("CHECK STUDENT")

    tk.Label(
        content,
        text="Enter Student Code",
        font=(FONT, 11),
        bg=LIGHT,
        fg=NAVY
    ).pack(pady=5)

    codeEntry = tk.Entry(content, font=(FONT, 12), width=25)
    codeEntry.pack(pady=5)

    result = tk.Frame(content, bg=LIGHT)
    result.pack(pady=15)

    def findStudent():
        for s in students:
            if s["code"] == codeEntry.get().strip():

                for widget in result.winfo_children():
                    widget.destroy()

                details = [
                    ("Student Name", s["name"]),
                    ("Student Code", s["code"]),
                    ("Coursework 1", s["c1"]),
                    ("Coursework 2", s["c2"]),
                    ("Coursework 3", s["c3"]),
                    ("Exam Marks", s["exam"]),
                    ("Total Marks", getTotal(s)),
                    ("Percentage", f"{getPercentage(s):.1f}%"),
                    ("Grade", getGrade(s))
                ]

                for label, value in details:
                    tk.Label(
                        result,
                        text=f"{label}: {value}",
                        font=(FONT, 11),
                        bg=LIGHT,
                        fg=NAVY
                    ).pack(anchor="w", pady=2)

                return

        messagebox.showerror("Not Found", "Student code not found.")

    actionButton(content, "CHECK STUDENT", findStudent).pack(pady=8)


# Search students by name or student code
def searchStudent():
    clearPanel()
    panelTitle("SEARCH STUDENT")

    tk.Label(
        content,
        text="Enter student name or code",
        font=(FONT, 11),
        bg=LIGHT,
        fg=NAVY
    ).pack(pady=5)

    searchEntry = tk.Entry(content, font=(FONT, 12), width=30)
    searchEntry.pack(pady=5)

    resultFrame = tk.Frame(content, bg=LIGHT)
    resultFrame.pack(fill="both", expand=True)

    def search():
        query = searchEntry.get().strip().lower()

        matches = [
            s for s in students
            if query in s["name"].lower()
            or query in s["code"].lower()
        ]

        for widget in resultFrame.winfo_children():
            widget.destroy()

        if matches:
            showTableInFrame(resultFrame, matches)
        else:
            tk.Label(
                resultFrame,
                text="No matching student found.",
                font=(FONT, 12),
                bg=LIGHT,
                fg=NAVY
            ).pack(pady=20)

    actionButton(content, "SEARCH", search).pack(pady=8)


# Display matching search results in a smaller table
def showTableInFrame(parent, records):
    columns = ("code", "name", "total", "percentage", "grade")

    table = ttk.Treeview(
        parent,
        columns=columns,
        show="headings",
        height=9
    )

    headings = ["Code", "Student Name", "Total", "Percentage", "Grade"]

    for col, heading in zip(columns, headings):
        table.heading(col, text=heading)
        table.column(col, anchor="center", width=135)

    for s in records:
        table.insert("", "end", values=(
            s["code"],
            s["name"],
            getTotal(s),
            f"{getPercentage(s):.1f}%",
            getGrade(s)
        ))

    table.pack(fill="both", expand=True, padx=15, pady=5)


# Find the student with the highest or lowest marks
def showTopStudent(highest=True):
    clearPanel()

    if not students:
        panelTitle("NO STUDENT RECORDS")
        return

    s = (max if highest else min)(students, key=getTotal)

    panelTitle("HIGHEST MARKS" if highest else "LOWEST MARKS")

    details = [
        ("Student Name", s["name"]),
        ("Student Code", s["code"]),
        ("Total Marks", f"{getTotal(s)} / 160"),
        ("Percentage", f"{getPercentage(s):.1f}%"),
        ("Grade", getGrade(s))
    ]

    for label, value in details:
        tk.Label(
            content,
            text=f"{label}: {value}",
            font=(FONT, 13, "bold"),
            bg=LIGHT,
            fg=NAVY
        ).pack(pady=7)


# Allow the user to choose how to sort student marks
def sortStudents():
    clearPanel()
    panelTitle("SORT STUDENTS")

    tk.Label(
        content,
        text="Choose how to arrange student marks",
        font=(FONT, 11),
        bg=LIGHT,
        fg=NAVY
    ).pack(pady=10)

    buttons = tk.Frame(content, bg=LIGHT)
    buttons.pack(pady=10)

    actionButton(
        buttons,
        "Ascending Order",
        lambda: displaySorted(False),
        GOLD
    ).pack(side="left", padx=10)

    actionButton(
        buttons,
        "Descending Order",
        lambda: displaySorted(True)
    ).pack(side="left", padx=10)


# Display the sorted student records
def displaySorted(descending):
    clearPanel()
    panelTitle("SORTED STUDENT RECORDS")

    records = sorted(
        students,
        key=getTotal,
        reverse=descending
    )

    showTable(records)


# Create reusable input fields for adding and updating students
def createFields(fieldNames):
    entries = {}

    form = tk.Frame(content, bg=LIGHT)
    form.pack(pady=5)

    for i, name in enumerate(fieldNames):
        row = i // 2
        col = (i % 2) * 2

        tk.Label(
            form,
            text=name,
            font=(FONT, 10, "bold"),
            bg=LIGHT,
            fg=NAVY
        ).grid(row=row, column=col, padx=8, pady=8, sticky="w")

        entry = tk.Entry(form, font=(FONT, 11), width=17)
        entry.grid(row=row, column=col + 1, padx=8, pady=8)

        entries[name] = entry

    return entries


# Validate the marks entered by the user
def readMark(entry, maximum):
    value = entry.get().strip()

    if not value.isdigit() or not 0 <= int(value) <= maximum:
        raise ValueError(f"Enter a mark between 0 and {maximum}.")

    return int(value)


# Add a new student record
def addStudent():
    clearPanel()
    panelTitle("ADD NEW STUDENT")

    fields = createFields([
        "Student Code",
        "Student Name",
        "Course 1 ( /20)",
        "Course 2 ( /20)",
        "Course 3 ( /20)",
        "Exam Marks ( /100)"
    ])

    def save():
        code = fields["Student Code"].get().strip()
        name = fields["Student Name"].get().strip()

        if not code or not name:
            messagebox.showerror("Error", "Enter the student code and name.")
            return

        if any(s["code"] == code for s in students):
            messagebox.showerror("Error", "Student code already exists.")
            return

        try:
            newStudent = {
                "code": code,
                "name": name,
                "c1": readMark(fields["Course 1 ( /20)"], 20),
                "c2": readMark(fields["Course 2 ( /20)"], 20),
                "c3": readMark(fields["Course 3 ( /20)"], 20),
                "exam": readMark(fields["Exam Marks ( /100)"], 100)
            }

        except ValueError as error:
            messagebox.showerror("Invalid Marks", str(error))
            return

        students.append(newStudent)
        saveStudents()

        messagebox.showinfo("Success", "Student added successfully.")
        viewAll()

    actionButton(
        content,
        "SAVE STUDENT",
        save,
        "#16834A"
    ).pack(pady=12)


# Update the marks of an existing student
def updateStudent():
    clearPanel()
    panelTitle("UPDATE STUDENT MARKS")

    fields = createFields([
        "Student Code",
        "Course 1 ( /20)",
        "Course 2 ( /20)",
        "Course 3 ( /20)",
        "Exam Marks ( /100)"
    ])

    def update():
        code = fields["Student Code"].get().strip()

        s = next(
            (x for x in students if x["code"] == code),
            None
        )

        if s is None:
            messagebox.showerror("Not Found", "Student code not found.")
            return

        try:
            s["c1"] = readMark(fields["Course 1 ( /20)"], 20)
            s["c2"] = readMark(fields["Course 2 ( /20)"], 20)
            s["c3"] = readMark(fields["Course 3 ( /20)"], 20)
            s["exam"] = readMark(fields["Exam Marks ( /100)"], 100)

        except ValueError as error:
            messagebox.showerror("Invalid Marks", str(error))
            return

        saveStudents()

        messagebox.showinfo("Success", "Marks updated successfully.")
        viewAll()

    actionButton(
        content,
        "UPDATE MARKS",
        update,
        "#16834A"
    ).pack(pady=12)


# Delete a student record using the student code
def deleteStudent():
    clearPanel()
    panelTitle("DELETE STUDENT")

    tk.Label(
        content,
        text="Enter Student Code",
        font=(FONT, 11),
        bg=LIGHT,
        fg=NAVY
    ).pack(pady=8)

    codeEntry = tk.Entry(content, font=(FONT, 12), width=25)
    codeEntry.pack(pady=5)

    def delete():
        code = codeEntry.get().strip()

        for s in students:
            if s["code"] == code:

                if messagebox.askyesno(
                    "Confirm Delete",
                    f"Delete {s['name']} from the records?"
                ):
                    students.remove(s)
                    saveStudents()

                    messagebox.showinfo("Success", "Student deleted.")
                    viewAll()

                return

        messagebox.showerror("Not Found", "Student code not found.")

    actionButton(
        content,
        "DELETE STUDENT",
        delete,
        "#A52A2A"
    ).pack(pady=12)


# Display the welcome page
def showHome():
    clearPanel()

    tk.Label(
        content,
        text="WELCOME TO STUDENT MANAGER",
        font=(FONT, 21, "bold"),
        bg=LIGHT,
        fg=NAVY
    ).pack(pady=(95, 15))

    tk.Label(
        content,
        text="Select an operation from the menu to manage student records.",
        font=(FONT, 12),
        bg=LIGHT,
        fg=NAVY
    ).pack(pady=5)

    tk.Label(
        content,
        text=f"Total Students: {len(students)}",
        font=(FONT, 15, "bold"),
        bg=LIGHT,
        fg=GOLD
    ).pack(pady=20)


# Store menu options and their related functions
menuItems = [
    ("View All Students", viewAll),
    ("Check Student", checkStudent),
    ("Search Student", searchStudent),
    ("Highest Marks", lambda: showTopStudent(True)),
    ("Lowest Marks", lambda: showTopStudent(False)),
    ("Sort Students", sortStudents),
    ("Add Student", addStudent),
    ("Update Marks", updateStudent),
    ("Delete Student", deleteStudent)
]

menuY = [211, 257, 301, 346, 390, 433, 477, 519, 558]
menuTextItems = []


# Create clickable text for each background oval
for (buttonText, command), y in zip(menuItems, menuY):

    textItem = canvas.create_text(
        145,
        y,
        text=buttonText,
        font=(FONT, 9, "bold"),
        fill=NAVY
    )

    canvas.tag_bind(
        textItem,
        "<Button-1>",
        lambda event, cmd=command: cmd()
    )

    canvas.tag_bind(
        textItem,
        "<Enter>",
        lambda event: canvas.config(cursor="hand2")
    )

    canvas.tag_bind(
        textItem,
        "<Leave>",
        lambda event: canvas.config(cursor="")
    )

    menuTextItems.append(textItem)


# Resize the background and all elements to fill the window
def resizeLayout(event):
    global backgroundPhoto

    width = event.width
    height = event.height

    if width < 1 or height < 1:
        return

    # Stretch the background image to the complete window size
    scaleX = width / 1100
    scaleY = height / 620

    resizedBackground = backgroundOriginal.resize(
        (width, height),
        Image.Resampling.LANCZOS
    )

    backgroundPhoto = ImageTk.PhotoImage(resizedBackground)
    canvas.itemconfig(backgroundItem, image=backgroundPhoto)
    canvas.coords(backgroundItem, 0, 0)

    # Resize and reposition the main heading
    canvas.coords(
        headingItem,
        550 * scaleX,
        55 * scaleY
    )

    canvas.itemconfig(
        headingItem,
        font=(FONT, max(16, int(25 * min(scaleX, scaleY))), "bold")
    )

    # Resize and reposition the menu heading
    canvas.coords(
        menuHeadingItem,
        145 * scaleX,
        151 * scaleY
    )

    canvas.itemconfig(
        menuHeadingItem,
        font=(FONT, max(9, int(12 * min(scaleX, scaleY))), "bold")
    )

    # Resize the right-side display panel
    canvas.coords(
        contentWindow,
        680 * scaleX,
        350 * scaleY
    )

    canvas.itemconfig(
        contentWindow,
        width=int(780 * scaleX),
        height=int(420 * scaleY)
    )

    # Keep each menu label centred on its background oval
    for textItem, y in zip(menuTextItems, menuY):
        canvas.coords(
            textItem,
            145 * scaleX,
            y * scaleY
        )

        canvas.itemconfig(
            textItem,
            font=(FONT, max(8, int(9 * min(scaleX, scaleY))), "bold")
        )


# Run the resize function whenever the window changes size
canvas.bind("<Configure>", resizeLayout)

# Display the welcome page
showHome()

# Start the Tkinter event loop
root.mainloop()




