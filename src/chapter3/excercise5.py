""""A PROGRAM THAT PROMPTS THE USER FOR 
 THE NUMBER OF PEOPLE ATTENDING THEIR WEDDING AND PRINTS THE CORRESPONDING PRICE IN THE CONSOLE"""""
try:
    a = int(input('Number of guests'))
    if 0 < a <= 50:
        print('price =$4000')
    elif 50 < a <= 100:
        print('price = $10000')
    elif 100 < a <= 200:
        print('price = $15000')
    elif a > 200:
        print('price = $20000')
except:
    print('error, please enter a digit')

