from pathlib import Path

import pandas as pd


SUBJECT_COLUMNS = ["Math", "Science", "English"]
REQUIRED_COLUMNS = ["Student", *SUBJECT_COLUMNS]


def load_and_analyze_students(csv_path: str | Path) -> pd.DataFrame:
    """Load student marks and add total, average, and grade columns."""
    students = pd.read_csv(csv_path)

    missing_columns = [
        column for column in REQUIRED_COLUMNS if column not in students.columns
    ]
    if missing_columns:
        raise ValueError(f"CSV is missing required columns: {', '.join(missing_columns)}")
    if students.empty:
        raise ValueError("The CSV does not contain any students.")

    for subject in SUBJECT_COLUMNS:
        students[subject] = pd.to_numeric(students[subject], errors="raise")

    if ((students[SUBJECT_COLUMNS] < 0) | (students[SUBJECT_COLUMNS] > 100)).any().any():
        raise ValueError("Marks must be between 0 and 100.")

    students["Total"] = students[SUBJECT_COLUMNS].sum(axis=1)
    students["Average"] = students[SUBJECT_COLUMNS].mean(axis=1).round(2)
    students["Grade"] = students["Average"].apply(assign_grade)
    return students


def assign_grade(average: float) -> str:
    """Return a letter grade for an average mark out of 100."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def get_highest_performing_student(students: pd.DataFrame) -> pd.Series:
    """Return the student with the highest average mark."""
    return students.loc[students["Average"].idxmax()]


def get_students_needing_improvement(students: pd.DataFrame) -> pd.DataFrame:
    """Return students whose average mark is below 50."""
    return students.loc[students["Average"] < 50]


def get_class_summary(students: pd.DataFrame) -> dict[str, int | float]:
    """Calculate a few useful class-wide performance figures."""
    return {
        "student_count": len(students),
        "class_average": round(float(students["Average"].mean()), 2),
        "highest_average": float(students["Average"].max()),
        "improvement_count": len(get_students_needing_improvement(students)),
    }
