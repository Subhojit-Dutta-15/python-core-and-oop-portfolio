"""
================================================================================
03. Functions, Closures, Lambdas & Recursion
================================================================================
Overview:
    Modular programming patterns in Python demonstrating flexible function
    signatures, stateful closures, higher-order functions, and recursion.

Key Concepts Covered:
    - Flexible Parameters: Default arguments, *args, and **kwargs
    - Closures: Stateful inner functions using the nonlocal keyword
    - Functional Programming: Lambda expressions passed as higher-order callbacks
    - Recursion: Base cases and recurrence relations (factorial, digit sum, power)
"""

# ------------------------------------------------------------------------------
# 1. *args and **kwargs Student Result Generator
# ------------------------------------------------------------------------------
"""
def generate_student_report(name, *marks, **details):
    avg = sum(marks) / len(marks) if marks else 0.0
    print(f"===== Student Report: {name} =====")
    for key, val in details.items():
        print(f"{key.capitalize()}: {val}")
    print(f"Marks  : {marks}")
    print(f"Average: {avg:.2f}")
    print("=" * 34)

generate_student_report("Subhojit", 90, 95, 100, age=21, city="Kolkata", branch="CSE")
"""

# ------------------------------------------------------------------------------
# 2. Stateful Closure Using nonlocal
# ------------------------------------------------------------------------------
"""
def create_score_tracker(step=10):
    score = 0
    def increment():
        nonlocal score
        score += step
        return score
    return increment

player_one = create_score_tracker(10)
print("Score 1:", player_one())
print("Score 2:", player_one())
"""

# ------------------------------------------------------------------------------
# 3. Higher-Order Functions & Lambdas
# ------------------------------------------------------------------------------
"""
def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

nums = [10, 20, 30, 40, 50]
print("Doubled :", apply_operation(nums, lambda x: x * 2))
print("Squared :", apply_operation(nums, lambda x: x ** 2))
print("Plus 10 :", apply_operation(nums, lambda x: x + 10))
"""

# ------------------------------------------------------------------------------
# 4. Classic Recursive Algorithms
# ------------------------------------------------------------------------------
"""
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def sum_of_digits(n):
    return 0 if n == 0 else (n % 10) + sum_of_digits(n // 10)

def power(base, exp):
    return 1 if exp == 0 else base * power(base, exp - 1)

print("Factorial(5)       :", factorial(5))
print("Sum of digits(1234):", sum_of_digits(1234))
print("Power(2, 5)        :", power(2, 5))
"""
