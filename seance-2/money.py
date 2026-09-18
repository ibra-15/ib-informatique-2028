montant= int(input("Quel est le montant que vous souhaitez obtenir la monnaie ? "))
monnaie_a_rendre = (1, 5000,1000,500,100)


def monnaie(montant_donne):
   for monnaie_val in monnaie_a_rendre:
    pos = monnaie_a_rendre.index(monnaie_val)
    if monnaie_a_rendre[pos+1] > len(monnaie_a_rendre):
       reste = (montant_donne % monnaie_val)
       return reste
    else:
       n_billet_piece = (montant_donne % monnaie_val) // monnaie_a_rendre[pos+1]
       return n_billet_piece,"x",monnaie_a_rendre[pos+1]

print(monnaie(montant))