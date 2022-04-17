import pygame, sys, os
from pygame.locals import *
import constantes as cst

ACCUEIL_BACKGROUND = pygame.image.load(os.path.join('images', 'accueil_background_4.png'))

def shouldQuit(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

def shouldResize(event, image=ACCUEIL_BACKGROUND):
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
    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w), int(image_size[1] * percentage * cst.w / image_size[0])))
    rect = image.get_rect(center = center_coord)
    cst.fenetre.blit(image, rect)

def rectDrawImage(center_coord, image, percentage = 1):
    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w), int(image_size[1] * percentage * cst.w / image_size[0])))
    return image.get_rect(center = center_coord)

def drawImageBotRight(bot_right_coord, image, percentage = 1):
    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    rect = image.get_rect(bottomright = bot_right_coord)
    cst.fenetre.blit(image, rect)

def drawImageTopLeft(top_left_coord, image, percentage = 1):
    image_size = image.get_size()
    image = pygame.transform.scale(image, (int(percentage * cst.w * image_size[0] / image_size[1]), int(percentage * cst.w)))
    rect = image.get_rect(topleft = top_left_coord)
    cst.fenetre.blit(image, rect)