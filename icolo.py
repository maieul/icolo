# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE - Licence GPL 3.0
# Version 1.0

def trouver_maximum(tableau,nationalite):
	maxi = 0
	for equipe in tableau.keys() :
		maxi = max(tableau[equipe][nationalite],maxi)
	for equipe in tableau.keys() :
		if tableau[equipe][nationalite] == maxi:
			tableau[equipe]['max_'+nationalite] = True
			print "Max de " + nationalite + " : " + equipe
		else :
			 tableau[equipe]['max_'+nationalite] = False
	return tableau

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
	#if equipe['suisses'] >= 1 and equipe['francais'] >= 1 and equipe['belges'] >= 1 and equipe['canadiens'] >= 1:
	#	points = points * 2
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
		points =  points + 5
	affiche_points(19,points)
	
	#20 : Si vous êtes un garçon et que vous possèdez plus de filles que de garçons dans votre équipe, vous marquez 5 points supplémentaires
	print equipe['sexe']
	if equipe['sexe'] == 1 and equipe['garcons']<equipe['filles'] :
		points =  points + 5
	affiche_points(20,points)
	
	#5 : Si votre équipe comporte des personnes de chaque nationalité, votre nombre de points est doublé
	if equipe['suisses'] >= 1 and equipe['francais'] >= 1 and equipe['belges'] >= 1 and equipe['canadiens'] >= 1:
		points = points * 2
	
	affiche_points(5,points)
	
	return points

def verifier_equipe(equipe):
	if (equipe['garcons'] + equipe['filles']) == (equipe['suisses'] + equipe['francais'] + equipe['belges'] + equipe['canadiens']):
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
		equipe['nom'] = unicode(raw_input("Votre nom ? : "),'utf-8')
	except: 
		return creer_equipe()
	
	
	
	equipe['sexe'] = demander_sexe()
	print ("Attention : si un personnage est un double, ne le comptez qu'une fois (règle n° 17) \n Listing des personnages")
	erreur_nombre = False
	total_membre_equipe = 0
	while erreur_nombre == False or total_membre_equipe!=8:
		equipe['canadiens'] = poser_question('Nombre de Canadiens')
		equipe['suisses'] = poser_question('Nombre de Suisses')
		equipe['belges'] = poser_question('Nombre de Belges')
		equipe['francais'] = poser_question('Nombre de Français')
		equipe['filles'] = poser_question('Nombre de filles')
		equipe['garcons'] = poser_question('Nombre de garcons')
		total_membre_equipe = equipe['garcons']+equipe['filles']
		erreur_nombre = verifier_equipe(equipe)
		if erreur_nombre == False :
			print ("Il y a erreur dans votre équipe : si on additionne les animateurs et les animatrices, le total est différent de la somme des animateurs de chaque nationalité")
		if total_membre_equipe!=8:
			print ("Votre équipe n'est pas constituée de 8 membres")
	
	equipe['stagiaires'] = poser_question('Nombre de stagiaires')
	equipe['aquatiques'] = poser_question('Nombre d\'animateurs aquatiques')
	equipe['nationalite_directeur'] = poser_question('Nombre d\'anim de la nationalité du directeur')
	equipe['triplet'] = poser_question('Nombre de triplets')
	print ("Merci, l'équipe « "+equipe['nom'].encode('utf-8')+" » a été créée")
	return equipe
def creer_et_stocker_equipe():
	import os
	import sys
	from pickle import dump, load
	from os import chdir
	chdir (sys.path[0])

	try:
		fichier = open('icolo_stockage.txt',"r")
	except IOError:
		fichier = open('icolo_stockage.txt','a')
	try:
		equipes = load(fichier)
		fichier.close()
	except:
		equipes = {}
	fichier = open('icolo_stockage.txt',"w")
	equipe = creer_equipe()
	equipes[equipe['nom']] = equipe
	dump(equipes,fichier)
	fichier.close()
	
def afficher_equipes():
	import os
	import sys
	from pickle import dump, load
	from os import chdir
	chdir (sys.path[0])

	fichier = open('icolo_stockage.txt',"r")
	try:
		equipes = load(fichier)
		fichier.close()
	except:
		equipes = {}
	nom_equipes = equipes.keys()
	liste = []
	juste_nom 	= input("Afficher juste les noms (1 pour oui)? ")
	print ("Il y a "+str(len(nom_equipes))+" équipes")
	for nom in nom_equipes:
		if juste_nom != 1 :
			afficher_config_equipe(nom,equipes[nom])
		else :
			liste.append(nom)
	if juste_nom == 1 :
		liste.sort()
		for nom in liste:
			print nom
	fichier.close()
	function_de_base()
    
def afficher_config_equipe(nom,equipe):
	print nom + " : "
	print "\t Sexe \t\t\t:\t" + str(equipe['sexe'])
	print "\t Garçons \t\t:\t" + str(equipe['garcons'])
	print "\t Filles \t\t:\t" + str(equipe['filles'])
	print "\t Canadiens \t\t:\t" + str(equipe['canadiens'])
	print "\t Suisses \t\t:\t" + str(equipe['suisses'])
	print "\t Belges \t\t:\t" + str(equipe['belges'])
	print "\t Français \t\t:\t" + str(equipe['francais'])
	print "\t Stagiaires \t\t:\t" + str(equipe['stagiaires'])
	print "\t Aquatiques \t\t:\t" + str(equipe['aquatiques'])
	print "\t Nationalité dirlo \t:\t" + str(equipe['nationalite_directeur'])
	print "\t triplet \t\t:\t" + str(equipe['triplet'])
	
def cmpval(x,y):
    if x[1]>y[1]:
        return 1
    elif x[1]==y[1]:
        return 0
    else:
        return -1

def supprimer_equipe():
	import os
	import sys
	from pickle import dump, load
	from os import chdir
	chdir (sys.path[0])

	fichier = open('icolo_stockage.txt',"r")
	try:
		equipes = load(fichier)
		fichier.close()
	except:
		equipes = {}
	afficher_equipes()
	sup = unicode(input("Equipes à supprimer (\"fin\" pour cesser) "),'utf-8')
	if sup != 'fin':
		try:
			del(equipes[sup])
		except:
			print "L'équipe demandée ( "+sup.encode('utf-8')+" ) n'existe pas"
		fichier = open('icolo_stockage.txt',"w")
		dump(equipes,fichier)
		fichier.close()
		supprimer_equipe()
	function_de_base()
	
def calculer_tout_les_points():
	import os
	import sys
	from pickle import dump, load
	from os import chdir
	chdir (sys.path[0])

	fichier = open('icolo_stockage.txt',"r")
	try:
		equipes = load(fichier)
		fichier.close()
	except:
		equipes = {}
	equipes = trouver_maximum(equipes,'francais')
	equipes = trouver_maximum(equipes,'belges')
	equipes = trouver_maximum(equipes,'suisses')
	points = {}
	for nom in equipes.keys():
		print "* "+ nom + " *" 
		afficher_config_equipe(nom,equipes[nom])
		points[nom] = calcul_point(equipes[nom])
	print "\n\n\n Résultats : "
	points = points.items()
	points.sort(cmpval)
	for nom in points:
		print nom[0] + "\t : \t" + str(nom[1]) 
	function_de_base()
	
def function_de_base():
	try:
		reponse = input("Que voulez vous faire ? : 1 pour créer une nouvelle équipe, 0 pour calculer les points,-1 pour afficher les équipes, -2 pour en supprimer, -3 pour quitter ")
	except:
		function_de_base()

	if reponse == 1:
		creer_et_stocker_equipe()
		function_de_base()
	elif reponse == -1:
		afficher_equipes()
	elif reponse == 0:
		calculer_tout_les_points()
	elif reponse == -2:
		supprimer_equipe()
	elif reponse == -3:
		quit()
		
	

function_de_base()
