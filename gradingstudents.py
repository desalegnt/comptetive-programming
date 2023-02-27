def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        next_multiple = grade + 5 - grade % 5
        difference = 5 - grade%5
        if grade >= 38 and difference < 3:
            new_grade = next_multiple
        else:
            new_grade = grade 
        new_grades.append(new_grade)
    return new_grades
