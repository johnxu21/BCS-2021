try:
    age = int(input('enter age'))
    if age >= 18:
        print('you can vote')
    elif 0 <= age <= 17:
        print('too young to vote')
    elif age < 0:
        print('you are a time traveller')
except:
    print('error, please enter a digit')

