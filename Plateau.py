from abc import abstractmethod, ABCMeta
from numpy.random import randint
import random as rd


class Plateau():
    def __init__(self, rdPlateau = False):
        self.tiles = [WoodTile(self, 1, 6), WoolTile(self, 2, 3), WoolTile(self, 3, 8), WheatTile(self, 4, 2), StoneTile(self, 5, 4), WheatTile(self, 6, 5), WoodTile(self, 7, 10), WoodTile(self, 8, 5), ClayTile(self, 9, 9), DesertTile(self, 10, 7), StoneTile(self, 11, 6), WheatTile(self, 12, 9), WheatTile(self, 13, 10), StoneTile(self, 14, 11), WoodTile(self, 15, 3), WoolTile(self, 16, 12), ClayTile(self, 17, 8), WoolTile(self, 18, 4), ClayTile(self, 19, 11)]
        self.intersections = []
        self.routes = []
        if rdPlateau:
            Lindices = [i for i in range(1,7)] + [i for i in range(8,20)]
            rd.shuffle(Lindices)
            Lindices += [7]
            Lindices[18],Lindices[9] = Lindices[9], 7
            Lvalues = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
            rd.shuffle(Lvalues)
            Lvalues += [7]
            Lvalues[18],Lvalues[9] = Lvalues[9], 7
            Ltiles = []
            self.tiles = []

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
        self.coût = []

class Ville(Colonie):
    def __init__(self):
        super.__init__(self)
        self.multiplicateur = 2
        self.coût = []

class Route():
    def __init__(self):
        self.joueur = ""
        self.coords = []
        self.coût = []

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
        self.coût = []

    def effet():
        print("No Effect")

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