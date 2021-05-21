x = (input("enters hours"))
y = (input("enters rate"))


def compute_pay(hours, rate):
    """The try block ensures that the user enters a
   value between from 0-1 otherwise an error message pops up"""
    try:
        hours = float(x)
        rate = float(y)
        if hours <= 40:
            pay= float(hours * rate)
        else:
            pay = float(40 * rate + (hours - 40) * 1.5 * rate)
        return pay
    except ValueError:
        return "INVALID ENTRY"


pay = compute_pay(x, y)
print(pay)
