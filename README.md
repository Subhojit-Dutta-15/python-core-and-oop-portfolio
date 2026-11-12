![Python CI](https://github.com/Subhojit-Dutta-15/python-core-and-oop-portfolio/actions/workflows/tests.yml/badge.svg)

# Python Core, OOP & Data Engineering Portfolio

A structured, production-styled collection of Python fundamentals, object-oriented design patterns, CLI applications, automated `pytest` suites, and `pandas` data pipelines.

## Repository Architecture

| File / Path | Domain | Key Concepts & Implementation |
| :--- | :--- | :--- |
| `01_python_fundamentals.py` | Core Syntax & Logic | String manipulation, inline conditionals, tiered electricity billing, grade evaluation |
| `02_data_structures.py` | Collections & Algorithms | Palindrome verification, O(n) Two-Sum hash map, list comprehensions, set theory, nested dicts |
| `03_functions_and_recursion.py` | Functional Programming | `*args`/`**kwargs` reporting, `nonlocal` closures, higher-order lambdas, recursion |
| `04_oop_concepts.py` | Object-Oriented Design | Encapsulation (`__private`), inheritance & `super()`, `@classmethod`/`@property`, dunder overloading |
| `05_applied_python_and_projects.py` | Applied Python | File I/O text processing, `secrets` password generation, raw `socket` HTTP client |
| `student_performance_cli.py` | Featured CLI App | Type-hinted student management system with JSON persistence and input validation |
| `csv_data_analyzer.py` | Data Engineering Mini-Project | Automated `pandas` cleaning pipeline (deduplication, imputation, JSON/CSV reporting) |
| `test_student_performance.py` | Automated Testing | `pytest` unit test suite validating calculations, grade boundaries, and persistence |
| `.github/workflows/tests.yml` | CI/CD Pipeline | GitHub Actions workflow running `pytest` automatically on every push |

## Quickstart

1. **Clone the repository**
   ```bash
   git clone https://github.com/Subhojit-Dutta-15/python-core-and-oop-portfolio.git
   cd python-core-and-oop-portfolio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the featured projects or test suite**
   ```bash
   python student_performance_cli.py
   python csv_data_analyzer.py
   pytest -v
   ```
