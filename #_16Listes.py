#coding:utf-8
"""
Chacun des éléments d'une liste à des indices!
liste[:X] affiche les X premier éléments de la liste!
liste[X:] affiche les X derniers éléments!
liste[-X] affiche le Xème élément de la liste en partant de la fin!!!
liste[A:B] affiche de l'élément d'indice A à l'indice B (avec B exclus)

"""

#Création d'une liste

inventaire = ["arc", "fleche", "épée", "pistolet", "galil", "laser", "m14", "katana"]
print(inventaire[-7:-3])

print("index de fleche: {}".format(inventaire.index("fleche")))
#la méthode sort permet de lister les éléments de la liste en ordre!
#Soit en ordre croissant soit par ordre alphabétique!
inventaire.sort()
print(inventaire)
del inventaire[0]
print(inventaire)

for x, y in enumerate(inventaire):
	print(f"index: {x},\tvaleur: {y}")

inventaire[:] = [] #vidage d'une liste!
print(inventaire)