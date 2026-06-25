import pandas as pd


def run_analysis(filename):
    try:
        df = pd.read_csv(filename)

        print("\nStudent Analytics Results")
        print("-------------------------")

        print("\n1. Average Grade Per Course:")
        average_per_course = df.groupby("course")["grade"].mean()
        print(average_per_course)

        print("\n2. Top Student:")
        top_student = df.loc[df["grade"].idxmax()]
        print(f"{top_student['name']} scored the highest grade: {top_student['grade']}")

        print("\n3. Number of Students Per Course:")
        student_count = df["course"].value_counts()
        print(student_count)

        print("\n4. Students Who Scored Above 80:")
        students_above_80 = df[df["grade"] > 80]
        print(students_above_80[["name", "course", "grade"]])

    except FileNotFoundError:
        print("Error: CSV file not found. Please export the data first.")

    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")

    except KeyError:
        print("Error: Required column is missing from the CSV file.")

    except Exception as error:
        print("Unexpected error:", error)