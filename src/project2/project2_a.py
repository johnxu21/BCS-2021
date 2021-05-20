# The program in “project2_a.py” will copy selected lines from “measles.txt” into a
# file selected by the user.
try:
    file_input = open('measles.txt', 'r')
except FileNotFoundError:
    print('File cannot be opened:', ' measles.txt')
    quit()

out_put_file = input('enter output file >>>')
year = (input('enter the year>>>'))
converted_year = year
if len(year) <=4:
    out_put_file = open(out_put_file, 'w')
if len(year) >= 5:
    print('Please enter correct year')  # this pops up when  the length of the year is not 4
for line in file_input:
    if converted_year == line[88:88 + len(year)]:
        out_put_file.write(line)
    elif year == ("", "all", "ALL"):
        out_put_file.write(line)

file_input.close()
out_put_file.close()
