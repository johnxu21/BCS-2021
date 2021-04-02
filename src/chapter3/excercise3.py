try:
    score = (input('enter score'))
    if score < 0.6:
        print('F')
        if score >= 0.6:
            print('D')
        if score >= 0.7:
            print('C')
        if score >= 0.8:
            print('B')
            if score >= 0.9:
                print('A')
except:
    print('error, out of range')



