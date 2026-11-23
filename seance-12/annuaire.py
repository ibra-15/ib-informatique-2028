noms = ["Samba","Babacar","Bobo","Bibi","Bibicir"]
telephone = ["778696996","788345676","789890987","774342324","789800890"]
def nom_numero(nom):

    for nom_i in range(len(noms)):
        if noms[nom_i] == nom:
            return nom,telephone[nom_i]
    return "Le nom est absent!"

def numero_nom(numero):
    for num_i in range(len(telephone)):
        if telephone[num_i] == numero:
            return noms[num_i], numero
    return "Le numéro n'est pas présent!"

Input= input("Tapez 1 si vous voulez recuperer le numéro à partir du nom ou 2 si l'inverse ! ")
resultat = ""
if Input == "1":
    nom = input("Nom recherché : ").strip()
    resultat = nom_numero(nom)
elif Input == "2":
    numero = input("Numero recheché : ").strip()
    resultat = numero_nom(numero)


print(resultat)