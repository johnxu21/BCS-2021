amount = float(input("Enter amount: "))

if amount > 20:

    d_t = int(amount//20)
    amt1 = d_t*20
    print(str(d_t) + " twenties")

    rem1 = int((amount % 20))
    d_t2 = rem1//10
    amt2 = d_t2*10
    print(str(d_t2) + ' tens')

    rem2 = (rem1 % 10)
    d_t3 = rem2//5
    amt3 = d_t3*5
    print(str(d_t3) + " fives")

    rem3 = rem2 % 5
    d_t4 = rem3 // 1
    amt4 = d_t4*1
    print(str(d_t4) + " Ones")

    dec = amount-(amt1+amt2+amt3+amt4)

    q = dec//0.25
    print(str(int(q))+' Quarters')

    d = dec % 0.25
    print(str(int(d//0.1)) + ' Dimes')

    n = d % 0.1
    print(str(int(n//0.05)) + ' Nickels')
    p = n % 0.05
    print(str(int(p // 0.01)) + ' Pennies')

