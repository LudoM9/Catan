import pygame
import Plateau
import Joueur

class Catan():
    """
    Classe qui représente une partie de jeu
    """
    def __init__(self, joueurs, rdPlateau = False):
        """
        Initialisation de ma classe

        Args:
            joueurs (list(string)): Liste de nom de joueurs
            rdPlateau (bool, optional): Booléen pour savoir si le plateau est aléatoire. Defaults to False.
        """
        self.plateau = Plateau.Plateau(rdPlateau)
        self.joueurs = []
        self.valeurDes = 0
        for i, joueur in enumerate(joueurs):
            self.joueurs.append(Joueur.Joueur(joueur, i, self.plateau))

    def lancerDes(self, joueur):
        s = sum(rd.randrange(1,7)+rd.randrange(1,7))
        self.valeurDes = s

    def donRessource(self):
        tiles = []
        for tile in self.plateau:
            if tile.value == self.valeurDes:
                tiles.append(tile)
        for tile in tiles:
            if tile.coords != self.plateau.voleur.coords:
                elems = self.plateau.colonieAdjacenteTile(tile.coords)
                for elem in elem:
                    elem.joueur.ressource += elem.multiplicateur*tile.ressource
    
    def deplacerVoleur(self, coords):
        ancienneCoords = self.plateau.voleur.coords
        if coords != ancienneCoords:
            self.plateau.voleur.coords = coords

    def construireColonie(self, joueur, coords):
        if joueur.ressourceSuffisante(np.array([1,1,1,1,0])):
            if self.plateau.intersectionDispoConstruction(coords):
                if self.plateau.routeAdjacenteColonieExiste(joueur, coords):
                    joueur.ressource -= np.array([1,1,1,1,0])
                    colonie = Colonie(joueur, coords)
                    self.plateau.intersections.append(colonie)
                    joueur.colonies.append(colonie)
                    self.ajoutPort(joueur, coords)
    
    def construireVille(self, joueur, coords):
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
        if joueur.ressourceSuffisante(np.array([1,1,0,0,0])):
            if self.plateau.routeDispoConstruction(coords):
                if self.plateau.routeAdjacenteRouteExiste(joueur, coords) or self.plateau.colonieAdjacenteRouteExiste(joueur, coords):
                    joueur.ressource -= np.array([1,1,0,0,0])
                    route = Route(joueur, coords)
                    self.plateau.routes.append(route)
                    joueur.routes.append(route)

    def construireColonieGratuit(self, joueur, coords):
        if self.plateau.intersectionDispoConstruction(coords):
            colonie = Colonie(joueur, coords)
            self.plateau.intersections.append(colonie)
            joueur.colonies.append(colonie)
            self.ajoutPort(joueur, coords)

    def construireRouteGratuit(self, joueur, coords):
        if self.plateau.routeDispoConstruction(coords):
            if self.plateau.routeAdjacenteExiste(joueur, coords) or self.plateau.colonieAdjacenteExiste(joueur, coords):
                route = Route(joueur, coords)
                self.plateau.routes.append(route)
                joueur.routes.append(route)

    def ajoutPort(self, joueur, coords):
        for port in self.plateau.ports:
            if port.coords == coords:
                joueur.ports.append(port)
            
    def achatCarteDev(self, joueur):
        if len(self.plateau.pioche.carteDev)>0:
            if joueur.ressourceSuffisante(np.array([0,0,1,1,1])):
                joueur.ressource -= np.array([0,0,1,1,1])
                joueur.carteDev.append(self.plateau.pioche.carteDev.pop())

    def echangeBanque(self, joueur, don, recu):
        joueur.calculValeurEchange()
        if joueur.ressourceSuffisante(don):
            c = 0
            for j in range(len(don)):
                c += don[j]//joueur.valeurEchange[j]
            if sum(recu)<=c:
                joueur.ressource = joueur.ressource - don + recu

    def echangeJoueur(self, joueur1, joueur2, don, recu):
        if joueur1.ressourceSuffisante(don) and joueur2.ressourceSuffisante(recu):
            joueur1.ressource = joueur1.ressource - don + recu
            joueur2.ressource = joueur2.ressource + don - recu

    def calculPlusGrandeArmee(self):
        m = 0
        n = 0
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


