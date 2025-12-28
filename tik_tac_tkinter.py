import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game variables
current_player = "X"
buttons = [[None]*3 for _ in range(3)]

# Function to check winner
def check_winner():
    for i in range(3):
        # Check rows and columns
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

# Check for draw
def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# Button click function
def on_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""

# Create buttons
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            root,
            text="",
            font=("Arial", 24),
            width=6,
            height=3,
            command=lambda r=i, c=j: on_click(r, c)
        )
        buttons[i][j].grid(row=i, column=j)

# Run the app
root.mainloop()
