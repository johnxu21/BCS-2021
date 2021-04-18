hours = float(input("Enter the hours: "))
rate = float(input("Enter the rate: "))
def computepay(hours, rate):
    if hours > 40:
      regular_pay = (hours * rate)
      extra_pay = ((hours-40)*0.5*rate)
      overTime_pay = regular_pay + extra_pay
      print(overTime_pay)
    else:
      normal_pay = hours * rate
      prnt(normal_pay)
computepay(hours, rate)
