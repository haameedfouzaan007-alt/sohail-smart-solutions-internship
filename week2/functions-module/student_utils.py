# Utility functions for student records


def find_student(students, name):
    """
    Search for a student by name.

    Args:
        students (dict): Student records with names and universities.
        name (str): Name of the student to search.

    Returns:
        str or None: University name if the student is found, otherwise None.
    """
    if name in students:
        return students[name]
    else:
        return None


def add_student(students, name, university):
    """
    Add a new student to the student records.

    Args:
        students (dict): Student records.
        name (str): Name of the student.
        university (str): University of the student.

    Returns:
        dict: Updated student records.
    """
    students[name] = university
    return students


def unique_universities(students):
    """
    Find all unique universities from the student records.

    Args:
        students (dict): Student records.

    Returns:
        set: A set of unique university names.
    """
    return set(students.values())