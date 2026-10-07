from pathlib import Path

from analyzer import (
    get_class_summary,
    get_highest_performing_student,
    get_students_needing_improvement,
    load_and_analyze_students,
)


def main() -> None:
    csv_path = Path(__file__).with_name("students.csv")

    try:
        students = load_and_analyze_students(csv_path)
    except (OSError, ValueError) as error:
        print(f"Could not analyze student data: {error}")
        return

    print("STUDENT PERFORMANCE REPORT")
    print("=" * 80)
    print(students.to_string(index=False))

    top_student = get_highest_performing_student(students)
    print("\nHighest-performing student:")
    print(
        f"{top_student['Student']} - average {top_student['Average']:.2f}, "
        f"grade {top_student['Grade']}"
    )

    students_to_help = get_students_needing_improvement(students)
    print("\nStudents needing improvement (average below 50):")
    if students_to_help.empty:
        print("None")
    else:
        for _, student in students_to_help.iterrows():
            print(f"{student['Student']} - average {student['Average']:.2f}")

    summary = get_class_summary(students)
    print("\nClass summary:")
    print(f"Students analyzed: {summary['student_count']}")
    print(f"Class average: {summary['class_average']:.2f}")
    print(f"Highest student average: {summary['highest_average']:.2f}")
    print(f"Students needing improvement: {summary['improvement_count']}")


if __name__ == "__main__":
    main()
