
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

class CarteDeveloppement():
    def __init__(self):
        self.joueur = ""
        self.coût = []
        self.type = []

class Voleur():
    def __init__(self):
        self.coords = []

class Port():
    def __init__(self):
        self.coords = []
        self.joueur = ""
        self.echange = []