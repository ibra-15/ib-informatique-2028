notes = [14.5, 11, 17.5, 9.5, 16, 8, 13]

max = notes[0]
min = notes[0]
n_moyenne = 0
sum = 0
for note in notes:
    if note > max:
        max = note
    elif note < min:
        min = note
        
    if note >= 10:
        n_moyenne += 1
    sum += note

moyenne = round(sum / len(notes))
print(f"La moyenne est de {moyenne} \n. La meilleur note est {max}, et la pire note est {min}. Il y a {n_moyenne} élèves qui ont la moyenne")