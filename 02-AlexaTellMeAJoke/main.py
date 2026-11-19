
import tkinter as tk

# AI assistance acknowledgement:
# Tool: ChatGPT (OpenAI)
# Purpose: Assistance with developing a Tkinter joke application.

# Colour theme
NAVY = "#172554"
LIGHT_GREY = "#F0F4F8"
WHITE = "#FFFFFF"

# Font settings
FONT = "Segoe UI"

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
