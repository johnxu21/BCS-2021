# the first 5 lines indicate the initial number of stock in the machine
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

print(" >>>> =========================" "RESTART" "=========================\n >>>>")
print("welcome to the vending machine change make program")
print("change maker initialised. ")
print('stock contains :\n{} quarters\n{} dimes\n{} nickels\n{} ones \n{} fives\n'
      .format(quarters, dimes, nickels, ones, fives))

while True:
    int_str = input("\nPlease enter purchase price (XX.XX) or 'q' to quit:")
    if int_str == 'q':
        break
    price = float(int_str)
    if price > 0 and (price % 5 * 100) != 0:
        break
    else:
        print('Illegal price: must be  a non negative multiple of five cents')

while int_str != 'q':
    while True:
        dollar = float(input('\nenter the number of dollar for payment:'))
        if dollar > price:
            price = price * 100
            dollar *= 100
            break
        else:
            print('insufficient amount')

