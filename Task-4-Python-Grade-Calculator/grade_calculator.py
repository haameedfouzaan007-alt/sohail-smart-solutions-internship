# Grade Calculator
# This program takes marks for three subjects and calculates the total, average, and grade.

# Get marks from the user
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Check if the entered marks are valid(1 to 100)
if subject1 < 0 or subject1 > 100 or subject2 < 0 or subject2 > 100 or subject3 < 0 or subject3 > 100:
    print("Invalid input. Marks should be between 0 and 100.")
else:
    # Calculate total and average
    total = subject1 + subject2 + subject3
    average = total / 3

    # Decide the grade based on the average
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    # Show the final result
    print("\n-----Grade Calculator Result -----")
    print("Total Marks:", total)
    print("Average:", average)
    print("Grade:", grade)



 