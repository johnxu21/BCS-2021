
my_numlist = []
while True:
    str_val = input('Enter a number: ')
    if str_val == 'done':
        break
    try:
        val = float(str_val)
    except:
        print('Invalid input')
        continue
    my_numlist.append(val)
print(min(my_numlist), max(my_numlist))