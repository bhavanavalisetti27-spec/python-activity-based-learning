def evaluate_scholarships(students):
    eligible_students = []
    
    for student in students:
        name, agg_marks, sub_min, attendance, income = student
        if agg_marks >= 400 and sub_min >= 70 and attendance >= 85 and income <= 600000:
            eligible_students.append(student)
            
    # Custom tie-breaking sort using bubble sort or sort key
    # Key criteria: (-agg_marks, -attendance, income)
    n = len(eligible_students)
    for i in range(n):
        for j in range(0, n - i - 1):
            s1 = eligible_students[j]
            s2 = eligible_students[j + 1]
            # Compare agg_marks
            if s1[1] < s2[1]:
                eligible_students[j], eligible_students[j+1] = eligible_students[j+1], eligible_students[j]
            elif s1[1] == s2[1]:
                # Tie-break 1: Attendance
                if s1[3] < s2[3]:
                    eligible_students[j], eligible_students[j+1] = eligible_students[j+1], eligible_students[j]
                elif s1[3] == s2[3]:
                    # Tie-break 2: Income (lower is preferred)
                    if s1[4] > s2[4]:
                        eligible_students[j], eligible_students[j+1] = eligible_students[j+1], eligible_students[j]

    return eligible_students

# Test Dataset
student_data = [
    ("Rahul", 460, 80, 92, 450000),
    ("Priya", 460, 75, 95, 500000),
    ("Anish", 420, 68, 88, 300000),  # Ineligible: sub_min < 70
    ("Sneha", 460, 82, 92, 350000),  # Tied with Rahul on marks and attendance, lower income
    ("Kiran", 480, 88, 90, 550000)
]

ranked = evaluate_scholarships(student_data)

print("--- University Scholarship Selection Matrix ---")
print(f"{'Rank':<5}{'Name':<10}{'Marks':<8}{'Attendance':<12}{'Income (INR)':<12}")
for rank, s in enumerate(ranked, 1):
    print(f"{rank:<5}{s[0]:<10}{s[1]:<8}{s[3]:<12}{s[4]:<12}")