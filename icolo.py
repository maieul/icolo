# -*- coding: utf-8 -*-
equipe = {
'sexe' 			: 1, # un pour garçon, 2 pour fille
'garcons' 		: 5,
'filles'	 	: 5,
'canadiens' 	: 2,
'suisses'		: 2,
'belges'		: 1,
'francais'		: 3,
'stagiaires'	: 3,
'aquatiques'	: 2,
'nationalite_directeur' : 0,
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
	points = points + 5 * equipe['francais']
	affiche_points(4,points)
	
	#5 : Si votre équipe comporte des personnes de chaque nationalité, votre nombre de points est doublé -> appliquer à la finally
	
	#6 : Si votre équipe comporte au moins un stagiaire vous marquez un bonus de 10 points
	if equipe['stagiaires']>=1:
		points = points + 10
	affiche_points(6,points)	
	#7 : Si vous possédez autant de filles que de garçons dans votre équipe, vous perdez 5 points
	if equipe['filles'] == equipe['garcons']:
		points = points - 5
	affiche_points(7,points)
	
	#8 : Si un de vos animateurs est spécialisé dans une discipline aquatique, vous marquez 10 points
	
	if equipe['aquatiques'] >= 1:
		points = points + 10
	affiche_points(8,points)
	
	#9 : Si aucun animateur n'est de la même nationalité que le directeur, vous perdez 10 points
	if equipe['nationalite_directeur']	< 1 :
		points = points - 10
	affiche_points(9,points)
	
	
def affiche_points(etape,points):
	print ("regle "+str(etape)+" : "+str(points)+" points")
calcul_point(equipe)