"""
Module contenant tous les éléments qui apparaissent dans une partie de jeu.
"""

import pygame
import Plateau
import Joueur

class Catan():
    """
    Classe représentant une partie de jeu : le lancer dés, le voleur, les échanges, la
    construction, les achats et divers autres calculs nécéssaires au déroulement du jeu.

    Attributs
    ---------
    plateau : Plateau
        plateau sur le quel le jeu évolue
    joueurs : list(string)
        liste des joueurs participant au jeu
    valeurDes : bool
        résultat de la somme de deux lancers de dés à six faces réguliers
    """

    def __init__(self, joueurs, rdPlateau = False):
        """
        Parametres
        ----------
        joueurs : list(string)
            Liste des noms des joueurs
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
        

    def lancerDes(self, joueur):
        """
        Lance deux dés réguliersà six faces et somme les deux résultats.

        Parametres
        ----------
        joueur : Joueur
            Joueur qui lance les dés
        """

        s = sum(rd.randrange(1,7)+rd.randrange(1,7))
        self.valeurDes = s

    def donRessource(self):
        """
        Distribue au joueur les ressources des cases définies par le lancer de dés dont le joueur a un une colonie ou ville adjacente.

        Parametres
        ----------
        aucun
        """
        tiles = []
        for tile in self.plateau:
            if tile.value == self.valeurDes:
                tiles.append(tile)
        for tile in tiles:
            if tile.coords != self.plateau.voleur.coords:
                elems = self.plateau.colonieAdjacenteTile(tile.coords)
                for elem in elems:
                    elem.joueur.ressource += elem.multiplicateur*tile.ressource
    
    def deplacerVoleur(self, coords):
        """
        Déplace le voleur selon le choix du joueur ayant obtenu 7 au lancer de dés.

        Parametres
        ----------
        coords : ndarray
            Coordonnées anciennes du voleur
        """
        ancienneCoords = self.plateau.voleur.coords
        if coords != ancienneCoords:
            self.plateau.voleur.coords = coords

    def construireColonie(self, joueur, coords):
        """
        Construit une colonie à trois conditions : l'intersection ou sommet est libre, il
        n'y a pas d'infrastructure adjacente et le joueur possède suffisamment de ressources.
        Le coût de la colonie est prélevé au joueur.

        Parametres
        ----------
        joueur : Joueur
            Joueur qui construit la colonie
        coords : ndarray
            Coordonnées de la nouvelle colonie
        """

        if joueur.ressourceSuffisante(np.array([1,1,1,1,0])):
            if self.plateau.intersectionDispoConstruction(coords):
                if self.plateau.routeAdjacenteColonieExiste(joueur, coords):
                    joueur.ressource -= np.array([1,1,1,1,0])
                    colonie = Colonie(joueur, coords)
                    self.plateau.intersections.append(colonie)
                    joueur.colonies.append(colonie)
                    self.ajoutPort(joueur, coords)
    
    def construireVille(self, joueur, coords):
        """
        Construit une ville à trois conditions : l'intersection ou sommet est libre, il
        n'y a pas d'infrastructure adjacente et le joueur possède suffisamment de ressources.
        Le coût de la ville est prélevé au joueur.

        Parametres
        ----------
        joueur : Joueur
            Joueur qui construit la ville
        coords : ndarray
            Coordonnées de la nouvelle ville
        """

        if joueur.ressourceSuffisante(np.array([0,0,0,2,3])):
            if joueur.colonieExiste(coords):
                joueur.ressource -= np.array([0,0,0,2,3])
                ville = Ville(joueur, coords)
                colonie = joueur.getColonie(coords)
                self.plateau.intersections.remove(colonie)
                joueur.colonies.remove(colonie)
                self.plateau.intersections.append(ville)
                joueur.villes.append(ville)
    
    def construireRoute(self, joueur, coords):
        """
        Construit une route à deux conditions : l'emplacement choisi est vide
        et le joueur possède suffisamment de ressources.
        Le coût de la route est prélevé au joueur.

        Parametres
        ----------
        joueur : Joueur
            Joueur qui construit la route
        coords : ndarray
            Coordonnées de la nouvelle route
        """

        if joueur.ressourceSuffisante(np.array([1,1,0,0,0])):
            if self.plateau.routeDispoConstruction(coords):
                if self.plateau.routeAdjacenteRouteExiste(joueur, coords) or self.plateau.colonieAdjacenteRouteExiste(joueur, coords):
                    joueur.ressource -= np.array([1,1,0,0,0])
                    route = Route(joueur, coords)
                    self.plateau.routes.append(route)
                    joueur.routes.append(route)

    def construireColonieGratuit(self, joueur, coords):
        """
        Construit une colonie à deux conditions : l'intersection ou sommet est libre et il
        n'y a pas d'infrastructure adjacente.
        Le coût de la colonie n'est pas prélevé au joueur.

        Parametres
        ----------
        joueur : Joueur
            Joueur qui construit la colonie
        coords : ndarray
            Coordonnées de la nouvelle colonie
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

        Parametres
        ----------
        joueur : Joueur
            Joueur qui construit la route
        coords : ndarray
            Coordonnées de la nouvelle route
        """

        if self.plateau.routeDispoConstruction(coords):
            if self.plateau.routeAdjacenteExiste(joueur, coords) or self.plateau.colonieAdjacenteExiste(joueur, coords):
                route = Route(joueur, coords)
                self.plateau.routes.append(route)
                joueur.routes.append(route)
                return True
        return False
        

    def ajoutPort(self, joueur, coords):
        """
        Ajoute à la liste des ports du joueur un port qu'il a atteint grâce à la construction d'une colonie.

        Parametres
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

        Parametres
        ----------
        joueur : Joueur
            Joueur qui achète la carte développement
        """
        if len(self.plateau.pioche.carteDev)>0:
            if joueur.ressourceSuffisante(np.array([0,0,1,1,1])):
                joueur.ressource -= np.array([0,0,1,1,1])
                joueur.carteDev.append(self.plateau.pioche.carteDev.pop())

    def echangeBanque(self, joueur, don, recu):
        """
        Procède à un échange de ressources entre le joueur et la banque à un taux déterminé par ses ports.

        Parametres
        ----------
        joueur : Joueur
            Joueur qui échange avec la banque
        don : ndarray
            Ressources que le joueur perd
        recu : ndarray
            Ressources que le joueur gagne
        """

        joueur.calculValeurEchange()
        if joueur.ressourceSuffisante(don):
            c = 0
            for j in range(len(don)):
                c += don[j]//joueur.valeurEchange[j]
            if sum(recu)<=c:
                joueur.ressource = joueur.ressource - don + recu

    def echangeJoueur(self, joueur1, joueur2, don, recu):
        """
        Procède à un échange entre le joueur actif et un autre joueur
        qui choisissent ce qu'ils veulent donner et recevoir.

        Parametres
        ----------
        joueur1 : Joueur
            Premier joueur participant à l'échange, dont c'est le tour
        joueur2 : Joueur
            Second jour participant à l'échange dont ce n'est pas le tour
        don : ndarray
            Ressources que le joueur1 perd et que le joueur2 gagne
        recu : ndarray
            Ressources que le joueur2 perd et que le joueur1 gagne

        """
        if joueur1.ressourceSuffisante(don) and joueur2.ressourceSuffisante(recu):
            joueur1.ressource = joueur1.ressource - don + recu
            joueur2.ressource = joueur2.ressource + don - recu

    def tourSuivant(self):
        print("Tour Suivant")
        self.numeroJoueurActuel += 1
        if self.numeroJoueurActuel >= len(self.joueurs):
            self.numeroJoueurActuel = 0   
        self.joueurActuel = self.joueurs[self.numeroJoueurActuel]

    def tourSuivantDebut(self):
        print("Joueur Suivant")
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

        Parametres
        ---------
        aucun
        """

        m = 0 #nombre maximum de chevaliers
        n = 0 #nombre de chevalier de chaque joueur
        numeroJoueur = 0
        for joueur in joueurs:
            if joueur.plusGrandeArmee:
                m = joueur.nombreChevalier()
                numeroJoueur = joueur.numero
        for joueur in joueurs:
            joueur.plusGrandeArmee = False   
            n = joueur.nombreChevalier()
            if n > m:
                m = n
                numeroJoueur = joueur.numero
        if m >= 3:
            self.joueurs[numeroJoueur].plusGrandeArmee = True


