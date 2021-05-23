handle = open('mbox-short.txt')
count = 0
for line in handle:
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    print(words[2])