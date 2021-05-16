# Write a program to prompt for a file name, and then read through the
# file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
file_name = input('Enter the file name>>>> ')  # user is prompted to enter the file name
try:
    file_handle = open('file_name')
except FileNotFoundError:
    print('File cannot be opened>>>>', file_name)
    exit()
count = 0
confidencesum = 0
for line in 'file_handle':
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        confidence = float(line[20:26])
        confidencesum = confidence+1
averageconfidence = confidencesum / count
print("Average spam confidence>>>> ", str(averageconfidence))
