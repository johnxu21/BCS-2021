def investment(C,r,n,t):
    P = C * ((1 + ((r) / n)) ** (t * n))
    return P

C = float(input('Enter initial amount; '))
r = float(input('Enter the yearly rate; '))
n = float(input('Enter compound interest; '))
t = float(input('Enter years till maturation; '))

print(f"The final value is {investment(C,r,t,n): 2f}")