import pygame
import Plateau
import Joueur

class Catan():
    def __init__(self, joueurs, rdPlateau = False):
        self.plateau = Plateau(rdPlateau)
        self.joueurs = [Joueur("Robert", 1), Joueur("Michel", 2), Joueur("Patrick", 3)]
    
    def startGame(self):
        for joueur in joueurs:
            joueur.constructionGratuite(Colonie)
