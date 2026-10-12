def somme(liste):
    sum = 0
    for n in liste:
        sum += n
    return sum
def moyenne(liste):
    return somme(liste) / len(liste)
def maximum(liste):
    max = liste[0]
    for n in liste:
        if n > max:
            max = n
    return max
def minimum(liste):
    min = liste[0]
    for n in liste:
        if n < min:
            min = n
    return min

note = [14] 
print(somme(note))
print(moyenne(note))
print(maximum(note))
print(minimum(note))