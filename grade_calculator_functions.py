# Week 05 - Working with Functions
# Laboratory # 19 - Group Activity # 01 - Problem 01: Enhanced Grade Calculator with Function Decomposition


def get_student_score():
    """Prompts the user to enter their score and returns it as a float."""
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def calculate_grade(score):
    """Determines the letter grade based on the given score."""
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

# Main execution flow (without if __name__ == "__main__")
score = get_student_score()
grade = calculate_grade(score)
print(f"Your Grade is: {grade}")
