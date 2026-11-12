"""
Student Performance Management CLI
A persistent, type-hinted command-line application for managing student academic records.
"""

import json
from pathlib import Path
from typing import Callable, Dict, List, Optional, Any

DATA_FILE = Path("students_data.json")


def load_students(filepath: Path = DATA_FILE) -> List[Dict[str, Any]]:
    """Load student records from a JSON file if it exists."""
    if not filepath.exists():
        return []
    try:
        with filepath.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_students(students: List[Dict[str, Any]], filepath: Path = DATA_FILE) -> None:
    """Persist student records to a JSON file."""
    with filepath.open("w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)


def calculate_grade(average: float) -> str:
    """Return letter grade based on average percentage."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    if average >= 50:
        return "E"
    return "F"


def compute_statistics(student: Dict[str, Any]) -> Dict[str, Any]:
    """Compute total, average, min, max, grade, and pass/fail status for a student."""
    marks: List[float] = student.get("marks", [])
    if not marks:
        return {
            "total": 0.0,
            "average": 0.0,
            "highest": 0.0,
            "lowest": 0.0,
            "count": 0,
            "grade": "F",
            "status": "FAIL",
        }
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    return {
        "total": round(total, 2),
        "average": round(average, 2),
        "highest": max(marks),
        "lowest": min(marks),
        "count": len(marks),
        "grade": grade,
        "status": "PASS" if average >= 50 else "FAIL",
    }


def apply_score_transformation(
    marks: List[float], operation: Callable[[float], float]
) -> List[float]:
    """Apply a pure mathematical transformation across a list of marks."""
    return [round(operation(m), 2) for m in marks]


def find_student(
    students: List[Dict[str, Any]], name: str
) -> Optional[Dict[str, Any]]:
    """Case-insensitive lookup for a student by name."""
    target = name.strip().lower()
    for student in students:
        if student["name"].strip().lower() == target:
            return student
    return None


def prompt_int(message: str) -> Optional[int]:
    """Safely parse an integer from user input."""
    try:
        return int(input(message).strip())
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None


def add_student_interactive(students: List[Dict[str, Any]]) -> None:
    """Prompt user for details and append a validated student record."""
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if find_student(students, name):
        print(f"Student '{name}' already exists.")
        return

    age = prompt_int("Enter student age: ")
    if age is None or age <= 0:
        print("Age must be a positive integer.")
        return

    raw_marks = input("Enter marks separated by spaces (0-100): ").strip()
    try:
        marks = [float(x) for x in raw_marks.split()]
        if not marks or any(m < 0 or m > 100 for m in marks):
            print("Please enter at least one valid mark between 0 and 100.")
            return
    except ValueError:
        print("Invalid marks format. Use numbers separated by spaces.")
        return

    students.append({"name": name, "age": age, "marks": marks})
    save_students(students)
    print(f"Student '{name}' saved successfully.")


def view_all_students(students: List[Dict[str, Any]]) -> None:
    """Display all stored student records."""
    if not students:
        print("No student records found.")
        return
    print("\n===== ALL STUDENT RECORDS =====")
    for s in students:
        marks_str = ", ".join(map(str, s["marks"]))
        print(f"Name: {s['name']} | Age: {s['age']} | Marks: [{marks_str}]")


def display_student_stats(students: List[Dict[str, Any]]) -> None:
    """Search for a student and print their computed academic statistics."""
    name = input("Enter student name: ").strip()
    student = find_student(students, name)
    if not student:
        print("Student record not found.")
        return
    stats = compute_statistics(student)
    print(f"\n===== STATISTICS FOR {student['name'].upper()} =====")
    print(f"Total Marks:        {stats['total']}")
    print(f"Average Marks:      {stats['average']:.2f}")
    print(f"Highest Mark:       {stats['highest']}")
    print(f"Lowest Mark:        {stats['lowest']}")
    print(f"Subjects Count:     {stats['count']}")
    print(f"Grade:              {stats['grade']}")
    print(f"Status:             {stats['status']}")


def transform_student_marks(students: List[Dict[str, Any]]) -> None:
    """Preview functional transformations on a student's marks."""
    name = input("Enter student name: ").strip()
    student = find_student(students, name)
    if not student:
        print("Student record not found.")
        return

    print("\n1. Add +5 Bonus Marks (capped at 100)")
    print("2. Scale Marks by 1.1x (capped at 100)")
    choice = prompt_int("Select transformation (1-2): ")
    if choice == 1:
        transformed = apply_score_transformation(
            student["marks"], lambda x: min(100.0, x + 5)
        )
    elif choice == 2:
        transformed = apply_score_transformation(
            student["marks"], lambda x: min(100.0, x * 1.1)
        )
    else:
        print("Invalid selection.")
        return

    print(f"Original Marks:    {student['marks']}")
    print(f"Transformed Marks: {transformed}")


def main() -> None:
    """Main CLI event loop."""
    students = load_students()
    while True:
        print("\n==========================================")
        print("     STUDENT PERFORMANCE MANAGEMENT       ")
        print("==========================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student Statistics")
        print("4. Preview Marks Transformation")
        print("5. Exit")

        choice = prompt_int("Enter your choice (1-5): ")
        if choice == 1:
            add_student_interactive(students)
        elif choice == 2:
            view_all_students(students)
        elif choice == 3:
            display_student_stats(students)
        elif choice == 4:
            transform_student_marks(students)
        elif choice == 5:
            print("Exiting Student Performance Management. Goodbye!")
            break
        else:
            print("Please select an option between 1 and 5.")


if __name__ == "__main__":
    main()
