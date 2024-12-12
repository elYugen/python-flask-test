# entier et décimaux
chiffre1 = 5 
chiffre2 = 14.12

# chaine de cara
texte = "merde"

# booleen
jeVaisBien = False

# connaitre le type d'une variable (int, boolean, string)
print(type(chiffre1))

calcul = chiffre1 + chiffre2
print(calcul)

prenom = "jean"
nomDeFamille = "pierre"
nomComplet = "Mon nom est " + prenom + " " + nomDeFamille
print(nomComplet)

# condition
if jeVaisBien == False:
    print("Je vais mal")
else: 
    print("ça va pour le moment")

# boucle for
for i in range(10):
    print(i)


def coucou(name):
    return f"salut, {name}"

message = coucou("Bob")
print(message)

gens = {"nom": "Jacque", "age": 20}
print(gens)
