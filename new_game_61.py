import random

number = random.randint(1, 50)
attempts = 0

print("🎮 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("📉 Too Low!")
    elif guess > number:
        print("📈 Too High!")
    else:
        print("🎉 Correct! You won in", attempts, "attempts.")
        break
