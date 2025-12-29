from dataclasses import dataclass
from datetime import datetime

@dataclass
class Student:
    name: str
    roll_no: int
    course: str

    def display(self) -> None:
        print(f"Name   : {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Course : {self.course}")


def main() -> None:
    student = Student(
        name="Ayan",
        roll_no=101,
        course="B.Tech (Agri IT)"
    )

    print("Student Details")
    print("-" * 20)
    student.display()
    print("\nGenerated on:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))


if __name__ == "__main__":
    main()
