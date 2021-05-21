

def compute_pay(hours, rate):
    if hours > 40:
        pay = (hours-40)*rate*0.5 + (hours*rate)  
        return pay
    else:
        pay = hours*rate 
        return pay


try:
    hours_worked = float(input("Enter hours : "))
    hourly_rate = float(input("Enter  rate: "))
    print("Pay is: ", compute_pay(hours_worked, hourly_rate))
except:
    print("Please enter a number:  ")
