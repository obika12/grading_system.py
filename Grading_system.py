# Simple Grading System
# Student: Obika ikenna kelvin 

def grading_system():
    # Input student details
    student_name = input("Enter student name: ")
    
    try:
        score = float(input("Enter student score (0-100): "))
        
        # Validate score
        if score < 0 or score > 100:
            print("Invalid score! Score must be between 0 and 100.")
            return
        
        # Determine grade
        if score >= 70:
            grade = "A"
        elif score >= 60:
            grade = "B"
        elif score >= 50:
            grade = "C"
        elif score >= 45:
            grade = "D"
        elif score >= 40:
            grade = "E"
        else:
            grade = "F"
        
        # Display result
        print(f"{student_name}'s grade is: {grade}")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value for the score.")

# Run the grading system
grading_system()
