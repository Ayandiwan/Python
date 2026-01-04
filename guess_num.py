import random

number = random.randint(1, 10)

print("🎮 Guess the number between 1 and 10")

guess = int(input("Your guess: "))

if guess == number:
    print("🎉 Congratulations! You guessed right.")
else:
    print("❌ Wrong guess!")
    print("The correct number was:", number)
