import csv

# Global parallel arrays
student_id = []
name = []
email = []
year = []
course = []
qualification = []
study_mode = []
fees = []

FILENAME = 'students.csv'  # reading data from the csv file

def load_records():
    try:
        with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Clear arrays before loading new data
            student_id.clear()
            name.clear()
            email.clear()
            year.clear()
            course.clear()
            qualification.clear()
            study_mode.clear()
            fees.clear()
            for row in reader:
                student_id.append(row[0])
                name.append(row[1])
                email.append(row[2])
                year.append(row[3])
                course.append(row[4])
                qualification.append(row[5])
                study_mode.append(row[6])
                fees.append(row[7])
        print("\nRecords loaded successfully.\n")
    except FileNotFoundError:
        print(f"\nError: File '{FILENAME}' not found. Please make sure it exists.\n")

def display_records():
    if not student_id:
        print("\nNo records to display. Please load or add records first.\n")
        return
    print(
        f"{'Student-ID':>8}  {'Name':<10}  {'Email':<25}  {'Year':>6}  {'Course':<15}  {'Qualification.':<18}  {'Study-Mode':<10}  {'Fees':>10}")
    print("-" * 110)
    for i in range(len(student_id)):
        print(f"{student_ids[i]:>8}  {names[i]:<10}  {emails[i]:<25}  {years[i]:>6}  "
              f"{courses[i]:<15}  {qualifications[i]:<18}  {study_modes[i]:<10}  {fees[i]:>10}")
    print()

def add_record():
    print("\nEnter new student record:")
    student_id.append(input("Student ID: "))
    name.append(input("Name: "))
    email.append(input("Email: "))
    year.append(input("Year: "))
    course.append(input("Course: "))
    qualification.append(input("Qualification: "))
    study_mode.append(input("Study Mode (Online/On-campus): "))
    fees.append(input("Fees: "))
    print("\n Record added successfully.\n")

    # Display all record after successfully adding files
    print("\n current Records:")
    display_records()

def delete_record():
    if not student_id:
        print("\nNo records to delete. Please load records first.\n")
        return

    delete_id = input("Enter Student ID to delete: ")
    if delete_id in student_id:
        index = student_id.index(delete_id)
        # Remove from all arrays
        student_id.pop(index)
        name.pop(index)
        email.pop(index)
        year.pop(index)
        course.pop(index)
        qualification.pop(index)
        study_mode.pop(index)
        fees.pop(index)
        print("\nRecord deleted successfully.\n")
    else:
        print("\nStudent ID not found.\n")