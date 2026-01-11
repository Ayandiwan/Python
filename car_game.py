import tkinter as tk
import random

# window
root = tk.Tk()
root.title("Car Racing Game")
root.geometry("400x600")
root.resizable(False, False)

canvas = tk.Canvas(root, width=400, height=600, bg="gray")
canvas.pack()

# road lines
for i in range(0, 600, 100):
    canvas.create_line(200, i, 200, i+50, fill="white", width=5)

# player car
player = canvas.create_rectangle(170, 500, 230, 580, fill="blue")

# enemy car
enemy = canvas.create_rectangle(170, 0, 230, 80, fill="red")

speed = 5
score = 0

score_text = canvas.create_text(50, 20, text="Score: 0", fill="white", font=("Arial", 12))

# move player
def move_left(event):
    if canvas.coords(player)[0] > 0:
        canvas.move(player, -20, 0)

def move_right(event):
    if canvas.coords(player)[2] < 400:
        canvas.move(player, 20, 0)

# game loop
def move_enemy():
    global score, speed
    canvas.move(enemy, 0, speed)
    if canvas.coords(enemy)[3] > 600:
        x = random.randint(50, 350)
        canvas.coords(enemy, x-30, 0, x+30, 80)
        score += 1
        canvas.itemconfig(score_text, text="Score: " + str(score))
        speed += 0.2

    # collision check
    p = canvas.coords(player)
    e = canvas.coords(enemy)
    if not (p[2] < e[0] or p[0] > e[2] or p[3] < e[1] or p[1] > e[3]):
        canvas.create_text(200, 300, text="GAME OVER", fill="yellow", font=("Arial", 24))
        return

    root.after(30, move_enemy)

# key binding
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

move_enemy()
root.mainloop()
