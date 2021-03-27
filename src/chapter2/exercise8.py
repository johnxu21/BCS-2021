t = float(input("Enter t"))
C = float(input("Enter C"))
r = float(input("Enter r"))
n = float(input("Enter n"))
p = round(C * (1 + (r / n)) ** (t * n), 2)  # The value of "p" already is rounded off to 2 dp using the round function
print(p)
