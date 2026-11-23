nom = ["Samba","Babacar","Bobo","Bibi","Bibicir"]
telephone = ["778696996","788345676","789890987","774342324","789800890"]
def nom_numero(indice):

    for nom_i in range(len(nom)):
        if nom[nom_i] == indice:
            return indice,telephone[nom_i]
    return "Le nom est absent!"
def numero_nom(indice):
    for num_i in range(len(telephone)):
        if telephone[num_i] == indice:
            return nom[num_i], indice
    return "Le numéro n'est pas présent!"
Input= input("You want to get number from name ? [Yes] or [No]")
resultat = ""
if Input == "Yes":
    indice = input("Nom recherché : ").strip()
    resultat = nom_numero(indice)
elif Input == "No":
    indice = input("Numero recheché : ").strip()
    resultat = numero_nom(indice)


print(resultat)