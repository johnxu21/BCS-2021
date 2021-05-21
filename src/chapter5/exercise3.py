# Vending Machine Change Maker



print("Welcome to the Vending Machine Change Maker Program")
print("Change maker initialized.")
print("Stock contains:\n    25 nickels\n    25 dimes\n    25 quarters\n    0 ones\n    0 fives")

nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")

while price_str != 'q':
    price_flo = float(price_str)
    total_cents = round(price_flo * 100)
    dollars = total_cents // 100
    cents = total_cents - (dollars * 100)

    if total_cents % 5 == 0 and total_cents > 0:
        print("\nMenu for deposits:\n  'n' - deposit a nickel\n  'd' - deposit a dime", \
              "\n  'q' - deposit a quarter\n  'o' - deposit a one dollar bill\n  'f' - deposit a five dollar bill", \
              "\n  'c' - cancel the purchase")
        print("\nPayment due: ", dollars, "dollars and ", cents, "cents")
        deposit_str = input("Indicate your deposit: ")
while total_cents > 0:
            if deposit_str.isdigit() == False:
                if deposit_str == 'n':
                    total_cents -= 5
                    nickels += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit_str == 'd':
                    total_cents -= 10
                    dimes += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit_str == 'q':
                    total_cents -= 25
                    quarters += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit_str == 'o':
                    total_cents -= 100
                    ones += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit_str == 'f':
                    total_cents -= 500
                    fives += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit_str == 'c':
                    break
                else:
                    print("Illegal deposit: ", deposit_str)
                if total_cents > 0:
                    print("\nPayment due: ", dollars, "dollars and ", cents, "cents")
                    deposit_str = input("Indicate your deposit: ")
                else:
                    if total_cents == 0:
                        print("\nPlease take the change below.\n   No change due.")
                        break
                    change_quarters = abs(total_cents) // 25
                    if change_quarters > quarters:
                        change_quarters = quarters
                        quarters = 0
                    else:
                        quarters -= change_quarters
                    total_cents += change_quarters * 25
                    change_dimes = abs(total_cents) // 10
                    if change_dimes > dimes:
                        change_dimes = dimes
                        dimes = 0
                    else:
                        dimes -= change_dimes
                    total_cents += change_dimes * 10
                    change_nickels = abs(total_cents) // 5
                    if change_nickels > nickels:
                        change_nickels = nickels
                        nickels = 0
                    else:
                        nickels -= change_nickels
                    total_cents += change_nickels * 5
                    print("\nPlease take the change below.\n  ", change_quarters, "quarters\n  ", change_dimes,
                          "dimes\n  ", change_nickels, "nickels")
                    if total_cents < 0:
                        dollars = abs(total_cents) // 100
                        cents = abs(total_cents) - (dollars * 100)
                        print("Machine is out of change.\nSee store manager for remaining change.\nAmount due is: ",
                              dollars, "dollars and", cents, "cents.")
                    break
            
                print("Illegal deposit: ", deposit_str)
                deposit_str = input("\nIndicate your deposit: ")

    # else:
        print("Illegal price: Must be a non-negative multiple of 5 cents.")

    print("\nStock contains:\n    ", nickels, " nickels\n    ", dimes, " dimes\n    ", \
          quarters, " quarters\n    ", ones, " ones\n    ", fives, " fives")

    price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")

print('\nThank You for using the Vending Machine Change Maker Program')
