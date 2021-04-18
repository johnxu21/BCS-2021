c = float(input('enter c'))
n = float(input('enter n'))
r = float(input('enter r'))
t = float(input('enter t'))
p = round(c * (1 + (r / n)) ** (t * n), 2)  # p is rounded to 2 dp using the round function


def investment(c, n, r, t):
    return p


p = investment(c, r, n, t)
print(p)
