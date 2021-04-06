try:
    hours = int(input('enter the hours worked'))
    rate = float(input('enter the payment rate'))
    if hours <= 40:
        payment = rate * 40
        print(payment)
    if hours > 40:
        payment = rate * hours
        extra = 1.5 * (hours - 40) * 10
        pay = payment + extra
        print(pay)
except:
    print('error, please enter numeric input')


