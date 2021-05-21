count = 0
total = 0
numbers = list()
while True:
    line = input("Enter number here: ")
    try:
        line = int(line)
        numbers.append(line)
        total = total + line
        count = count + 1
        average = total/count
        maximum=max(numbers)
        minimum = min(numbers)
    except:
        if line =="done":
            break
        else:
            print("Invalid input")

print ("maximum =", maximum)
print ("minimum =", minimum)

