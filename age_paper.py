import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("User Information Form")
root.geometry("350x350")

def calculate_age():
    fname = first_name.get()
    lname = last_name.get()
    gender = gender_var.get()

    if fname == "" or lname == "" or gender == "":
        messagebox.showerror("Error", "All fields are required")
        return

    # ---------- NO TRY-EXCEPT → USE isdigit() ----------
    if not (birth_day.get().isdigit() and
            birth_month.get().isdigit() and
            birth_year.get().isdigit()):
        messagebox.showerror("Error", "Birth date must be numbers only!")
        return
    # ----------------------------------------------------

    bd = int(birth_day.get())
    bm = int(birth_month.get())
    by = int(birth_year.get())

    # basic validation
    if not (1 <= bd <= 31):
        messagebox.showerror("Error", "Invalid day value!")
        return

    if not (1 <= bm <= 12):
        messagebox.showerror("Error", "Invalid month value!")
        return

    if by <= 1900:
        messagebox.showerror("Error", "Invalid birth year!")
        return

    # fixed today
    td = 24
    tm = 11
    ty = 2025

    # age logic
    age = ty - by
    if (tm, td) < (bm, bd):
        age -= 1

    lbl_result.config(text=f"Hello {fname} {lname}\nYour age is {age} years.")

# UI
tk.Label(root, text="First Name").pack()
first_name = tk.Entry(root)
first_name.pack()

tk.Label(root, text="Last Name").pack()
last_name = tk.Entry(root)
last_name.pack()

gender_var = tk.StringVar()
tk.Label(root, text="Gender").pack()

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Birth Day").pack()
birth_day = tk.Entry(root)
birth_day.pack()

tk.Label(root, text="Birth Month").pack()
birth_month = tk.Entry(root)
birth_month.pack()

tk.Label(root, text="Birth Year").pack()
birth_year = tk.Entry(root)
birth_year.pack()

tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

lbl_result = tk.Label(root, text="", font=("Arial", 12))
lbl_result.pack()

root.mainloop()
