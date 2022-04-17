import os, pygame

# Fenêtre
w = 640
h = 480
fenetre = pygame.Surface((0, 0))

# Titre de la fenêtre
TITLE = "Catan"

################ Images

# Icône
ICONE = pygame.image.load(os.path.join('images', 'catan.png'))
