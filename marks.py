# Student Marks and Result Program

name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 60:
    print("Result: First Class")
elif percentage >= 50:
    print("Result: Second Class")
elif percentage >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")
