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

