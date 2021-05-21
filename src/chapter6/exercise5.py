str = 'X-DSPAM-Confidence: 0.8475'
 # Finds the colon character
col_pos = str.find(':')
 # Extracts portion after colon
var = str [col_pos+1:]
# Converts to floating point number
var = float(var)
print('This is a floating point number %g.' % (var))

