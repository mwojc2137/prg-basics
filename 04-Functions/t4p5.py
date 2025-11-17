def grade(pts):
    grade = ""
    if pts >= 18:
        grade = "Excellent"
    elif pts >= 14:
        grade = "Good"
    elif pts >= 10:
        grade = "Satisfactory"
    else:
        grade = "Fail"
    return grade

pts = int(input("Enter score: "))

print(f'You scored {pts} points. Your result is {grade(pts)}')