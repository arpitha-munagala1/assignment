import csv # To read and write CSV files, import the CSV module.

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
        print(f"{student_id[i]:>8}  {name[i]:<10}  {email[i]:<25}  {year[i]:>6}  "
              f"{course[i]:<15}  {qualification[i]:<18}  {study_mode[i]:<10}  {fees[i]:>10}")
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
        
def save_records():
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in range(len(student_id)):
            writer.writerow([
                student_id[i], name[i], email[i], year[i],
                course[i], qualification[i], study_mode[i], fees[i]
            ])
    print("\nRecords saved successfully.\n")

def menu():
    while True:
        print("\n=== Student Information System ===")
        print("1. Load records")
        print("2. Display")
        print("3. Add record")
        print("4. Delete record")
        print("5. Save records")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
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

# Entry point
if __name__ == "__main__":
    print("\n Welcome to Arpitha and Chandu Project")
    menu()
