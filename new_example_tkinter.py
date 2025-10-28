import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x450")
root.config(bg="#e3f2fd")

# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#e3f2fd", fg="#1565c0")
title_label.pack(pady=10)

# Entry field
task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", font=("Arial", 12), bg="#64b5f6", fg="white", command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", font=("Arial", 12), bg="#ef5350", fg="white", command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", font=("Arial", 12), bg="#81c784", fg="white", command=clear_tasks)
clear_button.grid(row=0, column=2, padx=5)

# Listbox for tasks
task_listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=10, selectbackground="#64b5f6", selectmode=tk.SINGLE)
task_listbox.pack(pady=20)

root.mainloop()
