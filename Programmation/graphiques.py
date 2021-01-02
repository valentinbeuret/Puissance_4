from graphics import *
from variables import *

def dessiner_grille(couleur,f):

    # boucle sur le nombre de colonnes
    for i in range(0,NOMBRE_COLONNES):
        # boucle sur le nombre de cases
        for j in range(0,NOMBRE_CASES):
            dessiner_case(f,i,j)


def dessiner_case(f,i,j):
    p1=(0+DIMENSION_CASE*i,0+DIMENSION_CASE*j)
    p2=(DIMENSION_CASE*(i+1),DIMENSION_CASE*(j+1))
    draw_fill_rectangle(p1,p2,bleu,f)
    centre=(int(p2[0]-DIMENSION_CASE/2),int(p2[1]-DIMENSION_CASE/2))
    draw_fill_circle(centre,RAYON,blanc,f)

def dessiner_pion(colonne,case,couleur,f):
    abs_centre = int(DIMENSION_CASE/2 + (colonne - 1)*DIMENSION_CASE)
    ord_centre = int(DIMENSION_CASE/2 + (NOMBRE_CASES - case - 1)*DIMENSION_CASE)
    centre = (abs_centre,ord_centre)
    # console
    print(f"le centre du pion est {centre}")
    draw_fill_circle(centre,RAYON,couleur,f)



