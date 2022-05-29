"""
Module contenant tous les éléments qui apparaissent dans une partie de jeu.
"""

import pygame
import Plateau
import Joueur
import random as rd
import numpy as np

class Catan():
    """
    Classe représentant une partie de jeu : le lancer dés, le voleur, les échanges, la
    construction, les achats et divers autres calculs nécéssaires au déroulement du jeu.

    Attributs
    ---------
    plateau : Plateau
        plateau sur le quel le jeu évolue
    joueurs : list(Joueur)
        liste des joueurs participant au jeu
    valeurDes : int
        résultat de la somme de deux lancers de dés à six faces réguliers
    numeroJoueurActuel : int
        numéro du joueur actif, attribué automatiquement au remplissage de self.joueurs
    joueurActuel : Joueur
        joueur actif
    numeroJoueurActuelDebut : int
        numéro du joueur actif lors du placement des premières colonies
    """

    def __init__(self, joueurs, rdPlateau = False):
        """
        Paramètres
        ----------
        joueurs : list(string)
            Liste des joueurs
        rdPlateau : bool, optionnel, False par défaut
            Booléen pour savoir si le plateau est aléatoire
        """

        self.plateau = Plateau.Plateau(rdPlateau)
        self.joueurs = []
        self.valeurDes = 0
        for i, joueur in enumerate(joueurs):
            self.joueurs.append(Joueur.Joueur(joueur, i, self.plateau))
        self.numeroJoueurActuel = 0
        self.joueurActuel = self.joueurs[self.numeroJoueurActuel]
        self.numeroJoueurActuelDebut = 0
        

    def lancerDes(self):
        """
        Lance deux dés réguliers à six faces et somme les deux résultats.

        Paramètres
        ----------
        aucun
        """

        s = rd.randrange(1,7)+rd.randrange(1,7)
        self.valeurDes = s

    def ressourceDebut(self):
        """
        Distribue aux joueurs les ressources des tuiles adjacentes à leurs premières colonies en début de partie.

        Paramètres
        ----------
        aucun
        """

        for joueur in self.joueurs:
            for colonie in joueur.colonies:
                for tile_coord in self.plateau.getAdjacentTilesFromVertice(colonie.coords):
                    for tile in self.plateau.tiles:
                        if tile_coord == tile.coords:
                            joueur.ressource += tile.ressource

    def donRessource(self):
        """
        Distribue aux joueurs les ressources des cases définies par le lancer de dés dont les
        joueurs ont une colonie ou ville adjacente et si le voleur n'est pas sur la case.

        Paramètres
        ----------
        aucun
        """
        tiles = []
        for tile in self.plateau.tiles:
            if tile.value == self.valeurDes:
                tiles.append(tile)
        for tile in tiles:
            if tile.coords != self.plateau.voleur.coords:
                elems = self.plateau.colonieAdjacenteTile(tile.coords)
                for elem in elems:
                    elem.joueur.ressource += elem.multiplicateur*tile.ressource
    
    def deplacerVoleur(self, joueurVoleur, coords):
        """
        Déplace le voleur selon le choix du joueur ayant obtenu 7 au lancer de dés.

        Paramètres
        ----------
        joueurVoleur : Joueur
            Joueur qui déplace le voleur et vole une carte à un adversaire un poss-de une
            colonie adjacente à la nouvelle position du voleur.
        coords : ndarray
            Coordonnées anciennes du voleur
        """

        ancienneCoords = self.plateau.voleur.coords
        if coords != ancienneCoords:
            self.plateau.voleur.coords = coords
            ressource = np.array([0,0,0,0,0])
            elems = self.plateau.colonieAdjacenteTile(coords)
            if len(elems) != 0:
                i = rd.randint(0, len(elems)-1)
                ressource = elems[i].joueur.ressources
                e = rd.randint(1, sum(ressource))
                if e <= ressource[0]:
                    elems[i].joueur.ressources -= np.array([1,0,0,0,0])
                    joueurVoleur.ressources += np.array([1,0,0,0,0])
                elif e <= ressource[0]+ressource[1]:
                    elems[i].joueur.ressources -= np.array([0,1,0,0,0])
                    joueurVoleur.ressources += np.array([0,1,0,0,0])
                elif e <= ressource[0]+ressource[1]+ressource[2]:
                    elems[i].joueur.ressources -= np.array([0,0,1,0,0])
                    joueurVoleur.ressources += np.array([0,0,1,0,0])
                elif e <= ressource[0]+ressource[1]+ressource[2]+ressource[3]:
                    elems[i].joueur.ressources -= np.array([0,0,0,1,0])
                    joueurVoleur.ressources += np.array([0,0,0,1,0])
                else:
                    elems[i].joueur.ressources -= np.array([0,0,0,0,1])
                    joueurVoleur.ressources += np.array([0,0,0,0,1])
            return True
        return False

    def construireColonie(self, joueur, coords):
        """
        Construit une colonie à trois conditions : l'intersection ou sommet est libre, il
        n'y a pas d'infrastructure adjacente et le joueur possède suffisamment de ressources.
        Le coût de la colonie est prélevé au joueur.

        Paramètres
        ----------
        joueur : Joueur
            Joueur qui construit la colonie
        coords : ndarray
            Coordonnées de la nouvelle colonie

        Renvoie
        -------
        True si la colonie est construite
        False sinon
        """

        if joueur.ressourceSuffisante(np.array([1,1,1,1,0])):
            if self.plateau.intersectionDispoConstruction(coords):
                if self.plateau.routeAdjacenteColonieExiste(joueur, coords):
                    joueur.ressource -= np.array([1,1,1,1,0])
                    colonie = Plateau.Colonie(joueur, coords)
                    self.plateau.intersections.append(colonie)
                    joueur.colonies.append(colonie)
                    self.ajoutPort(joueur, coords)
                    return True
        return False
    
    def construireVille(self, joueur, coords):
        """
        Construit une ville à trois conditions : l'intersection ou sommet est libre, il
        n'y a pas d'infrastructure adjacente et le joueur possède suffisamment de ressources.
        Le coût de la ville est prélevé au joueur.

        Paramètres
        ----------
        joueur : Joueur
            Joueur qui construit la ville
        coords : ndarray
            Coordonnées de la nouvelle ville

        Renvoie
        -------
        True si la ville est construite
        False sinon
        """

        if joueur.ressourceSuffisante(np.array([0,0,0,2,3])):
            if joueur.colonieExiste(coords):
                joueur.ressource -= np.array([0,0,0,2,3])
                ville = Plateau.Ville(joueur, coords)
                colonie = joueur.getColonie(coords)
                self.plateau.intersections.remove(colonie)
                joueur.colonies.remove(colonie)
                self.plateau.intersections.append(ville)
                joueur.villes.append(ville)
                return True
        return False
    
    def construireRoute(self, joueur, coords):
        """
        Construit une route à deux conditions : l'emplacement choisi est vide
        et le joueur possède suffisamment de ressources.
        Le coût de la route est prélevé au joueur.

        Paramètres
        ----------
        joueur : Joueur
            Joueur qui construit la route
        coords : ndarray
            Coordonnées de la nouvelle route

        Renvoie
        -------
        True si la route est construite
        False sinon
        """

        if joueur.ressourceSuffisante(np.array([1,1,0,0,0])):
            if self.plateau.routeDispoConstruction(coords):
                if self.plateau.routeAdjacenteRouteExiste(joueur, coords) or self.plateau.colonieAdjacenteRouteExiste(joueur, coords):
                    joueur.ressource -= np.array([1,1,0,0,0])
                    route = Plateau.Route(joueur, coords)
                    self.plateau.routes.append(route)
                    joueur.routes.append(route)
                    return True
        return False

    def construireColonieGratuit(self, joueur, coords):
        """
        Construit une colonie à deux conditions : l'intersection ou sommet est libre et il
        n'y a pas d'infrastructure adjacente.
        Le coût de la colonie n'est pas prélevé au joueur.

        Paramètres
        ----------
        joueur : Joueur
            Joueur qui construit la colonie
        coords : ndarray
            Coordonnées de la nouvelle colonie

        Renvoie
        -------
        True si la colonie est construite
        False sinon
        """

        if self.plateau.intersectionDispoConstruction(coords):
            colonie = Plateau.Colonie(joueur, coords)
            self.plateau.intersections.append(colonie)
            joueur.colonies.append(colonie)
            self.ajoutPort(joueur, coords)
            return True
        return False

    def construireRouteGratuit(self, joueur, coords):
        """
        Construit une route à l'emplacement choisi s'il est vide.
        Le coût de la route n'est pas prélevé au joueur.

        Paramètres
        ----------
        joueur : Joueur
            Joueur qui construit la route
        coords : ndarray
            Coordonnées de la nouvelle route

        Renvoie
        -------
        True si la route est construite
        False sinon
        """

        if self.plateau.routeDispoConstruction(coords):
            if self.plateau.routeAdjacenteRouteExiste(joueur, coords) or self.plateau.colonieAdjacenteRouteExiste(joueur, coords):
                route = Plateau.Route(joueur, coords)
                self.plateau.routes.append(route)
                joueur.routes.append(route)
                return True
        return False
        

    def ajoutPort(self, joueur, coords):
        """
        Ajoute à la liste des ports du joueur un port qu'il a atteint grâce à la construction d'une colonie.

        Paramètres
        ----------
        joueur : Joueur
            Joueur qui a construit une colonie liée à un port
        coords : ndarray
            Coordonnées du port
        """

        for port in self.plateau.ports:
            if port.coords == coords:
                joueur.ports.append(port)
            
    def achatCarteDev(self, joueur):
        """
        Donne au joueur une carte développement de la pioche contre son coût.

        Paramètres
        ----------
        joueur : Joueur
            Joueur qui achète la carte développement

        Renvoie
        -------
        True si la carte est achetée
        False sinon
        """

        if len(self.plateau.pioche.devCards)>0:
            if joueur.ressourceSuffisante(np.array([0,0,1,1,1])):
                joueur.ressource -= np.array([0,0,1,1,1])
                joueur.carteDev.append(self.plateau.pioche.devCards.pop())
                return True
        return False

    def echangeBanque(self, joueur, don, recu):
        """
        Procède à un échange de ressources entre le joueur et la banque à un taux déterminé par ses ports.

        Paramètres
        ----------
        joueur : Joueur
            Joueur qui échange avec la banque
        don : ndarray
            Ressources que le joueur perd
        recu : ndarray
            Ressources que le joueur gagne

        Renvoie
        -------
        True si l'échange est effectué
        False sinon
        """

        joueur.calculValeurEchange()
        if joueur.ressourceSuffisante(don):
            c = 0
            for j in range(len(don)):
                c += don[j]//joueur.valeurEchange[j]
            if sum(recu)<=c:
                joueur.ressource = joueur.ressource - don + recu
                return True
        return False

    def echangeJoueur(self, joueur1, joueur2, don, recu):
        """
        Procède à un échange entre le joueur actif et un autre joueur
        qui choisissent ce qu'ils veulent donner et recevoir.

        Paramètres
        ----------
        joueur1 : Joueur
            Premier joueur participant à l'échange, dont c'est le tour
        joueur2 : Joueur
            Second jour participant à l'échange dont ce n'est pas le tour
        don : ndarray
            Ressources que le joueur1 perd et que le joueur2 gagne
        recu : ndarray
            Ressources que le joueur2 perd et que le joueur1 gagne

        Renvoie
        -------
        True si l'échange est effectué
        False sinon
        """

        if joueur1.ressourceSuffisante(don) and joueur2.ressourceSuffisante(recu):
            joueur1.ressource = joueur1.ressource - don + recu
            joueur2.ressource = joueur2.ressource + don - recu
            return True
        return False

    def tourSuivant(self):
        """
        Passe au tour du joueur suivant qui lance les dés et donne ainsi des ressources aux joueurs.

        Paramètres
        ----------
        aucun
        """

        #print("Tour Suivant")
        self.calculPlusGrandeArmee()
        self.numeroJoueurActuel += 1
        if self.numeroJoueurActuel >= len(self.joueurs):
            self.numeroJoueurActuel = 0   
        self.joueurActuel = self.joueurs[self.numeroJoueurActuel]
        self.joueurActuel.calculPV()
        self.lancerDes()
        self.donRessource()

    def tourSuivantDebut(self):
        """
        Passe au tour du joueur suivant lors du placement des premières colonies et premières routes.

        Paramètres
        ----------
        aucun

        Renvoie
        -------
        True si tous les joueurs ont placé leurs premières colonies et routes
        """

        #print("Joueur Suivant")
        ordre = [0,1,2,2,1,0]
        if len(self.joueurs) == 4:
            ordre = [0,1,2,3,3,2,1,0]
        self.numeroJoueurActuelDebut += 1
        if self.numeroJoueurActuelDebut >= len(ordre):
            self.numeroJoueurActuelDebut = 0
            return True
        self.numeroJoueurActuel = ordre[self.numeroJoueurActuelDebut]   
        self.joueurActuel = self.joueurs[self.numeroJoueurActuel]

    def calculPlusGrandeArmee(self):
        """
        Calcule quel joueur dans la partie possède la plus grande armée
        et si elle est composée d'au moins 3 chevaliers.

        Paramètres
        ----------
        aucun
        """

        m = 0 #nombre maximum de chevaliers
        n = 0 #nombre de chevalier de chaque joueur
        numeroJoueur = 0
        for joueur in self.joueurs:
            if joueur.plusGrandeArmee:
                m = joueur.nombreChevalier()
                numeroJoueur = joueur.numero
        for joueur in self.joueurs:
            joueur.plusGrandeArmee = False   
            n = joueur.nombreChevalier()
            if n > m:
                m = n
                numeroJoueur = joueur.numero
        if m >= 3:
            self.joueurs[numeroJoueur].plusGrandeArmee = True


