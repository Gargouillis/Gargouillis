# ctrl + d permet de changer des meme caractère en meme temps
# 3 facons de mettre un chemin windows
import os

# le double \ permet de ne pas que Python interprete \t comme une tabulation par exemple
chemin = "C:\\Formation_Udemy\\Python_A_a_Z"
# la foicntion r (= raw string) force python a bien prendre en compte \ et ne pas interpreter \t par exemple
chemin = r"C:\Formation_Udemy\Python_A_a_Z"
# ou alors on met le slash normal et python sait que c'est un chemin windows
chemin = "/workspaces/Gargouillis"

chemin = "/workspaces/Gargouillis/fichier.txt"
print(chemin)
# la méthode with ... est pratique car elle comprend, quand on quitte le with, la fermeture du fichier = f.close()
with open(chemin, "r") as f:
    contenu = f.read()
    contenu2 = repr(contenu)
    contenu3 = contenu.splitlines()
    print(contenu)
    print(contenu2)
    print(contenu3)

# écrire dans un fichier
with open(chemin, "a") as f:
    for i in range(3):
        ajout = "\ntest"
        f.write(ajout)

with open(chemin, "r") as f2:
    contenu4 = f2.read()
    print(contenu4)

# f.close est inutile quand on utilise with open...
#f.close()