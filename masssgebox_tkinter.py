import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200")

# Function to display message
def show_message():
    name = entry.get()
    if name:
        messagebox.showinfo("Greeting", f"Hello, {name}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name!")

# Create label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Create entry box
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

# Create button
button = tk.Button(root, text="Greet Me", command=show_message)
button.pack(pady=10)

# Run the application
root.mainloop()
