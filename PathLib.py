from pathlib import Path
"""
# on recupère le répertoire de travail
print(Path.home())
# on récupère le répertoire courant
print(Path.cwd())

p = Path("/users/Documents/fichier.txt")
print(p)
print(p.parent)
print(p.suffix)

t = Path("users")
print(t)

t = t / "Documents" / "fichier.txt"
print(t)

r = Path("users")
print(r.joinpath("Documents", "liste_course.json"))
print(r.joinpath("Documents", "liste_course.json").suffix)   """

s = Path("/workspaces/Gargouillis/LesFichiers.py")

print(s.name)
print(s.parent.parent)
print(s.parent)
print(s.stem)
print(s.suffix)
print(s.suffixes)
print(s.parts)
print(s.exists())
print(s.is_dir())
print(s.is_file())

print(dir(s))
