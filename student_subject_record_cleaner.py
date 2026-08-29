student_records = {
    "STU001": {"name": "Rajdip", "subject": "Math", "grade": "A"},
    "STU002": {"name": "Bob", "subject": "Science", "grade": "B"},
    "STU003": {"name": "Charlie", "subject": "History", "grade": "C"},
    "STU004": {"name": "Duplicate Bob", "subject": "Science", "grade": "B"},
    "STU005": {"name": "Invalid Entry", "subject": "None", "grade": "F"},
}

print(f"Original dictionary length: {len(student_records)}")

safe_student = student_records.get("STU001", "Student not found")
missing_student = student_records.get("STU999", "Student not found")

print(f"Safe access (Found): {safe_student}")
print(f"Safe access (Missing): {missing_student}")

student_records["STU003"]["grade"] = "B"
student_records.update({"STU001": {"name": "Alice", "subject": "Advanced Math", "grade": "A+"}})

if "STU004" in student_records:
    del student_records["STU004"]

student_records.pop("STU005", None)

final_length = len(student_records)
print(f"Final dictionary length: {final_length}")

print("\n--- Final Cleaned Student Records ---")
for student_id, details in student_records.items():
    print(f"ID: {student_id} | Name: {details['name']} | Subject: {details['subject']} | Grade: {details['grade']}")