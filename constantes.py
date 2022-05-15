"""
Module contnant des constantes relatives à l'affichage du jeu.
"""

import os, pygame

# Fenêtre
w = 640 #largeur de la fenêtre
h = 480 # hauteur de la fenêtre
fenetre = pygame.Surface((0, 0))

# Titre de la fenêtre
TITLE = "Catan"

################ Images

# Icône
ICONE = pygame.image.load(os.path.join('images', 'catan.png'))
