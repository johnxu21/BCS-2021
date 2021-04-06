try:
    g = input('enter job location')
    b = int(input('enter pay'))
    if g.upper() == 'MBARARA' and b <= 4000000:
        print('No Thanks, I can find something better')
    elif g.upper() == 'MBARARA' and b > 4000000:
        print('I can work with this')
    elif g.upper() == 'KAMPALA' and b >= 10000000:
        print('I can work with this')
    elif g.upper() == 'KAMPALA' and b < 10000000:
        print('No Way!')
    elif g.upper() == 'SPACE' and b >= 0:
        print('Without doubt, I will work')
    elif b >= 6000000:  # g==other districts and y>=6000000
        print('I will surely work')
    else:
        print('No thanks, I can find something better')
except:
   print('invalid entry')


