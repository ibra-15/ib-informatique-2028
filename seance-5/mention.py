note = int(input("Saisissez une note sur 20"))

if note < 0 or note >20:
    print("Note invalide")

elif note >=16:
    print("Tres bien")
elif note >= 14:
    print("Bien")
elif note >=12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
    # elif note < 10 :
    #     print("Insuffisant") Inutile car si on arrive ici c'est forcement < 10
else:
    print("Insuffisant")