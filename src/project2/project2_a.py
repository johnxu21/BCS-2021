# A program in “project2_a.py” will copy selected lines from “measles.txt” into a
# file selected by the user
try:
    file = open('measles.txt', 'r')
    output_file = (input('Output file name>>')).lower()
    year = input('Enter year >>')
    if '.txt' in output_file:
        pass
    else:
        print('Error,output file should have [.txt] extension,re-run!!')  # output file should have an extension
        exit()
    file_saved = open(output_file, 'w')
    for line in file:
        if (year == " ") or (year.lower() == "all"):
            file_saved.write(line)  # This is to add data to the new file created.
        elif line[88:].startswith(year):  # #year begins at index 88
            file_saved.write(line)
except FileNotFoundError:
    print("COULD NOT OPEN FILE")

file.close()
output_file.close()
