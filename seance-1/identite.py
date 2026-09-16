prenom = input("Quel est votre prénom ? ")
annee_naissance = int(input("En quelle année êtes vous né? "))
annee_en_cours = 2026
age = annee_en_cours - annee_naissance
taille = float(input("Quelle taille fait-tu (en m)? "))
taille_cm = round(taille*100)
print(taille_cm)
majeur = age >= 18
if majeur:
    majorité = "Vous êtes majeur"
else:
    majorité = "Vous êtes mineur"

print(f"Bonjour {prenom}, vous êtes né en {annee_naissance} et vous avez {age} ans. \n Vous faites {taille_cm} cm. \n Votre initiale est {prenom[0]} \n {majorité}")

print(type(prenom))
print(type(annee_naissance))
print(type(annee_en_cours))
print(type(age))
print(type(taille))
print(type(majeur))
