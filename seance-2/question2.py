second_input = int(input("Saisissez un nombre de secondes entier: "))
heures = second_input// 3600
minutes = (second_input % 3600) // 60
seconde_restant = (second_input % 3600) % 60
print(f"{heures}:{minutes}:{seconde_restant}")