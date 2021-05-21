string = 'X-DSPAM-Confidence:0.8475'  # we changed  'str' to 'string'  since str being a built in word, it was
#  it was causing a warning
colon = string.find(':')
extract = string[colon + 1:]
# print(type(extract))
print(extract)
f = float(extract)
# print(type(f))
print('FLOAT VALUE =', f)
