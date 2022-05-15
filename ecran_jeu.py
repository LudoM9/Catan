import pygame, os
from pygame.locals import *
import constantes as cst
import fonctions as fct
import numpy as np

pygame.font.init()
Broadwfont = pygame.font.Font(os.path.join('fonts', 'BROADW.TTF'), 30)
basefont = pygame.font.Font(None, 18)

RECT_MAIN = pygame.Rect(0, 0, 0, 0)
RECT_CONSTRUIRE = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGER = pygame.Rect(0, 0, 0, 0)

def main():
    global RECT_MAIN, RECT_CONSTRUIRE, RECT_ECHANGER

    run=True
    l = np.round(cst.h / 12)
    c = np.round(l/2 * 3 ** (1 / 3))
    positions = [(3*c,l),(5*c,l),(7*c,l),
                 (2*c,np.round(5*l/2)),(4*c,np.round(5*l/2)),(6*c,np.round(5*l/2)),(8*c,np.round(5*l/2)),
                 (c,4*l),(3*c,4*l),(5*c,4*l),(7*c,4*l),(9*c,4*l),
                 (2*c,np.round(11*l/2)),(4*c,np.round(11*l/2)),(6*c,np.round(11*l/2)),(8*c,np.round(11*l/2)),
                 (3*c,7*l),(5*c,7*l),(7*c,7*l)]
    hexagons=['bois','mouton','mouton','ble','minerai','ble','bois','bois','argile','desert','minerai','ble','ble','minerai','bois','mouton','argile','mouton','argile']
    numbers=[6,3,8,2,4,5,10,5,9,0,6,9,10,11,3,12,8,4,11]


    while run:
        pygame.time.Clock().tick(30)

        cst.fenetre.fill((0,0,255))

        for i in range(19):
            fct.drawHexagon(cst.fenetre, hexagons[i], positions[i],numbers[i])

        for event in pygame.event.get():
            fct.shouldQuit(event)

        pygame.display.update()

def resetRect():
    global RECT_MAIN, RECT_CONSTRUIRE, RECT_ECHANGER

    RECT_MAIN = pygame.Rect(0, 0, 0, 0)
    RECT_CONSTRUIRE = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGER = pygame.Rect(0, 0, 0, 0)