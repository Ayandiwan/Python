# Student Result Management System

students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks (out of 100): "))

    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students[roll] = {
        "Name": name,
        "Marks": marks,
        "Grade": grade
    }
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("❌ No student records found.\n")
        return

    print("\n--- Student Records ---")
    for roll, info in students.items():
        print(f"Roll No: {roll}")
        print(f"Name   : {info['Name']}")
        print(f"Marks  : {info['Marks']}")
        print(f"Grade  : {info['Grade']}")
        print("----------------------")
    print()

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("👋 Program exited")
        break
    else:
        print("⚠️ Invalid choice, try again.\n")
