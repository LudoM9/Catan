"""
Module contenant l'affichage de l'écran d'accueil du jeu ainsi que de l'écran de choix du nombre de joueurs et des noms de joueurs.
"""

import pygame, os
from pygame.locals import *
import constantes as cst
import fonctions as fct

pygame.font.init()
Broadwfont = pygame.font.Font(os.path.join('fonts', 'BROADW.TTF'), 30)
basefont = pygame.font.Font(None, 18)
textsurface = Broadwfont.render("© MUSTIERE-LAURENT", False, pygame.Color('white'))

RECT_START = pygame.Rect(0, 0, 0, 0)
RECT_3 = pygame.Rect(0, 0, 0, 0)
RECT_4 = pygame.Rect(0, 0, 0, 0)
RECT_RETOUR = pygame.Rect(0, 0, 0, 0)
RECT_J1 = pygame.Rect(0, 0, 0, 0)
RECT_J2 = pygame.Rect(0, 0, 0, 0)
RECT_J3 = pygame.Rect(0, 0, 0, 0)
RECT_J4 = pygame.Rect(0, 0, 0, 0)
RECT_DEMARRER = pygame.Rect(0, 0, 0, 0)
RECT_ALEATOIRE = pygame.Rect(0, 0, 0, 0)

ACCUEIL_BACKGROUND = pygame.image.load(os.path.join('images', 'accueil_background_4.png'))
START = pygame.image.load(os.path.join('images', 'Start Image.png'))
NB_JOUEUR = pygame.image.load(os.path.join('images', 'Nombre de joueurs.png'))
IMAGE_3 = pygame.image.load(os.path.join('images', 'Image 3.png'))
IMAGE_4 = pygame.image.load(os.path.join('images', 'Image 4.png'))
RETOUR = pygame.image.load(os.path.join('images', 'Retour.png'))
JOUEUR1 = pygame.image.load(os.path.join('images', 'Joueur 1.png'))
JOUEUR2 = pygame.image.load(os.path.join('images', 'Joueur 2.png'))
JOUEUR3 = pygame.image.load(os.path.join('images', 'Joueur 3.png'))
JOUEUR4 = pygame.image.load(os.path.join('images', 'Joueur 4.png'))
DEMARRER = pygame.image.load(os.path.join('images', 'Demarrer.png'))
PLATEAU_ALEATOIRE = pygame.image.load(os.path.join('images', 'Plateau aleatoire.png'))
CASE_OFF_ALEATOIRE = pygame.image.load(os.path.join('images', 'Case vide.png'))
CASE_ON_ALEATOIRE = pygame.image.load(os.path.join('images', 'Case cochée.png'))


def main():
    global RECT_START, RECT_RETOUR, RECT_3, RECT_4, RECT_J1, RECT_J2, RECT_J3, RECT_J4, RECT_DEMARRER, RECT_ALEATOIRE

    run = True
    start = True
    nbjoueur = False
    choixNoms = False
    plateau_aleatoire = False
    activetextJ1 = False
    activetextJ2 = False
    activetextJ3 = False
    activetextJ4 = False
    n = 0
    textJ1 = ''
    textJ2 = ''
    textJ3 = ''
    textJ4 = ''

    while run:
        pygame.time.Clock().tick(30)

        fct.drawImage((cst.w//2, cst.h//2), ACCUEIL_BACKGROUND.convert_alpha())
        fct.drawImage((cst.w//2, 0.95*cst.h), textsurface, 0.2)

        for event in pygame.event.get():
            fct.shouldQuit(event)
            fct.shouldResize(event, ACCUEIL_BACKGROUND)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if RECT_START.collidepoint(event.pos):
                    start = False
                    nbjoueur = True
                elif RECT_3.collidepoint(event.pos):
                    nbjoueur = False
                    choixNoms = True
                    n = 3
                elif RECT_4.collidepoint(event.pos):
                    nbjoueur = False
                    choixNoms = True
                    n = 4
                elif RECT_ALEATOIRE.collidepoint(event.pos):
                    plateau_aleatoire = not(plateau_aleatoire)
                elif RECT_J1.collidepoint(event.pos):
                    activetextJ1 = True
                    activetextJ2 = False
                    activetextJ3 = False
                    activetextJ4 = False
                elif RECT_J2.collidepoint(event.pos):
                    activetextJ2 = True
                    activetextJ1 = False
                    activetextJ3 = False
                    activetextJ4 = False
                elif RECT_J3.collidepoint(event.pos):
                    activetextJ3 = True
                    activetextJ1 = False
                    activetextJ2 = False
                    activetextJ4 = False
                elif RECT_J4.collidepoint(event.pos):
                    activetextJ4 = True
                    activetextJ1 = False
                    activetextJ2 = False
                    activetextJ3 = False
                elif RECT_DEMARRER.collidepoint(event.pos):
                    run = False  
                elif RECT_RETOUR.collidepoint(event.pos):
                    if nbjoueur:
                        start = True
                        nbjoueur = False
                    elif choixNoms:
                        nbjoueur = True
                        choixNoms = False
                        activetextJ1 = False
                        activetextJ2 = False
                        activetextJ3 = False
                        activetextJ4 = False
                        n = 0
                        textJ1 = ''
                        textJ2 = ''
                        textJ3 = ''
                        textJ4 = ''
            elif event.type == pygame.KEYDOWN:
                if activetextJ1:
                    if event.key == pygame.K_BACKSPACE:
                        textJ1 = textJ1[:-1]
                    else:
                        textJ1 += event.unicode
                elif activetextJ2:
                    if event.key == pygame.K_BACKSPACE:
                        textJ2 = textJ2[:-1]
                    else:
                        textJ2 += event.unicode
                elif activetextJ3:
                    if event.key == pygame.K_BACKSPACE:
                        textJ3 = textJ3[:-1]
                    else:
                        textJ3 += event.unicode
                elif activetextJ4:
                    if event.key == pygame.K_BACKSPACE:
                        textJ4 = textJ4[:-1]
                    else:
                        textJ4 += event.unicode

        if start:
            resetRect()
            fct.drawImageBotRight((cst.w-20, cst.h//2), START, 0.05)
            RECT_START = fct.rectDrawImageBotRight((cst.w-20, cst.h//2), START, 0.05)
        if nbjoueur:
            resetRect()
            fct.drawImageTopLeft((20, cst.h//4), NB_JOUEUR, 0.05)
            fct.drawImage((cst.w//4, cst.h//2), IMAGE_3, 0.10)
            fct.drawImage((3*cst.w//4, cst.h//2), IMAGE_4, 0.10)
            fct.drawImageTopLeft((20, cst.h//8), RETOUR, 0.03)
            fct.drawImage((2*cst.w//3, 3*cst.h//4), PLATEAU_ALEATOIRE, 0.20)
            if plateau_aleatoire:
                fct.drawImage((cst.w//3, 3*cst.h//4), CASE_ON_ALEATOIRE, 0.10)
                RECT_ALEATOIRE = fct.rectDrawImage((cst.w//3, 3*cst.h//4), CASE_ON_ALEATOIRE, 0.10)
            else:
                fct.drawImage((cst.w//3, 3*cst.h//4), CASE_OFF_ALEATOIRE, 0.10)
                RECT_ALEATOIRE = fct.rectDrawImage((cst.w//3, 3*cst.h//4), CASE_OFF_ALEATOIRE, 0.10)
            RECT_3 = fct.rectDrawImage((cst.w//4, cst.h//2), IMAGE_3, 0.10)
            RECT_4 = fct.rectDrawImage((3*cst.w//4, cst.h//2), IMAGE_4, 0.10)
            RECT_RETOUR = fct.rectDrawImageTopLeft((20, cst.h//8), RETOUR, 0.03)
        if choixNoms:
            resetRect()

            fct.drawImageTopLeft((20, cst.h//8), RETOUR, 0.03)
            RECT_RETOUR = fct.rectDrawImageTopLeft((20, cst.h//8), RETOUR, 0.03)

            fct.drawImage((cst.w//4, cst.h//(n+1)), JOUEUR1, 0.15)
            fct.drawImage((cst.w//4, 2*cst.h//(n+1)), JOUEUR2, 0.15)
            fct.drawImage((cst.w//4, 3*cst.h//(n+1)), JOUEUR3, 0.15)
            rectJ1 = fct.rectDrawImage((cst.w//4, cst.h//(n+1)), JOUEUR1, 0.15)
            rectJ2 = fct.rectDrawImage((cst.w//4, 2*cst.h//(n+1)), JOUEUR2, 0.15)
            rectJ3 = fct.rectDrawImage((cst.w//4, 3*cst.h//(n+1)), JOUEUR3, 0.15)

            RECT_J1 = pygame.Rect(rectJ1.x + rectJ1.width + 30, rectJ1.y, 100, rectJ1.height)
            RECT_J2 = pygame.Rect(rectJ2.x + rectJ2.width + 30, rectJ2.y, 100, rectJ2.height)
            RECT_J3 = pygame.Rect(rectJ3.x + rectJ3.width + 30, rectJ3.y, 100, rectJ3.height)

            text_surface_J1 = basefont.render(textJ1, True, (255, 255, 255))
            text_surface_J2 = basefont.render(textJ2, True, (255, 255, 255))
            text_surface_J3 = basefont.render(textJ3, True, (255, 255, 255))

            RECT_J1.width = max(100, text_surface_J1.get_width() + 10)
            RECT_J2.width = max(100, text_surface_J2.get_width() + 10)
            RECT_J3.width = max(100, text_surface_J3.get_width() + 10)

            pygame.draw.rect(cst.fenetre, cst.couleurj1, RECT_J1, 2)
            pygame.draw.rect(cst.fenetre, cst.couleurj2, RECT_J2, 2)
            pygame.draw.rect(cst.fenetre, cst.couleurj3, RECT_J3, 2)

            cst.fenetre.blit(text_surface_J1, (RECT_J1.x + 5, RECT_J1.y + 5))
            cst.fenetre.blit(text_surface_J2, (RECT_J2.x + 5, RECT_J2.y + 5))
            cst.fenetre.blit(text_surface_J3, (RECT_J3.x + 5, RECT_J3.y + 5))

            if n == 4:
                fct.drawImage((cst.w//4, 4*cst.h//(n+1)), JOUEUR4, 0.15)
                rectJ4 = fct.rectDrawImage((cst.w//4, 4*cst.h//(n+1)), JOUEUR4, 0.15)
                RECT_J4 = pygame.Rect(rectJ4.x + rectJ4.width + 30, rectJ4.y, 100, rectJ4.height)
                text_surface_J4 = basefont.render(textJ4, True, (255, 255, 255))
                RECT_J4.width = max(100, text_surface_J4.get_width() + 10)
                pygame.draw.rect(cst.fenetre, cst.couleurj4, RECT_J4, 2)
                cst.fenetre.blit(text_surface_J4, (RECT_J4.x + 5, RECT_J4.y + 5))

            if len(textJ1)>0 and len(textJ2)>0 and len(textJ3)>0:
                if textJ1 != textJ2 and textJ1 != textJ3 and textJ2 != textJ3:
                    if n == 4:
                        if len(textJ4)>0:
                            if textJ1 != textJ4 and textJ2 != textJ4 and textJ3 != textJ4:
                                fct.drawImage((cst.w//2, 7*cst.h//8), DEMARRER, 0.15)
                                RECT_DEMARRER = fct.rectDrawImage((cst.w//2, 7*cst.h//8), DEMARRER, 0.15)
                    else:
                        fct.drawImage((cst.w//2, 7*cst.h//8), DEMARRER, 0.15)
                        RECT_DEMARRER = fct.rectDrawImage((cst.w//2, 7*cst.h//8), DEMARRER, 0.15)

        pygame.display.update()

    return plateau_aleatoire, [textJ1, textJ2, textJ3, textJ4]


def resetRect():
    """
    Réinitialise les rectangles utilisés dans l'affichage
    """
    global RECT_START, RECT_RETOUR, RECT_3, RECT_4, RECT_J1, RECT_J2, RECT_J3, RECT_J4, RECT_DEMARRER, RECT_ALEATOIRE

    RECT_START = pygame.Rect(0, 0, 0, 0)
    RECT_3 = pygame.Rect(0, 0, 0, 0)
    RECT_4 = pygame.Rect(0, 0, 0, 0)
    RECT_RETOUR = pygame.Rect(0, 0, 0, 0)
    RECT_J1 = pygame.Rect(0, 0, 0, 0)
    RECT_J2 = pygame.Rect(0, 0, 0, 0)
    RECT_J3 = pygame.Rect(0, 0, 0, 0)
    RECT_J4 = pygame.Rect(0, 0, 0, 0)
    RECT_DEMARRER = pygame.Rect(0, 0, 0, 0)
    RECT_ALEATOIRE = pygame.Rect(0, 0, 0, 0)