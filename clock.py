import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")

# Create a label to display the time
label = tk.Label(root, font=("Helvetica", 48, "bold"), bg="black", fg="cyan")
label.pack(anchor="center", expand=True)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  # update every 1 second

update_time()  # start the clock

root.mainloop()
