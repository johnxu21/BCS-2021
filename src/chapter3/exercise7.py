location = input("Enter your location: ")
pay =  int(input("Enter your pay: "))
if location == "Space" and pay >= 0:
    print(" Decision: Without doubt I'll take it")
elif location == "Mbarara" and pay > 4000000:
    print("Decision: Sure, l can l work with this" )
elif location == "Mbarara" and pay < 4000000:
    print("Decision: No thanks,I can find something better")    
elif location == "Kampala" and pay >= 10000000:
    print("Descion: Without dounbt I'll take it")
elif location == "Kampala" and pay < 10000000:
    print("Decision: No way")   
elif pay < 6000000:
    print("Decision: No thankds i can find something better")
else:
    print("Decision: Sure,I can work this")