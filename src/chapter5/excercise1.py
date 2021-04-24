try:
    total = 0
    count = 0
    while True:
        x = input('enter a number')
        if x == 'done':
            break
        x = int(x)
        total = total + x
        count = count + 1
        average = total / count
    print('done!')
    print(count, total, average)
except:
    print('Invalid Input')