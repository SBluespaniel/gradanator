"""File: gradanator.py
Date completed: 01/30/2023
Description: This program takes user input of grades from three exams,
homework assignments, grade weights for the exams and homework, and computes
weighted scores for these. It then prints the user's letter grade and an
encouraging message.
"""


# Print opening line
print(f"This program reads exam/homework scores and reports course grade.\n")


def query_int(message):
    """Collect integer from user. Makes the following code cleaner."""
    return int(input(message))


def exam_score(exam):
    """Collect exam grade inputs and calculate weighted exam score.
    
        Returns:
            weighted_score: Exam score scaled to percentage of final grade.
    """
    print(exam)
    exam_weight = query_int("Weight (0-100)? ")
    # Capping total score at 100 points
    total_points = min(query_int("Score earned? "), 100)
    # Calculate weighted score, print
    print(f"Total points = {total_points} / 100")
    weighted_score = round(total_points / 100 * exam_weight, 1)
    print(f"Weighted score = {weighted_score}\n")

    return weighted_score


def homework_score():
    """Collect homework & section grade inputs, calculate weighted score.
    
        Returns:
            weighted_score: Total score scaled to percentage of final grade.
    """
    print("Homework:")
    homework_weight = query_int("Weight (0-100)? ")
    number_assignments = query_int("Number of assignments? ")
    
    # Loop returns cumulative sum of user-input assignment scores out of max
    i = 0
    assignment_score = 0
    assignment_max = 0
    for i in range(1, number_assignments+1):
        assignment_score += query_int(f"Assignment {i} score? ")
        assignment_max += query_int(f"Assignment {i} max? ")
        i += 1
    # Capping the total score at the maximum possible, if there's extra credit
    assignment_score = min(assignment_score, assignment_max)
    
    # Calculate weighted score, print
    sections_attended = query_int("How many sections did you attend? ")
    total_score = assignment_score + sections_attended * 3
    max_points = min(assignment_score, assignment_max) + 34
    print(f"Section points = {min((sections_attended * 3), 34)} / 34")
    print(f"Total points = {total_score} / {max_points}")
    weighted_score = round(total_score / max_points * homework_weight, 1)
    print(f"Weighted Score = {weighted_score}\n")
    
    return weighted_score

# Call all score functions
score_one = exam_score("Exam 1:")
score_two = exam_score("Exam 2:")
score_three = exam_score("Final Exam:")
score_four = homework_score()


def course_grade(score_one, score_two, score_three, score_four):
    """Calculate total class grade, assign letter grade and comment.
    
        Parameters:
            score_one: Weighted score of exam 1.
            score_two: Weighted score of exam 2.
            score_three: Weighted score of final exam.
            score_four: Weighted score of homework.
        Results:
            percentage: Sum of all weighted scores.
            letter_grade: Corresponding letter based on percentage.
            grade_message: Corresponding message for letter grade.
    """
    percentage = round(score_one + score_two + score_three + score_four, 1)
    print(f"Overall percentage = {percentage}")
    
    # Determine letter grade & message from final grade using if-elif-else
    if percentage >= 90.0:
        letter_grade = "A"
        grade_message = "Great job, congratulations!"
    elif (percentage <= 89.99) and (percentage >= 80):
        letter_grade = "B"
        grade_message = "Very respectable!"
    elif (percentage <= 79.99) and (percentage >= 70):
        letter_grade = "C"
        grade_message = "Cs get degrees!"
    elif (percentage <= 69.99) and (percentage >= 60):
        letter_grade = "D"
        grade_message = "It could have been worse!"
    else:
        letter_grade = "F"
        grade_message = "Bummer. Better luck next time."
    print(f"Your grade will be at least: {letter_grade}\n{grade_message}")


# Call course_grade function
course_grade(score_one, score_two, score_three, score_four)