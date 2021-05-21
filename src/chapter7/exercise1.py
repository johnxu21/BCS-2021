fhand = open('mbox-short.txt')

for line in fhand: 
                   
    shout = line.rstrip().upper()       
    print(shout)

