# A PROGRAM TO COMPUTE AND DISPLAY FOR A UTILITY COMPANY WHICH SUPPLIES WATER TO ITS CUSTOMERS #
print(">>> ====================================== RESTART ==================================================== >>>")


# calculating the number of gallons used by the customer
def meter_reading(a, b):
    if a < b:
        gallons = (b - a) / 10
    else:
        gallons = ((1000000000 - a) + b) / 10
    print(f'Gallons of water used:{gallons}')
    return gallons


# prompting the user for inputs
while True:
    code = input("Enter customer code:\n")
    if code == "R" or code == "r":
        beginning = int(input('Enter beginning meter reading:\n'))
        ending = int(input('Enter ending meter reading:\n'))
        print(f'Customer code:{code}')
        print(f'Beginning meter number:{beginning:9d}')
        print(f'Ending meter reading:{ending:9d}')
        gallons = meter_reading(beginning, ending)
        pay = 5.00 + (gallons * 0.0005)
        print(f'Amount billed: ${pay}')
#  elif code == "C" or code == "c":
