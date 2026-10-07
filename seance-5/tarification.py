age = int(input("Quelle age avez vous ?  "))
carte_membre = input("Avez vous une carte membre")

carte_membre_lower_Case = carte_membre.lower()

if carte_membre_lower_Case == "non":
    if age < 12:
        print("2000 FCFA")
    elif age >= 12 and age <= 17:
        print("3500 FCFA")
    else:
        print("5000 FCFA")
else:
    if age < 12:
        print("20 pourcent de 2000 FCFA")
    elif age >= 12 and age <= 17:
        print("20 pourcent de 3500 FCFA")
    else:
        print("20 pourcent de 5000 FCFA")