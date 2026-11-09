paire = {")":"(","]":"[","}":"{"}
pile = []

chaine = input("Chaine: ")
for char in chaine:
    try:
        print(pile)
        if char in "({[":
            pile.append(char)
        elif pile[-1] == paire[char]:
            pile.pop()
    except IndexError:
        continue
print(len(pile))
if pile:
    print("Non Equilibré")
else:
    print("Equilibré")