prenom = input("Quel est votre prénom ? ")
annee_naissance = int(input("En quelle année êtes vous né? "))
annee_en_cours = 2026
age = annee_en_cours - annee_naissance
taille = int(input("Quelle taille fait-tu ? "))
majeur = age >= 18
if majeur:
    majorité = "Vous êtes majeur"
else:
    majorité = "Vous êtes mineur"
    
print(f"Bonjour {prenom}, vous êtes né en {annee_naissance} et vous avez {age} ans. \n Vous faites {taille} cm. \n Votre initiale est {prenom[0]} \n {majorité}")