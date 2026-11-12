"""
Automated CSV Data Analyzer & Report Generator
An end-to-end data cleaning, profiling, and reporting pipeline built with pandas.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional
import pandas as pd


def create_sample_dataset(filepath: Path) -> None:
    """Generate a sample dataset containing duplicates and missing values for demonstration."""
    raw_data = {
        "Employee_ID": ["E101", "E102", "E103", "E104", "E105", "E102", "E106"],
        "Department": ["AI/ML", "Data Science", "Backend", "AI/ML", None, "Data Science", "Backend"],
        "Experience_Years": [2.0, 5.0, 3.0, None, 4.0, 5.0, 1.0],
        "Salary_INR": [850000, 1450000, 950000, 1200000, 1100000, 1450000, None],
        "Performance_Score": [4.6, 4.9, 4.1, 4.7, 4.3, 4.9, 3.8],
    }
    df = pd.DataFrame(raw_data)
    df.to_csv(filepath, index=False)


def clean_and_profile_dataset(
    input_csv: Path,
    cleaned_csv: Path = Path("cleaned_dataset.csv"),
    report_json: Path = Path("dataset_report.json"),
) -> Dict[str, Any]:
    """
    Load a CSV dataset, perform automated cleaning, compute summary statistics,
    and export both the cleaned dataset and a structured JSON profile report.
    """
    df_raw = pd.read_csv(input_csv)
    initial_rows = len(df_raw)
    missing_before = {col: int(val) for col, val in df_raw.isnull().sum().items()}

    # 1. Remove exact duplicate rows
    df_clean = df_raw.drop_duplicates().copy()
    duplicates_removed = initial_rows - len(df_clean)

    # 2. Impute missing values (median for numeric columns, 'Unknown' for categorical)
    for col in df_clean.columns:
        if pd.api.types.is_numeric_dtype(df_clean[col]):
            median_val = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(median_val)
        else:
            df_clean[col] = df_clean[col].fillna("Unknown")

    # 3. Compute numerical summary statistics
    numeric_summary: Dict[str, Dict[str, float]] = {}
    for col in df_clean.select_dtypes(include="number").columns:
        numeric_summary[col] = {
            "mean": round(float(df_clean[col].mean()), 2),
            "median": round(float(df_clean[col].median()), 2),
            "min": round(float(df_clean[col].min()), 2),
            "max": round(float(df_clean[col].max()), 2),
            "std": round(float(df_clean[col].std()), 2),
        }

    # 4. Compute categorical value distributions
    categorical_summary: Dict[str, Dict[str, int]] = {}
    for col in df_clean.select_dtypes(exclude="number").columns:
        if df_clean[col].nunique() <= 20:
            categorical_summary[col] = {
                str(k): int(v) for k, v in df_clean[col].value_counts().items()
            }

    # 5. Export cleaned data and JSON report
    df_clean.to_csv(cleaned_csv, index=False)

    report: Dict[str, Any] = {
        "source_file": str(input_csv),
        "cleaned_file": str(cleaned_csv),
        "row_counts": {
            "initial": initial_rows,
            "duplicates_removed": duplicates_removed,
            "final": len(df_clean),
        },
        "columns": list(df_clean.columns),
        "missing_values_imputed": missing_before,
        "numeric_summary": numeric_summary,
        "categorical_distributions": categorical_summary,
    }

    with report_json.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    return report


def run_pipeline(csv_path: Optional[str] = None) -> None:
    """Execute the end-to-end profiling workflow and print a summary."""
    target_path = Path(csv_path) if csv_path else Path("sample_engineering_data.csv")
    if not target_path.exists():
        print(f"No input file found at '{target_path}'. Generating sample dataset...")
        create_sample_dataset(target_path)

    report = clean_and_profile_dataset(target_path)

    print("\n================ DATASET PROFILE REPORT ================")
    print(f"Source File:         {report['source_file']}")
    print(f"Initial Rows:        {report['row_counts']['initial']}")
    print(f"Duplicates Removed:  {report['row_counts']['duplicates_removed']}")
    print(f"Final Clean Rows:    {report['row_counts']['final']}")
    print("\n--- Numeric Column Summaries ---")
    for col, stats in report["numeric_summary"].items():
        print(
            f"  {col}: Mean={stats['mean']} | Median={stats['median']} | "
            f"Min={stats['min']} | Max={stats['max']}"
        )
    print("\nOutputs saved to 'cleaned_dataset.csv' and 'dataset_report.json'.")
    print("========================================================")


if __name__ == "__main__":
    run_pipeline()
