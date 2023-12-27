# la boucle FOR

liste = "Jevaisbien"
for element in liste:
    print(element)

for i in [0, 5, 8, 4, 6]:
    print(i)

for i in range(10):
    print(f"Eleve  {i}")

# la boucle WHILE
        
i = 0
while i < 100:
    print("Bonjour")
    i += 1

# continuer = "o"
# while continuer == "o":
#     print("Bonjour")
#     continuer = input("Voulez vous continuer (o/n) ? : ")

# liste = []
# while liste == True:
#     print("Itération sur la liste")

# import time

# while True:
#     print("Sauvegarde en cours ...")
#     time.sleep(6)

# dans ce cas, le script va écrire Papa, Joe et Maman seulement et va zapper tous les nombres
liste = ["0", "15", "Papa", "45", "Joe", "4", "56", "Maman"]
for element in liste:
    if element.isdigit():
        continue
    print(element)

# dans ce cas, on va sortir tout de suite de la boucle for car 0 est bien un digit, rien ne sera affiché
liste = ["0", "15", "Papa", "45", "Joe", "4", "56", "Maman"]
for element in liste:
    if element.isdigit():
        break
    print(element)

# compréhension de liste
liste5 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 9]
nombre_positifs = []

for element in liste5:
    if element > 0:
        nombre_positifs.append(element)

print(liste5)
print(nombre_positifs)

# avec la comprehension de liste on peut simplifier le code ci-dessus

liste6 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 9]
nombre_positifs2 = [element * 2 for element in liste6 if element > 0]
print(nombre_positifs2)

# fonctions ANY et ALL

liste_true_false = [True, True, True, True]
print(any(liste_true_false))    # cette foncxtion permet de savoir si dans la liste il y a au moins 1 True et renvoie true si c'est le cas sinon false
print(all(liste_true_false))    # all vérifie si tout est à True et donc renvoie true mais si un seul est false, renvoie false

# dans ces 2 cas ci-dessus, c'est juste pour montrer comment marche les fonctions mais ca n'a pas d'interet
# all([f.endswith(".jpg") for f in files]), dans cette exemple on vérifie que tous les fichiers d'une liste f se termine bien par .jpg

# un autre exemple
notes = [12, 8, 19, 15, 13, 9]
print(any([x > 18 for x in notes]))