count = 0
total = 0

while True:
    line = input("Enter number here: ")
    try:
        line = int(line)
        total = total + line
        count = count + 1
        average = total/count

    except:
        if line =="done":
            break
        else:
            print("Invalid input")

print ("Total=", total, "Count=",  count ,"Average =", average)
