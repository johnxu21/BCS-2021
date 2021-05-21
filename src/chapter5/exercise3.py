# the first 5 lines indicate the initial number of stock in the machine
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

x = ('Menu for deposits :\nq-deposit a quarters\nd-deposit a dimes\n'
     'n-deposit a nickels\no-deposit a one dollar bill \nf-deposit a five dollar bill\n'
     .format(quarters, dimes, nickels, ones, fives))

n = "nickel"
d = "dimes"
q = "quarter"
o = "ones"
f = "fives"
print(" >>>> =========================" "RESTART" "=========================\n >>>>")
print("welcome to the vending machine change make program")
print("change maker initialised. ")
print('stock contains :\n{} quarters\n{} dimes\n{} nickels\n{} ones \n{} fives\n'
      .format(quarters, dimes, nickels, ones, fives))

while True:
    int_str = input("\nPlease enter purchase price (XX.XX) or 'q' to quit:")
    if int_str == 'q':
        break  # this terminates the program the moment q is entered
    price = float(int_str)
    if price > 0 or (price % 5 * 100) != 0:  # this makes sure that the purchase price is is a non negative value or a
        # multiple of 5
        print(x)
        break
    else:
        print('Illegal price: must be  a non negative multiple of five cents')

while int_str != 'q':
    while True:
        dollar = float(input('\nenter the number of dollar for payment:'))
        if dollar > price:
            price = price * 100
            dollar *= 100
            print(x)
            break
        else:
            print('insufficient amount')

    noOfQuarters = 0
    noOfDimes = 0
    noOfNickels = 0
    noOfOnes = 0
    noOfFives = 0
    change = dollar - price
    print('Please take the change below \n', (change / 100))

    noOfQuarters = int(change / 25)
    if noOfQuarters != 0:
        if noOfQuarters <= quarters:
            quarters -= noOfQuarters
            change -= noOfQuarters * 25
    else:
        noOfQuarters = quarters
        quarters = 0
        change -= noOfQuarters * 25

    noOfDimes = int(change / 10)
    if noOfDimes != 0:
        if noOfDimes <= dimes:
            dimes -= noOfDimes
            change -= noOfDimes * 10
    else:
        noOfDimes = dimes

        dimes = 0
        change -= noOfDimes * 10

    noOfNickels = int(change / 5)
    if noOfNickels != 0:
        if noOfNickels <= fives:
            fives -= noOfNickels
            change -= noOfNickels * 5
    else:
        noOfNickels = fives
        fives = 0
        change -= noOfNickels * 5

    totalCoin = noOfDimes + noOfQuarters + noOfNickels + noOfOnes + noOfFives
    print('\n Least number of coin needed to change is {}'.format(int(totalCoin)))
    if noOfQuarters != 0:
        print('{} quarters'.format(noOfQuarters))
    if noOfDimes != 0:
        print('{} dimes'.format(noOfDimes))
    if noOfNickels != 0:
        print('{} nickels'.format(noOfNickels))
    if noOfOnes != 0:
        print('{} ones'.format(noOfOnes))
    if noOfFives != 0:
        print('{} fives'.format(noOfFives))

    print('\nStock contains : {}quarters\n{}dimes\n {}nickels\n {}ones\n and {}fives'
          .format(quarters, dimes, nickels, ones, fives))
    while True:
        int_str = input('\n\n\nPlease enter the price in for of XX.XX or q to quit:')
        if int_str == 'q':
            break
        price = float(int_str)
        if price > 0 or (price % 5 * 100) != 0:  # this makes sure that the purchase price is is a non negative value
            # or a multiple of 5
            break
        else:
            print('Illegal price: must be  a non negative multiple of five cents')
