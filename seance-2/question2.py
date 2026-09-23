second_input = int(input("Saisissez un nombre de secondes entier: "))
day = second_input // 86400
heures = (second_input % 86400)// 3600
minutes = (second_input % 3600) // 60
seconde_restant = (second_input % 3600) % 60
print(f"{day}:{heures}:{minutes}:{seconde_restant}")