#coding:utf-8
"""
méthode de chaine travaille sur une copie et pas sur la chaine elle même
str.upper(); str.lower(); str.capitalize(); str.title()
str.center(largeur, caractère de remplissage)
str.find()
str.index()
str.strip() enlève tout les espaces
str.replace(nouvelle, occurence)

"""

chaine = "Bonjour je suis h4cK3rM4n04"
chaine = chaine.title()
#Comme remarque cette méthode met tout les lettres après les espaces en majuscules
print(chaine)

chaine = chaine.center(35, "-")
print(chaine)