import pygame
import numpy as np
import random as rd

class Joueur():
    def __init__(self, nom, numéro, plateau):
        self.nom = ""
        self.numero = 0
        self.ressource = np.array([0,0,0,0,0])
        self.carteDev = []
        self.pointsVictoire = 0
        self.colonies = []
        self.villes = []
        self.routes = []
        self.ports = []
        self.plusGrandeRoute = False
        self.plusGrandeArmee = False
        self.__plateau = plateau

    def turn(self):
        #Jouer un tour
        ...
    
    def echangeBanque(self, ):
        ...

    def echangeJoueur(self, joueur):
        ...

    def lancerDés(self):
        return sum(rd.randrange(1,7)+rd.randrange(1,7))

    def construction(self, type):
        ...

    def constructionGratuite(self, element, coords):
        if element == "Colonie":
            ...

    def achatCarteDev(self):
        if len(self.__plateau.pioche.carteDev)>0:
            if np.all(self.ressource-self.__plateau.CarteDeveloppement.coût>=0):
                self.ressource-=self.__plateau.CarteDeveloppement.coût
                self.carteDev.append(self.__plateau.pioche.carteDev.pop())

    def calculPV(self):
        n = 0
        for cartes in self.carteDev:
            if type==DevPV:
                n+=1
        for colonie in self.colonies:
            n+=1
        for ville in self.villes:
            n+=2
        if self.plusGrandeArmee:
            n+=3
        if self.plusGrandeRoute:
            n+=3
        return n

    def victoire(self):
        if self.calculPV()>=10:
            return True
        else:
            return False

    