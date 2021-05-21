try:
    score = float(input('enter score'))
    # A program that prompts a user to enter a score from 0 to 1 and prints the corresponding grade
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

except:
    print("INVALID ENTRY")
