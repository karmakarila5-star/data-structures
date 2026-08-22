marks = [85, 92, 78, 90, 88, 65, 95, 72]

total_students = len(marks)
print(f"Total number of students: {total_students}")

first_student = marks[0]
last_student = marks[-1]
top_three = marks[:3]

print(f"First student mark: {first_student}")
print(f"Last student mark: {last_student}")
print(f"First three marks: {top_three}")

total_marks = 0
highest_mark = marks[0]
lowest_mark = marks[0]

for mark in marks:
    total_marks += mark
    
    if mark > highest_mark:
        highest_mark = mark
        
    if mark < lowest_mark:
        lowest_mark = mark

average_mark = total_marks / total_students

print("\n--- MARKS LIST SUMMARY ---")
print(f"Total Marks Combined: {total_marks}")
print(f"Average Mark:         {average_mark:.2f}")
print(f"Highest Mark:         {highest_mark}")
print(f"Lowest Mark:          {lowest_mark}")