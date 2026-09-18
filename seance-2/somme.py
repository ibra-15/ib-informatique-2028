n = int(input("Saisissez un entier à 3 chiffres : "))

def somme(entier):
    u = entier % 10
    d = (entier //10) %10
    c = ((entier//10)//10 )% 10
    return u+d+c

print(f"La somme de ses chiffres est de : {somme(n)}")