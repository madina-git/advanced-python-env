import json

# Step 1: Read the original JSON file
with open("C:\\Users\\User\\OneDrive\\Desktop\\advanced-python-env\\week-5\\students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

# Step 2: Calculate average grade for each student
for student in students:
    grades = student.get('grades', [])
    if grades:
        avg = sum(grades) / len(grades)
    else:
        avg = 0
    student['average'] = avg  # Add new key for average

# Step 3: Write the updated data to a new JSON file
with open('students_with_average.json', 'w') as file:
    json.dump(students, file, indent=4)

print("Updated JSON file created: students_with_average.json")
