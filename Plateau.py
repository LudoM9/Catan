from abc import abstractmethod, ABCMeta
from numpy.random import randint
import random as rd


class Plateau():
    def __init__(self, rdPlateau = False):
        self.tiles = [WoodTile(self, (-2,-1), 6), WoolTile(self, (-1,-1), 3), WoolTile(self, (0,-2), 8), WheatTile(self, (-2,0), 2), StoneTile(self, (-1,0), 4), WheatTile(self, (0,-1), 5), WoodTile(self, (1,-1), 10), WoodTile(self, (-2,1), 5), ClayTile(self, (-1,1), 9), DesertTile(self, (0,0), 7), StoneTile(self, (1,0), 6), WheatTile(self, (2,-1), 9), WheatTile(self, (-1,2), 10), StoneTile(self, (0,1), 11), WoodTile(self, (1,1), 3), WoolTile(self, (2,0), 12), ClayTile(self, (0,2), 8), WoolTile(self, (1,2), 4), ClayTile(self, (2,1), 11)]
        self.intersections = []
        self.routes = []
        self.ports = []
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
    

class Tile(metaclass = ABCMeta):
    def __init__(self, plateau, coords, value):
        self.plateau = plateau
        self.coords = coords
        self.value = value
        self.type = ""
        self.color = ""

class WoodTile(Tile):
    def __init__(self, plateau, coords, value):
        super.__init__(plateau, coords, value)
        self.type = "Wood"
        self.color = 0x33855d

class WheatTile(Tile):
    def __init__(self, plateau, coords, value):
        super.__init__(plateau, coords, value)
        self.type = "Wheat"
        self.color = 0xffff00

class WoolTile(Tile):
    def __init__(self, plateau, coords, value):
        super.__init__(plateau, coords, value)
        self.type = "Wool"
        self.color = 0xf5f5f5

class ClayTile(Tile):
    def __init__(self, plateau, coords, value):
        super.__init__(plateau, coords, value)
        self.type = "Clay"
        self.color = 0xd2691e

class StoneTile(Tile):
    def __init__(self, plateau, coords, value):
        super.__init__(plateau, coords, value)
        self.type = "Stone"
        self.color = 0xa9a9a9

class DesertTile(Tile):
    def __init__(self, plateau, coords, value):
        super.__init__(plateau, coords, value)
        self.type = "Desert"
        self.color = 0xf0e68c

class Dices():
    def __init__(self):
        self.value = 0

class Ressource():
    def __init__(self):
        self.type = ""

class Colonie():
    def __init__(self):
        self.joueur = ""
        self.coords = []
        self.adjacent = []
        self.multiplicateur = 1
        self.__coût = [1,1,1,1,0]

class Ville(Colonie):
    def __init__(self):
        super.__init__(self)
        self.multiplicateur = 2
        self.__coût = [0,0,0,2,3]

class Route():
    def __init__(self):
        self.joueur = ""
        self.coords = []
        self.__coût = [1,1,0,0,0]
    
    #Check if player has now the longest road

class Voleur():
    def __init__(self):
        self.coords = []

class Port():
    def __init__(self):
        self.coords = []
        self.joueur = ""
        self.echange = []

class CarteDeveloppement():
    def __init__(self, joueur):
        self.joueur = joueur
        self.__coût = [0,0,1,1,1]

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