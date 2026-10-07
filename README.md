# Student Performance Analyzer

A beginner-friendly command-line application that analyzes student marks from a CSV file using pandas.

## Features

- Calculates each student's total and average across Math, Science, and English.
- Assigns grades based on the average: A (90+), B (80-89), C (70-79), D (60-69), or F (below 60).
- Identifies the student with the highest average.
- Lists students with an average below 50 who may need improvement.
- Displays a class summary with the class average and student counts.
- Checks that the input includes the required columns and marks are between 0 and 100.

## Installation

1. Install Python 3.10 or newer.
2. (Optional) Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   On macOS or Linux, activate it with `source .venv/bin/activate`.
3. Install the dependency:

   ```text
   pip install -r requirements.txt
   ```

## Run

Keep `students.csv` next to `app.py`, then run:

```text
python app.py
```

The CSV must have `Student`, `Math`, `Science`, and `English` columns. Marks should be numbers from 0 to 100. A sample file with 10 students is included.
