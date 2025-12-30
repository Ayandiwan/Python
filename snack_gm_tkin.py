import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 500
SIZE = 20
SPEED = 120

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game - Tkinter")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.score = 0
        self.label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.label.pack()

        self.direction = "Right"
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()

        self.draw_snake()
        self.move_snake()

        root.bind("<Up>", lambda e: self.change_direction("Up"))
        root.bind("<Down>", lambda e: self.change_direction("Down"))
        root.bind("<Left>", lambda e: self.change_direction("Left"))
        root.bind("<Right>", lambda e: self.change_direction("Right"))

    def create_food(self):
        x = random.randrange(0, WIDTH, SIZE)
        y = random.randrange(0, HEIGHT, SIZE)
        return self.canvas.create_oval(x, y, x+SIZE, y+SIZE, fill="red")

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x, y, x+SIZE, y+SIZE,
                fill="green", tag="snake"
            )

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= SIZE
        elif self.direction == "Down":
            head_y += SIZE
        elif self.direction == "Left":
            head_x -= SIZE
        elif self.direction == "Right":
            head_x += SIZE

        new_head = (head_x, head_y)
        self.snake.insert(0, new_head)

        # Food collision
        food_coords = self.canvas.coords(self.food)
        if food_coords and head_x == food_coords[0] and head_y == food_coords[1]:
            self.canvas.delete(self.food)
            self.food = self.create_food()
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
        else:
            self.snake.pop()

        # Wall collision
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.game_over()
            return

        # Self collision
        if new_head in self.snake[1:]:
            self.game_over()
            return

        self.draw_snake()
        self.root.after(SPEED, self.move_snake)

    def change_direction(self, new_dir):
        opposites = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }
        if opposites.get(new_dir) != self.direction:
            self.direction = new_dir

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            WIDTH//2, HEIGHT//2,
            text=f"GAME OVER\nScore: {self.score}",
            fill="white", font=("Arial", 24)
        )

# Run game
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
