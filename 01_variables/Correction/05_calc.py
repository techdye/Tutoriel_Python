# CORRECTION DE L'EXERCICE 5

# Demande à l'utilisateur de rentrer les valeurs
# des nombres, pour à la fin les additionner et
# l'afficher avec cette syntaxe : "Le résultat est 40."

a = 0
b = 0

# ____Première méthode____

a = int(input("Premier nombre : "))
b = int(input("Second nombre : "))

result = a + b

print(f"Le résultat est {result}.")

# ____Seconde méthode_____

a = int(input("Premier nombre : "))
b = int(input("Second nombre : "))

print(f"Le résultat est {a + b}.")
