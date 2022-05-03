import pygame, os
from pygame.locals import *
import constantes as cst
import fonctions as fct
import numpy as np

pygame.font.init()
Broadwfont = pygame.font.Font(os.path.join('fonts', 'BROADW.TTF'), 30)
basefont = pygame.font.Font(None, 18)

NEXTTURN = pygame.image.load(os.path.join('images', 'NextTurn.png'))

RECT_MAIN = pygame.Rect(0, 0, 0, 0)
RECT_CONSTRUIRE = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGER = pygame.Rect(0, 0, 0, 0)
RECT_NEXTTURN = pygame.Rect(0, 0, 0, 0)

def main(catan):
    global RECT_MAIN, RECT_CONSTRUIRE, RECT_ECHANGER, RECT_NEXTTURN

    run=True

    color = pygame.Color('white')

    joueurActuel = catan.joueurActuel
    if joueurActuel.numero == 0:
        color = (255, 0, 0)
    elif joueurActuel.numero == 1:
        color = (0, 0, 255)
    elif joueurActuel.numero == 2:
        color = (0, 255, 0)
    elif joueurActuel.numero == 3:
        color = (138,43,226)
    playerTextsurface = basefont.render(joueurActuel.nom, False, color)

    l = np.round(cst.h / 3)
    c = np.round(l * 3 ** (1 * 3))
    positions = [(3*c,l),(5*c,l),(7*c,l),
                 (2*c,np.round(5*l/2)),(4*c,np.round(5*l/2)),(6*c,np.round(5*l/2)),(8*c,np.round(5*l/2)),
                 (c,4*l),(3*c,4*l),(5*c,4*l),(7*c,4*l),(9*c,4*l),
                 (2*c,np.round(11*l/2)),(4*c,np.round(11*l/2)),(6*c,np.round(11*l/2)),(8*c,np.round(11*l/2)),
                 (3*c,7*l),(5*c,7*l),(7*c,7*l)]
    hexagons=['bois','mouton','mouton','ble','minerai','ble','bois','bois','argile','desert','minerai','ble','ble','minerai','bois','plaine','argile','mouton','argile']
    numbers=[6,3,8,2,4,5,10,5,9,0,6,9,10,11,3,12,8,4,11]


    while run:
        pygame.time.Clock().tick(30)
        
        joueurActuel = catan.joueurActuel
        if joueurActuel.numero == 0:
            color = (255, 0, 0)
        elif joueurActuel.numero == 1:
            color = (0, 0, 255)
        elif joueurActuel.numero == 2:
            color = (0, 255, 0)
        elif joueurActuel.numero == 3:
            color = (138,43,226)
        playerTextsurface = basefont.render(joueurActuel.nom, False, color)

        cst.fenetre.fill((0,191,255))

        fct.drawImageTopLeft((0,0), playerTextsurface, 0.05)
        fct.drawImageTopLeft((cst.w/2, 0), NEXTTURN, 0.2)
        RECT_NEXTTURN = fct.rectDrawImageTopLeft((cst.w/2, 0), NEXTTURN, 0.2)

        for i in range(19):
            fct.drawHexagon(hexagons[i],positions[i])

        for event in pygame.event.get():
            fct.shouldQuit(event)
            fct.shouldResize(event)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if RECT_NEXTTURN.collidepoint(event.pos):
                    catan.tourSuivant()

        pygame.display.update()

def resetRect():
    global RECT_MAIN, RECT_CONSTRUIRE, RECT_ECHANGER, RECT_NEXTTURN

    RECT_MAIN = pygame.Rect(0, 0, 0, 0)
    RECT_CONSTRUIRE = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGER = pygame.Rect(0, 0, 0, 0)
    RECT_NEXTTURN = pygame.Rect(0, 0, 0, 0)