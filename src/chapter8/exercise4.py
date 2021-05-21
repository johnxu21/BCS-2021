fhand = open('romeo.txt')
lst = list()
for line in fhand:  # to read every line of file romeo.txt
    word = line.rstrip().split()  # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:
        if element in lst:  # if element is repeated
            continue
        else:
            lst.append(element)
lst.sort()  # this sorts the words when the loop ends.
print(lst)
