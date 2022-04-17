import pygame, os
from pygame.locals import *
import constantes as cst
import fonctions as fct

pygame.font.init()
myfont = pygame.font.SysFont(None, 50)
textsurface = myfont.render("© MUSTIERE-LAURENT", False, pygame.Color('white'))

ACCUEIL_BACKGROUND = pygame.image.load(os.path.join('images', 'accueil_background_4.png'))
START = pygame.image.load(os.path.join('images', 'Start Button', 'Start Button.png'))
STARTPUSHED = pygame.image.load(os.path.join('images', 'Start Button', 'Start Button Pushed.png'))

def main():
    run = True
    fct.drawImage((cst.w//2, cst.h//2), ACCUEIL_BACKGROUND.convert_alpha())
    image_to_display = START

    while run:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            fct.shouldQuit(event)
            fct.shouldResize(event, ACCUEIL_BACKGROUND)
            if event.type == MOUSEBUTTONDOWN:
                image_to_display = STARTPUSHED
            elif event.type == MOUSEBUTTONUP:
                image_to_display = START
                run = False

        fct.drawImage((cst.w//2, cst.h//2), image_to_display.convert_alpha(), 0.5)
        fct.drawImage((cst.w//2, 0.8 * cst.h), textsurface, 0.4)

        pygame.display.flip()