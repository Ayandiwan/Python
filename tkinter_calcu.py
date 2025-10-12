import tkinter as tk

# Function to update the expression
def press(num):
    entry_field.insert(tk.END, str(num))

# Function to evaluate the expression
def equal():
    try:
        result = str(eval(entry_field.get()))
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except Exception:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Function to clear the entry
def clear():
    entry_field.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry_field = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify='right')
entry_field.pack(pady=10, padx=10, fill="x")

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(frame, text=text, width=5, height=2, font=("Arial", 16),
                  command=equal, bg="#00b894", fg="white").grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(frame, text=text, width=5, height=2, font=("Arial", 16),
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text="Clear", font=("Arial", 14), bg="#d63031", fg="white", command=clear)\
    .pack(fill="x", padx=10, pady=10)

# Run the app
root.mainloop()
