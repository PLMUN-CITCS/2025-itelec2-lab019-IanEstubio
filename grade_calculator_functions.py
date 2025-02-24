# Week 05 - Working with Functions
# Laboratory # 19 - Group Activity # 01 - Problem 01: Enhanced Grade Calculator with Function Decomposition

def get_student_score() -> float:
    """
    Prompts the user to enter their score, validates input, and returns a numerical score.
    
    Returns:
        float: The student's score as a floating-point number.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:  # Valid score range
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score and grading scale.
    
    Args:
        score (float): The student's score.
    
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
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

# Main program flow
if __name__ == "__main__":
    student_score = get_student_score()
    student_grade = calculate_grade(student_score)
    print(f"Your Grade is: {student_grade}")
