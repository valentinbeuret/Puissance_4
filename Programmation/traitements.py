# Créé par Eleve, le 29/12/2020 en Python 3.7
from constantes import *
from graphiques import *

def selectionner_colonne(x,tableau):
    # déterminer la colonne
    indice_colonne = x // DIMENSION_CASE + 1
    # rend la liste du tableau correspondant à la colonne
    colonne = tableau[indice_colonne-1]
    # console
    print(f"la colonne {indice_colonne} contient {colonne}")
    # déterminer la prochaine case encore disponible
    if 0 in colonne:
        prochaine_case = colonne.index(0)
    else:
        prochaine_case = -1
    # console
    print(f"la prochaine case disponoible est {prochaine_case}")
    #retourne colonne et prochaine_case
    return indice_colonne,prochaine_case

def afficher_pion(colonne,case,joueur,couleur,tableau,fenetre):
    # si la case est disponible alors afficher un pion
    if case >= 0:
        # afficher un pion
        dessiner_pion(colonne,case,couleur,fenetre)
        # afficher dans le tableau qu'il y a deja un pion dans une case
        tableau[colonne-1][case] = joueur

def alterner_joueur(joueur,couleur):
    #
    if joueur == 1:
        joueur = 2
        couleur = rouge
    else:
        joueur = 1
        couleur = jaune

    return joueur, couleur

def verifier_gagnant(tableau,joueur):
    sequence = [joueur,joueur,joueur,joueur]
    #vertical
    # boucle sur le nombre de colonnes
    for i in range(0,NOMBRE_COLONNES):
        colonne = tableau[i]
        for j in range(0,3):
            if colonne[j:j+4] == sequence:
                #console
                print("partie gagnée")
                return True

    #horizontal
    for i in range(0,NOMBRE_CASES):
        ligne = []
        for j in range(0,4):
            ligne.append(tableau[j][i])
        if ligne == sequence:
            #console
            print("partie gagnée")
            return True

    #diagonale
    for diagonale in DIAGONALES:
        diag = []
        for i,j in diagonale:
            diag.append(tableau[i][j])
        #console
        print(f"la diagonale est {diag}")

        nombre_comparaisons = len(diagonale) - 3

        for k in range(0,nombre_comparaisons):
            #console
            print(f"comparaison de {diag[k:4+k]} et {sequence}")
            if diag[k:4+k] == sequence:
                #console
                print("partie gagnée")
                return True

    return False

def vérifier_nul(tableau,gagnant,fenetre):
    for colonne in tableau:
        if 0 in colonne:
            return False

    ecrire_partie_nulle(fenetre)
    attendre(1000)
    return True

def vérifier_partie(nul,gagnant,fenetre):
    if gagnant == True:
        ecrire_partie_terminee(fenetre)
        attendre(1000)
        return True

    if nul == True:
        ecrire_partie_nulle(fenetre)
        attendre(1000)
        return True

    return False





