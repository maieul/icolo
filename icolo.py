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
	#etape 1 : Chaque personne canadienne a une valeur de base de 4 points
	points = points + 4 * equipe['canadiens']
	
	affiche_points(1,points)
	
def affiche_points(etape,points):
	print ("etape "+str(etape)+" : "+str(points)+" points")
calcul_point(equipe)