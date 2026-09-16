entier1 = int(input("Saisir un nombre entier "))
entier2 = int(input("Saisir un autre nombre entier "))

def somme(a,b):
    resultat = a+b
    return resultat

somme_input = somme(entier1,entier2)
print(f"Voici la somme des entiers choisi : \n {somme_input}")