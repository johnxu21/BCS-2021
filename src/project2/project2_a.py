# The program in “project2_a.py” will copy selected lines from “measles.txt” into a
# file selected by the user.
try:
    file1 = open('measles.txt', 'r')
except FileNotFoundError:
    print('File cannot be opened:', ' measles.txt')
    quit()
while True:
    out_put_file = input('enter output file >>>')
    year = input('enter the year')
    if len(year) == 4:
        converted_year = year
        output_file = open('file_out', 'w')
        for line in 'file1':
            if  converted_year == line[88:88 + len(year)]:
                output_file.write(line)
            elif year == ("", "all", "ALL"):
                output_file.write(line)
    else:
        print('enter correct year')  # this pops up when  the length of the year is not 4
