n = int(input("Saisissez un entier à 3 chiffres : "))
somme =0 

while n > 0 :
    chiffre = n%10
    n //= 10
    somme += chiffre

print(somme)
