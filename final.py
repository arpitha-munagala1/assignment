import csv  # TO READ and WRITE from csv file,importing the CSV module.

# Declaring global parallel arrays to store student data.
# Each array will hold a specific attribute of student records given in the csv file .
student_id = []
name = []
email = []
year = []
course = []
qualification = []
study_mode = []
fees = []

# File name that stores student records in CSV format.
FILENAME = 'students.csv'


def load_records():
    # Loads student records from a CSV file into parallel arrays.
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.reader(file)

            # Clear existing data before loading new records.
            student_id.clear()
            name.clear()
            email.clear()
            year.clear()
            course.clear()
            qualification.clear()
            study_mode.clear()
            fees.clear()

            # Read each row and append data to respective arrays.
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
    # Displays all student records in a structured format.

    if not student_id:  # Check if records exist
        print("\nNo records to display. Please load or add records first.\n")
        return

    # Print column headers with proper formatting.
    print(
        f"{'Student-ID':>8}  {'Name':<10}  {'Email':<25}  {'Year':>6}  {'Course':<15}  {'Qualification':<18}  {'Study-Mode':<10}  {'Fees':>10}")
    print("-" * 110)

    # Print each student record in a structured format(in a table format).
    for i in range(len(student_id)):
        print(
            f"{student_id[i]:>8}  {name[i]:<10}  {email[i]:<25}  {year[i]:>6}  {course[i]:<15}  {qualification[i]:<18}  {study_mode[i]:<10}  {fees[i]:>10}")
    print()


def add_record():
    # Prompts the user to enter a new student record and adds it to the arrays.

    print("\nEnter new student record:")
    student_id.append(input("Student ID: "))
    name.append(input("Name: "))
    email.append(input("Email: "))
    year.append(input("Year: "))
    course.append(input("Course: "))
    qualification.append(input("Qualification: "))
    study_mode.append(input("Study Mode (Online/On-campus): "))
    fees.append(input("Fees: "))
    print("\nRecord added successfully.\n")

    # Display all records after adding a new entry.
    print("\nCurrent Records:")
    display_records()


def delete_record():
    # Deletes a student record based on the provided Student ID.
    if not student_id:  # Ensure there are records to delete
        print("\nNo records to delete. Please load records first.\n")
        return

    delete_id = input("Enter Student ID to delete: ")
    if delete_id in student_id:
        index = student_id.index(delete_id)  # Find index of student ID

        # Remove the record from all parallel arrays.
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


def save_records():
    # Saves all student records back to the CSV file.
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write each student's data as a row in the CSV file.
        for i in range(len(student_id)):
            writer.writerow([
                student_id[i], name[i], email[i], year[i],
                course[i], qualification[i], study_mode[i], fees[i]
            ])
    print("\nRecords saved successfully.\n")


def menu():
    # Displays a menu for user interaction and performs actions based on user choice.
    while True:
        print("\n=== Student Information System ===")
        print("1. Load records")
        print("2. Display records")
        print("3. Add record")
        print("4. Delete record")
        print("5. Save records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        # Execute the function based on the user choice.
        if choice == '1':
            load_records()
        elif choice == '2':
            display_records()
        elif choice == '3':
            add_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            save_records()
        elif choice == '6':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.\n")


# Entry point for the program "this will be the welcome text in the output".
if __name__ == "__main__":
    print("\nWelcome to Arpitha and Chandu Project")
    menu()