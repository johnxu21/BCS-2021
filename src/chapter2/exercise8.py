#user must input C, r, n and t
c = float(input('Enter initial amount of investment c:'))
r = float(input('Enter yearly rate of interest r:'))
n = float(input('Enter number of time interest is compound annually:'))
t = float(input('Enter number of years:'))

final = c * (((1 + (r/n))**(n * t)))
print('the final amount after', t, 'years is', round(final, 2))