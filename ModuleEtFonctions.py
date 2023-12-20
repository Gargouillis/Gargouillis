import random
import os
from pprint import pprint


"""
r = random.randint(0, 10)
print(r)

s = random.uniform(0, 1)
print(s)

# attention, la fct randrange est exclusive, donc le numéro donné ne sera jamais pris en compte
# on aura jamais 999
t = random.randrange(999)
print(t)

# autre chose interressante sur randrange, c'est qu"on peut lui donner des pas
# il va prendre dezs nombres entre 0 et 1001 mais qui sont multiple de 100 donc 0, 100, 200, 700 etc jusque 1000 max !
u = random.randrange(0 , 1001, 100)
print(u)



a = random.randint(0, 50)
b = random.randint(0, 50)
print(a)
print(b)

if a == b:
    print("Le nombre a et le nombre b sont égaux.")
elif a > b:
    print("Le nombre a est plus grand que le nombre b.")
else:
    print("Le nombre b est plus grand que le nombre a.")



chemin = "C:\\Formation_Udemy"

# on utilise join au lieu de concaténation de dossier (string)
# jon permet de créer plusieurs dossier en meme temps
dossier = os.path.join(chemin, "Dossier1", "Dossier2")

print(dossier)

# on utilise makedirs au lieu de mkdir car mkdir ne peut pas créer 2 dossiers en même temps
if not os.path.exists(dossier):
    os.makedirs(dossier)
else:
    print("Les dossiers existent")

# autre facon de gérer le cas où le fichier existe
os.makedirs(dossier, exist_ok=True)

# remodirs pour supprimer les dossiers
if os.path.exists(dossier):
    os.removedirs(dossier)
    print("dossier supprimé")

"""

# print(dir(random))

#  help(random.uniform)

# pprint(dir(random))

# fonction callable

print(callable(pprint))
print(callable(os))
print(callable(os.name))
print(os.name)