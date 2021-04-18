x = (input("enters hours"))
y = float(input("enters rate"))


def compute_pay(hours, rate):
    hours = float(x)
    rate = float(y)

    if hours <= 40:
        pay = float(hours * rate)
    else:
        pay = float(40 * rate + (hours - 40) * 1.5 * rate)
    return pay


pay = compute_pay(45, 10)
print(pay)
