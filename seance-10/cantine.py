menu = {"0": "Add a student","1":"Serve a student","2":"Qui est en tête","3":"nombre d'eleve en attente","-1":"Leave"}
file = []
def affichage_menu():
    print("\n")
    print("================================================================================================================")      
    for navigation in menu:
        if len(file) == 0 and navigation =="1":
            continue
        if len(file) == 0 and navigation =="2":
            continue
        if len(file) == 0 and navigation =="3":
            continue
        print(navigation,":",menu[navigation])  
    print("================================================================================================================")      
    print("\n") 

def lire_entier(message):

    while True:        
        try:    
            affichage_menu() 
            num = int(input(message))
        
        except ValueError:
            continue
        else:
            

            if num == 0:
                name = input("Quelle est le nom de l'élève? ")
                file.append(name)

            elif num == 1:
                eleve = file.pop(0)
                print(f"{eleve} a été servi !")

            elif num == 2:
                eleve = file[0]
                print(f"{eleve} est le prochain")
            elif num == 3:
                print(f"Il y a {len(file)} en attente")
            elif num == -1:
                print("Leaving the cantine")
                break
lire_entier("Input : ")