# Week 05 - Working with Functions
# Laboratory # 19 - Group Activity # 01 - Problem 01: Enhanced Grade Calculator with Function Decomposition

def get_student_score():
    score = float(input("Enter your score: "))
    return score

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Main program execution

if __name__ == "__main__":
    student_score = get_student_score()
    student_grade = calculate_grade(student_score)
    print(f"Your Grade is: {student_grade}")
