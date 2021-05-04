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
