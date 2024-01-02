import json

chemin = "/workspaces/Gargouillis/fichier.json"
chemin2 = "/workspaces/Gargouillis/fichier.txt"

# with open(chemin, "w") as f:
#     json.dump("Test", f)
"""
with open(chemin, "a") as f2:
    json.dump(list(range(10)), f2, indent= 4)

with open(chemin, "r") as f3:
    liste = json.load(f3)
    print(liste)
    print(type(liste))
    """

with open(chemin, "r") as f:
    donnees = json.load(f)

print(donnees)

donnees.append("Pèche") # attention au caractère spéciaux, dans le JSON on aura "P\u00e8che" avec \u00e8 = è, pour éviter cela on peut mettre comme ci-dessous

with open(chemin, "w") as f:
    json.dump(donnees, f, indent= 4, ensure_ascii= False) # ensure_ascii= False permet de mettre le è normalement

with open(chemin, "r") as f:
    donnees2 = json.load(f)

print(donnees2)

# f.seek(0) permet de remttre le curseur à la position 0, mais on peut mettre la valeur qu'on veut
# quand on fait un f.read(), le curseur se positionne à la dernière ligne lu
# quand on refait un f.read(), Python n'affiche rien car le curseur est resté à la fin du fichier
# et il n'y a donc rien à afficher
f2 = open(chemin2)
print(f2.read(10))

f2.seek(5)

print(f2.read())