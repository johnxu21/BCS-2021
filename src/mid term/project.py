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
        initial_meter = int(input('Enter beginning meter reading:\n'))
        if initial_meter < 0 or initial_meter >= 1000000000:
            print("invalid entry, please enter a valid meter number")
            break
        else:
            final_meter = int(input('Enter ending meter reading:\n'))
        if final_meter < 0 or final_meter >= 1000000000:
            print(" invalid entry , please enter a valid meter number")
        print(f'Customer code:{code}')
        print(f'initial meter number:{initial_meter:9d}')
        print(f'final meter reading:{final_meter:9d}')
        gallons = meter_reading(initial_meter, final_meter)

        # calculating the pay bill for residential customers
        pay_bill = 5.00 + (gallons * 0.0005)
        print(f'Amount billed: ${pay_bill :.02f}')

    # calculating the pay bill for commercial  customers
    elif code == "c" or code == "C":
        initial_meter = int(input('Enter beginning meter reading:\n'))
        if initial_meter < 0 or initial_meter >= 1000000000:
            print("invalid entry, please enter a valid meter number")
            break
        else:
            final_meter = int(input('Enter ending meter reading:\n'))
        if final_meter < 0 or final_meter >= 1000000000:
            print(" invalid entry , please enter a valid meter number")
        print(f'Customer code:{code}')
        print(f'initial meter number:{initial_meter:9d}')
        print(f'final meter reading:{final_meter:9d}')
        gallons = meter_reading(initial_meter, final_meter)
        if gallons <= 4000000:
            pay_bill = 1000
        else:
            pay_bill = 1000 + (gallons - 4000000) * 0.00025
            print(f' pay_bill: ${pay_bill: .02f}')

            # calculating the pay bill for industrial customers
    elif code == "i" or code == "I":
        initial_meter = int(input('Enter beginning meter reading:\n'))
        if initial_meter < 0 or initial_meter >= 1000000000:
            print("invalid entry, please enter a valid meter number")
            break
        else:
            final_meter = int(input('Enter ending meter reading:\n'))
        if final_meter < 0 or final_meter >= 1000000000:
            print(" invalid entry , please enter a valid meter number")
        print(f'Customer code:{code}')
        print(f'initial meter number:{initial_meter:9d}')
        print(f'final meter reading:{final_meter:9d}')
        gallons = meter_reading(initial_meter, final_meter)
        if gallons <= 4000000:
            pay_bill = 1000.00
        elif 4000000 < gallons <= 10000000:
            pay_bill = 2000.00
        else:
            pay_bill = 2000.00 + (gallons - 10000000) * 0.00025
        print(f' pay_bill: ${pay_bill: .02f}')
    else:
        print(" Invalid code")
        break
