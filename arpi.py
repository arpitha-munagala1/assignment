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

def load_records():
    try:
        with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Clear arrays before loading new data
            student_ids.clear()
            names.clear()
            emails.clear()
            years.clear()
            courses.clear()
            qualifications.clear()
            study_modes.clear()
            fees.clear()
            for row in reader:
                student_ids.append(row[0])
                names.append(row[1])
                emails.append(row[2])
                years.append(row[3])
                courses.append(row[4])
                qualifications.append(row[5])
                study_modes.append(row[6])
                fees.append(row[7])
        print("\nRecords loaded successfully.\n")
    except FileNotFoundError:
        print(f"\nError: File '{FILENAME}' not found. Please make sure it exists.\n")