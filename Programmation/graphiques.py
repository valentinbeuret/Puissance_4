from graphics import *
from constantes import *

#i = colonne
#j = ligne
#f = fenetre

def dessiner_case(f,i,j):

    p1=(0+DIMENSION_CASE*i,0+DIMENSION_CASE*j)
    p2=(DIMENSION_CASE*(i+1),DIMENSION_CASE*(j+1))
    # creation d'un rectangle bleu
    draw_fill_rectangle(p1,p2,bleu,f)
    centre=(int(p2[0]-DIMENSION_CASE/2),int(p2[1]-DIMENSION_CASE/2))
    # creation d'un cercle blanc
    draw_fill_circle(centre,RAYON,blanc,f)

def dessiner_grille(couleur,f):

    # boucle sur le nombre de colonnes
    for i in range(0,NOMBRE_COLONNES):
        # boucle sur le nombre de cases
        for j in range(0,NOMBRE_LIGNES):
            dessiner_case(f,i,j)

def dessiner_pion(colonne,case,couleur,fenetre):

    # en fonctioin de si une case est prise ou non on calcule la cordonne du centre du pion a afficher
    abs_centre = int(DIMENSION_CASE/2 + (colonne - 1)*DIMENSION_CASE)
    ord_centre = int(DIMENSION_CASE/2 + (NOMBRE_LIGNES - case - 1)*DIMENSION_CASE)
    centre = (abs_centre,ord_centre)
    draw_fill_circle(centre,RAYON,couleur,fenetre)

def ecrire_partie_terminee(f):
    ecrire("Partie terminée",DEPART_TEXTE,40,blanc,f)

def ecrire_partie_nulle(f):
    ecrire("Partie nulle",DEPART_TEXTE,40,blanc,f)
