c = (input('ENTER INITIAL AMOUNT OF INVESTMENT >>'))
n = (input('ENTER NUMBER OF YEARS THE INTEREST IS COMPOUNDED PER YEAR>>'))
r = (input('ENTER YEARLY RATE OF INTEREST>> '))
t = (input('ENTER NUMBER OF YEARS UNTIL MATURATION>>'))


def investment(w, x, y, z):
    try:
        w = float(c)
        x = float(n)
        y = float(r)
        z = float(t)
        p = round(w * (1 + (y / x)) ** (z * x), 2)  # p is rounded to 2 dp using the round function
        return p
    except ValueError:
        return "INVALID ENTRY"


p = investment(c, r, n, t)
print(p)
