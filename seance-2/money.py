montant= int(input("Quel est le montant que vous souhaitez obtenir la monnaie ? "))
monnaie_a_rendre = (5000,1000,500,100)
while montant > 0:
    for monnaie_val in monnaie_a_rendre:
        n_billet_piece = ( montant ) // monnaie_val
        montant %= monnaie_val
        print(f"{n_billet_piece} x {monnaie_val}")
        if monnaie_val == 100 and montant > 0 :
            print(f"restant : {montant}")
            montant = 0
        
    
