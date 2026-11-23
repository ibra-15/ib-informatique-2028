TEMPS_PAR_PAGE = 5
file_document = []
menu = {"0": "Add document","1":"Print them","-1":"Leave"}

def affichage_menu():
    print("\n")
    print("================================================================================================================")      
    for navigation in menu:
        if len(file_document) == 5 and navigation =="0":
            continue
        if len(file_document) == 0 and navigation =="1":
            continue
        print(navigation,":",menu[navigation])  
    print("================================================================================================================")      
    print("\n") 

def ajout():
    nom = input("Quel est le nom du document? ")
    n_page = int(input("Combien de page y a-t-il ? "))
    if n_page <= 0 or not nom:
        print("Entree non valide")
        return 
    doc= [nom,n_page]
    file_document.append(doc)

def imprimer():
    while file_document:
        for document in file_document:
            if document == file_document.pop(0):
                print(document)
                print(f"{document[0]} a été imprimé !")
                print(f"Il a pris {document[1] * TEMPS_PAR_PAGE} secondes!")
    print("Tout les documents ont été imprimés!")
    0
def lire_entier(message):

    while True:        
        try:    
            affichage_menu() 
            num = int(input(message))

        except ValueError:
            continue
        else:
            

            if num == 0:
                ajout()
            elif num == 1:
                imprimer()
                        
            elif num == -1:
                print("Leaving the print")
                break
lire_entier("Input : ")
