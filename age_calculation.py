from datetime import date

# Take birth date input
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Get today's date
today = date.today()

# Calculate age
age = today.year - birth_year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

# Display result
print(f"You are {age} years old.")
