"""
Module contenant toutes les informations relatives au plateau de jeu et aux déplacments sur celui-ci.
"""
from abc import abstractmethod, ABCMeta
from numpy.random import randint
import random as rd
import numpy as np


class Plateau():
    """
    Classe représentant le plateau de jeu : son caractère aléatoire et des calculs pour pouvoir interagir avec lui.
    Si le plateau n'est pas aléatoire (rdPlateau==False), le plateau alors créé est prédéfini et équilibré.

    Attributs
    ---------
    tiles : list(Tile)
        liste des tuiles du plateau
    intersections : list
        liste des intersections ou sommets du plateau
    routes : list
        liste des routes ou chemin du plateau
    ports : list(Port)
        liste des ports du plateau
    voleur : Voleur
        voleur présent sur le plateau
    pioche : Pioche
        pioche de cartes développement
    """
    def __init__(self, rdPlateau = False):
        """
        Parametres
        ----------
        rdPlateau : bool, optionnel, False par défaut
            Booléen pour savoir si le plateau est aléatoire
        """

        self.tiles = [WoodTile(self, (-2,-1), 6), WoolTile(self, (-1,-1), 3), WoolTile(self, (0,-2), 8), WheatTile(self, (-2,0), 2), StoneTile(self, (-1,0), 4), WheatTile(self, (0,-1), 5), WoodTile(self, (1,-1), 10), WoodTile(self, (-2,1), 5), ClayTile(self, (-1,1), 9), DesertTile(self, (0,0), 7), StoneTile(self, (1,0), 6), WheatTile(self, (2,-1), 9), WheatTile(self, (-1,2), 10), StoneTile(self, (0,1), 11), WoodTile(self, (1,1), 3), WoolTile(self, (2,0), 12), ClayTile(self, (0,2), 8), WoolTile(self, (1,2), 4), ClayTile(self, (2,1), 11)]
        self.intersections = []
        self.routes = []
        self.ports = [Port((-2,-2), [3,3,3,3,3]), Port((-2,-1), [3,3,3,3,3]), Port((-1,-3), [4,4,2,4,4]), Port((0,-3), [4,4,2,4,4]), Port((1,-3), [3,3,3,3,3]), Port((2,-3), [3,3,3,3,3]), Port((3,-2), [3,3,3,3,3]), Port((3,-1), [3,3,3,3,3]), Port((3,1), [4,2,4,4,4]), Port((3,2), [4,2,4,4,4]), Port((2,4), [2,4,4,4,4]), Port((2,5), [2,4,4,4,4]), Port((0,4), [3,3,3,3,3]), Port((1,4), [3,3,3,3,3]), Port((-1,4), [4,4,4,2,4]), Port((-1,5), [4,4,4,2,4]), Port((-2,1), [4,4,4,4,2]), Port((-2,2), [4,4,4,4,2])]
        self.voleur = Voleur((0,0))
        self.pioche = Pioche()
        if rdPlateau:
            Lcoords = [(i,j) for i in range(-2,3) for j in range (-2,3) if abs(i+j)<=3 and abs(i)+abs(j)<=3 and not(abs(i)>0 and j==-2)]
            Lvalues = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
            rd.shuffle(Lvalues)
            Lvalues += [7]
            Lvalues[18],Lvalues[9] = Lvalues[9], 7
            Ltiles = []
            for i in range (4):
                Ltiles.append("Wood")
                Ltiles.append("Wheat")
                Ltiles.append("Wool")
                if i < 3:
                    Ltiles.append("Stone")
                    Ltiles.append("Clay") 
            rd.shuffle(Ltiles)
            Ltiles += ["Desert"]
            Lvalues[18],Lvalues[9] = Lvalues[9], Ltiles[18]           
            self.tiles = []
            for i in range(19):
                if Ltiles[i] == "Wood":
                    self.tiles.append(WoodTile(self, Lcoords[i], Lvalues[i]))
                elif Ltiles[i] == "Wheat":
                    self.tiles.append(WheatTile(self, Lcoords[i], Lvalues[i]))
                elif Ltiles[i] == "Wool":
                    self.tiles.append(WoolTile(self, Lcoords[i], Lvalues[i]))
                elif Ltiles[i] == "Stone":
                    self.tiles.append(StoneTile(self, Lcoords[i], Lvalues[i]))
                elif Ltiles[i] == "Clay":
                    self.tiles.append(ClayTile(self, Lcoords[i], Lvalues[i]))
    
    def getAdjacentTilesFromTile(self, tile):
        """
        Parametres
        ----------
        tile : Tile
            Tuile dont on souhaite connaîntre les tuiles adjacentes

        Renvoie
        -------
        adjTiles : list(Tile)
            Liste des tuiles adjacentes à la tuile en entrée
        """

        adjTiles = []
        x = tile[0]
        y = tile[1]
        offset = 1
        if x % 2 != 0:
            offset = -1

        if y+1 < 3 and (abs(x)+abs(y+1)) <= 3:
          adjTiles.append((x,y+1))
        if (y >= -1 and abs(x+y-1) <= 3 and y-1!=-2) or (x==0 and y-1==-2):
          adjTiles.append((x,y-1))
        if x+1 < 3 and (abs(x+1)+abs(y)) <= 3:
            if x+1 == 1 and y == -2: 
                ...
            else:
                adjTiles.append((x+1,y))
        if abs(x-1+y) <= 3 and abs(x-1)!=3 and (abs(x-1)+abs(y)) <= 3:
            if x-1 == -1 and y == -2: 
                ...
            else:
                adjTiles.append((x-1,y))
        if abs(y+offset) < 3:
            if (x+1) < 3 and (abs(x+1)+abs(y+offset)) <= 3:
                adjTiles.append((x+1,y+offset)) 
            if x >= -1 and abs(x-1 + y+offset) <= 3:
                adjTiles.append((x-1,y+offset))
        return adjTiles

    def getAdjacentTilesFromVertice(self, vertice):
        """
        Parametres
        ----------
        vertice : ndarray
            Coordonnées d'un sommet dont on souhaite connaître les tuiles adjacents

        Renvoie
        -------
        adjTiles : list(Tile)
            Liste des tuiles adjacentes au sommet en entrée
        """

        adjTiles = []
        x = vertice[0]
        y = vertice[1]
        xOffset = x % 2
        yOffset = y % 2

        if abs(x+y//2)<=3 and abs(x)+abs(y//2)<=3 and not(abs(x)>0 and y//2==-2) and abs(x)<3 and abs(y//2)<3:
            adjTiles.append((x,y//2))

        weirdX = x
        if (xOffset+yOffset) == 1: 
            weirdX = x-1

        weirdY = y//2 
        if yOffset == 1: 
            weirdY += 1
        else: 
            weirdY -= 1

        if abs(weirdX+weirdY)<=3 and abs(weirdX)+abs(weirdY)<=3 and not(abs(weirdX)>0 and weirdY==-2) and abs(weirdX)<=2 and abs(weirdY)<=2:
            adjTiles.append((weirdX, weirdY))
        if x >= -1 and abs(x-1+y//2)<=3 and abs(x-1)+abs(y//2)<=3 and abs(x-1)<3 and abs(y//2)<3 and not(abs(x-1)==1 and y//2==-2):
            adjTiles.append((x-1, y//2))
        return adjTiles

    def getVerticesFromTile(self, tile):
        """
        Parametres
        ----------
        tile : Tile
            Tuile dont on souhaite connaîntre les sommets adjacents

        Renvoie
        -------
        vertices : list(ndarray)
            Liste des sommets adjacents à la tuile en entrée
        """

        vertices = []
        x = tile[0]
        y = tile[1]
        offset = x % 2
        offset = 0-offset
        vertices.append((x, 2*y+offset))
        vertices.append((x, 2*y+1+offset))
        vertices.append((x, 2*y+2+offset))
        vertices.append((x+1, 2*y+offset))
        vertices.append((x+1, 2*y+1+offset))
        vertices.append((x+1, 2*y+2+offset))
        return vertices

    def getEdgesFromTile(self, tile):
        """
        Parametres
        ----------
        tile : Tile
            Tuile dont on souhaite connaître les chemins adjacents

        Renvoie
        -------
        edges : list(ndarray)
            Liste des chemins adjacents à la tuile en entrée
        """

        edges = []
        x = tile[0]
        y = tile[1]
        offset = x % 2
        offset = 0-offset
        edges.append((2*x,2*y+offset))
        edges.append((2*x,2*y+1+offset))
        edges.append((2*x+1,2*y+offset))
        edges.append((2*x+1,2*y+2+offset))
        edges.append((2*x+2,2*y+offset))
        edges.append((2*x+2,2*y+1+offset))
        return edges

    def getAdjacentVerticesFromVertice(self, vertice):
        """
        Parametres
        ----------
        vertice : ndarray
            Coordonnées d'un sommet dont on souhaite connaître les sommets adjacents

        Renvoie
        -------
        adjTiles : list(ndarray)
            Liste des sommets adjacentes au sommet en entrée
        """

        adjVertices = []
        adjTiles = self.getAdjacentTilesFromVertice(vertice)
        allVertices = []
        if len(adjTiles) == 1:
            x = vertice[0]
            y = vertice[1]

            #Nord
            if abs(x)+abs(y) == 4:
                adjVertices.append((x,y+1))
                adjVertices.append((x+1,y))
            #Sud
            elif abs(x)+abs(y) == 7:
                adjVertices.append((x-1,y))
                adjVertices.append((x,y-1))
            #SW
            elif abs(x)+abs(y) == 6:
                adjVertices.append((x+1,y))
                adjVertices.append((x,y-1))
            #NE
            elif abs(x)+abs(y) == 5:
                adjVertices.append((x-1,y))
                adjVertices.append((x,y+1))
            #NW or SE
            elif x==-2 or x==3:
                adjVertices.append((x,y+1))
                adjVertices.append((x,y-1))
        else:
            for tile in adjTiles:
                allVertices.append(self.getVerticesFromTile(tile))
            for i in range(len(allVertices)):
                j = i + 1
                while j<len(allVertices):
                    print(j)
                    adjVertices += [element for element in allVertices[i] if element in allVertices[j] and element!=vertice]
                    j += 1
        return list(set(adjVertices))
    

    def getAdjacentEdgesFromVertice(self, vertice):
        """
        Parametres
        ----------
        vertice : ndarray
            Coordonnées d'un sommet dont on souhaite connaître les chemins adjacents

        Renvoie
        -------
        adjEdges : list(ndarray)
            Liste des chemins adjacentes au sommet en entrée
        """

        adjEdges = []
        adjTiles = self.getAdjacentTilesFromVertice(vertice)
        allEdges = []
        x = vertice[0]
        y = vertice[1]
        offset = 1
        if x%2 != y%2:
            offset = -1
        if len(adjTiles) == 1:
            adjTilesFromTile = self.getAdjacentTilesFromTile(adjTiles[0])
            edgeOfTile = self.getEdgesFromTile(adjTiles[0])
            for tile in adjTilesFromTile:
                allEdges.append(self.getEdgesFromTile(tile))
            for edges in allEdges:
                for edge in edges:
                    if edge in edgeOfTile:
                        edgeOfTile.remove(edge)
            if len(edgeOfTile)>=3:
                #Nord
                if abs(x)+abs(y) == 4:
                    adjEdges.append((x*2,y))
                    adjEdges.append((x*2+1,y))
                #Sud
                elif abs(x)+abs(y) == 7:
                    adjEdges.append((x*2-1,y))
                    adjEdges.append((x*2,y-1))
                #SW
                elif abs(x)+abs(y) == 6:
                    adjEdges.append((x*2,y-1))
                    adjEdges.append((x*2+1,y))
                #NE
                elif abs(x)+abs(y) == 5:
                    adjEdges.append((x*2-1,y))
                    adjEdges.append((x*2,y))
                #NW or SE
                elif x==-2 or x==3:
                    adjEdges.append((x*2,y-1))
                    adjEdges.append((x*2,y))
            else:
                adjEdges = edgeOfTile
        else:
                adjEdges += [(x*2,y), (x*2,y-1), (x*2+offset,y)]
        return adjEdges

    def getVerticesOfEdge(self, edge):
        """
        Parametres
        ----------
        edge : ndarray
            Chemin dont on souhaite connaître les sommets adjacents

        Renvoie
        -------
        vertices : list(ndarray)
            Liste des sommets adjacents au chemin en entrée
        """
        vertices = []
        x = edge[0]
        y = edge[1]
        vertice1 = (int((x-1)/2), y)
        vertice2 = (int((x+1)/2), y)
        if x%2 == 0:
          vertice1 = (int(x/2), y)
          vertice2 = (int(x/2), y+1)
        vertices = [vertice1, vertice2]
        return vertices

    def getAdjacentEdgesFromEdge(self, edge):
        """"
        Parametres
        ----------
        edge : ndarray
            Chemin dont on souhaite connaître les chemins adjacents

        Renvoie
        -------
        adjEdges : list(ndarray)
            Liste des chemins adjacents au chemin en entrée
        """

        adjEdges = []
        vertices = self.getVerticesOfEdge(edge)
        for vertice in vertices:
            adjEdges += self.getAdjacentEdgesFromVertice(vertice)
            adjEdges = list(set(adjEdges))
        adjEdges.remove(edge)
        return adjEdges

    def intersectionDispoConstruction(self, coords):
        """
        Vérifie que la construction d'une colonie est possible : le sommet et les sommets adjacents doivent être vides.

        Parametres
        ----------
        coords : ndarray
            Coordonnées d'un sommet/d'une intersection que l'on souhaite tester

        Renvoie
        -------
        True si les conditions sont véfifiées
        False sinon
        """

        for elem in self.intersections:             #elem = Villes et colonies
            if coords == elem.coords:
                return False
            elif elem.coords in self.getAdjacentVerticesFromVertice(self, coords):
                return False
        return True

    def routeDispoConstruction(self, coords):
        """
        Vérifie que la construction d'une route est possible : le chemin
        est vide et relié à une autre infrastructure du joueur.

        Parametres
        ----------
        coords : ndarray
            Coordonnées d'un chemin l'on souhaite tester

        Renvoie
        -------
        True si les conditions sont véfifiées
        False sinon
        """

        for route in self.routes:
            if coords == route.coords:
                return False
        return True

    def routeAdjacenteRouteExiste(self, joueur, coords):
        """
        Vérifie qu'un joueur possède une route adjacente à un chemin avant de construire une route sur ce chemin.

        Parametres
        ----------
        joueur : Joueur
            Joueur dont la présence d'une route adjacente est testée
        coords : ndarray
            Coordonnées du chemin à tester
        Renvoie
        -------
        True si la condition est vérifiée
        False sinon
        """

        for route in self.routes:
            if route.joueur == joueur:
                if route.coords in self.getAdjacentEdgesFromEdge(coords):
                    return True
        return False

    def colonieAdjacenteRouteExiste(self, joueur, coords):
        """
        Vérifie si un joueur possède une colonie ou une ville adjacente à un chemin testé.

        Parametres
        ----------
        joueur : Joueur
            Joueur dont la présence d'une colonie adjacente est testée
        coords : ndarray
            Coordonnées du chelin à tester
        Renvoie
        -------
        True si la condition est vérifiée
        False sinon
        """

        for elem in self.intersections:
            if elem.joueur == joueur:
                if elem.coords in self.getVerticesOfEdge(coords):
                    return True
        return False

# à modifier
    def routeAdjacenteColonieExiste(self, joueur, coords):
        """
        Vérifie qu'un joueur possède une route adjacente à une colonie ou une ville.

        Parametres
        ----------
        joueur : Joueur
            Joueur dont la présence de route adjacente est testée
        coords : ndarray
            Coordonnées de la colonie ou de la ville à tester
        Renvoie
        -------
        True si la condition est vérifiée
        False sinon
        """

        for elem in self.intersections: #il faudrait plutot regarder les routes
            if elem.joueur == joueur:
                if elem.coords in self.getAdjacentEdgesFromVertice(coords):
                    return True
        return False

    def colonieAdjacenteTile(self, coords):
        """
        Trouve les colonies ou villes adjacentes à une tuile.

        Parametres
        ----------
        coords : ndarray
            Coordonnées de la tuile à tester
        Renvoie
        -------
        elems : liste(array)
            Liste de colonies ou villes adjacentes à la tuile testée
        """

        elems = []
        for elem in self.intersections:
            if elem.coords in self.getVerticesFromTile(coords):
                elems.append(elem)
        return elems

class Tile(metaclass = ABCMeta):
    """
    Classe représentant les tuiles hexagonales du plateau de jeu,
    mère des classes représentant chaque type de tuiles.

    Attributs
    ---------
    plateau : Plateau
        plateau dans lequel la tuile se trouve
    coords : ndarray
        coordonnées la la tuile
    value : int
        valeur du numéro de la case correspondant au résultat des dés
    ressource : ndarray
        ressource liée à la case
    color : int
        Couleur de la case sous forme hexadécimale
    """

    def __init__(self, plateau, coords, value):
        """
        Parametres
        ----------
        plateau : Plateau
            Plateau dans lequel la tuile se trouve
        coords : ndarray
            Coordonnées la la tuile
        value : int
            Valeur du numéro de la case correspondant au résultat des dés
        """

        self.plateau = plateau
        self.coords = coords
        self.value = value
        self.ressource = np.array([0,0,0,0,0])
        self.color = ""

class WoodTile(Tile):
    """
    Classe représentant les tuiles produisant du bois, fille de la classe Tile.

    Attributs
    ---------
    ressource : ndarray
        ressource liée à la case
    color : int
        Couleur de la case sous forme hexadécimale
    """

    def __init__(self, plateau, coords, value):
        """
        Parametres
        ----------
        plateau : Plateau
            Plateau dans lequel la tuile se trouve
        coords : ndarray
            Coordonnées la la tuile
        value : int
            Valeur du numéro de la case correspondant au résultat des dés
        """
        super().__init__(plateau, coords, value)
        self.ressource = np.array([1,0,0,0,0])
        self.color = 0x33855d

class WheatTile(Tile):
    """
    Classe représentant les tuiles produisant du blé, fille de la classe Tile.

    Attributs
    ---------
    ressource : ndarray
        ressource liée à la case
    color : int
        Couleur de la case sous forme hexadécimale
    """

    def __init__(self, plateau, coords, value):
        """
        Parametres
        ----------
        plateau : Plateau
            Plateau dans lequel la tuile se trouve
        coords : ndarray
            Coordonnées la la tuile
        value : int
            Valeur du numéro de la case correspondant au résultat des dés
        """

        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,0,0,1,0])
        self.color = 0xffff00

class WoolTile(Tile):
    """
    Classe représentant les tuiles produisant de la laine, fille de la classe Tile.

    Attributs
    ---------
    ressource : ndarray
        ressource liée à la case
    color : int
        Couleur de la case sous forme hexadécimale
    """

    def __init__(self, plateau, coords, value):
        """
        Parametres
        ----------
        plateau : Plateau
            Plateau dans lequel la tuile se trouve
        coords : ndarray
            Coordonnées la la tuile
        value : int
            Valeur du numéro de la case correspondant au résultat des dés
        """

        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,0,1,0,0])
        self.color = 0xf5f5f5

class ClayTile(Tile):
    """
    Classe représentant les tuiles produisant de l'argile, fille de la classe Tile.

    Attributs
    ---------
    ressource : ndarray
        ressource liée à la case
    color : int
        Couleur de la case sous forme hexadécimale
    """

    def __init__(self, plateau, coords, value):
        """
        Parametres
        ----------
        plateau : Plateau
            Plateau dans lequel la tuile se trouve
        coords : ndarray
            Coordonnées la la tuile
        value : int
            Valeur du numéro de la case correspondant au résultat des dés
        """

        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,1,0,0,0])
        self.color = 0xd2691e

class StoneTile(Tile):
    """
    Classe représentant les tuiles produisant de la pierre, fille de la classe Tile.

    Attributs
    ---------
    ressource : ndarray
        ressource liée à la case
    color : int
        Couleur de la case sous forme hexadécimale
    """

    def __init__(self, plateau, coords, value):
        """
        Parametres
        ----------
        plateau : Plateau
            Plateau dans lequel la tuile se trouve
        coords : ndarray
            Coordonnées la la tuile
        value : int
            Valeur du numéro de la case correspondant au résultat des dés
        """

        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,0,0,0,1])
        self.color = 0xa9a9a9

class DesertTile(Tile):
    """
    Classe représentant la tuile fixe au centre, position initiale du voleur et ne produisant rien.

    Attributs
    ---------
    ressource : ndarray
        ressource liée à la case
    color : int
        Couleur de la case sous forme hexadécimale
    """
    def __init__(self, plateau, coords, value):
        """
        Parametres
        ----------
        plateau : Plateau
            Plateau dans lequel la tuile se trouve
        coords : ndarray
            Coordonnées la la tuile
        value : int
            Valeur du numéro de la case correspondant au résultat des dés
        """

        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,0,0,0,0])
        self.color = 0xf0e68c

class Colonie():
    """
    Classe représentant une colonie, mère de Ville.

    Attributs
    ---------
    joueur : Joueur
        joueur possédant la colonie
    coords : ndarray
        coordonnées de la colonie
    adjacent : list
        liste des sommets adjacents, qui ne doivent pas contenir d'autres colonies ou villes.
    multiplicateur : int
        nombre de points de victoire conférés à la construction d'une colonie
    coût : ndarray
        prix de la construction d'une colonie
    """

    def __init__(self, joueur, coords):
        """
        Parametres
        ----------
        joueur : Joueur
            Joueur possédant la colonie
        coords : ndarray
            Coordonnées de la colonie
        """
        self.joueur = joueur
        self.coords = coords
        self.adjacent = []
        self.multiplicateur = 1
        self.coût = np.array([1,1,1,1,0])

class Ville(Colonie):
    """
    Classe représentant une Ville, fille de Colinie.

    Attributs
    ---------
    joueur : Joueur
        joueur possédant la ville
    coords : ndarray
        coordonnées de la ville
    adjacent : list
        liste des sommets adjacents, qui ne doivent pas contenir d'autres colonies ou villes.
    multiplicateur : int
        nombre de points de victoire conférés à la construction d'une ville
    coût : ndarray
        prix de la construction d'une ville
    """

    def __init__(self, joueur, coords):
        """
        Parametres
        ----------
        joueur : Joueur
            Joueur possédant la ville
        coords : ndarray
            Coordonnées de la ville
        """

        super().__init__(self, joueur, coords)
        self.multiplicateur = 2
        self.coût = np.array([0,0,0,2,3])

class Route():
    """
    Classe représentant une route.

    Attributs
    ---------
    joueur : Joueur
        joueur possédant la route
    coords : ndarray
        coordonnées de la route
    coût : ndarray
        prix de la construction d'une route
    """

    def __init__(self, joueur, coords):
        """
        Parametres
        ----------
        joueur : Joueur
            Joueur possédant la route
        coords : ndarray
            Coordonnées de la route
        """
        self.joueur = joueur
        self.coords = coords
        self.coût = np.array([1,1,0,0,0])
    
    #Check if player has now the longest road

class Voleur():
    """
    Classe représentant le voleur.

    Attributs
    ---------
    coords : ndarray
        position du voleur, initialement placé au centre sur la case de type désert
    """

    def __init__(self, coords):
        """
        Parametres
        ----------
        coords : ndarray
            Coordonnées du voleur
        """

        self.coords = coords

class Port():
    """
    Classe représentant un port.

    Attributs
    ---------
    coords : ndarray
        coordonnées du port
    echange : ndarray
        echanges de ressources possibles pour ce type de port
    """

    def __init__(self, coords, echange):
        """
        Parametres
        ----------
        coords : ndarray
            Coordonnées du port
        echange : ndarray
            Echanges de ressources possibles pour ce type de port
        """

        self.coords = coords
        self.echange = np.array([])

class CarteDeveloppement():
    """
    Classe représentant une carte développement, mère des types de telles cartes.

    Attributs
    ---------
    joueur : Joueur
        joueur possédant la carte développement
    coût : ndarray
        prix d'une carte développement
    """

    def __init__(self, joueur):
        """
        Parametres
        ----------
        joueur : Joueur
            Joueur possédant la carte développement
        """

        self.joueur = joueur
        self.coût = np.array([0,0,1,1,1])

    def effet(self):
        """
        Affiche l'effet d'une carte développement

        Parametres
        ----------
        aucun
        """

        print("No Effect")

    #Check if player has the greatest army    

class DevConstructionDeRoutes(CarteDeveloppement):
    """
    Classe représentant une carte construction de route, fille de CarteDeveloppement.
    """

    def __init__(self, joueur):
        """
        Parametres
        ----------
        joueur : Joueur
            Joueur possédant la carte construction de route
        """
        super().__init__(joueur)
    
class DevMonopole(CarteDeveloppement):
    """
    Classe représentant une carte monopole, fille de CarteDeveloppement.
    """

    def __init__(self, joueur):
        """
        Parametres
        ----------
        joueur : Joueur
            Joueur possédant la carte monopole
        """
        super().__init__(joueur)

class DevInvention(CarteDeveloppement):
    """
    Classe représentant une carte invention, fille de CarteDeveloppement.
    """
    def __init__(self, joueur):
        """
        Parametres
        ----------
        joueur : Joueur
            Joueur possédant la carte invention
        """
        super().__init__(joueur)

class DevPV(CarteDeveloppement):
    """
    Classe représentant une carte point de victoire, fille de CarteDeveloppement.
    """
    def __init__(self, joueur):
        """
        Parametres
        ----------
        joueur : Joueur
            Joueur possédant la carte point de victoire
        """
        super().__init__(joueur)

class DevChevalier(CarteDeveloppement):
    """
    Classe représentant une carte chevalier, fille de CarteDeveloppement.
    """
    def __init__(self, joueur):
        """
        Parametres
        ----------
        joueur : Joueur
            Joueur possédant la carte chevalier
        """
        super().__init__(joueur)

class Pioche():
    """
    Classe représentant la pioche.

    Attributs
    ---------
    wheatRessources : int
        nombre de cartes ressource de blé restantes dans la pioche
    woodRessources : int
        nombre de cartes ressource de bois restantes dans la pioche
    woolRessources : int
        nombre de cartes ressource de laine restantes dans la pioche
    clayRessources : int
        nombre de cartes ressource d'argile restantes dans la pioche
    stoneRessources : int
        nombre de cartes ressource de pierre restantes dans la pioche
    devCards : list
        liste des cartes développement dans la pioche, remplie aléatoirement
    """

    def __init__(self):
        """
        Parametres
        ----------
        aucun
        """
        self.wheatRessources = 19
        self.woodRessources = 19
        self.woolRessources = 19
        self.clayRessources = 19
        self.stoneRessources = 19
        self.devCards = [DevConstructionDeRoutes(""), DevConstructionDeRoutes(""), DevInvention(""), DevInvention(""), DevMonopole(""), DevMonopole("")]
        for i in range(14):
            self.devCards.append(DevChevalier(""))
            if i < 5:
                self.devCards.append(DevPV(""))
        rd.shuffle(self.devCards)