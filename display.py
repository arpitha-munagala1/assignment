import csv

# Global parallel arrays
student_ids = []
names = []
emails = []
years = []
courses = []
qualifications = []
study_modes = []
fees = []

FILENAME = 'students.csv'  # reading data from the csv file

def display_records():
    if not student_ids:
        print("\nNo records to display. Please load or add records first.\n")
        return
    print(
        f"{'ID':>8}  {'Name':<10}  {'Email':<25}  {'Year':>6}  {'Course':<15}  {'Qual.':<18}  {'Mode':<10}  {'Fees':>10}")
    print("-" * 110)
    for i in range(len(student_ids)):
        print(f"{student_ids[i]:>8}  {names[i]:<10}  {emails[i]:<25}  {years[i]:>6}  "
              f"{courses[i]:<15}  {qualifications[i]:<18}  {study_modes[i]:<10}  {fees[i]:>10}")
    print()

def add_record():
    print("\nEnter new student record:")
    student_ids.append(input("Student ID: "))
    names.append(input("Name: "))
    emails.append(input("Email: "))
    years.append(input("Year: "))
    courses.append(input("Course: "))
    qualifications.append(input("Qualification: "))
    study_modes.append(input("Study Mode (Online/Oncampus): "))
    fees.append(input("Fees: "))
    print("\n Record added successfully.\n")

    # Display all record after successfullyy adding files
    print("\n current Records:")
    display_records()

 def delete_record():
        if not student_ids:
            print("\nNo records to delete. Please load records first.\n")
            return

        delete_id = input("Enter Student ID to delete: ")
        if delete_id in student_ids:
            index = student_ids.index(delete_id)
            # Remove from all arrays
            student_ids.pop(index)
            names.pop(index)
            emails.pop(index)
            years.pop(index)
            courses.pop(index)
            qualifications.pop(index)
            study_modes.pop(index)
            fees.pop(index)
            print("\nRecord deleted successfully.\n")
        else:
            print("\nStudent ID not found.\n")