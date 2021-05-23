#  a program that reads through the mail box  splits the line starting "From
filename = input('Enter a file name: ')
count = 0

fhand = open(filename)
for line in fhand:
    if line.startswith('From: '):
        print(line.split(' ')[1])
        count = count + 1
print('There were', count, 'lines that start with From')