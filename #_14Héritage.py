#coding:utf-8

"""méthode isinstance permet de verifier si le premier argument est dans la classe passé dans le deuxième paramètre !!!"""

#Class Mère
class Vehicle:

	"""docstring for Vehicle"""

	def __init__(self, name, max_fuel):

		self.name = name
		self.max_fuel = max_fuel

	def move_vehicle(self):
		return "The vehicle is moving!"

#Class Fille
class Voiture(Vehicle):

	"""docstring for Voiture"""

	def __init__(self, name, max_fuel, energy,):
		Vehicle.__init__(self, name, max_fuel)
		self.energy = energy

	def _vehicle_number(self):
		return self.energy + self.max_fuel
	x = property(_vehicle_number)

#Class Fille
class Avion(Vehicle):

	"""docstring for Avion"""
	number = 0

	def __init__(self, name, max_fuel, nbr_merchandise):
		Vehicle.__init__(self, name, max_fuel)
		self.nbr_merchandise = nbr_merchandise
		Avion.number += 1

if __name__ == "__main__":

	v1 = Vehicle("F_22 Raptor", 2400)
	v2 = Vehicle("Toyota Supra", 90)
	print(v2.move_vehicle(), v1.max_fuel)

	Voiture_1 = Voiture("309", 100, 1000)
	print(Voiture_1.x)

	Avion_1 = Avion("Marlo", 2000, 150)
	Avion_2 = Avion("Merlin", 2000, 150)
	Avion_3 = Avion("Max", 2000, 150)
	print(Avion.number)

	if isinstance(v1, Vehicle):
		print(True)
	else:
		print(False)