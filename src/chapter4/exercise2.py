
#user must input C, r, n and t
c = float(input('Enter initial amount of investment c:'))
r = float(input('Enter yearly rate of interest r:'))
n = float(input('Enter number of time interest is compound annually:'))
t = float(input('Enter number of years:'))

def investment(c, r, n, t):
    final = c * (((1 + (r/n))**(n * t)))
    print(final)
investment(c, r, n, t)