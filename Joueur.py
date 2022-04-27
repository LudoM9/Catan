import pygame
import numpy as np
import random as rd

class Joueur():
    def __init__(self, nom, numéro):
        self.nom = ""
        self.numero = 0
        self.ressource = np.array([0,0,0,0,0])
        self.carteDev = []
        self.pointsVictoire = 0
        self.colonies = []
        self.villes = []
        self.routes = []
        self.ports = []
        self.valeurEchange = np.array([4,4,4,4,4])
        self.plusGrandeRoute = False
        self.plusGrandeArmee = False

    def calculValeurEchange(self):
        for port in self.ports:
            for i in range(len(self.valeurEchange)):
                if port[i]<self.valeurEchange[i]:
                    self.valeurEchange[i] = port[i]

    def ressourceSuffisante(self, valeur):
        ressourceSuffisante = False
        if np.all(self.ressource - valeur >= 0):
            ressourceSuffisante = True
        return ressourceSuffisante

    def colonieExiste(self, coords):
        for colonie in self.colonies:
            if coords == colonie.coords:
                return True
        return False

    def getColonie(self, coords):
        if self.colonieExiste(coords):
            for colonie in self.colonies:
                if coords == colonie.coords:
                    return colonie

    def nombreChevalier(self):
        n = 0
        for carte in self.carteDev:
            if type == DevChevalier:
                n += 1
        return n

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

    