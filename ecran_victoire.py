import pygame, os
from pygame.locals import *
import constantes as cst
import fonctions as fct

pygame.font.init()
Broadwfont = pygame.font.Font(os.path.join('fonts', 'BROADW.TTF'), 30)
basefont = pygame.font.Font(None, 100)

ACCUEIL_BACKGROUND = pygame.image.load(os.path.join('images', 'accueil_background_4.png'))
MENU = pygame.image.load(os.path.join('images', 'Menu.png'))

def main(vainqueur, numero):

    run = True

    while run:
        pygame.time.Clock().tick(30)

        fct.drawImage((cst.w//2, cst.h//2), ACCUEIL_BACKGROUND.convert_alpha())

        if numero == 0:
            color = cst.couleurj1
        elif numero == 1:
            color = cst.couleurj2
        elif numero == 2:
            color = cst.couleurj3
        elif numero == 3:
            color = cst.couleurj4
        
        victoireTextSurface = basefont.render("Victoire de " + vainqueur, False, color)
        fct.drawImage((cst.w//2, cst.h//2), victoireTextSurface, 0.5)

        fct.drawImage((cst.w//2, 3*cst.h/4), MENU, 0.2)
        RECT_MENU = fct.rectDrawImage((cst.w//2, 3*cst.h/4), MENU, 0.2)

        for event in pygame.event.get():
            fct.shouldQuit(event)
            fct.shouldResize(event, ACCUEIL_BACKGROUND)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if RECT_MENU.collidepoint(event.pos):
                    run = False

        pygame.display.update()
