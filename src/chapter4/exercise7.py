def compute_grade(s):

    if 0.0 <= s <= 1.0:
        if s >= 0.9:
            return 'A'
        if s >= 0.8:
            return 'B'
        if s >= 0.7:
            return 'C'
        if s >= 0.6:
            return 'D'
        return 'F'
    return 'bad score'


s = input('enter score')
try:
    compute_grade(s)
except ValueError:
    print(' big error, enter digits please')
    quit()

grade = compute_grade(s)
print(grade)
