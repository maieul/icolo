# -*- coding: utf-8 -*-
equipe = {
'sexe' 			: 1, # un pour garçon, 2 pour fille
'garcons' 		: 3,
'filles'	 	: 5,
'canadiens' 	: 2,
'suisses'		: 2,
'belges'		: 1,
'français'		: 3,
'stagiaires'	: 3,
'aquatiques'	: 2,
'nationalite_directeur' : 2,
'triplet'		: 0	
}
#fonction de calcul des points
def calcul_point(equipe) :
	points = 0
	
	#1 Chaque personne canadienne a une valeur de base de 4 points
	points = points + 4 * equipe['canadiens']
	affiche_points(1,points)
	
	#2 : Chaque personne suisse a une valeur de base de 6 points
	points = points + 6 * equipe['suisses']
	affiche_points(2,points)
	
	#3 : Chaque personne belge a la même valeur qu'une personne canadienne plus 1 point (= 5)
	points = points + 5 * equipe['belges']
	affiche_points(3,points)
	
	#4 : Chaque personne française a la même valeur qu'une personne canadienne plus 1 point (=5)
	points = points + 5 * equipe['points']
	affiche_points(4,equipe)
	
	#5 Si votre équipe comporte des personnes de chaque nationalité, votre nombre de points est doublé
	
	
	
	affiche_points(4,points)
	
def affiche_points(etape,points):
	print ("etape "+str(etape)+" : "+str(points)+" points")
calcul_point(equipe)