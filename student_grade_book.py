grade_book = {
    "rajdip": 100,
    "anikit": 92,
    "ram": 78,
    "arnab"
    "arav": 95,
    "rohan": 88
}

total_score = 0
for score in grade_book.values():
    total_score += score

class_average = total_score / len(grade_book)

highest_score = max(grade_book.values())
lowest_score = min(grade_book.values())

print("--- Class Performance Summary ---")
print(f"Class Average: {class_average:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score:  {lowest_score}")
print("-" * 33)

while True:
    search_name = input("\nEnter a student's name to look up their score (or type 'exit' to quit): ").strip()
    
    if search_name.lower() == 'exit':
        print("Exiting grade book. Goodbye!")
        break
        
    found = False
    for student, score in grade_book.items():
        if student.lower() == search_name.lower():
            print(f" {student}'s score is: {score}")
            found = True
            break
            
    if not found:
        print(f" Student '{search_name}' not found in the grade book. Please try again.")