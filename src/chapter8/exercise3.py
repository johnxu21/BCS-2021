handle = open('mbox-short.txt')
count = 0
for line in handle:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        print(words[2])