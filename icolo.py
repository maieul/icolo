# -*- coding: utf-8 -*-
equipe = {
'sexe' 			: 1, # un pour garçon, 2 pour fille
'garcons' 		: 0,
'filles'	 	: 1,
'canadiens' 	: 6,
'suisses'		: 4,
'belges'		: 2,
'francais'		: 3,
'stagiaires'	: 3,
'aquatiques'	: 2,
'nationalite_directeur' : 0,
'triplet'		: 1,
'max_francais'		: True,	
'max_belges'	: True,
'max_suisses'	: True
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
	
	#10 : Si vous ne possédez pas de garçons dans votre équipe, vous perdez 10 points
	if equipe['garcons'] < 1 :
		points = points - 10
	affiche_points(10,points)
	
	#11 : Si vous ne possédez pas de fille dans votre équipe, vous perdez 10 points
	if equipe['filles'] < 1 :
		points = points - 10
	affiche_points(11,points) 
	
	#12 : Chaque paire de personne canadienne double la valeur d'une personne suisse
	points = points + min(equipe['canadiens'] / 2,equipe['suisses']) * 6
	affiche_points(12,points) 
	
	#13 : Chaque paire de personne belge double la valeur d'une personne française
	points = points + min(equipe['belges'] / 2,equipe['francais']) * 5
	affiche_points(13,points) 
	
	#14 : Celui qui a le plus de français dans son équipe reçoit un bonus de 3 points par français
	if equipe['max_francais'] == True: 
		points = points + 3 * equipe['francais']
	affiche_points(14,points) 
	
	#15 : Celui qui a le plus de belges dans son équipe reçoit un bonus de 3 point par personne féminine de son équipe
	if equipe['max_belges'] == True :
		points = points + 3 * equipe['filles']
	affiche_points(15,points) 
	
	#16 : Celui qui a le plus de suisse dans son équipe à la fin du jeu reçoit un bonus de 3 points par stagiaire de son équipe
	if equipe['max_suisses'] == True:
		points = points + 3 * equipe['stagiaires']
	affiche_points(16,points)
	
	#17 : attention à afficher avant : "Si une personne est en double dans une équipe (exactement la même carte), elle ne compte qu'une fois"
	
	#18 : Si une personne est en triple dans une équipe (exactement la même carte), vous recevez un bonus de 10 points
	points = points + 10 * equipe['triplet']
	affiche_points(18,points)
	
def affiche_points(etape,points):
	print ("regle "+str(etape)+" : "+str(points)+" points")
calcul_point(equipe)