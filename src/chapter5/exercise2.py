total = 0
count = 0
average = 0
smallest = None
largest = None
print('before largest:', largest)
while True:
    inp = input('>')
    if inp == "done":
        break
    try:
        if float(inp):
            total += float(inp)
            count += 1
            new_value = float(inp)
            if largest is None or new_value > largest:
                largest = new_value
            print('new_largest is', largest)
            if smallest is None or new_value < smallest:
                smallest = new_value
            print('new_smallest is', smallest)
    except ValueError:
        print('invalid input')
    if count != 0:
        print('done')
        print('largest is', largest)
        print('smallest is', smallest)
        print('count is', count)
        print(total)
        print('average=', total / count)
    else:
        print('enter a number please')
