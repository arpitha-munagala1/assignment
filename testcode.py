import csv # In order to handle reading data, import the CSV module.

# Global parallel arrays to hold various student data fields
student_id = []  # Student numbers are stored as integers.
name = []  # stores Student names.
email = []  # stores email id of students
year = []  # stores year of enrolment
course = []  # stores course/module names
qualification = []  # Stores level of study (e.g., Diploma, Bachelor)
study_mode = []  # stores learning modes, like as on-campus and online.
fees = []  # Stores fees as integers

def load_data(filename):
    """ loads student data into the parallel arrays from the designated CSV file.
        There is a header row in the CSV file that will be skipped."""
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        # Append values to the respective arrays by iterating through each row.
        for row in reader:
            student_id.append(int(row[0]))  # Convert student ID to int
            name.append(row[1])  # Student name
            email.append(row[2])  # Email ID
            year.append(int(row[3]))  # Enrolment year as int
            course.append(row[4])  # Course/module name
            qualification.append(row[6])  # Level of study
            study_mode.append(row[5])  # Mode of delivery
            fees.append(int(row[7]))  # Fees as int

def display_table():
    """ Displays the student data in formatted table. """
    # Print the table header
    print(f"{'ID':>7} | {'Name':<10} | {'Email':<25} | {'Year':>4} | {'Course':<15} | {'Qualification':<18} | {'Mode':<10} | {'Fees':>6}")
    print("-" * 120)
    # Print all student's data row by row
    for i in range(len(student_id)):
        print(f"{student_id[i]:>7} | {name[i]:<10} | {email[i]:<25} | {year[i]:>4} | "
              f"{course[i]:<15} | {study_mode[i]:<18} | {qualification[i]:<10} | {fees[i]:>6}")


# Entry point for testing the program
if __name__ == "__main__":
    load_data("students.csv")
    display_table()