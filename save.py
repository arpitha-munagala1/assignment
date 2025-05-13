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
def save_records():
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in range(len(student_ids)):
            writer.writerow([
                student_ids[i], names[i], emails[i], years[i],
                courses[i], qualifications[i], study_modes[i], fees[i]
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