try:
    x = float(input("enters hours"))
    y = float(input("enters rate"))
    z = (x * y)  # this is the pay for hours of work below or equal to 40
    q = y * 40
    m = (1.5 * (x - 40) * y)  # m is the extra hours worked beyond the 40 hours .
    r = (q + m)  # this is the pay for hours of work above 40
    if x <= 40:
        print(z)
    elif x > 40:
        print(r)
except:
    print("ERROR, PLEASE ENTER NUMERIC INPUT")
