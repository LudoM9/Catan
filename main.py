import pygame
import constantes as cst
import fonctions as fct
import accueil
import Catan
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

    #if ecranAccueil:
    #    plateau_aleatoire, joueurs = accueil.main()
    #    ecranAccueil = False
    plateau_aleatoire = False
    joueurs  = ["Jeep", "Nikos", "Dany"]
    ecranAccueil = False
    catan = Catan.Catan(joueurs, plateau_aleatoire)
    ecranJeu = True
    cst.fenetre.fill(pygame.Color('black'))

    if ecranJeu:
        ...

    pygame.display.flip()