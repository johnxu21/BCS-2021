num_list = []
while True:
    input_number = (input('Enter a number>>> ')).lower()  # THE INPUT IS AUTOMATICALLY CONVERTED INTO LOWERCASE
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('INVALID ENTRY')
        continue

    num_list.append(number)  # add each number input to the list that was created above

if num_list:
    print(num_list)
    print('Maximum: ', max(num_list) or None)
    print('Minimum: ', min(num_list) or None)
