#!/usr/bin/python3

import random
import os
import doctest

NAVIRES = {'Porte-avion':5,'Croiseur':4,'Contre-torpilleur':3,'Sous-marin':3,'Torpilleur':2}

LIGNES = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

LETTRES = ['A','B','C','D','E','F','G','H','I','J']

SENS = ['H','V']

IA_PORTE_AVION = []
IA_TIR_PORTE_AVION = []
IA_CROISEUR = []
IA_TIR_CROISEUR = []
IA_CONTRE_TORPILLEUR = []
IA_TIR_CONTRE_TORPILLEUR = []
IA_SOUS_MARIN = []
IA_TIR_SOUS_MARIN = []
IA_TORPILLEUR = []
IA_TIR_TORPILLEUR = []

UTILI_PORTE_AVION = []
UTILI_TIR_PORTE_AVION = []
UTILI_CROISEUR = []
UTILI_TIR_CROISEUR = []
UTILI_CONTRE_TORPILLEUR = []
UTILI_TIR_CONTRE_TORPILLEUR = []
UTILI_SOUS_MARIN = []
UTILI_TIR_SOUS_MARIN = []
UTILI_TORPILLEUR = []
UTILI_TIR_TORPILLEUR = []

def initialiser_grille(symbole)->list:
	grille=[]
	for i in range(10):
		grille.append([])
		for j in range(10):
			grille[i].append(symbole)
	return grille


def bateau_possible(i:int, j:int, longueur:int, sens:int, grille:list)->int:
	if sens == 1:
		if j<=(10-longueur) and j+(longueur-1)<10:
			j1 = j
			cpt = 0
			possible = 1
			while cpt !=longueur and possible ==1:
				possible = 0
				if grille[i][j1] == 0:
					possible = 1
					j1+=1
					cpt+=1
			return possible
		else:
			return 0

	else:
		if i<=(10-longueur) and i+(longueur-1)<10:
			i1 = i
			cpt = 0
			possible = 1
			while cpt !=longueur and possible ==1:
				possible = 0
				if grille[i1][j] == 0:
					possible = 1
					i1+=1
					cpt+=1
			return possible
		else:
			return 0


def ajoute_coord(x:int, y:int, bateau:str, joueur:str):
	if joueur=='ia':
		if bateau =="Porte-avion":
			IA_PORTE_AVION.append((x,y))
		elif bateau == "Croiseur":
			IA_CROISEUR.append((x,y))
		elif bateau == "Contre-torpilleur":
			IA_CONTRE_TORPILLEUR.append((x,y))
		elif bateau == "Sous-marin":
			IA_SOUS_MARIN.append((x,y))
		elif bateau == "Torpilleur":
			IA_TORPILLEUR.append((x,y))

	elif joueur=='utilisateur':
		if bateau =="Porte-avion":
			UTILI_PORTE_AVION.append((x,y))
		elif bateau == "Croiseur":
			UTILI_CROISEUR.append((x,y))
		elif bateau == "Contre-torpilleur":
			UTILI_CONTRE_TORPILLEUR.append((x,y))
		elif bateau == "Sous-marin":
			UTILI_SOUS_MARIN.append((x,y))
		elif bateau == "Torpilleur":
			UTILI_TORPILLEUR.append((x,y))


def placer_bateaux(i:int, j:int, bateau:str, sens:int, grille:list, joueur:str)->list:
	longueur=NAVIRES[bateau]
	if sens == 1:
		if j<=(10-longueur) and j+(longueur-1)<10:
			i1 = i-1
			for cpt in range(3):
				j1 = j-1
				for cpt1 in range(longueur+2):
					if i1<10 and i1>=0 and j1<10 and j1>=0:
						grille[i1][j1]=2
					j1+=1
				i1+=1
			j1=j
			for cpt in range(longueur):
				grille[i][j1]=1
				ajoute_coord(i, j1, bateau, joueur)
				j1+=1
			return grille

	else:
		if i<=(10-longueur) and i+(longueur-1)<10:
			j1 = j-1
			for cpt in range(3):
				i1 = i-1
				for cpt1 in range(longueur+2):
					if i1<10 and i1>=0 and j1<10 and j1>=0:
						grille[i1][j1]=2
					i1+=1
				j1+=1
			i1=i
			for cpt in range(longueur):
				grille[i1][j]=1
				ajoute_coord(i1, j, bateau, joueur)
				i1+=1
			return grille
		

def placer_bateaux_aleatoirement(grille:list)->list:
	for bateau in NAVIRES:
		longueur = NAVIRES[bateau]
		ok = 0
		while ok != 1:
			positionx = random.randint(0,9)
			positiony = random.randint(0,9)
			direction = random.randint(1,2)
			ok = bateau_possible(positionx, positiony, longueur, direction, grille)
		placer_bateaux(positionx, positiony, bateau, direction, grille, "ia")
	return grille


def placer_bateau_utilisateur(bateaux:list)->list:
	for bateau in NAVIRES :
		longueur=NAVIRES[bateau]
		print("\nVous allez placer le bateau :", bateau)
		print("Sa longueur est de", longueur, "cases.\n")
		afficher_grille_bateau(bateaux)
		ok = 0
		while ok != 1:
			pos_depart_x=str(input("\nEntrer ici la lettre souhaitée :"))
			pos_depart_x=pos_depart_x.upper()
			while pos_depart_x not in LETTRES:
				print("⚠️ Erreur de lettre, resaisie ta lettre ! ⚠️ ")
				pos_depart_x=str(input("Entrer ici la lettre souhaitée :"))
				pos_depart_x=pos_depart_x.upper()
			pos_depart_x=int(LIGNES[pos_depart_x])

			cond=0
			while cond!=1:	
				pos_depart_y = input("Entrer ici la colonne souhaitée :")
				while not pos_depart_y.isdigit():
					print("⚠️ Erreur de colonne, ressaisie ta colonne ! ⚠️ ")
					pos_depart_y = input("Entrer ici la colonne souhaitée :")
				pos_depart_y=int(pos_depart_y)
				if pos_depart_y in range(1,11):
					pos_depart_y=pos_depart_y-1
					cond=1
				else:
					print("⚠️ Erreur de colonne, ressaisie ta colonne ! ⚠️ ")

			sens=str(input("Entrer ici le sens souhaité (Horizontal ou Vertical) [H/V] :"))
			sens=sens.upper()
			while sens not in SENS:
				print("⚠️ Erreur de sens, resaisie te sens ! ⚠️ ")
				sens=str(input("Entrer ici le sens souhaité (Horizontal ou Vertical) [H/V] :"))
				sens=sens.upper()
			if sens=='H':
				sens=1
			elif sens=="V":
				sens=2

			ok = bateau_possible(pos_depart_x, pos_depart_y, longueur, sens, bateaux)
			if ok==0:
				print("Erreur dans le placement, recommence ton placement !")
		placer_bateaux(pos_depart_x, pos_depart_y, bateau, sens, bateaux, 'utilisateur')
	return bateaux


def tir_valide(tirs:list, ligne:int, colonne:int)->bool:
	if (0<=ligne<=9) and (0<=colonne<=9) and (tirs[ligne][colonne]==-1):
		return True
	else:
		return False


def prochain_coup(tirs:list, joueur:str)->tuple:
	if joueur=='utilisateur':
		print("Saisissez la position du prochain tir :")
		ligne=str(input("Lettre : "))
		ligne=ligne.upper() #Répare l'erreur si l'utilisateur rentre un a au lieu de A
		while ligne not in LETTRES:
			print("⚠️ Erreur de lettre, resaisie ta lettre ! ⚠️ ")
			ligne=str(input("Lettre : "))
			ligne=ligne.upper()
		ligne=int(LIGNES[ligne])

		cond=0
		while cond!=1:	
			colonne = input("Colonne :")
			while not colonne.isdigit():
				print("⚠️ Erreur de colonne, ressaisie ta colonne ! ⚠️ ")
				colonne=input("Colonne :")
			colonne=int(colonne)
			if colonne in range(1,11):
				colonne=colonne-1 #car colonne 5 en vrai = colonne 4 en python
				cond=1
			else:
				print("⚠️ Erreur de colonne, ressaisie ta colonne ! ⚠️ ")

	elif joueur=='ia':
		ligne=random.randint(0,9)
		colonne=random.randint(0,9)

	if tir_valide(tirs, ligne, colonne):
		return (ligne, colonne)
	else:
		if joueur=='utilisateur':
			print("⚠️ Erreur tir, déjà fait ou incorrect, recommence le tir ! ⚠️ ")
		return prochain_coup(tirs, joueur)


def resultat_tir(bateaux:list, ligne:int, colonne:int, joueur:str)->int:
	if joueur=='utilisateur':
		PORTE_AVION = IA_PORTE_AVION
		TIR_PORTE_AVION = IA_TIR_PORTE_AVION
		CROISEUR = IA_CROISEUR
		TIR_CROISEUR = IA_TIR_CROISEUR
		CONTRE_TORPILLEUR = IA_CONTRE_TORPILLEUR
		TIR_CONTRE_TORPILLEUR = IA_TIR_CONTRE_TORPILLEUR
		SOUS_MARIN = IA_SOUS_MARIN
		TIR_SOUS_MARIN = IA_TIR_SOUS_MARIN
		TORPILLEUR = IA_TORPILLEUR
		TIR_TORPILLEUR = IA_TIR_TORPILLEUR
	
	elif joueur=='ia':
		PORTE_AVION = UTILI_PORTE_AVION
		TIR_PORTE_AVION = UTILI_TIR_PORTE_AVION
		CROISEUR = UTILI_CROISEUR
		TIR_CROISEUR = UTILI_TIR_CROISEUR
		CONTRE_TORPILLEUR = UTILI_CONTRE_TORPILLEUR
		TIR_CONTRE_TORPILLEUR = UTILI_TIR_CONTRE_TORPILLEUR
		SOUS_MARIN = UTILI_SOUS_MARIN
		TIR_SOUS_MARIN = UTILI_TIR_SOUS_MARIN
		TORPILLEUR = UTILI_TORPILLEUR
		TIR_TORPILLEUR = UTILI_TIR_TORPILLEUR

	if (bateaux[ligne][colonne]==0) or (bateaux[ligne][colonne]==2):
		return 0
	if bateaux[ligne][colonne]==1:
		if ((ligne, colonne) in PORTE_AVION):
			PORTE_AVION.remove((ligne, colonne))
			TIR_PORTE_AVION.append((ligne, colonne))
			if len(PORTE_AVION)!=0:
				return 1
			elif len(PORTE_AVION)==0:
				return 2

		elif ((ligne, colonne) in CROISEUR):
			CROISEUR.remove((ligne, colonne))
			TIR_CROISEUR.append((ligne, colonne))
			if len(CROISEUR)!=0:
				return 1
			elif len(CROISEUR)==0:
				return 2

		elif ((ligne, colonne) in CONTRE_TORPILLEUR):
			CONTRE_TORPILLEUR.remove((ligne, colonne))
			TIR_CONTRE_TORPILLEUR.append((ligne, colonne))
			if len(CONTRE_TORPILLEUR)!=0:
				return 1
			elif len(CONTRE_TORPILLEUR)==0:
				return 2

		elif ((ligne, colonne) in SOUS_MARIN):
			SOUS_MARIN.remove((ligne, colonne))
			TIR_SOUS_MARIN.append((ligne, colonne))
			if len(SOUS_MARIN)!=0:
				return 1
			elif len(SOUS_MARIN)==0:
				return 2

		elif ((ligne, colonne) in TORPILLEUR):
			TORPILLEUR.remove((ligne, colonne))
			TIR_TORPILLEUR.append((ligne, colonne))
			if len(TORPILLEUR)!=0:
				return 1
			elif len(TORPILLEUR)==0:
				return 2


def tirer(bateaux:list, tirs:list, ligne:int, colonne:int, joueur:str)->int:
	if joueur=='utilisateur':
		PORTE_AVION = IA_PORTE_AVION
		TIR_PORTE_AVION = IA_TIR_PORTE_AVION
		CROISEUR = IA_CROISEUR
		TIR_CROISEUR = IA_TIR_CROISEUR
		CONTRE_TORPILLEUR = IA_CONTRE_TORPILLEUR
		TIR_CONTRE_TORPILLEUR = IA_TIR_CONTRE_TORPILLEUR
		SOUS_MARIN = IA_SOUS_MARIN
		TIR_SOUS_MARIN = IA_TIR_SOUS_MARIN
		TORPILLEUR = IA_TORPILLEUR
		TIR_TORPILLEUR = IA_TIR_TORPILLEUR
		resultat_tir_eau = "Dans l'eau 💦!\n"
		resultat_tir_touche = "Touché 🔥!\n"
		resultat_tir_coule = "Coulé 💥!\n"

	elif joueur=='ia':
		PORTE_AVION = UTILI_PORTE_AVION
		TIR_PORTE_AVION = UTILI_TIR_PORTE_AVION
		CROISEUR = UTILI_CROISEUR
		TIR_CROISEUR = UTILI_TIR_CROISEUR
		CONTRE_TORPILLEUR = UTILI_CONTRE_TORPILLEUR
		TIR_CONTRE_TORPILLEUR = UTILI_TIR_CONTRE_TORPILLEUR
		SOUS_MARIN = UTILI_SOUS_MARIN
		TIR_SOUS_MARIN = UTILI_TIR_SOUS_MARIN
		TORPILLEUR = UTILI_TORPILLEUR
		TIR_TORPILLEUR = UTILI_TIR_TORPILLEUR
		resultat_tir_eau = "L'ordinateur à fait : Dans l'eau 💦!\n"
		resultat_tir_touche = "L'ordinateur à fait : Touché 🔥!\n"
		resultat_tir_coule = "L'ordinateur à fait : Coulé 💥!\n"

	res=resultat_tir(bateaux, ligne, colonne, joueur)
	if res==0:
		print(resultat_tir_eau)
		tirs[ligne][colonne]=0
		return 0

	elif res==1:
		print(resultat_tir_touche)
		tirs[ligne][colonne]=1
		return 1

	elif res==2:
		print(resultat_tir_coule)
		if ((ligne, colonne)) in TIR_PORTE_AVION:
			for elt in TIR_PORTE_AVION:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in TIR_CROISEUR:
			for elt in TIR_CROISEUR:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in TIR_CONTRE_TORPILLEUR:
			for elt in TIR_CONTRE_TORPILLEUR:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in TIR_SOUS_MARIN:
			for elt in TIR_SOUS_MARIN:
				tirs[elt[0]][elt[1]]=2
			return 2

		elif ((ligne, colonne)) in TIR_TORPILLEUR:
			for elt in TIR_TORPILLEUR:
				tirs[elt[0]][elt[1]]=2
			return 2


def partie_finie(tirs:list)->bool:
	compteur=0
	for ligne in tirs:
		for valeur in ligne:
			if valeur==2:
				compteur +=1
	total=0
	for valeur in NAVIRES.values():
		total += valeur
	if compteur==total:
		return True
	else:
		return False


def afficher_grille(tirs:list):
	numcolonne=1
	print("   ", end="")
	while numcolonne<=10:
		print(numcolonne, end="  ")
		numcolonne+=1
	print()
	lettre=0
	while lettre<=9:
		for ligne in tirs:
			print(LETTRES[lettre], end=" ")
			for element in ligne:
				if element==-1:
					print("🟦", end=" ")
				elif element==0:
					print("💦", end=" ")
				elif element==1:
					print("🔥", end=" ")
				elif element==2:
					print("💥", end=" ")
			print()
			lettre+=1


def afficher_grille_bateau(bateaux:list):
	numcolonne=1
	print("   ", end="")
	while numcolonne<=10:
		print(numcolonne, end="  ")
		numcolonne+=1
	print()
	lettre=0
	while lettre<=9:
		for ligne in bateaux:
			print(LETTRES[lettre], end=" ")
			for element in ligne:
				if element==0:
					print("🟦", end=" ")
				elif element==2:
					print("🔵", end=" ")
				elif element==1:
					print("⚓️", end=" ")
				elif element=='tirmanqué':
					print("💦", end=" ")
				elif element=='tirtouché':
					print("🔥", end=" ")
			print()
			lettre+=1
			
def intro():
	"""
	Fonction qui affiche l'introduction du jeu.
	"""
	print("#######################################################################")
	print("##############Bataille navalle Spécialitée NSI 1ère JASA ##############")
	print("#######################################################################\n")
	print("\nVous jouez contre l'ordinateur : il a placé ses bateaux aléatoirement.")
	print("La flotte est composée de :")
	print(" - 1 Porte-avion (5 cases)\n - 1 Croiseur (4 cases)\n - 1 Contre-torpilleur (3 cases)\n - 1 Sous-marin (3 cases)\n - 1 Torpilleur (2 cases)\n")
	print("Règles :")
	print(" - Les bateaux peuvent être disposés horizontalement ou verticalement,\n   mais jamais en diagonale.")
	print(" - Deux bateaux ne peuvent pas non plus se chevaucher, ni être collés \n   l'un à l'autre : au moins une case doit les séparer.")
	print("\nPrêt ? C'est parti, bonne chance ! \n")

def gagne():
	"""
	Fonction qui affiche le message si l'utilisateur à gagné.
	"""
	print("\n#######################################################################")
	print("###################### Bravo, vous avez gagné !🎉 #####################")
	print("#######################################################################\n")


def jouer():
	os.system("clear")
	bateaux=initialiser_grille(0)
	bateaux=placer_bateaux_aleatoirement(bateaux)

	tirs=initialiser_grille(-1)

	joueur='utilisateur'

	intro()

	while not partie_finie(tirs):
		afficher_grille(tirs)
		res=prochain_coup(tirs, joueur)
		tirer(bateaux, tirs, res[0], res[1], joueur)
	
	gagne()
	afficher_grille(tirs)
	
def ami():
	os.system("clear")
	print("Ce mode de jeu n'est pas encore disponible😪")
	bateaux=initialiser_grille(0)
	bateaux=placer_bateaux_aleatoirement(bateaux)
	
	tirs=initialiser_grille(-1)
	
	joueur='utilisateur'
	
	intro()
	
	while not partie_finie(tirs):
		afficher_grille(tirs)
		res=prochain_coup(tirs, joueur)
		tirer(bateaux, tirs, res[0], res[1], joueur)
		
	gagne()
	afficher_grille(tirs)


def jouer_ia():
	os.system("clear")
	bateaux_utilisateur=initialiser_grille(0)
	tirs_utilisateur=initialiser_grille(-1)

	bateaux_ia=initialiser_grille(0)
	bateaux_ia=placer_bateaux_aleatoirement(bateaux_ia)
	tirs_ia=initialiser_grille(-1)

	intro()

	print("Pour placer tes bateaux, saisie la case de départ,\nensuite son sens, il se placera automatiquement :\n - Vers la droite à partir de la case de départ si tu choisis horizontalement\n - Vers le bas à partir de la case de départ si tu choisis verticalement.\n")
	input("Appuie sur <Entrée ⏎>pour commencer à placer tes bateaux...")
	os.system("clear")

	placer_bateau_utilisateur(bateaux_utilisateur)
	print()

	copie_bateaux_utilisateur=list(bateaux_utilisateur)

	input("Ta grille est prête, appuie sur <Entrée> pour commencer à jouer...")
	while not partie_finie(tirs_utilisateur) and not partie_finie(tirs_ia):
		os.system('clear')
		print("Ton placement (⚓️) et les tirs de l'ordinateur :\n - (💦) pour un tir manqué\n - (🔥) pour un bon tir\n - (💥) pour un bateau coulé\n")
		afficher_grille_bateau(copie_bateaux_utilisateur)
		print("\nTa grille de tirs :\n")
		afficher_grille(tirs_utilisateur)
		print("\nA toi de jouer !\n")

		res=prochain_coup(tirs_utilisateur, 'utilisateur')
		tirer(bateaux_ia, tirs_utilisateur, res[0], res[1], 'utilisateur')

		res_ordi=prochain_coup(tirs_ia, 'ia')
		print("L'ordinateur à tiré en", LETTRES[res_ordi[0]], res_ordi[1]+1)
		res=tirer(bateaux_utilisateur, tirs_ia, res_ordi[0], res_ordi[1], 'ia')
		if res==0:
			copie_bateaux_utilisateur[res_ordi[0]][res_ordi[1]]='tirmanqué'
		else:
			copie_bateaux_utilisateur[res_ordi[0]][res_ordi[1]]='tirtouché'

		if partie_finie(tirs_utilisateur):
			gagne()
		elif partie_finie(tirs_ia):
			print("\n#######################################################################")
			print("################### L'ordinateur à gagné, dommage ... #################")
			print("#######################################################################\n")
		else:
			input("Appuie sur <Entrée> pour continuer...")

def menu():
	os.system("clear")
	print("#######################################################################")
	print("############## Bataille navalle Spécialitée NSI1ère JASA ##############")
	print("#######################################################################\n")

	print("Choisis ton mode de jeu : 🎮")
	print(" 1 - Jouer seul : l'ordinateur a placé ses bateaux, et tu dois les trouver seul.")
	print(" 2 - Jouer contre l'ordinateur : Tu places tes bateaux, l'ordinateur aussi, et vous jouez à tour de rôle.")
	print(" 3 - Jouer contre un ami : Vous placez chacun vos bateaux puis vous jouez.\n")

	cond=0
	while cond!=1:	
		mode_jeu = input("Ton mode de jeu est [1/2/3] : ")
		while not mode_jeu.isdigit():
			print("⚠️ Erreur de saisie, recommence ! ⚠️ ")
			mode_jeu=input("Ton mode de jeu est [1/2/3] : ")
		mode_jeu=int(mode_jeu)
		if mode_jeu in range(1,4):
			cond=1
		else:
			print("⚠️ Erreur de saisie, recommence ! ⚠️ ")

	if mode_jeu==1:
		jouer()
	elif mode_jeu==2:
		jouer_ia()
	elif mode_jeu==3:
		ami()

doctest.testmod()

menu()
