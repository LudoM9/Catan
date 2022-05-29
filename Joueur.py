"""
Module contenant les informations relatives aux joueurs.
"""

import pygame
import random as rd
import numpy as np
import Plateau

class Joueur():
    """
    Classe décrivant un joueur : son nom, son numéro, ses cartes, ses infrastructures et ses points de victoire.

    Attributs
    ---------
    nom : string
        nom ou pseudo que choisit le joueur
    numero : int
        numéro du joueur
    ressource : darray
        ressources que possède le joueur
    carteDev : list(Plateau.CartesDeveloppement)
        cartes développement que possède le joueur
    pointsVictoire : int
        points de victoire que posséde le joueur
    colonies : list
        colonies que possède le joueur
    villes : list
        villes que possède le joueur
    routes : list
        routes que possède le joueur
    ports : list
        ports que possède le joueur
    valeurEchange : ndarray
        taux des échanges de ressources avec la banque variant selon le nombre et type de ports possédés par le joueur
    plusGrandeRoute : bool
        vrai si le joueur possède la plus grande suite d'au moins 5 routes
    plusGrandeArmee : bool
    vrai si le joueur possède la plus grande armée d'au moins 3 chevaliers
    """

    def __init__(self, nom, num, plateau):
        """
        Paramètres
        ----------
        nom : string
            Nom ou pseudo que choisit le joueur
        num : int
            Numéro du joueur
        plateau : Plateau
            Plateau dans le quel évolue le joueur
        """

        self.nom = nom
        self.numero = num
        self.ressource = np.array([0,0,0,0,0])
        self.carteDev = []
        self.pointsVictoire = 0
        self.colonies = []
        self.villes = []
        self.routes = []
        self.ports = []
        self.valeurEchange = np.array([4,4,4,4,4])
        self.nbChevalier = 0
        self.nbRoutes = 0
        self.plusGrandeRoute = False
        self.plusGrandeArmee = False

    def calculValeurEchange(self):
        """
        Calcule les taux d'échanges d'un joueur avec la banque selon les ports qu'il possède.

        Paramètres
        ----------
        aucun
        """

        for port in self.ports:
            for i in range(len(self.valeurEchange)):
                if port[i]<self.valeurEchange[i]:
                    self.valeurEchange[i] = port[i]

    def ressourceSuffisante(self, valeur):
        """
        Vérifie qu'un joueur possède suffisamment de ressources pour effectuer un achat ou une construction.

        Paramètres
        ----------
        valeur : ndarray
            Coût de l'achat ou de la construction

        Renvoie
        -------
        ressourceSuffisante : bool
            True si la condition le joueur possède suffisamment de ressources, False sinon
        """

        ressourceSuffisante = False
        if np.all(self.ressource - valeur >= 0):
            ressourceSuffisante = True
        return ressourceSuffisante

    def colonieExiste(self, coords):
        """
        Vérifie que le joueur possède une colonie au sommet testé.

        Paramètres
        ----------
        coords : ndarray
            Coordonnées du sommet  à tester

        Renvoie
        -------
        True si le joueur possède une colonie au sommet testé
        False sinon
        """

        for colonie in self.colonies:
            if coords == colonie.coords:
                return True
        return False

    def getColonie(self, coords):
        """
        Trouve la colonie d'un joueur à un sommet donné s'il en possède une.

        Paramètres
        ----------
        coords : ndarray
            Coordonnées du sommet à tester

        Renvoie
        -------
        colonie : Colonie
            Colonie du joueur présente au sommet testé s'il en possède une
        """

        if self.colonieExiste(coords):
            for colonie in self.colonies:
                if coords == colonie.coords:
                    return colonie

    def calculPV(self):
        """
        Compte le nombre de points de victoire que possède un joueur.

        Paramètres
        ----------
        aucun

        Renvoie
        -------
        n : int
            Nombre de points de victoire du joueur
        """

        n = 0
        for carte in self.carteDev:
            if carte.type == "PV":
                n+=1
        for colonie in self.colonies:
            n+=1
        for ville in self.villes:
            n+=2
        if self.plusGrandeArmee:
            n+=2
        if self.plusGrandeRoute:
            n+=2
        return n
    
    def removeRoutes(self):
        c = 0
        for i, carte in enumerate(self.carteDev):
            if carte.type == "Routes":
                c = i
        del self.carteDev[c]
    
    def removeChevalier(self):
        c = 0
        for i, carte in enumerate(self.carteDev):
            if carte.type == "Chevalier":
                c = i
        self.nbChevalier += 1
        del self.carteDev[c]

    def removeInvention(self):
        c = 0
        for i, carte in enumerate(self.carteDev):
            if carte.type == "Invention":
                c = i
        del self.carteDev[c]
    
    def removeMonopole(self):
        c = 0
        for i, carte in enumerate(self.carteDev):
            if carte.type == "Monopole":
                c = i
        del self.carteDev[c]

    def victoire(self):
        """
        Vérifie si un joueur possède assez de points de victoire pour gagner la partie.

        Paramètres
        ----------
        aucun

        Renvoie
        -------
        True si le joueur gagne la partie
        False sinon
        """

        if self.calculPV()>=10:
            return True
            print(self.nom)
        else:
            return False
            print("A pas gagné")
