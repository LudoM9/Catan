"""
Module contnant des constantes relatives à l'affichage du jeu.
"""

import os, pygame

# Fenêtre
w = 640 #largeur de la fenêtre
h = 480 # hauteur de la fenêtre
fenetre = pygame.Surface((0, 0))
xoff = 20 #Offset pour le plateau
yoff = 20 #Offset pour le plateau

# Titre de la fenêtre
TITLE = "Catan"

#Couleur des joueurs
couleurj1 = (255, 0, 0)
couleurj2 = (0, 0, 255)
couleurj3 = (0, 255, 0)
couleurj4 = (138,43,226)

################ Images

# Icône
ICONE = pygame.image.load(os.path.join('images', 'catan.png'))
