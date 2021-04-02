try:
    x = input('enter location(capitalise the first letter)>>')
    y = float(input('enter pay>>'))
    if x == 'Mbarara' and y > 4000000:
        print('I WILL TAKE THE JOB')
    elif x == 'Mbarara' and y <= 4000000:
        print('SORRY, I CAN NOT WORK FOR THAT')
    elif x == 'Kampala' and y > 10000000:
        print('I WILL DEFINENTLY WORK')
    elif x == 'Kampala' and y <= 10000000:
        print('NO WAY !')
    elif x == 'Space' and y >= 0:
        print('WITHOUT DOUBT, I WILL TAKE IT')
    elif y >= 6000000:  # x==other districts and y>=6000000
        print('I will surely work')
    else:
        print('No thanks, I can find something better')
except:
   print('invalid entry')


