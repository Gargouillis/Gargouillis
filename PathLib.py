from pathlib import Path

print(Path.home())
print(Path.cwd())

p = Path("/users/Documents/fichier.txt")
print(p)
print(p.parent)
print(p.suffix)