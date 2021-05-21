c = float(input("Enter Amount Between 0-99 :"))
print(c // 20, "Twenties")
c = c % 20
print(c // 10, "Tens")
c = c % 10
print(c // 5, "Fives")
c = c % 5
print(c // 1, "Ones")
c = c % 1
print(c // 0.25, "Quarters")
c = c % 0.25
print(c // 0.1, "Dimes")
c = c % 0.1
print(c // 0.05, "Nickles")
c = c % 0.05
print(c // 0.01, "Pennies")
