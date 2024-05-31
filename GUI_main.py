import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms

# Improved UI design elements
background_color = "#f0f0f0"  # Light gray
button_color = "#4CAF50"  # Green

root = tk.Tk()
root.configure(background=background_color)

# ... (other elements and code)

# Enhanced button styles
button1 = tk.Button(
    frame_alpr,
    text="Login",
    command=log,
    width=10,
    height=1,
    font=("Arial", 20, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_color,  # Hover effect
    activeforeground="black",
    cursor="hand2"  # Change cursor on hover
)
button2 = tk.Button(
    frame_alpr,
    text="Register",
    command=reg,
    width=10,
    height=1,
    font=("Arial", 20, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_color,
    activeforeground="black",
    cursor="hand2"
)

# ... (other buttons and layout)

root.mainloop()
