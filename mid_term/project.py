

def gallon(beg_meter_reading, end_meter_reading):
    if end_meter_reading>beg_meter_reading:
        gallons=(end_meter_reading-beg_meter_reading)/10
    else:
        beg_meter_reading=(1000000000-beg_meter_reading)
        gallons=(end_meter_reading+beg_meter_reading)/10
    return gallons
    
def output():  
    print(f'Customer code {customer_code}')
    print(f'Beginnig meter reading: {beg_meter_reading:09d}')
    print(f'Ending meter reading: {end_meter_reading:09d}')


while True:
    try:
        customer_code=input('Enter the customer code: ').lower()
        beg_meter_reading=int(input('Enter the begining meter reading: '))
        end_meter_reading=int(input('Enter the endining meter reading: '))
    except:
        print('Invalid input')
        

    gallons = gallon(beg_meter_reading, end_meter_reading)
    if 0 < beg_meter_reading <9999999999  and 0 < end_meter_reading <9999999999:
            if customer_code == 'r':
                amount_billed=(5.00+(0.0005*gallons))
                amount_billed= round(amount_billed,2)
                output()
                print(f'Gallons of water used:{gallons}')
                print(f'Amount billed: ${amount_billed}')
            elif customer_code== 'c':
                if gallons<=4000000:
                    output()
                    print(f'Gallons of water used:{gallons}')
                    print(f'Amount billed:${1000.0}')
                elif gallons>40000000:
                    output()
                    amount_billed=1000+(gallons-4000000)*0.00025
                    print(f'Gallons of water used:{gallons}')
                    print(f'Amount billed ${amount_billed}')
            elif customer_code=='i': 
                if gallons<=4000000:
                    output()
                    print(f'Gallons of water used:{gallons}')
                    print(f'Amount billed ${1000.00}')
                elif gallons>40000000:
                    output()
                    print(f'Gallons of water used:{gallons}')
                    print(f'Amount billed ${2000.00}')
                elif gallons>10000000:
                    output()
                    amount_billed=(2000.00+(0.00025)*gallons)
                    print(f'Amount billed: ${amount_billed}')
            else:
                print('Ivalid input')
    else:
        print('Invalid input')


