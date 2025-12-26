import sqlite3

# ------------------ Database Connection ------------------
def connect_db():
    return sqlite3.connect("student.db")

# ------------------ Create Table ------------------
def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            marks INTEGER
        )
    """)
    conn.commit()
    conn.close()

# ------------------ INSERT (CREATE) ------------------
def insert_student():
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (name, course, marks)
        VALUES (?, ?, ?)
    """, (name, course, marks))
    conn.commit()
    conn.close()
    print("✅ Student added successfully")

# ------------------ SELECT (READ) ------------------
def view_students():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    if not rows:
        print("⚠ No records found")
    else:
        print("\nID  Name        Course        Marks")
        print("--------------------------------------")
        for row in rows:
            print(row[0], row[1], row[2], row[3])

    conn.close()

# ------------------ UPDATE ------------------
def update_student():
    sid = int(input("Enter Student ID to Update: "))
    new_marks = int(input("Enter New Marks: "))

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET marks = ?
        WHERE id = ?
    """, (new_marks, sid))

    if cur.rowcount == 0:
        print("❌ Student not found")
    else:
        print("✅ Record updated")

    conn.commit()
    conn.close()

# ------------------ DELETE ------------------
def delete_student():
    sid = int(input("Enter Student ID to Delete: "))

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (sid,))

    if cur.rowcount == 0:
        print("❌ Student not found")
    else:
        print("✅ Record deleted")

    conn.commit()
    conn.close()

# ------------------ MAIN MENU ------------------
def menu():
    create_table()

    while True:
        print("\n===== STUDENT DATABASE MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            insert_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid choice")

# ------------------ Run Program ------------------
menu()
