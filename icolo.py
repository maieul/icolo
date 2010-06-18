# -*- coding: utf-8 -*-
equipe = {
'sexe' 			: 1, # un pour garçon, 2 pour fille
'garcons' 		: 2,
'filles'	 	: 3,
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
	
	#19 : Si vous êtes une fille et que vous possèdez plus de garçons que de fille dans votre équipe, vous marquez 5 points supplémentaires
	if equipe['sexe'] == 2 and equipe['garcons']>equipe['filles'] :
		points =  points = points + 5
	affiche_points(19,points)
	
	#20 : Si vous êtes un garçon et que vous possèdez plus de filles que de garçons dans votre équipe, vous marquez 5 points supplémentaires
	if equipe['sexe'] == 1 and equipe['garcons']<equipe['filles'] :
		points =  points = points + 5
	affiche_points(20,points)
	
	#5 : Si votre équipe comporte des personnes de chaque nationalité, votre nombre de points est doublé
	if equipe['suisses'] >= 1 and equipe['francais'] >= 1 and equipe['belges'] >= 1 and equipe['canadiens'] >= 1:
		points = points * 2
	
	affiche_points(5,points)
	
	return points

def verifier_equipe(equipe):
	if (equipe['garcons'] + equipe['filles']) == (equipe['suisses'] + equipe['francais'] + equipe['belges'] + equipe['canadiens']):
		print ("Il y a erreur dans votre équipe : si on additionne les animateurs et les animatrices, le total est différent de la somme des animateurs de Nchaque nationalités")
		return True
	else : 
		return False
def affiche_points(etape,points):
	print ("regle "+str(etape)+" : "+str(points)+" points")

def poser_question(question,erreur=False):
	try:
		if erreur==False:
			solution = input(question + " ? : ")
		else :
			solution = input(question + " ? => Cela doit être un ENTIER  : ")
		int(solution)
		return int(solution)
	except:
	 	return poser_question(question,True)
def demander_sexe():
	sexe = input("Votre sexe ? Mettez 1 pour un garcon, 2 pour une fille : ")
	if sexe != 1 and sexe !=2:
		sexe = demander_sexe()
	return sexe
	
def creer_equipe():
	
	equipe = {}
	try :
		equipe['nom'] = input("Votre nom ? (entourer le de guillemet) : ")
	except: 
		return creer_equipe()
	
	
	
	equipe['sexe'] = demander_sexe()
	print ("Attention : si un personnage est un double, ne le comptez qu'une fois (règles n° 17) \n Listing des personnages")
	erreur_nombre = False
	while erreur_nombre == False:
		equipe['canadiens'] = poser_question('Nombre de Canadiens')
		equipe['suisses'] = poser_question('Nombre de Suisses')
		equipe['belges'] = poser_question('Nombre de Belges')
		equipe['francais'] = poser_question('Nombre de Français')
		equipe['filles'] = poser_question('Nombre de filles')
		equipe['garcons'] = poser_question('Nombre de garcons')
		erreur_nombre = verifier_equipe(equipe)
		
	
	
	equipe['aquatiques'] = poser_question('Nombre d\'animateurs aquatiques')
	equipe['stagiaires'] = poser_question('Nombre de stagiaires')
	equipe['triplet'] = poser_question('Nombre de triplets')
	equipe['nationalite_directeur'] = poser_question('Nombre d\'anim de la nationalitè du directeur')
	
	return equipe


print (creer_equipe())