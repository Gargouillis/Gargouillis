"""
for i in range (1,11):
    print(f"Utilisateur {i}")

mot = "Python"
i = len(mot)
while i >0:
    print(mot[i-1])
    i -= 1

for lettre in reversed(mot):
    print(lettre)

mot = mot[::-1]
for lettres in mot:
    print(lettres)    

py = "python"
for i in range(0, len(py)):
    print(py[-i-1])

mot = "Python"
for i in range(len(mot)):
    print(i)

nombre = 7
for i in range(0,11):
    print(f"{i} x {nombre} = {i*nombre}")



i = 0
while i < 10:
    i += 1
    pass
	
resultat = "Exercice réussi !"
print(resultat)      

continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")   

nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i%2 ==0]
# for i in nombres:
#     if i % 2 == 0:
#         nombres_pairs.append(i)
print(nombres_pairs)

# ---------------------------------------------------- #

nombres = range(-10, 10)
nombres_positifs = [i for i in nombres if i >= 0]
# for i in nombres:
#     if i >= 0:
#         nombres_positifs.append(i)
print(nombres_positifs)

# ---------------------------------------------------- #

nombres = range(5)
nombres_doubles = [i * 2 for i in nombres]
# for i in nombres:
#     nombres_doubles.append(i * 2)
print(nombres_doubles)

# ---------------------------------------------------- #

nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]
# for i in nombres:
#     if i % 2 == 0:
#         nombres_inverses.append(i)
#     else:
#         nombres_inverses.append(-i)
print(nombres_inverses)


valide = True
nombre_str_un = input("Entrez un premier nombre : ")
nombre_str_deux = input("Entrez un deuxième nombre : ")
if not nombre_str_un.isdigit() or not nombre_str_deux.isdigit():
    valide = False

if valide == True:
    print(f"Le résultat de l'addition de {nombre_str_un} avec {nombre_str_deux} est égal à {int(nombre_str_un) + int(nombre_str_deux)}")
else:
    print("Veuillez entrer deux nombres valides")    """
continuer = True
while continuer == True:
    try:
        a = int(input("Entrez un premier nombre : "))
        b = int(input("Entrez un deuxième nombre : "))
        print(f"Le résultat de l'addition de {a} avec {b} est égal à {a + b}")
        continuer = False
    except:
        print("les valeures ne sont pas bonne")