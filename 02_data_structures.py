"""
================================================================================
02. Data Structures: Lists, Tuples, Sets & Dictionaries
================================================================================
Overview:
    Clean implementations of Python's four built-in collection types, including
    algorithmic problem-solving (Two Sum, Palindrome check) and comprehensions.

Key Concepts Covered:
    - Lists & Comprehensions: Slicing, sorting, Palindrome verification, Two Sum
    - Tuples: Immutable records, unpacking, frequency analysis
    - Sets: Union, intersection, difference, symmetric difference, deduplication
    - Dictionaries: Nested schemas, dictionary comprehensions, data aggregation
"""

# ------------------------------------------------------------------------------
# 1. Lists: Palindrome Check & Two-Sum Algorithm
# ------------------------------------------------------------------------------
"""
# Palindrome List Verification
items = [1, "abc", "abc", 1]
if items == items[::-1]:
    print(f"{items} is a Palindrome list.")
else:
    print(f"{items} is NOT a Palindrome list.")

# Optimal O(n) Two-Sum Using Hash Map
nums = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        print(f"Two-Sum Indices for target {target}: {[seen[complement], i]}")
        break
    seen[num] = i
"""

# ------------------------------------------------------------------------------
# 2. List Comprehensions: Dynamic Cart & Price Filtering
# ------------------------------------------------------------------------------
"""
cart = [250, 1200, 450, 80, 999, 150, 2000, 350]
budget_items = [p for p in cart if p <= 500]
premium_items = [p for p in cart if p > 500]
final_prices = [round(p * 0.95, 2) if p <= 500 else round(p * 0.85, 2) for p in cart]

print("Budget Items :", budget_items)
print("Premium Items:", premium_items)
print("Final Prices :", final_prices)
print(f"Cart Total After Tiered Discount: {sum(final_prices):.2f}")
"""

# ------------------------------------------------------------------------------
# 3. Sets: Multi-Course Enrollment Analyzer
# ------------------------------------------------------------------------------
"""
python_students = {"Subhojit", "Anu", "Riya", "Esha", "Rahul", "Amit"}
ml_students = {"Subhojit", "Riya", "Sayani", "Rahul", "Amit"}
sql_students = {"Subhojit", "Anu", "Sayani", "Esha", "Amit"}

all_students = python_students | ml_students | sql_students
print("Total Unique Students   :", len(all_students))
print("Enrolled in All Three   :", python_students & ml_students & sql_students)
print("Python Only (Not ML)    :", python_students - ml_students)
print("Either Python or ML     :", python_students ^ ml_students)
"""

# ------------------------------------------------------------------------------
# 4. Dictionaries: Relational Student & Course Analytics
# ------------------------------------------------------------------------------
"""
students = [("S101", "Subhojit"), ("S102", "Rahul"), ("S103", "Amit"), ("S104", "Priya")]
enrollments = {
    "S101": ["Python", "SQL", "Machine Learning"],
    "S102": ["Python", "Java"],
    "S103": ["Python", "SQL"],
    "S104": ["Java", "Machine Learning"],
}
marks = {"S101": 92, "S102": 76, "S103": 48, "S104": 85}

student_map = dict(students)
all_courses = [c for courses in enrollments.values() for c in courses]
course_counts = {c: all_courses.count(c) for c in set(all_courses)}
top_students = {sid: m for sid, m in marks.items() if m >= 80}
topper_id = max(marks, key=marks.get)

print("Course Popularity :", course_counts)
print("Top Scorers (>=80):", top_students)
print(f"Class Topper      : {student_map[topper_id]} ({marks[topper_id]})")
"""
