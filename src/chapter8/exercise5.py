try:
    fname = input('please enter file name >>>')
    fhand = open(fname)  # make the input file readable.
    count = 0
    for line in fhand:
        words = line.split()  # this splits the line into words
        if len(words) < 3 or words[0] != 'From':
            continue
        print(words[1])
        count += 1
    print('There were %d lines in the file with From as the first word' % count)
except FileNotFoundError:
    print('file not found')
