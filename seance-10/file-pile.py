pile_entree = []
pile_sortie = []

menu = {"0": "Add element","1":"Transvase","2":"Treat element","-1":"Leave"}
def affichage_menu():
    print("\n")
    print("================================================================================================================")      
    for navigation in menu:
        if len(pile_sortie)==0 and navigation == "2":
            continue
        elif len(pile_entree)==0 and navigation == "1" or len(pile_sortie) > 0 and navigation == "1":
            continue
        print(navigation,":",menu[navigation])  
    print("================================================================================================================")      
    print("\n") 
def transvase():
    while pile_entree:
        last = pile_entree.pop(0)
        print(last)
        pile_sortie.append(last)
    print(pile_sortie)
def treat_element():
    element_treated = pile_sortie.pop(0)
    print(element_treated,"has been treated")
    
def lire_entier(message):
    element_count = 0
    while True:        
        try:    
            affichage_menu() 
            num = int(input(message))
        
        except ValueError:
            continue
        else:
            if num == 0 :
                element_count += 1
                pile_entree.append(element_count)
                print(element_count)
            elif num == 1:
                if not pile_sortie and pile_entree:
                    transvase()
            elif num == 2:
                treat_element()
            elif num == -1:
                print("Left program")
                break
lire_entier("Input : ")