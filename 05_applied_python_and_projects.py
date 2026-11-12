"""
================================================================================
05. File I/O, Networking, Security Utilities & CLI Capstone Projects
================================================================================
Overview:
    Practical applied Python scripts showcasing file handling, cryptographic
    password generation, HTTP socket requests, basic Pandas DataFrame analysis,
    and full menu-driven CLI applications.

Key Concepts Covered:
    - File I/O: Safe context managers (with open), search/replace, and parsing
    - Security & Networking: Cryptographic passwords (secrets) & raw HTTP sockets
    - Data Analysis: Pandas DataFrame creation, loc/iloc indexing, and filtering
    - CLI Applications: Interactive ATM, Number Guessing Game, Shopping & Student Systems
"""

import os
import random
import secrets
import socket
import string


# ------------------------------------------------------------------------------
# 1. File I/O: Search, Replace & Number Parity Parser
# ------------------------------------------------------------------------------
def file_io_demo():
    filename = "practice_io.txt"
    with open(filename, "w") as f:
        f.write("Hi everyone.\nWe are learning file I/O using Java.\nI like Java.")

    with open(filename, "r") as f:
        updated = f.read().replace("Java", "Python")

    with open(filename, "w") as f:
        f.write(updated)

    with open(filename, "r") as f:
        for line_no, line in enumerate(f, start=1):
            if "learning" in line:
                print(f"'learning' found on line {line_no}")

    os.remove(filename)


# ------------------------------------------------------------------------------
# 2. Cryptographic Password Generator (secrets module)
# ------------------------------------------------------------------------------
def generate_secure_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))


# ------------------------------------------------------------------------------
# 3. Raw HTTP Socket Client
# ------------------------------------------------------------------------------
def fetch_http_text():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
        mysock.connect(("data.pr4e.org", 80))
        cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if not data:
                break
            print(data.decode(), end="")


# ------------------------------------------------------------------------------
# 4. Pandas DataFrame Indexing & Filtering Demo
# ------------------------------------------------------------------------------
def pandas_dataframe_demo():
    import pandas as pd

    songs_data = {
        "Songs": ["Thriller", "Back in Black", "Dark Side of the Moon", "The Bodyguard"],
        "Released": [1982, 1980, 1973, 1992],
        "Length": [42, 43, 45, 57],
    }
    df = pd.DataFrame(songs_data, index=["a", "b", "c", "d"])
    print(df)
    print("\nSongs released after 1979:\n", df[df["Released"] > 1979])
    print("\nSliced via loc:\n", df.loc["a":"b", "Songs":"Released"])


# ------------------------------------------------------------------------------
# 5. CLI Capstone: Student Performance Management System
# ------------------------------------------------------------------------------
def student_management_cli():
    students = []

    while True:
        print("\n========== STUDENT PERFORMANCE SYSTEM ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Student Statistics")
        print("4. Apply Curve / Operation to Marks")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            name = input("Student Name: ").strip()
            age = int(input("Student Age : "))
            marks = [float(x) for x in input("Enter marks (space-separated): ").split()]
            students.append({"Name": name, "Age": age, "Marks": marks})
            print(f"Added {name}.")

        elif choice == "2":
            if not students:
                print("No records found.")
            for s in students:
                print(f"Name: {s['Name']} | Age: {s['Age']} | Marks: {s['Marks']}")

        elif choice == "3":
            target = input("Enter student name: ").strip().lower()
            match = next((s for s in students if s["Name"].lower() == target), None)
            if not match or not match["Marks"]:
                print("Student or marks not found.")
                continue
            m = match["Marks"]
            avg = sum(m) / len(m)
            print(f"Total: {sum(m):.2f} | Avg: {avg:.2f} | High: {max(m)} | Low: {min(m)} | Status: {'PASS' if avg >= 50 else 'FAIL'}")

        elif choice == "4":
            target = input("Enter student name: ").strip().lower()
            match = next((s for s in students if s["Name"].lower() == target), None)
            if not match:
                print("Student not found.")
                continue
            bonus = float(input("Enter bonus marks to add: "))
            match["Marks"] = [min(100.0, x + bonus) for x in match["Marks"]]
            print("Updated Marks:", match["Marks"])

        elif choice == "5":
            print("Exiting Student Performance System.")
            break
        else:
            print("Invalid choice.")


# ------------------------------------------------------------------------------
# 6. CLI Mini-Project: Number Guessing Game with Dynamic Hints
# ------------------------------------------------------------------------------
def number_guessing_game():
    target = random.randint(1, 100)
    attempts = 0
    print("Guess a number between 1 and 100 (10 attempts max)!")

    while attempts < 10:
        guess = int(input("Your guess: "))
        if not (1 <= guess <= 100):
            print("Please stay within 1 to 100.")
            continue
        attempts += 1
        if guess == target:
            print(f"Correct! You won in {attempts} attempts.")
            return
        print("Too low!" if guess < target else "Too high!")
        if attempts == 3:
            print(f"Hint: The number is {'Even' if target % 2 == 0 else 'Odd'}.")

    print(f"Game over! The number was {target}.")


if __name__ == "__main__":
    print("Sample Secure Password:", generate_secure_password(16))
    file_io_demo()
