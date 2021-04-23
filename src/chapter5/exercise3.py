# Vending Machine Change Maker



print("Welcome to the Vending Machine Change Maker Program")
print("Change maker initialized.")
# Intial Stock
print("Stock contains:\n    25 nickels\n    25 dimes\n    25 quarters\n    0 ones\n    0 fives")
#initialize costants
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

price = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")

while price!= 'q':
    price_flo= float(price)
         #Converting into cents & dollars
    total_cents = round(price_flo* 100)
    dollars = total_cents // 100
    cents = total_cents - (dollars * 100)
    #checking for the price if it is non negative and multiple of .05
    if total_cents % 5 == 0 and total_cents > 0:
                       #MENU DEPOSITES
        print("\nMenu for deposits:\n  'n' - deposit a nickel\n  'd' - deposit a dime", \
              "\n  'q' - deposit a quarter\n  'o' - deposit a one dollar bill\n  'f' - deposit a five dollar bill", \
              "\n  'c' - cancel the purchase")
        print("\nPayment due: ", dollars, "dollars and ", cents, "cents")
        deposit= input("Indicate your deposit: ")
    else:
          print("Illegal price: Must be a non-negative multiple of 5 cents.")



    price= input("Enter the purchase price (xx.xx) or 'q' to quit: ")

print('Thank You for using the Vending Machine Change Maker Program')
     
     

