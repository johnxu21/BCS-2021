

def compute_investment(c, r, n, t):
    p = c*(1 + (r/n))**(t*n)
    return p


try:
    c = int(input("Enter initial amount:"))
    r = float(input("Enter the yearly rate: "))
    n = int(input("Enter the number of times interest is compounded: "))
    t = int(input("Enter the number of years until maturation:  "))

    compound_interest = compute_investment(c, r, n, t)
    print("The compound interest is", round(compound_interest, 2))
except:
    print("Please enter a numeric value:\n")
