"""
Une methode est une fonction qui appartient à un objet
"""

# exemple avec sorted et sort
# sorted tri une liste sans l'écraser

liste = [5, 3, 7, 1, 9]
sorted(liste) # sorted ne trie pas la liste original sauf si on l'affecte à liste comme liste = sorted(liste)
liste.sort() # pour agir sur la liste, il faut utiliser sa méthode
print(liste)

# objet muable : LISTE, DICTIONNAIRE, SETS
# objet immuable : CHIANE DE CARACTERES, NOMBRES

titre_film = "le seigneur des anneaux"
titre = titre_film.title()   # ici, on utilise la methode de la chaine de caractète MAIS on ne peut pas changer la variable titre_film car c'est immuable
print(titre_film)
print(titre)

# fonctions LEN, ROUND, MIN, MAX, SUM, RANGE
# len
langage = "Python"
print(len(langage))
tableau = [2, 3, 6, 8]
print(len(tableau))

# round
print(round(6.2548751,3))
print(round(2.7))

# MAX and MIN
print(min([5, 3, 7, 1, 9]))
print(max([5, 3, 7, 1, 9]))

# MIN et MAX s'utilise ausi sur des chaines de caractères
print(min("juteacprt"))
print(max("juteacprt"))

# SUM
print(sum([5, 3, 7, 1, 9]))

# RANGE
liste3 = list(range(0,8))
print(liste3)
liste4 = list(range(3,8))
print(liste4)