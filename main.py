"""
Module principal de l'interface homme-machine, qui réalise l'affichage des différentes phases de jeu.
"""

import pygame
import constantes as cst
import fonctions as fct
import accueil
import ecran_jeu
import ecran_victoire
import Catan
import Plateau
from pygame.locals import *

ecranAccueil = True
ecranJeu = False

pygame.init()

# Création de la fenêtre
flags = pygame.RESIZABLE
cst.fenetre = pygame.display.set_mode((cst.w, cst.h), flags)

# Icône
pygame.display.set_icon(cst.ICONE)

# Titre
pygame.display.set_caption(cst.TITLE)

while True:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        fct.shouldQuit(event)
        fct.shouldResize(event)

    if ecranAccueil:
        plateau_aleatoire, joueurs = accueil.main()
        ecranAccueil = False
        catan = Catan.Catan(joueurs, plateau_aleatoire)
        ecranJeu = True

    if ecranJeu:
        vainqueur, numero = ecran_jeu.main(catan)
        ecranJeu = False
        ecranVictoire = True

    if ecranVictoire:
        ecran_victoire.main(vainqueur, numero)
        ecranVictoire = False
        ecranAccueil = True

    pygame.display.flip()