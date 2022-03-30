import random as rd

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


P = Pioche()
#print(P.devCards)
Lcoords = [(i,j) for i in range(-2,3) for j in range (-2,3) if abs(i+j)<3]
Lcoords = [(i,j) for i in range(-2,3) for j in range (-2,3) if abs(i+j)<=3 and abs(i)+abs(j)<=3 and not(abs(i)>0 and j==-2)]
print(Lcoords)
print(len(Lcoords))
