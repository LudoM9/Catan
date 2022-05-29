"""
Module contenant des fonctions relatives à l'affichage du jeu.
"""

import pygame, sys, os
from pygame.locals import *
import constantes as cst
import numpy as np
import ecran_jeu

ACCUEIL_BACKGROUND = pygame.image.load(os.path.join('images', 'accueil_background_4.png'))

def shouldQuit(event):
    """
    Désactive la bibliothèque pygame lorsqu'un événement est terminé.

    Paramètres
    ----------
    event : pygame.Event
        Evénement comparé à l'événement QUIT
    """

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def shouldResize(event, image=ACCUEIL_BACKGROUND):
    """
    Redimensionne la fenêtre.

    Paramètres
    ----------
    event : pygame.Event
        Evénement actuel
    image : pygame.Surface
        Image à transformer
    """

    if event.type == VIDEORESIZE:
        cst.w, cst.h = event.w, event.h
        cst.fenetre.blit(pygame.transform.scale(image, (cst.w, cst.h)), (0, 0))
        pygame.display.flip()
    elif event.type == VIDEOEXPOSE:
        cst.w, cst.h = cst.fenetre.get_size()
        cst.fenetre.fill((0, 0, 0))
        cst.fenetre.blit(pygame.transform.scale(image, (cst.w, cst.h)), (0, 0))
        pygame.display.flip()

def drawImage(center_coord, image, percentage = 1): #Pour positioner une image en donnant les coordonnées de son centre
    """
    Affiche une image positionnée par rapport à son centre

    Paramètres
    ----------
    center_coord : tuple(int)
        Coordonnées du centre de l'image
    image: pygame.Surface
        Image à afficher
    percentage : float
        Ratio de la taille
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w), int(image_size[1] * percentage * cst.w / image_size[0])))
    rect = image.get_rect(center = center_coord)
    cst.fenetre.blit(image, rect)

def rectDrawImage(center_coord, image, percentage = 1):
    """
    Créé un rectangle cliquable associé à une image

    Renvoie
    -------
    Le rectangle associé à l'image et positionné par rapport à son centre
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w), int(image_size[1] * percentage * cst.w / image_size[0])))
    return image.get_rect(center = center_coord)

def drawImageBotRight(bot_right_coord, image, percentage = 1):
    """
    Affiche une image positionnée par rapport à son coin bas droit

    Paramètres
    ----------
    bot_right_coord : tuple(int)
        Coordonnées du coin bas droit de l'image
    image: pygame.Surface
        Image à afficher
    percentage : float
        Ratio de la taille
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    rect = image.get_rect(bottomright = bot_right_coord)
    cst.fenetre.blit(image, rect)

def rectDrawImageBotRight(bot_right_coord, image, percentage = 1):
    """
    Créé un rectangle cliquable associé à une image

    Renvoie
    -------
    Le rectangle associé à l'image et positionné par rapport à son coin bas droit
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    return image.get_rect(bottomright = bot_right_coord)

def drawImageTopLeft(top_left_coord, image, percentage = 1):
    """
    Affiche une image positionnée par rapport à son coin haut gauche

    Paramètres
    ----------
    top_left_coord : tuple(int)
        Coordonnées du coin haut gauche de l'image
    image: pygame.Surface
        Image à afficher
    percentage : float
        Ratio de la taille
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    rect = image.get_rect(topleft = top_left_coord)
    cst.fenetre.blit(image, rect)

def rectDrawImageTopLeft(top_left_coord, image, percentage = 1):
    """
    Créé un rectangle cliquable associé à une image

    Renvoie
    -------
    Le rectangle associé à l'image et positionné par rapport à son coin haut gauche
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    return image.get_rect(topleft = top_left_coord)

def drawImageTopRight(top_right_coord, image, percentage = 1):
    """
    Affiche une image positionnée par rapport à son coin haut droit

    Paramètres
    ----------
    top_right_coord : tuple(int)
        Coordonnées du coin haut droit de l'image
    image: pygame.Surface
        Image à afficher
    percentage : float
        Ratio de la taille
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    rect = image.get_rect(topright = top_right_coord)
    cst.fenetre.blit(image, rect)

def rectDrawImageTopRight(top_right_coord, image, percentage = 1):
    """
    Créé un rectangle cliquable associé à une image

    Renvoie
    -------
    Le rectangle associé à l'image et positionné par rapport à son coin haut droit
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    return image.get_rect(topright = top_right_coord)

def drawImageMidLeft(mid_left_coord, image, percentage = 1):
    """
    Affiche une image positionnée par rapport à son côté gauche

    Paramètres
    ----------
    mid_left_coord : tuple(int)
        Coordonnées du côté gauche de l'image
    image: pygame.Surface
        Image à afficher
    percentage : float
        Ratio de la taille
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    rect = image.get_rect(midleft = mid_left_coord)
    cst.fenetre.blit(image, rect)

def rectDrawImageMidLeft(mid_left_coord, image, percentage = 1):
    """
    Créé un rectangle cliquable associé à une image

    Renvoie
    -------
    Le rectangle associé à l'image et positionné par rapport à son côté gauche
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    return image.get_rect(midleft = mid_left_coord)

def drawImageMidRight(mid_right_coord, image, percentage = 1):
    """
    Affiche une image positionnée par rapport à son côté droit

    Paramètres
    ----------
    mid_right_coord : tuple(int)
        Coordonnées du côté droit de l'image
    image: pygame.Surface
        Image à afficher
    percentage : float
        Ratio de la taille
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    rect = image.get_rect(midright = mid_right_coord)
    cst.fenetre.blit(image, rect)

def rectDrawImageMidRight(mid_right_coord, image, percentage = 1):
    """
    Créé un rectangle cliquable associé à une image

    Renvoie
    -------
    Le rectangle associé à l'image et positionné par rapport à son côté droit
    """

    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    return image.get_rect(midright = mid_right_coord)

def drawHexagon(type, position, number):
    """
    Affiche une tuile composée d'un hexagone de la couleur de la ressource de la tuile et le numéro de la case

    Paramètres
    ----------
    type : string
        Nom du type de ressource produite par la case ou "desert" pour le désert
    position : tuple(int)
        Coordonnées du centre de l'hexagone à dessiner
    number : int
        Nombre à afficher sur la case
    """

    x,y = position[0]+cst.xoff, position[1]+cst.yoff
    l = np.round(cst.h / 12)
    c = np.round(l/2 * 3 ** (1 / 3))
    lint,cint=l*4/5,c*4/5

    couleur=(0,0,0)
    if type=='bois':
        couleur=(51, 133, 93)
    if type == 'mouton':
        couleur = (245, 245, 245)
    if type == 'ble':
        couleur = ((255, 255, 0))
    if type == 'minerai':
        couleur = (169, 169, 169)
    if type == 'argile':
        couleur = (210, 105, 30)
    if type == 'desert':
        couleur = (240, 230, 140)

    pygame.draw.polygon(cst.fenetre, (0,0,0), ((x, y-l),(x+c,y-np.round(l/2)),(x+c,y+np.round(l/2)),(x,y+l),(x-c,y+np.round(l/2)),(x-c,y-np.round(l/2))))
    pygame.draw.polygon(cst.fenetre, couleur, ((x, y-lint),(x+cint,y-np.round(lint/2)),(x+cint,y+np.round(lint/2)),(x,y+lint),(x-cint,y+np.round(lint/2)),(x-cint,y-np.round(lint/2))))

    pygame.font.init()
    basefont = pygame.font.Font(None, 20)
    if type!="desert":

        pygame.draw.circle(cst.fenetre, (0, 0, 0), (int(x), int(y)), 15)
        if number == 6 or number == 8:
            text=basefont.render(str(number), False, (255,0,0))
        else:
            text=basefont.render(str(number), False, pygame.Color('white'))
        cst.fenetre.blit(text,(x-5,y-5))
