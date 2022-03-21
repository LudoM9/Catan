from abc import abstractmethod, ABCMeta
from numpy.random import randint

class Plateau():
    def __init__(self):
        self.tiles = []
        self.intersections = []
        self.routes = []

class Tile(metaclass = ABCMeta):
    def __init__(self):
        self.plateau = []
        self.coords = []
        self.value = 0
        self.type = ""
        self.color = ""

class WoodTile(Tile):
    def __init__(self):
        super.__init__(self)
        self.type = "Wood"
        self.color = 0x33855d

class WheatTile(Tile):
    def __init__(self):
        super.__init__(self)
        self.type = "Wheat"
        self.color = 0xffff00

class WoolTile(Tile):
    def __init__(self):
        super.__init__(self)
        self.type = "Wool"
        self.color = 0xf5f5f5

class ClayTile(Tile):
    def __init__(self):
        super.__init__(self)
        self.type = "Clay"
        self.color = 0xd2691e

class StoneTile(Tile):
    def __init__(self):
        super.__init__(self)
        self.type = "Stone"
        self.color = 0xa9a9a9

class DesertTile(Tile):
    def __init__(self):
        super.__init__(self)
        self.type = "Desert"
        self.color = 0xf0e68c

class Dices():
    def __init__(self):
        self.value = 0
    

