try:
    x = float(input('enter hours'))
    y = float(input('enter rate'))
    q = 1.5 * y
    w = q * x
    z = x * y
    if x < 40:
        print(z)
    else:
        print(w)
except:
    print('error, please enter numeric input')


