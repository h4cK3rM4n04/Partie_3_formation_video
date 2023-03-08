#coding:utf-8

"""

Manière de manipuler des attributs dans une classe | Propriété d'encapsulation!!!

"""

class Humain:

	'''Docstring for Humain'''

	nbr_humain = 0
	nbr_nourriture = 3

	def __init__(self, name, older):
		self.name = name
		self._older_ = older
		Humain.nbr_humain += 1
		Humain.nbr_nourriture = Humain.nbr_humain + Humain.nbr_nourriture

	def _getAge(self):
		try:
			return self._older_
		except AttributeError:
			return "L'objet à été détruit par vous même !!!"

	def get_corrompt_nbrHumain(cls, variable):
		Humain._older_ = variable
		return Humain._older_
	x = classmethod(get_corrompt_nbrHumain)

	def reset():
		try:
			del Humain._older_
		except AttributeError:
			print("L'objet âge à été détrut par vous même!!!")
	de = staticmethod(reset)

	def _getAge(self):
		return self._older_
	y = property(_getAge)



#type de valeurs passé en paramètre de property (getter) (setter) (deleter) (helper)

if __name__ == "__main__":

	h1 = Humain("h4cK3rM4n04", 16)
	h2 = Humain(h1.name[::-1], h1._older_ % 2)
	h3 = Humain(h1.name[-1::-1], h1._older_ % 4)
	h4 = Humain(h1.name[-2::-1], h1._older_ % 8)
	print(h1.x(10101111010))#Essayez de muter cette ligne pour voir le résultat!!!
	h1.de()
	#Dans les deux cas ils s'affichent tous car c'est dans le document dans la création de la classe!!!!
	print(h1._getAge()) #Premier cas
	print(h1._older_)	#Deuxième cas
	print(h1.y)
	print(h1._getAge())
	print("Il y aura :	", Humain.nbr_nourriture, "Nourriture!")

	help(Humain)