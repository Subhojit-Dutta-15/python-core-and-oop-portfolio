"""
================================================================================
01. Python Fundamentals: Variables, Strings, Operators & Conditionals
================================================================================
Overview:
    Curated foundational examples covering Python data types, string methods,
    operators, conditional logic, and practical real-world calculators.

Key Concepts Covered:
    - String Manipulation: Slicing, case conversion, stripping, splitting
    - Operators & Ternary Expressions: Arithmetic, logical, and inline conditionals
    - Decision Making: Nested if-elif-else blocks (Electricity Bill, Grading, ATM)
"""

# ------------------------------------------------------------------------------
# 1. String Manipulation & Methods
# ------------------------------------------------------------------------------
"""
sample_text = "  Python Programming for AI & Data Science  "
cleaned = sample_text.strip()
print("Original:", repr(sample_text))
print("Cleaned :", cleaned)
print("Upper   :", cleaned.upper())
print("Words   :", cleaned.split())
print("Index of 'AI':", cleaned.find("AI"))
"""

# ------------------------------------------------------------------------------
# 2. Ternary & Compact Conditional Expressions
# ------------------------------------------------------------------------------
"""
age = int(input("Enter your age: "))
eligibility = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(eligibility)

salary = float(input("Enter annual salary: "))
tax_rate = (0.10, 0.20)[salary > 50000]
print(f"Applicable Tax: {salary * tax_rate:.2f}")
"""

# ------------------------------------------------------------------------------
# 3. Tiered Electricity Bill Calculator
# ------------------------------------------------------------------------------
"""
units = int(input("Enter electricity units consumed: "))
if units < 0:
    print("Invalid units entered.")
else:
    if units <= 100:
        energy_charge = units * 5
    elif units <= 200:
        energy_charge = units * 7
    elif units <= 300:
        energy_charge = units * 10
    else:
        energy_charge = units * 15

    fixed_charge = 50
    print(f"Units Consumed : {units}")
    print(f"Energy Charge  : {energy_charge}")
    print(f"Fixed Charge   : {fixed_charge}")
    print(f"Total Bill     : {energy_charge + fixed_charge}")
"""

# ------------------------------------------------------------------------------
# 4. Student Grade & Scholarship Eligibility Evaluator
# ------------------------------------------------------------------------------
"""
name = input("Enter student name: ")
age = int(input("Enter student age: "))
marks = int(input("Enter marks (0-100): "))

if not (0 <= marks <= 100):
    print("Invalid Marks.")
else:
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    elif marks >= 50:
        grade = "E"
    else:
        grade = "F"

    if grade in ("A", "B") or (grade in ("C", "D") and age <= 21):
        scholarship = "Eligible"
    else:
        scholarship = "Not Eligible"

    print("======== STUDENT REPORT ========")
    print(f"Name        : {name}")
    print(f"Marks/Grade : {marks} ({grade})")
    print(f"Scholarship : {scholarship}")
    print("================================")
"""
