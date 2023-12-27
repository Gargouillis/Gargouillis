"""
Le programme doit permettre de réaliser 5 actions :

1: Ajouter un élément à la liste de courses

2: Retirer un élément de la liste de courses

3: Afficher les éléments de la liste de courses

4: Vider la liste de courses

5: Quitter le programme

"""
liste_de_course = []
choix = ""

while choix == "":
    print("1: Ajouter un élément à la liste de courses")
    print("2: Retirer un élément de la liste de courses")
    print("3: Afficher les éléments de la liste de courses")
    print("4: Vider la liste de courses")
    print("5: Quitter le programme")
    KO = True
    while KO == True:
        try:
            choix = input("Votre choix : ")
            if choix.isdigit():
                if int(choix) in (1, 2, 3, 4, 5):
                    KO = False
                else:
                    print("Choix entre 1 et 5 uniquement")
            else:
                print("Choisir un chiffre numérique entre 1 et 5")
        except:
            pass


while choix != "5":
    if choix == "3":
        print(liste_de_course)
        print("1: Ajouter un élément à la liste de courses")
        print("2: Retirer un élément de la liste de courses")
        print("3: Afficher les éléments de la liste de courses")
        print("4: Vider la liste de courses")
        print("5: Quitter le programme")
        KO = True
        while KO == True:
            try:
                choix = input("Votre choix : ")
                if choix.isdigit():
                    if int(choix) in (1, 2, 3, 4, 5):
                        KO = False
                    else:
                        print("Choix entre 1 et 5 uniquement")
                else:
                    print("Choisir un chiffre numérique entre 1 et 5")
            except:
                pass
    elif choix == "1":
        nouvel_ingredient = input("Saisir un ingrédient : ")
        liste_de_course.append(nouvel_ingredient)
        print("1: Ajouter un élément à la liste de courses")
        print("2: Retirer un élément de la liste de courses")
        print("3: Afficher les éléments de la liste de courses")
        print("4: Vider la liste de courses")
        print("5: Quitter le programme")
        KO = True
        while KO == True:
            try:
                choix = input("Votre choix : ")
                if choix.isdigit():
                    if int(choix) in (1, 2, 3, 4, 5):
                        KO = False
                    else:
                        print("Choix entre 1 et 5 uniquement")
                else:
                    print("Choisir un chiffre numérique entre 1 et 5")
            except:
                pass
    elif choix == "2":
        suppression_ingredient = input("Ingredient à supprimer : ")
        liste_de_course.remove(suppression_ingredient)
        print("1: Ajouter un élément à la liste de courses")
        print("2: Retirer un élément de la liste de courses")
        print("3: Afficher les éléments de la liste de courses")
        print("4: Vider la liste de courses")
        print("5: Quitter le programme")
        KO = True
        while KO == True:
            try:
                choix = input("Votre choix : ")
                if choix.isdigit():
                    if int(choix) in (1, 2, 3, 4, 5):
                        KO = False
                    else:
                        print("Choix entre 1 et 5 uniquement")
                else:
                    print("Choisir un chiffre numérique entre 1 et 5")
            except:
                pass
    elif choix == "4":
        liste_de_course.clear()
        print("1: Ajouter un élément à la liste de courses")
        print("2: Retirer un élément de la liste de courses")
        print("3: Afficher les éléments de la liste de courses")
        print("4: Vider la liste de courses")
        print("5: Quitter le programme")
        KO = True
        while KO == True:
            try:
                choix = input("Votre choix : ")
                if choix.isdigit():
                    if int(choix) in (1, 2, 3, 4, 5):
                        KO = False
                    else:
                        print("Choix entre 1 et 5 uniquement")
                else:
                    print("Choisir un chiffre numérique entre 1 et 5")
            except:
                pass

print("Programme terminé")