""" dans ce module on va aborder les listes et les tuples"""

# les listes sont mutables, c'est a dire qu'on pezut ajouter/modifier ou supprimer des élèments
# les listes c'est avec des parenthèses

ma_liste = [250, "Python", True]
print(ma_liste)
print(type(ma_liste))

# les tuples c'est la même chose que les listes mais on ne peut pas les modifier ainsi il y a moins de fonctionnalité
# et donc les tuples sont plus rapide à utiliser

# les tuples c'est avec des parenthèses

mon_tuple = (250, "Python", True)
print(mon_tuple)
print(type(mon_tuple))

# on peut changer un tuple en liste et vice versa, exemple

mon_tuple = list(mon_tuple)
print(mon_tuple)
print(type(mon_tuple))

mon_tuple = tuple(mon_tuple)
print(mon_tuple)
print(type(mon_tuple))

# ajouter 1 ou plusieurs élèments à une liste append pour 1 elts et extend pour plusieurs elts

ma_liste.append(5)
print(ma_liste)

ma_liste.extend([6, 7, "Jamais"])
print(ma_liste)

# supprimer des elts, utiliser remove qui enleve que la 1ere valeure trouvée
# pour sup^primer plusieurs occurences de 5, il faut appeler plusieurs fois remove

ma_liste.remove(5)
print(ma_liste)

# récupere des elts
print(ma_liste[3])

# récuperer le dernier elts et ainsi de suite
# dernier
print(ma_liste[-1])

# avant dernier
print(ma_liste[-2])

liste1 = ["Utilisateur_01",
          "Utilisateur_02",
          "Utilisateur_03",
          "Utilisateur_04",
          "Utilisateur_05",
          "Utilisateur_06"]

print(liste1)

# pour récupérer uniquement les 4 premiers elts donc jusque Utilisateur_04 
print(liste1[0:4])

# on peut récuperer autrement, voici un autre exemple, pour récuperer la liste sauf le dernier elt
print(liste1[:-1])

# pour commencer à l'indice 2 jusqu'à la fin
print(liste1[2:])

# pour récuperer un elt sur 2 par exemple
print(liste1[::2])
print(liste1[1::2])
# pour avoir la liste dans l'ordre inverse
print(liste1[::-1])

