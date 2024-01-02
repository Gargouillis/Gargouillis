# ctrl + d permet de changer des meme caractère en meme temps
# 3 facons de mettre un chemin windows
import os

# le double \ permet de ne pas que Python interprete \t comme une tabulation par exemple
chemin = "C:\\Formation_Udemy\\Python_A_a_Z"
# la foicntion r (= raw string) force python a bien prendre en compte \ et ne pas interpreter \t par exemple
chemin = r"C:\Formation_Udemy\Python_A_a_Z"
# ou alors on met le slash normal et python sait que c'est un chemin windows
chemin = "C:/Formation_Udemy/Python_A_a_Z"

chemin = "fichier.txt"
print(chemin)
with open(chemin, "r") as f:
    reader = f.read()
    print(reader)

# f.close()