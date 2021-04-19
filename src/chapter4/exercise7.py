
def compute_grade(score):
    if 0.9 <= score <= 1.0:
        return 'A'
    elif 0.8 <= score <= 0.89:
        return 'B'
    elif 0.7 <= score <= 0.79:
        return  C
    elif 0.6 <= score <= 0.69:
        return 'D'
    elif score == 0 and score < 0.59:
        return  F
    else:
        return 'Bad score.'


try:
    marks = float(input("Enter your score:  "))
    print("Your score:", compute_grade(marks))
except:
    print("Enter a number: ")
