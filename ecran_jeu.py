import pygame, os
from pygame.locals import *
import constantes as cst
import fonctions as fct
import numpy as np

pygame.font.init()
Broadwfont = pygame.font.Font(os.path.join('fonts', 'BROADW.TTF'), 30)
basefont = pygame.font.Font(None, 100)

NEXTTURN = pygame.image.load(os.path.join('images', 'TourSuivant.png'))
CONSTRUCT = pygame.image.load(os.path.join('images', 'Construction.png'))
BRICK = pygame.image.load(os.path.join('images', 'Brick Image.png'))
STONE = pygame.image.load(os.path.join('images', 'Stone Image.png'))
WHEAT = pygame.image.load(os.path.join('images', 'Wheat Image.png'))
WOOD = pygame.image.load(os.path.join('images', 'Wood Image.png'))
WOOL = pygame.image.load(os.path.join('images', 'Wool Image.png'))
PV = pygame.image.load(os.path.join('images', 'PV Image.png'))
BACKGROUNDUI = pygame.image.load(os.path.join('images', 'BackgroundUI.jpg'))

RECT_MAIN = pygame.Rect(0, 0, 0, 0)
RECT_CONSTRUIRE = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGER = pygame.Rect(0, 0, 0, 0)
RECT_NEXTTURN = pygame.Rect(0, 0, 0, 0)
RECT_BRICKIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_STONEIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_WHEATIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_WOODIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_WOOLIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_PVIMAGE = pygame.Rect(0, 0, 0, 0)

def main(catan):
    global RECT_MAIN, RECT_CONSTRUIRE, RECT_ECHANGER, RECT_NEXTTURN, RECT_BRICKIMAGE, RECT_STONEIMAGE, RECT_WHEATIMAGE, RECT_WOODIMAGE, RECT_WOOLIMAGE, RECT_PVIMAGE

    run=True
    xoffset = 5
    yoffset = 5

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
        pygame.draw.rect(cst.fenetre, (211,211,211), Rect(0, 3*cst.h/4, cst.w, cst.h/4))

        fct.drawImageTopLeft((xoffset,0), playerTextsurface, 0.035)
        fct.drawImageTopRight((cst.w, 0), NEXTTURN, 0.05)
        RECT_NEXTTURN = fct.rectDrawImageTopRight((cst.w, 0), NEXTTURN, 0.05)

        fct.drawImageTopLeft((xoffset,3*cst.h/4 + yoffset), BRICK, 0.05)
        fct.drawImageTopLeft((xoffset,3*cst.h/4+(1/3)*cst.h/4 + yoffset), STONE, 0.05)
        fct.drawImageTopLeft((xoffset,3*cst.h/4+(2/3)*cst.h/4 + yoffset), WHEAT, 0.05)
        fct.drawImageTopLeft((80+xoffset,3*cst.h/4 + yoffset), WOOD, 0.05)
        fct.drawImageTopLeft((80+xoffset,3*cst.h/4+(1/3)*cst.h/4 + yoffset), WOOL, 0.05)
        fct.drawImageTopLeft((80+xoffset,3*cst.h/4+(2/3)*cst.h/4 + yoffset), PV, 0.05)
        RECT_BRICKIMAGE = fct.rectDrawImageTopLeft((xoffset,3*cst.h/4 + yoffset), BRICK, 0.05)
        RECT_STONEIMAGE = fct.rectDrawImageTopLeft((xoffset,3*cst.h/4+(1/3)*cst.h/4 + yoffset), STONE, 0.05)
        RECT_WHEATIMAGE = fct.rectDrawImageTopLeft((xoffset,3*cst.h/4+(2/3)*cst.h/4 + yoffset), WHEAT, 0.05)
        RECT_WOODIMAGE = fct.rectDrawImageTopLeft((80+xoffset,3*cst.h/4 + yoffset), WOOD, 0.05)
        RECT_WOOLIMAGE = fct.rectDrawImageTopLeft((80+xoffset,3*cst.h/4+(1/3)*cst.h/4 + yoffset), WOOL, 0.05)
        RECT_PVIMAGE = fct.rectDrawImageTopLeft((80+xoffset,3*cst.h/4+(2/3)*cst.h/4 + yoffset), PV, 0.05)

        brickTextsurface = basefont.render(str(joueurActuel.ressource[1]), False, (0,0,0))
        stoneTextsurface = basefont.render(str(joueurActuel.ressource[4]), False, (0,0,0))
        wheatTextsurface = basefont.render(str(joueurActuel.ressource[3]), False, (0,0,0))
        woodTextsurface = basefont.render(str(joueurActuel.ressource[0]), False, (0,0,0))
        woolTextsurface = basefont.render(str(joueurActuel.ressource[2]), False, (0,0,0))
        pvTextsurface = basefont.render(str(joueurActuel.pointsVictoire), False, (0,0,0))
        fct.drawImageMidLeft(RECT_BRICKIMAGE.midright, brickTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_STONEIMAGE.midright, stoneTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_WHEATIMAGE.midright, wheatTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_WOODIMAGE.midright, woodTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_WOOLIMAGE.midright, woolTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_PVIMAGE.midright, pvTextsurface, 0.035)
        

        for i in range(19):
            fct.drawHexagon(hexagons[i], positions[i],numbers[i])

        for event in pygame.event.get():
            fct.shouldQuit(event)
            fct.shouldResize(event)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if RECT_NEXTTURN.collidepoint(event.pos):
                    catan.tourSuivant()

        pygame.display.update()

def resetRect():
    global RECT_MAIN, RECT_CONSTRUIRE, RECT_ECHANGER, RECT_NEXTTURN, RECT_BRICKIMAGE, RECT_STONEIMAGE, RECT_WHEATIMAGE, RECT_WOODIMAGE, RECT_WOOLIMAGE, RECT_PVIMAGE

    RECT_MAIN = pygame.Rect(0, 0, 0, 0)
    RECT_CONSTRUIRE = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGER = pygame.Rect(0, 0, 0, 0)
    RECT_NEXTTURN = pygame.Rect(0, 0, 0, 0)
    RECT_BRICKIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_STONEIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_WHEATIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_WOODIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_WOOLIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_PVIMAGE = pygame.Rect(0, 0, 0, 0)