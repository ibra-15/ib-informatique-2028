temp_F = float(input("Saisissez la température afficher par le thermomètre de la salle en (°F) : "))

def convertion(temperature):
    return round((temperature-32)*5 / 9, 1)

print(f"La temperature de la salle en degré Celsus (°C) est de : \n {convertion(temp_F)}")