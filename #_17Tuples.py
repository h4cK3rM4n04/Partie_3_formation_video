#coding:utf-8
"""
Les tuples sont non modifiable!
même s'il n'y a qu'une seule valeur dans le tuple, il faut mettre une virgule(,) else : Python va le considérer étant comme un simple entier de type integer
Création d'un tuple:	tupl = () tuple vide
						tupl = (45,) avec une seule valeur
						tupl = 45, idem qu'au dessus
						tupl = (12, 23, "bonjour Je suis un élément du tuple!")

"""
liste = [10, 56, 12, 31, 10, 12, 65, 78, 61, 97, 59, 87]
for x, y in enumerate(liste):
	print(x, y)

entier_1 = (45)
print(type(entier_1))

tuple_1 = (45,)
print(type(tuple_1))

tuple_2 = (10, 56, 12, 31, 10, 12, 65, 78, 61, 97, 59, 87)
print(tuple_2[1])

def get_player_position():
	posX = 12,
	posY = 10,
	return posX, posY

#Principal program
cordX = 0
cordY = 0
print(f"Les coordonnés du joueur sont: {cordX} et {cordY}")
cordX, cordY = (get_player_position())
print(f"Les coordonnés du joueur sont maintenant de: {cordX} et {cordY}; (Type tuple)")