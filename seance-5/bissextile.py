year = int(input("Choisissez une année : "))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} (oui)")
    elif year % 100 == 0 and year % 400 ==0 : 
        print(f"{year} (oui)")
    else:
        print(f"{year} (non)")
else:
    print(f"{year} (non)")


    