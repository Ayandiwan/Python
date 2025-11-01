import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(0, result)
        except Exception:
            screen.delete(0, tk.END)
            screen.insert(0, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry box
screen = tk.Entry(root, font="lucida 20 bold", borderwidth=5, relief=tk.SUNKEN, justify="right")
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# Buttons
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in button_texts:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for text in row:
        button = tk.Button(frame, text=text, font="lucida 15 bold", height=2, width=5)
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)

root.mainloop()
