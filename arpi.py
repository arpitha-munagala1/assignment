import csv
# Step 1: Create and save your CSV file
with open('students.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['student_no', 'student_name', 'email_id', 'year_of_enrolment', 'course_module',
                     'study_level', 'course_delivery', 'fees'])
    # Write your student data
    writer.writerow([106050, 'Chandu', 'chandu@gmail.com', 2025, 'Computer Science', 'Master', 'Online', 20000])
    writer.writerow([106051, 'Arpitha', 'arpitha@gmail.com', 2025, 'Data Science', 'Bachelor', 'Oncampus', 25000])
    writer.writerow([106052, 'srikar', 'srikar@gmail.com', 2025, 'Arts', 'Bachelor', 'Online', 25000])
    writer.writerow([106053, 'srinika', 'srinika@hotmail.com', 2025, 'Law', 'Diploma', 'Oncampus', 15000])
    writer.writerow([106054, 'riya', 'riyansh@outlook.com', 2025, 'Cybersecurity', 'Certificate', 'Oncampus', 8000])
    writer.writerow([106055, 'rishik', 'rishik@gmail.com', 2025, 'Arts', 'Diploma', 'Online', 10000])
    writer.writerow([106056, 'murali', 'murali@gmail.com', 2025, 'Animation', 'Advanced Diploma', 'Oncampus', 20000])
    writer.writerow([106057, 'helo', 'deepu@outlook.com', 2025, 'Health', 'Master', 'Online', 25000])