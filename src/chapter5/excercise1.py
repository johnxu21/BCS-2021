try:
    total = 0
    count = 0
# the user will be able to input numbers repeatedly
    while True:
        x = input('enter a number')
# when done is entered, the loop will be broken
        if x == 'done':
            break
        x = int(x)
# we are finding the total, count and average of the numbers entered
        total = total + x
        count = count + 1
        average = total / count
    print('done!')
    print(count, total, average)
except:
    print('Invalid Input')