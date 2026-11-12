"""
Automated pytest suite for student_performance_cli.py
Run with: pytest -v
"""

from pathlib import Path
from student_performance_cli import (
    apply_score_transformation,
    calculate_grade,
    compute_statistics,
    find_student,
    load_students,
    save_students,
)


def test_calculate_grade_boundaries() -> None:
    assert calculate_grade(95.0) == "A"
    assert calculate_grade(80.0) == "B"
    assert calculate_grade(72.5) == "C"
    assert calculate_grade(60.0) == "D"
    assert calculate_grade(50.0) == "E"
    assert calculate_grade(49.9) == "F"


def test_compute_statistics_pass_and_fail() -> None:
    passing_student = {"name": "Subhojit", "age": 21, "marks": [90.0, 80.0, 100.0]}
    stats = compute_statistics(passing_student)
    assert stats["total"] == 270.0
    assert stats["average"] == 90.0
    assert stats["highest"] == 100.0
    assert stats["lowest"] == 80.0
    assert stats["grade"] == "A"
    assert stats["status"] == "PASS"

    failing_student = {"name": "Alex", "age": 20, "marks": [30.0, 40.0]}
    fail_stats = compute_statistics(failing_student)
    assert fail_stats["average"] == 35.0
    assert fail_stats["status"] == "FAIL"


def test_compute_statistics_empty_marks() -> None:
    empty_student = {"name": "Empty", "age": 19, "marks": []}
    stats = compute_statistics(empty_student)
    assert stats["total"] == 0.0
    assert stats["status"] == "FAIL"


def test_apply_score_transformation() -> None:
    marks = [70.0, 98.0]
    boosted = apply_score_transformation(marks, lambda x: min(100.0, x + 5))
    assert boosted == [75.0, 100.0]


def test_find_student_case_insensitive() -> None:
    records = [{"name": "Subhojit Dutta", "age": 21, "marks": [95.0]}]
    assert find_student(records, "  subhojit dutta ") is not None
    assert find_student(records, "Unknown") is None


def test_json_persistence(tmp_path: Path) -> None:
    test_file = tmp_path / "test_students.json"
    sample_data = [{"name": "Priya", "age": 22, "marks": [88.0, 92.0]}]

    save_students(sample_data, filepath=test_file)
    loaded = load_students(filepath=test_file)

    assert loaded == sample_data
