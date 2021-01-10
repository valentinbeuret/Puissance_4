# Créé par Eleve, le 28/12/2020 en Python 3.7
import pygame
from graphics import *
from graphiques import *
from traitements import *

# variables
grille = [[0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0], \
    [0,0,0,0,0,0]]

# notation
# colonne 2 = grille[1]
# colonne 2 case 3 = grille[1][2]

# indique quel joueur a quelle valeur
joueur = 1
couleur_pion = jaune

# init
fenetre=init_graphics(DIMENSION_CASE*NOMBRE_COLONNES,DIMENSION_CASE*NOMBRE_LIGNES+DIMENSION_CONSOLE_LARGEUR)
dessiner_grille(bleu,fenetre)

# boucle
partie_terminée = False
#console
print("partie démarrée")
while partie_terminée == False:
    # attendre un événement utilisateur
    evenement = pygame.event.wait()

    if evenement.type == pygame.locals.MOUSEBUTTONUP:
        #console
        print(f"position de la souris {evenement.pos}")

        # séléctionner une colonne
        colonne, prochaine_case = selectionner_colonne(evenement.pos[0], grille)

        # afficher pion
        afficher_pion(colonne, prochaine_case, joueur, couleur_pion, grille ,fenetre)

        # vérifier si jeu gagnant
        gagnant = verifier_gagnant(grille, joueur)

        # vérifier si jeu nul
        partie_nulle = vérifier_nul(grille, gagnant, fenetre)

        # vérifier si la partie est terminée
        partie_terminée = vérifier_partie(partie_nulle, gagnant, fenetre)

        # alterner les joueur
        joueur, couleur_pion = alterner_joueur(joueur, couleur_pion, prochaine_case)

    '''
    if evenement.type == pygame.locals.KEYUP:
        # console
        print(f"type d'événement intercepté {evenement.type}")
        # récupérer la touche utilisée
        pass
    '''

    if evenement.type == pygame.locals.QUIT:
        #console
        print("la fenetre est fermée")
        # fin de partie
        partie_terminée = True

# fin du programme
quit_graphics()



