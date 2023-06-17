

# Les variables nous permettent de garder des valeurs pour les réutiliser plus tard.
# Il y a trois principaux types de variables.

text = "Hello World!"  # str

number = 100  # int

booleanTrue = True  # bool (Vrai)
booleanFalse = False  # bool (Faux)

# Le type est défini dynamiquement.

dynamic = 10

# En faisant print avec type, on peut récupérer le type d'un variable.

print(type(text))  # <class 'str'>
print(type(number))  # <class 'int'>
print(type(booleanTrue))  # <class 'bool'>


# On peut redéfinir une variable avec un autre type. 

variable = "Hello World!"
print(type(variable))  # <class 'str'>
variable = 100
print(type(variable))  # <class 'int'>


# Pour faire des opérations, on redéfini la variable.

number = 10
number = number + 10
print(number)  # 20

# La variable n'est pas réassignée

number = 10
number + 10
print(number)  # 10

# Plus simple en mettant le signe et un égale

number = 10
number += 10
print(number)  # 20


# Par contre, le langage est très typé, impossible de les additionner entre-eux.

try:
    
    print("Tu as " + 30 + " amis.")
    
except:
    
    print("Tu as 0 ami.")
    

# Pour additionner plusieurs types entre eux, il faut convertir avant.
# On utilise des fonctions qui utilisent le nom de leur type.

number = "32"
number = int(number)

calcul = number * 5


# Ça marche aussi avec les chaînes de caractères

print("Tu as " + str(30) + " amis")


# Par contre, il y a une meilleure manière de concaténer du texte.
# C'est en utilisant le f au début.
# Ça convertit ce qu'on lui donne automatiquement. 

account = 123
delete = 23

print(f"Vous avez {account} euros, mais après vous aurez {account - delete} euros.")


# Pour récuppérer une valeur renseignée par l'utilisateur, on utilise la fonction input.

money = int(input("Argent : "))
