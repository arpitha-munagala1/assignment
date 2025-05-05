import csv
# Global parallel arrays
3
email_ids = []
years_of_enrolment = []
course_modules = []
study_levels = []
course_deliveries = []
fees_list = []

def load_data(filename):
    """Loads student d from a CSV file into parallel arrays."""
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            student_nos.append(int(row[0]))
            student_names.append(row[1])
            email_ids.append(row[2])
            years_of_enrolment.append(int(row[3]))
            course_modules.append(row[4])
            study_levels.append(row[5])
            course_deliveries.append(row[6])
            fees_list.append(int(row[7]))

def display_table():
    """Displays the student data in formatted table."""
    print(f"{'ID':>7} | {'Name':<10} | {'Email':<25} | {'Year':>4} | {'Course':<15} | {'Level':<18} | {'Mode':<10} | {'Fees':>6}")
    print("-" * 120)
    for i in range(len(student_nos)):
        print(f"{student_nos[i]:>7} | {student_names[i]:<10} | {email_ids[i]:<25} | {years_of_enrolment[i]:>4} | "
              f"{course_modules[i]:<15} | {study_levels[i]:<18} | {course_deliveries[i]:<10} | {fees_list[i]:>6}")

# For testing
if __name__ == "__main__":
    load_data("students.csv")
    display_table()





