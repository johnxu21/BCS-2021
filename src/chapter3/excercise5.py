try:
    a = int(input('Number of guests'))
    if 0 < a <= 50:
        print('price =$4000')
    if 50 < a <= 100:
        print('price = $10000')
    if 100 < a <= 200:
        print('price = $15000')
    elif a > 200:
        print('price = $20000')
except:
    print('error, please enter a digit')

