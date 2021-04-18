# A program that prompts a user to enter a score from 0 to 1 and prints the corresponding grade
s = (input('enter score'))


def compute_grade(score):
    try:
        score = float(s)  # this makes sure that the user enters only float values otherwise an error message pops up
        if 0 <= score < 0.6:
            print(score, 'F')
        elif 0.6 <= score < 0.7:
            print(score, 'D')
        elif 0.7 <= score < 0.8:
            print(score, 'C')
        elif 0.8 <= score < 0.9:
            print(score, 'B')
        elif 0.9 <= score <= 1:
            print(score, 'A')
        else:
            print('error, out of range')
        return "grade"
    except:
        return "INVALID ENTRY"


grade = compute_grade(s)
print(grade)
