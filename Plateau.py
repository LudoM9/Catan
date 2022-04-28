from abc import abstractmethod, ABCMeta
from numpy.random import randint
import random as rd
import numpy as np


class Plateau():
    def __init__(self, rdPlateau = False):
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
    
    # NE PAS TOUCHER ABSOLUMENT (FONCTIONNE PARFAITEMENT)
    def getAdjacentTilesFromTile(self, tile):
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

    # NE PAS TOUCHER ABSOLUMENT (FONCTIONNE PARFAITEMENT)
    def getAdjacentTilesFromVertice(self, vertice):
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

    # NE PAS TOUCHER ABSOLUMENT (FONCTIONNE PARFAITEMENT)
    def getVerticesFromTile(self, tile):
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

    # NE PAS TOUCHER ABSOLUMENT (FONCTIONNE PARFAITEMENT)
    def getEdgesFromTile(self, tile):
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

    # NE PAS TOUCHER ABSOLUMENT (FONCTIONNE PARFAITEMENT)
    def getAdjacentVerticesFromVertice(self, vertice):
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
    

    # NE PAS TOUCHER ABSOLUMENT (FONCTIONNE PARFAITEMENT)
    def getAdjacentEdgesFromVertice(self, vertice):
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

    # NE PAS TOUCHER ABSOLUMENT (FONCTIONNE PARFAITEMENT)
    def getVerticesOfEdge(self, edge):
        x = edge[0]
        y = edge[1]
        vertice1 = (int((x-1)/2), y)
        vertice2 = (int((x+1)/2), y)
        if x%2 == 0:
          vertice1 = (int(x/2), y)
          vertice2 = (int(x/2), y+1)
        return [vertice1, vertice2]

    # NE PAS TOUCHER ABSOLUMENT (FONCTIONNE PARFAITEMENT)
    def getAdjacentEdgesFromEdge(self, edge):
        adjEdges = []
        vertices = self.getVerticesOfEdge(edge)
        for vertice in vertices:
            adjEdges += self.getAdjacentEdgesFromVertice(vertice)
            adjEdges = list(set(adjEdges))
        adjEdges.remove(edge)
        return adjEdges


    def intersectionDispoConstruction(self, coords):
        for elem in self.intersections:             #elem = Villes et colonies
            if coords == elem.coords:
                return False
            elif elem.coords in self.getAdjacentVerticesFromVertice(self, coords):
                return False
        return True

    def routeDispoConstruction(self, coords):
        for route in self.routes:
            if coords == route.coords:
                return False
        return True

    def routeAdjacenteRouteExiste(self, joueur, coords):
        for route in self.routes:
            if route.joueur == joueur:
                if route.coords in self.getAdjacentEdgesFromEdge(coords):
                    return True
        return False

    def colonieAdjacenteRouteExiste(self, joueur, coords):
        for elem in self.intersections:
            if elem.joueur == joueur:
                if elem.coords in self.getVerticesOfEdge(coords):
                    return True
        return False

    def routeAdjacenteColonieExiste(self, joueur, coords):
        for elem in self.intersections:
            if elem.joueur == joueur:
                if elem.coords in self.getAdjacentEdgesFromVertice(coords):
                    return True
        return False

    def colonieAdjacenteTile(self, coords):
        elems = []
        for elem in self.intersections:
            if elem.coords in self.getVerticesFromTile(coords):
                elems.append(elem)
        return elems

class Tile(metaclass = ABCMeta):
    def __init__(self, plateau, coords, value):
        self.plateau = plateau
        self.coords = coords
        self.value = value
        self.ressource = np.array([0,0,0,0,0])
        self.color = ""

class WoodTile(Tile):
    def __init__(self, plateau, coords, value):
        super().__init__(plateau, coords, value)
        self.ressource = np.array([1,0,0,0,0])
        self.color = 0x33855d

class WheatTile(Tile):
    def __init__(self, plateau, coords, value):
        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,0,0,1,0])
        self.color = 0xffff00

class WoolTile(Tile):
    def __init__(self, plateau, coords, value):
        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,0,1,0,0])
        self.color = 0xf5f5f5

class ClayTile(Tile):
    def __init__(self, plateau, coords, value):
        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,1,0,0,0])
        self.color = 0xd2691e

class StoneTile(Tile):
    def __init__(self, plateau, coords, value):
        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,0,0,0,1])
        self.color = 0xa9a9a9

class DesertTile(Tile):
    def __init__(self, plateau, coords, value):
        super().__init__(plateau, coords, value)
        self.ressource = np.array([0,0,0,0,0])
        self.color = 0xf0e68c

class Colonie():
    def __init__(self, joueur, coords):
        self.joueur = joueur
        self.coords = coords
        self.adjacent = []
        self.multiplicateur = 1
        self.coût = np.array([1,1,1,1,0])

class Ville(Colonie):
    def __init__(self, joueur, coords):
        super().__init__(self, joueur, coords)
        self.multiplicateur = 2
        self.coût = np.array([0,0,0,2,3])

class Route():
    def __init__(self, joueur, coords):
        self.joueur = joueur
        self.coords = coords
        self.coût = np.array([1,1,0,0,0])
    
    #Check if player has now the longest road

class Voleur():
    def __init__(self, coords):
        self.coords = coords

class Port():
    def __init__(self, coords, echange):
        self.coords = 0
        self.echange = np.array([])

class CarteDeveloppement():
    def __init__(self, joueur):
        self.joueur = joueur
        self.coût = np.array([0,0,1,1,1])

    def effet():
        print("No Effect")

    #Check if player has the greatest army    

class DevConstructionDeRoutes(CarteDeveloppement):
    def __init__(self, joueur):
        super().__init__(joueur)
    
class DevMonopole(CarteDeveloppement):
    def __init__(self, joueur):
        super().__init__(joueur)

class DevInvention(CarteDeveloppement):
    def __init__(self, joueur):
        super().__init__(joueur)

class DevPV(CarteDeveloppement):
    def __init__(self, joueur):
        super().__init__(joueur)

class DevChevalier(CarteDeveloppement):    
    def __init__(self, joueur):
        super().__init__(joueur)

class Pioche():
    def __init__(self):
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