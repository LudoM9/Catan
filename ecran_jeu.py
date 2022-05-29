import pygame, os
from pygame.locals import *
import constantes as cst
import fonctions as fct
import numpy as np

pygame.font.init()
Broadwfont = pygame.font.Font(os.path.join('fonts', 'BROADW.TTF'), 30)
basefont = pygame.font.Font(None, 100)
echangefont = pygame.font.Font(None, 40)

NEXTTURN = pygame.image.load(os.path.join('images', 'TourSuivant.png'))
BRICK = pygame.image.load(os.path.join('images', 'Brick Image.png'))
STONE = pygame.image.load(os.path.join('images', 'Stone Image.png'))
WHEAT = pygame.image.load(os.path.join('images', 'Wheat Image.png'))
WOOD = pygame.image.load(os.path.join('images', 'Wood Image.png'))
WOOL = pygame.image.load(os.path.join('images', 'Wool Image.png'))
PV = pygame.image.load(os.path.join('images', 'PV Image.png'))
BACKGROUNDUI = pygame.image.load(os.path.join('images', 'BackgroundUI.jpg'))
CERCLE = pygame.image.load(os.path.join('images','cercle.png'))

COLONIE = pygame.image.load(os.path.join('images', 'Colonie.png'))
VILLE = pygame.image.load(os.path.join('images', 'Ville.png'))
ROUTE = pygame.image.load(os.path.join('images', 'Route.png'))
CARTEDEV = pygame.image.load(os.path.join('images', 'CarteDev.png'))
ANNULER = pygame.image.load(os.path.join('images', 'Annuler.png'))
ECHANGEBANQUE = pygame.image.load(os.path.join('images', 'EchangeBanque.png'))
ECHANGEJOUEURS = pygame.image.load(os.path.join('images', 'EchangeJoueurs.png'))

COLONIE_J1 = pygame.image.load(os.path.join('images', 'Colonie_J1.png'))
COLONIE_J2 = pygame.image.load(os.path.join('images', 'Colonie_J2.png'))
COLONIE_J3 = pygame.image.load(os.path.join('images', 'Colonie_J3.png'))
COLONIE_J4 = pygame.image.load(os.path.join('images', 'Colonie_J4.png'))
VILLE_J1 = pygame.image.load(os.path.join('images', 'Ville_J1.png'))
VILLE_J2 = pygame.image.load(os.path.join('images', 'Ville_J2.png'))
VILLE_J3 = pygame.image.load(os.path.join('images', 'Ville_J3.png'))
VILLE_J4 = pygame.image.load(os.path.join('images', 'Ville_J4.png'))

VALIDER_ON = pygame.image.load(os.path.join('images', 'Valider_ON.png'))
VALIDER_OFF = pygame.image.load(os.path.join('images', 'Valider_OFF.png'))

CARTEDEV_CHEVALIER = pygame.image.load(os.path.join('images', 'CarteDevChevalier.png'))
CARTEDEV_INVENTION = pygame.image.load(os.path.join('images', 'CarteDevInvention.png'))
CARTEDEV_MONOPOLE = pygame.image.load(os.path.join('images', 'CarteDevMonopole.png'))
CARTEDEV_ROUTES = pygame.image.load(os.path.join('images', 'CarteDevRoutes.png'))

NB_CHEVALIER = pygame.image.load(os.path.join('images', 'NbChevalier.png'))
NB_ROUTES = pygame.image.load(os.path.join('images', 'NbRoutes.png'))

RECT_MAIN = pygame.Rect(0, 0, 0, 0)
RECT_NEXTTURN = pygame.Rect(0, 0, 0, 0)
RECT_BRICKIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_STONEIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_WHEATIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_WOODIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_WOOLIMAGE = pygame.Rect(0, 0, 0, 0)
RECT_PVIMAGE = pygame.Rect(0, 0, 0, 0)

RECTS_TILES = []
for t in range(19):
    RECTS_TILES.append(pygame.Rect(0,0,0,0))
RECTS_VERTICES = []
for v in range(54):
    RECTS_VERTICES.append(pygame.Rect(0,0,0,0))
RECTS_EDGES = []
for e in range(74):
    RECTS_EDGES.append(pygame.Rect(0,0,0,0))

RECT_COLONIE = pygame.Rect(0, 0, 0, 0)
RECT_VILLE = pygame.Rect(0, 0, 0, 0)
RECT_ROUTE = pygame.Rect(0, 0, 0, 0)
RECT_CARTEDEV = pygame.Rect(0, 0, 0, 0)
RECT_ANNULER = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGEBANQUE = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGEJOUEURS = pygame.Rect(0, 0, 0, 0)

RECT_ECHANGE_BRICK = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_STONE = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_WHEAT = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_WOOD = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_WOOL = pygame.Rect(0, 0, 0, 0)

RECT_ECHANGE_BRICK2 = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_STONE2 = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_WHEAT2 = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_WOOD2 = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_WOOL2 = pygame.Rect(0, 0, 0, 0)

RECT_ECHANGE_VALIDER = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_VALIDERJ1 = pygame.Rect(0, 0, 0, 0)
RECT_ECHANGE_VALIDERJ2 = pygame.Rect(0, 0, 0, 0)

RECT_CARTEDEV_ROUTES = pygame.Rect(0, 0, 0, 0)
RECT_CARTEDEV_INVENTION = pygame.Rect(0, 0, 0, 0)
RECT_CARTEDEV_MONOPOLE = pygame.Rect(0, 0, 0, 0)
RECT_CARTEDEV_CHEVALIER = pygame.Rect(0, 0, 0, 0)

RECT_CARTEDEV_BRICK = pygame.Rect(0, 0, 0, 0)
RECT_CARTEDEV_STONE = pygame.Rect(0, 0, 0, 0)
RECT_CARTEDEV_WHEAT = pygame.Rect(0, 0, 0, 0)
RECT_CARTEDEV_WOOD = pygame.Rect(0, 0, 0, 0)
RECT_CARTEDEV_WOOL = pygame.Rect(0, 0, 0, 0)

RECT_ECHANGE_JOUEURS = []
for j in range(3):
    RECT_ECHANGE_JOUEURS.append(pygame.Rect(0, 0, 0, 0))

RECT_PORT = pygame.Rect(0, 0, 0, 0)

def main(catan):
    global RECT_MAIN, RECT_NEXTTURN, RECT_BRICKIMAGE, RECT_STONEIMAGE, RECT_WHEATIMAGE, RECT_WOODIMAGE, RECT_WOOLIMAGE, RECT_PVIMAGE, RECT_COLONIE, RECT_VILLE, RECT_ROUTE, RECT_CARTEDEV, RECT_ANNULER, RECT_ECHANGEBANQUE, RECT_ECHANGEJOUEURS, RECTS_TILES, RECTS_VERTICES, RECTS_EDGES, RECT_ECHANGE_BRICK, RECT_ECHANGE_STONE, RECT_ECHANGE_WHEAT, RECT_ECHANGE_WOOD, RECT_ECHANGE_WOOL, RECT_ECHANGE_BRICK2, RECT_ECHANGE_STONE2, RECT_ECHANGE_WHEAT2, RECT_ECHANGE_WOOD2, RECT_ECHANGE_WOOL2, RECT_ECHANGE_VALIDER, RECT_ECHANGE_VALIDERJ1, RECT_ECHANGE_VALIDERJ2, RECT_ECHANGE_JOUEURS, RECT_CARTEDEV_ROUTES, RECT_CARTEDEV_INVENTION, RECT_CARTEDEV_MONOPOLE, RECT_CARTEDEV_CHEVALIER, RECT_CARTEDEV_BRICK, RECT_CARTEDEV_STONE, RECT_CARTEDEV_WHEAT, RECT_CARTEDEV_WOOD, RECT_CARTEDEV_WOOL, RECT_PORT

    run = True
    startingColonie = True
    startingRoute = False
    game = False
    constructionColonie = False
    constructionVille = False
    constructionRoute = False
    carteDeveloppement = False
    echangeBanque = False
    choixEchangeJoueurs = False
    echangeJoueurs = False
    indicText = False
    xoffset = 5
    yoffset = 5

    textBrick = '0'
    textStone = '0'
    textWheat = '0'
    textWood = '0'
    textWool = '0'
    activeTextBrick = False
    activeTextStone = False
    activeTextWheat = False
    activeTextWood = False
    activeTextWool = False

    textBrick2 = '0'
    textStone2 = '0'
    textWheat2 = '0'
    textWood2 = '0'
    textWool2 = '0'
    activeTextBrick2 = False
    activeTextStone2 = False
    activeTextWheat2 = False
    activeTextWood2 = False
    activeTextWool2 = False

    textInfo = ''
    validerJ1 = False
    validerJ2 = False

    numeroJoueurEchange = 0

    deplacerVoleur = False

    carteDevConstructionRoute = False
    carteDevMonopole = False
    carteDevInvention = False
    nbRouteGratuite = 0
    nbRessourceRecup = 0

    portOn = True

    l = np.round(cst.h / 12)
    c = np.round(l/2 * 3 ** (1 / 3))
    positions = np.array([(3*c,l),(5*c,l),(7*c,l),
                 		(2*c,5*l//2),(4*c,5*l//2),(6*c,5*l//2),(8*c,5*l//2),
                 		(c,4*l),(3*c,4*l),(5*c,4*l),(7*c,4*l),(9*c,4*l),
                 		(2*c,11*l//2),(4*c,11*l//2),(6*c,11*l//2),(8*c,11*l//2),
                 			(3*c,7*l),(5*c,7*l),(7*c,7*l)])
    hexagons = [tile.color for tile in catan.plateau.tiles]
    numbers = [tile.value for tile in catan.plateau.tiles]

    hexagon_coords =     [(-2,-1), (-1,-1), (0,-2),
                       (-2,0), (-1,0), (0,-1), (1,-1),
                     (-2,1), (-1,1), (0,0), (1,0), (2,-1),
                       (-1,2), (0,1),  (1,1),  (2,0),
                          (0,2),   (1,2),   (2,1)]

    vertices_coords = []
    edges_coords = []
    for tile_coord in hexagon_coords:
        for vertice_coord in catan.plateau.getVerticesFromTile(tile_coord):
            if vertice_coord not in vertices_coords:
                vertices_coords.append(vertice_coord)
        for edge_coord in catan.plateau.getEdgesFromTile(tile_coord):
            if edge_coord not in edges_coords:
                edges_coords.append(edge_coord)

    vertices=[]
    V=np.array([(0, -l),(-c,-l//2),(-c,l//2),(c,-l//2),(c,l//2),(0,l)])
    for i,t in enumerate(positions):
        for j in range(6):
            v=(positions[i][0] + V[j][0],positions[i][1] + V[j][1])
            if v not in vertices:
                vertices.append(v)
    #vertices=np.array([(x, y-l),(x+c,y-l//2),(x+c,y+l//2),(x,y+l),(x-c,y+l//2),(x-c,y-l//2)])
    vertices_available = [True for i in range(len(vertices))]

    edges=[]
    E=np.array([(-c//2,-3*l//4),(-c,0),(c//2,-3*l//4),(-c//2,3*l//4),(c,0),(c//2,3*l//4)])
    for i, t in enumerate(positions):
        for j in range(6):
            e = (positions[i][0] + E[j][0],positions[i][1] + E[j][1])
            if e not in edges:
                edges.append(e)
    #edges=np.array([(x+c//2,y-3*l//4),(x+c,y),(x+c//2,y+3*l//4),(x-c//2,y+3*l//4),(x-c,y),(x-c//2,y-3*l//4)])
    edges_available = [False for i in range(len(edges))]

    while run:
        pygame.time.Clock().tick(30)
        resetRect()
        
        joueurActuel = catan.joueurActuel
        if joueurActuel.numero == 0:
            color = cst.couleurj1
        elif joueurActuel.numero == 1:
            color = cst.couleurj2
        elif joueurActuel.numero == 2:
            color = cst.couleurj3
        elif joueurActuel.numero == 3:
            color = cst.couleurj4
        playerTextsurface = basefont.render(joueurActuel.nom, False, color)

        cst.fenetre.fill((0,191,255))
        pygame.draw.rect(cst.fenetre, (211,211,211), Rect(0, 3*cst.h/4, cst.w, cst.h/4))

        fct.drawImageTopLeft((xoffset,0), playerTextsurface, 0.035)

        fct.drawImageTopLeft((xoffset,3*cst.h/4 + yoffset), BRICK, 0.05)
        fct.drawImageTopLeft((xoffset,3*cst.h/4+(1/3)*cst.h/4 + yoffset), STONE, 0.05)
        fct.drawImageTopLeft((xoffset,3*cst.h/4+(2/3)*cst.h/4 + yoffset), WHEAT, 0.05)
        fct.drawImageTopLeft((80+xoffset,3*cst.h/4 + yoffset), WOOD, 0.05)
        fct.drawImageTopLeft((80+xoffset,3*cst.h/4+(1/3)*cst.h/4 + yoffset), WOOL, 0.05)
        fct.drawImageTopLeft((80+xoffset,3*cst.h/4+(2/3)*cst.h/4 + yoffset), PV, 0.05)
        RECT_BRICKIMAGE = fct.rectDrawImageTopLeft((xoffset,3*cst.h/4 + yoffset), BRICK, 0.05)
        RECT_STONEIMAGE = fct.rectDrawImageTopLeft((xoffset,3*cst.h/4+(1/3)*cst.h/4 + yoffset), STONE, 0.05)
        RECT_WHEATIMAGE = fct.rectDrawImageTopLeft((xoffset,3*cst.h/4+(2/3)*cst.h/4 + yoffset), WHEAT, 0.05)
        RECT_WOODIMAGE = fct.rectDrawImageTopLeft((80+xoffset,3*cst.h/4 + yoffset), WOOD, 0.05)
        RECT_WOOLIMAGE = fct.rectDrawImageTopLeft((80+xoffset,3*cst.h/4+(1/3)*cst.h/4 + yoffset), WOOL, 0.05)
        RECT_PVIMAGE = fct.rectDrawImageTopLeft((80+xoffset,3*cst.h/4+(2/3)*cst.h/4 + yoffset), PV, 0.05)

        brickTextsurface = basefont.render(str(joueurActuel.ressource[1]), False, (0,0,0))
        stoneTextsurface = basefont.render(str(joueurActuel.ressource[4]), False, (0,0,0))
        wheatTextsurface = basefont.render(str(joueurActuel.ressource[3]), False, (0,0,0))
        woodTextsurface = basefont.render(str(joueurActuel.ressource[0]), False, (0,0,0))
        woolTextsurface = basefont.render(str(joueurActuel.ressource[2]), False, (0,0,0))
        pvTextsurface = basefont.render(str(joueurActuel.pointsVictoire), False, (0,0,0))
        fct.drawImageMidLeft(RECT_BRICKIMAGE.midright, brickTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_STONEIMAGE.midright, stoneTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_WHEATIMAGE.midright, wheatTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_WOODIMAGE.midright, woodTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_WOOLIMAGE.midright, woolTextsurface, 0.035)
        fct.drawImageMidLeft(RECT_PVIMAGE.midright, pvTextsurface, 0.035)
        
        for i in range(19):
            fct.drawHexagon(hexagons[i], positions[i], numbers[i]) #construction des hexagones, chemins et numéros sur les tuiles
            #fct.drawImage((positions[i][0]+cst.xoff,positions[i][1]+cst.yoff),CERCLE,0.04)

        for i, hexagon_coord in enumerate(hexagon_coords):
            if catan.plateau.voleur.coords == hexagon_coord:
                rect = Rect((positions[i][0]+cst.xoff, positions[i][1]+cst.yoff), (40,40))
                rect.center = (positions[i][0]+cst.xoff, positions[i][1]+cst.yoff)
                pygame.draw.rect(cst.fenetre, (0,0,0), rect)
                voleurTextsurface = basefont.render("V", False, (255,255,255))
                fct.drawImage((positions[i][0]+cst.xoff, positions[i][1]+cst.yoff), voleurTextsurface, 0.035)

        for elem in catan.plateau.intersections:
            for i, vertice_coord in enumerate(vertices_coords):
                if elem.coords == vertice_coord:
                    if elem.multiplicateur == 1:
                        drawColonie((vertices[i][0]+cst.xoff,vertices[i][1]+cst.yoff), elem.joueur.numero)
                    elif elem.multiplicateur == 2:
                        drawVille((vertices[i][0]+cst.xoff,vertices[i][1]+cst.yoff), elem.joueur.numero)

        for route in catan.plateau.routes:
            for i, edge_coord in enumerate(edges_coords):
                if route.coords == edge_coord:
                    rect = Rect((edges[i][0]+cst.xoff,edges[i][1]+cst.yoff),(20,20))
                    rect.center = (edges[i][0]+cst.xoff,edges[i][1]+cst.yoff)
                    if route.joueur.numero == 0:
                        roadColor = cst.couleurj1
                    elif route.joueur.numero == 1:
                        roadColor = cst.couleurj2
                    elif route.joueur.numero == 2:
                        roadColor = cst.couleurj3
                    elif route.joueur.numero == 3:
                        roadColor = cst.couleurj4
                    pygame.draw.rect(cst.fenetre, roadColor, rect)
        if portOn:
            for port in catan.plateau.ports:
                for i, vertice_coord in enumerate(vertices_coords):
                    if port.coords == vertice_coord:
                        x = port.coords[0]
                        y = port.coords[1]
                        if x == -2:
                            drawPort((vertices[i][0]+cst.xoff,vertices[i][1]+cst.yoff), port, "W")
                        elif y == -3 and (y==0 or y==-1):
                            drawPort((vertices[i][0]+cst.xoff,vertices[i][1]+cst.yoff), port, "N")
                        elif x == 3 or y==-3:
                            drawPort((vertices[i][0]+cst.xoff,vertices[i][1]+cst.yoff), port, "E")
                        elif x == 2 or y == 6:
                            drawPort((vertices[i][0]+cst.xoff,vertices[i][1]+cst.yoff), port, "S")
                        elif x == -1:
                            drawPort((vertices[i][0]+cst.xoff,vertices[i][1]+cst.yoff), port, "W")

        if startingColonie or constructionColonie:
            if startingColonie:
                IndicTextsurface = basefont.render("Placez votre colonie", False, (0,0,0))
                fct.drawImageTopRight((cst.w-xoffset, yoffset), IndicTextsurface, 0.04)
            for i in range(len(vertices)):
                if vertices_available[i]:
                    rect = Rect((vertices[i][0]+cst.xoff,vertices[i][1]+cst.yoff),(20,20))
                    rect.center = (vertices[i][0]+cst.xoff,vertices[i][1]+cst.yoff)
                    pygame.draw.rect(cst.fenetre, (255,102,255), rect)
                    RECTS_VERTICES[i] = rect

        if startingRoute or constructionRoute or carteDevConstructionRoute:
            if startingRoute:
                IndicTextsurface = basefont.render("Placez vos routes", False, (0,0,0))
                fct.drawImageTopRight((cst.w-xoffset, yoffset), IndicTextsurface, 0.04)
            for i, coord in enumerate(edges_coords):
                for route in joueurActuel.routes:
                    if coord in catan.plateau.getAdjacentEdgesFromEdge(route.coords):
                        edges_available[i] = True
                for colonie in joueurActuel.colonies:
                    if coord in catan.plateau.getAdjacentEdgesFromVertice(colonie.coords):
                        edges_available[i] = True
            for i, coord in enumerate(edges_coords):
                for route in catan.plateau.routes:
                    if coord == route.coords:
                        edges_available[i] = False
            for i in range(len(edges)):
                if edges_available[i]:
                    rect = Rect((edges[i][0]+cst.xoff,edges[i][1]+cst.yoff),(20,20))
                    rect.center = (edges[i][0]+cst.xoff,edges[i][1]+cst.yoff)
                    pygame.draw.rect(cst.fenetre, (255,102,255), rect)
                    RECTS_EDGES[i] = rect

        if game:
            fct.drawImageTopRight((cst.w-xoffset, 3*cst.h/4+yoffset), VILLE, 0.08)
            RECT_VILLE = fct.rectDrawImageTopRight((cst.w-xoffset, 3*cst.h/4+yoffset), VILLE, 0.08)
            fct.drawImageTopRight((RECT_VILLE.left-xoffset, 3*cst.h/4+yoffset), COLONIE, 0.08)
            RECT_COLONIE = fct.rectDrawImageTopRight((RECT_VILLE.left-xoffset, 3*cst.h/4+yoffset), COLONIE, 0.08)
            fct.drawImageTopRight((cst.w-xoffset, RECT_VILLE.bottom+yoffset), CARTEDEV, 0.08)
            RECT_CARTEDEV = fct.rectDrawImageTopRight((cst.w-xoffset, RECT_VILLE.bottom+yoffset), CARTEDEV, 0.08)
            fct.drawImageTopRight((RECT_VILLE.left-xoffset, RECT_VILLE.bottom+yoffset), ROUTE, 0.08)
            RECT_ROUTE = fct.rectDrawImageTopRight((RECT_VILLE.left-xoffset, RECT_VILLE.bottom+yoffset), ROUTE, 0.08)
            fct.drawImageTopRight((RECT_COLONIE.left-xoffset, 3*cst.h/4+yoffset), ECHANGEBANQUE, 0.08)
            RECT_ECHANGEBANQUE = fct.rectDrawImageTopRight((RECT_COLONIE.left-xoffset, 3*cst.h/4+yoffset), ECHANGEBANQUE, 0.08)
            fct.drawImageTopRight((RECT_COLONIE.left-xoffset, RECT_COLONIE.bottom+yoffset), ECHANGEJOUEURS, 0.08)
            RECT_ECHANGEJOUEURS = fct.rectDrawImageTopRight((RECT_COLONIE.left-xoffset, RECT_COLONIE.bottom+yoffset), ECHANGEJOUEURS, 0.08)
            fct.drawImageTopRight((cst.w, 0), NEXTTURN, 0.05)
            RECT_NEXTTURN = fct.rectDrawImageTopRight((cst.w, 0), NEXTTURN, 0.05)
            diceTextsurface = basefont.render("Résultat dés : " + str(catan.valeurDes), False, (0,0,0))
            fct.drawImageTopRight((RECT_NEXTTURN.left-xoffset, yoffset), diceTextsurface, 0.035)
            rectDiceText = fct.rectDrawImageTopRight((RECT_NEXTTURN.left-xoffset, yoffset), diceTextsurface, 0.035)

            if portOn:
                fct.drawImageMidRight((rectDiceText.left-3*xoffset, rectDiceText.centery), VALIDER_ON, 0.035)
                RECT_PORT = fct.rectDrawImageMidRight((rectDiceText.left-3*xoffset, rectDiceText.centery), VALIDER_ON, 0.035)
            else:
                fct.drawImageMidRight((rectDiceText.left-3*xoffset, rectDiceText.centery), VALIDER_OFF, 0.035)
                RECT_PORT = fct.rectDrawImageMidRight((rectDiceText.left-3*xoffset, rectDiceText.centery), VALIDER_ON, 0.035)
            portTextsurface = basefont.render("Ports : ", False, (0,0,0))
            fct.drawImageTopRight((RECT_PORT.left, yoffset), portTextsurface, 0.035)

            nbChevalierTextsurface = basefont.render(": " + str(joueurActuel.nbChevalier), False, (0,0,0))
            fct.drawImageBotRight((cst.w-cst.xoff, 3*cst.h/4-cst.yoff/2), nbChevalierTextsurface, 0.035)
            rectNbChevalier = fct.rectDrawImageBotRight((cst.w-cst.xoff, 3*cst.h/4-cst.yoff/2), nbChevalierTextsurface, 0.035)
            fct.drawImageBotRight(rectNbChevalier.bottomleft, NB_CHEVALIER, 0.05)
            rectNbChevalier = fct.rectDrawImageBotRight(rectNbChevalier.bottomleft, NB_CHEVALIER, 0.05)
            nbRouteTextsurface = basefont.render(": " + str(joueurActuel.nbRoutes), False, (0,0,0))
            fct.drawImageBotRight((rectNbChevalier.left - cst.xoff, rectNbChevalier.bottom), nbRouteTextsurface, 0.035)
            rectNbRoute = fct.rectDrawImageBotRight((rectNbChevalier.left - cst.xoff, rectNbChevalier.bottom), nbRouteTextsurface, 0.035)
            fct.drawImageBotRight(rectNbRoute.bottomleft, NB_ROUTES, 0.05)

            j = 0
            for i, joueur in enumerate(catan.joueurs):
                if i == 0:
                    color = cst.couleurj1
                elif i == 1:
                    color = cst.couleurj2
                elif i == 2:
                    color = cst.couleurj3
                elif i == 3:
                    color = cst.couleurj4
                if joueur.numero != joueurActuel.numero:
                    rect = Rect(3*cst.w/4, 0, cst.w/4, cst.h/8)
                    rect.bottom = rectNbChevalier.top - cst.yoff - j*(rect.h+cst.yoff/4)
                    pygame.draw.rect(cst.fenetre, (211,211,211), rect)

                    joueurTextSurface = basefont.render(joueur.nom, False, color)
                    fct.drawImageTopLeft(rect.topleft, joueurTextSurface, 0.025)
                    rectJoueur = fct.rectDrawImageTopLeft(rect.topleft, joueurTextSurface, 0.025)

                    fct.drawImageTopLeft((rectJoueur.right + cst.xoff/2, rectJoueur.top), BRICK, 0.03)
                    RECT_BRICKIMAGE = fct.rectDrawImageTopLeft((rectJoueur.right + cst.xoff/2, rectJoueur.top), BRICK, 0.03)
                    brickTextsurface = basefont.render(str(joueur.ressource[1]), False, (0,0,0))
                    fct.drawImageMidLeft(RECT_BRICKIMAGE.midright, brickTextsurface, 0.025)
                    rectBrickTextSurface = fct.rectDrawImageMidLeft(RECT_BRICKIMAGE.midright, brickTextsurface, 0.025)

                    fct.drawImageTopLeft((rectBrickTextSurface.right + cst.xoff/2, rectJoueur.top), STONE, 0.03)
                    RECT_STONEIMAGE = fct.rectDrawImageTopLeft((rectBrickTextSurface.right + cst.xoff/2, rectJoueur.top), STONE, 0.03)
                    stoneTextsurface = basefont.render(str(joueur.ressource[4]), False, (0,0,0))
                    fct.drawImageMidLeft(RECT_STONEIMAGE.midright, stoneTextsurface, 0.025)

                    fct.drawImageTopLeft((rect.left, rectJoueur.bottom + cst.yoff/3), WHEAT, 0.03)
                    RECT_WHEATIMAGE = fct.rectDrawImageTopLeft((rect.left,rectJoueur.bottom + cst.yoff/3), WHEAT, 0.03)
                    wheatTextsurface = basefont.render(str(joueur.ressource[3]), False, (0,0,0))
                    fct.drawImageMidLeft(RECT_WHEATIMAGE.midright, wheatTextsurface, 0.025)
                    rectWheatTextSurface = fct.rectDrawImageMidLeft(RECT_WHEATIMAGE.midright, wheatTextsurface, 0.025)

                    fct.drawImageTopLeft((rectWheatTextSurface.right + cst.xoff/2, rectJoueur.bottom + cst.yoff/3), WOOD, 0.03)
                    RECT_WOODIMAGE = fct.rectDrawImageTopLeft((rectWheatTextSurface.right + cst.xoff/2, rectJoueur.bottom + cst.yoff/3), WOOD, 0.03)
                    woodTextsurface = basefont.render(str(joueur.ressource[0]), False, (0,0,0))
                    fct.drawImageMidLeft(RECT_WOODIMAGE.midright, woodTextsurface, 0.025)
                    rectWoodTextSurface = fct.rectDrawImageMidLeft(RECT_WOODIMAGE.midright, woodTextsurface, 0.025)

                    fct.drawImageTopLeft((rectWoodTextSurface.right + cst.xoff/2, rectJoueur.bottom + cst.yoff/3), WOOL, 0.03)
                    RECT_WOOLIMAGE = fct.rectDrawImageTopLeft((rectWoodTextSurface.right + cst.xoff/2, rectJoueur.bottom + cst.yoff/3), WOOL, 0.03)
                    woolTextsurface = basefont.render(str(joueur.ressource[2]), False, (0,0,0))
                    fct.drawImageMidLeft(RECT_WOOLIMAGE.midright, woolTextsurface, 0.025)
                    j+=1


            rect = fct.rectDrawImageMidLeft(RECT_PVIMAGE.midright, pvTextsurface, 0.035)
            rectRoutes = fct.rectDrawImageTopLeft((rect.right + xoffset, 3*cst.h/4), CARTEDEV_ROUTES, 0.2)
            rectInvention = fct.rectDrawImageTopLeft((rectRoutes.right, 3*cst.h/4), CARTEDEV_INVENTION, 0.2)
            rectMonopole = fct.rectDrawImageTopLeft((rectInvention.right, 3*cst.h/4), CARTEDEV_MONOPOLE, 0.2)
            rectChevalier = fct.rectDrawImageTopLeft((rectMonopole.right, 3*cst.h/4), CARTEDEV_CHEVALIER, 0.2)
            c_routes = 0
            c_invention = 0
            c_monopole = 0
            c_chevalier = 0
            for carteDev in joueurActuel.carteDev:
                if carteDev.type == "Routes":
                    c_routes += 1
                    fct.drawImageTopLeft((rect.right + xoffset, 3*cst.h/4), CARTEDEV_ROUTES, 0.2)
                    RECT_CARTEDEV_ROUTES = fct.rectDrawImageTopLeft((rect.right + xoffset, 3*cst.h/4), CARTEDEV_ROUTES, 0.2)
                elif carteDev.type == "Invention":
                    c_invention += 1
                    fct.drawImageTopLeft((rectRoutes.right, 3*cst.h/4), CARTEDEV_INVENTION, 0.2)
                    RECT_CARTEDEV_INVENTION = fct.rectDrawImageTopLeft((rectRoutes.right, 3*cst.h/4), CARTEDEV_INVENTION, 0.2)
                elif carteDev.type == "Monopole":
                    c_monopole += 1
                    fct.drawImageTopLeft((rectInvention.right, 3*cst.h/4), CARTEDEV_MONOPOLE, 0.2)
                    RECT_CARTEDEV_MONOPOLE = fct.rectDrawImageTopLeft((rectInvention.right, 3*cst.h/4), CARTEDEV_MONOPOLE, 0.2)
                elif carteDev.type == "Chevalier":
                    c_chevalier += 1
                    fct.drawImageTopLeft((rectMonopole.right, 3*cst.h/4), CARTEDEV_CHEVALIER, 0.2)
                    RECT_CARTEDEV_CHEVALIER = fct.rectDrawImageTopLeft((rectMonopole.right, 3*cst.h/4), CARTEDEV_CHEVALIER, 0.2)
            if c_routes != 0 and c_routes != 1:
                c_routesTextsurface = basefont.render(str(c_routes), False, (0,0,0))
                fct.drawImageTopRight(rectRoutes.topright, c_routesTextsurface, 0.025)
            if c_invention != 0 and c_invention != 1:
                c_inventionTextsurface = basefont.render(str(c_invention), False, (0,0,0))
                fct.drawImageTopRight(rectInvention.topright, c_inventionTextsurface, 0.025)
            if c_monopole != 0 and c_monopole != 1:
                c_monopoleTextsurface = basefont.render(str(c_monopole), False, (0,0,0))
                fct.drawImageTopRight(rectMonopole.topright, c_monopoleTextsurface, 0.025)
            if c_chevalier != 0 and c_chevalier != 1:
                c_chevalierTextsurface = basefont.render(str(c_chevalier), False, (0,0,0))
                fct.drawImageTopRight(rectChevalier.topright, c_chevalierTextsurface, 0.025)

        if constructionColonie or constructionVille or constructionRoute or echangeBanque or echangeJoueurs:
            fct.drawImageBotRight((cst.w-xoffset, 3*cst.h/4-yoffset), ANNULER, 0.08)
            RECT_ANNULER = fct.rectDrawImageBotRight((cst.w-xoffset, 3*cst.h/4-yoffset), ANNULER, 0.08)

        if indicText:
            fct.drawImageTopRight((cst.w-xoffset, RECT_NEXTTURN.bottom+yoffset), IndicTextsurface, 0.04)

        if choixEchangeJoueurs:
            pygame.draw.rect(cst.fenetre, (211,211,211), Rect(cst.w/4, cst.h/3, cst.w/2, cst.h/3))
            j = 0
            for i, joueur in enumerate(catan.joueurs):
                if i == 0:
                    color = cst.couleurj1
                elif i == 1:
                    color = cst.couleurj2
                elif i == 2:
                    color = cst.couleurj3
                elif i == 3:
                    color = cst.couleurj4
                if joueur.numero != joueurActuel.numero:
                    if len(catan.joueurs) == 3:
                        joueurTextSurface = basefont.render(joueur.nom, False, color)
                        fct.drawImage((cst.w/4 + (j+1)*cst.w/6, cst.h/2), joueurTextSurface, 0.1)
                        RECT_ECHANGE_JOUEURS[j] = fct.rectDrawImage((cst.w/4 + (j+1)*cst.w/6, cst.h/2), joueurTextSurface, 0.1)
                    else:
                        joueurTextSurface = basefont.render(joueur.nom, False, color)
                        fct.drawImage((cst.w/4 + (j+1)*cst.w/8, cst.h/2), joueurTextSurface, 0.1)
                        RECT_ECHANGE_JOUEURS[j] = fct.rectDrawImage((cst.w/4 + (j+1)*cst.w/8, cst.h/2), joueurTextSurface, 0.1)
                    j += 1

        if echangeBanque or echangeJoueurs:
            pygame.draw.rect(cst.fenetre, (211,211,211), Rect(cst.w/4, cst.yoff, cst.w/2, cst.h-2*cst.xoff))
            if echangeBanque:
                donTextsurface = basefont.render("Don", False, (0,0,0))
                fct.drawImage((cst.w/4+2*cst.w/10, cst.yoff+yoffset), donTextsurface, 0.035)
                tauxTextsurface = basefont.render("Taux", False, (0,0,0))
                fct.drawImage((cst.w/4+3*cst.w/10, cst.yoff+yoffset), tauxTextsurface, 0.035)
                banqueTextsurface = basefont.render("Reçu", False, (0,0,0))
                fct.drawImage((cst.w/4+4*cst.w/10, cst.yoff+yoffset), banqueTextsurface, 0.035)
            else:
                donTextsurface = basefont.render(joueurActuel.nom, False, (0,0,0))
                fct.drawImage((cst.w/4+2*cst.w/10, cst.yoff+yoffset), donTextsurface, 0.035)
                tauxTextsurface = basefont.render("Taux", False, (0,0,0))
                fct.drawImage((cst.w/4+3*cst.w/10, cst.yoff+yoffset), tauxTextsurface, 0.035)
                banqueTextsurface = basefont.render(catan.joueurs[numeroJoueurEchange].nom, False, (0,0,0))
                fct.drawImage((cst.w/4+4*cst.w/10, cst.yoff+yoffset), banqueTextsurface, 0.035)
            fct.drawImage((cst.w/4+4*cst.w/10, cst.yoff+yoffset), banqueTextsurface, 0.035)
            fct.drawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+cst.h/8), BRICK, 0.05)
            fct.drawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+2*cst.h/8), STONE, 0.05)
            fct.drawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+3*cst.h/8), WHEAT, 0.05)
            fct.drawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+4*cst.h/8), WOOD, 0.05)
            fct.drawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+5*cst.h/8), WOOL, 0.05)
            brickTextsurface = basefont.render(str(joueurActuel.ressource[1]), False, (0,0,0))
            stoneTextsurface = basefont.render(str(joueurActuel.ressource[4]), False, (0,0,0))
            wheatTextsurface = basefont.render(str(joueurActuel.ressource[3]), False, (0,0,0))
            woodTextsurface = basefont.render(str(joueurActuel.ressource[0]), False, (0,0,0))
            woolTextsurface = basefont.render(str(joueurActuel.ressource[2]), False, (0,0,0))
            fct.drawImage((cst.w/4+cst.w/10+cst.w/40, cst.yoff+yoffset+cst.h/8), brickTextsurface, 0.020)
            fct.drawImage((cst.w/4+cst.w/10+cst.w/40, cst.yoff+yoffset+2*cst.h/8), stoneTextsurface, 0.020)
            fct.drawImage((cst.w/4+cst.w/10+cst.w/40, cst.yoff+yoffset+3*cst.h/8), wheatTextsurface, 0.020)
            fct.drawImage((cst.w/4+cst.w/10+cst.w/40, cst.yoff+yoffset+4*cst.h/8), woodTextsurface, 0.020)
            fct.drawImage((cst.w/4+cst.w/10+cst.w/40, cst.yoff+yoffset+5*cst.h/8), woolTextsurface, 0.020)
            brickTauxTextsurface = basefont.render(str(joueurActuel.valeurEchange[1]) + ":1", False, (0,0,0))
            stoneTauxTextsurface = basefont.render(str(joueurActuel.valeurEchange[4]) + ":1", False, (0,0,0))
            wheatTauxTextsurface = basefont.render(str(joueurActuel.valeurEchange[3]) + ":1", False, (0,0,0))
            woodTauxTextsurface = basefont.render(str(joueurActuel.valeurEchange[0]) + ":1", False, (0,0,0))
            woolTauxTextsurface = basefont.render(str(joueurActuel.valeurEchange[2]) + ":1", False, (0,0,0))
            fct.drawImage((cst.w/4+3*cst.w/10, cst.yoff+yoffset+cst.h/8), brickTauxTextsurface, 0.03)
            fct.drawImage((cst.w/4+3*cst.w/10, cst.yoff+yoffset+2*cst.h/8), stoneTauxTextsurface, 0.03)
            fct.drawImage((cst.w/4+3*cst.w/10, cst.yoff+yoffset+3*cst.h/8), wheatTauxTextsurface, 0.03)
            fct.drawImage((cst.w/4+3*cst.w/10, cst.yoff+yoffset+4*cst.h/8), woodTauxTextsurface, 0.03)
            fct.drawImage((cst.w/4+3*cst.w/10, cst.yoff+yoffset+5*cst.h/8), woolTauxTextsurface, 0.03)

            rectBrick = fct.rectDrawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+cst.h/8), BRICK, 0.05)
            rectStone = fct.rectDrawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+2*cst.h/8), STONE, 0.05)
            rectWheat = fct.rectDrawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+3*cst.h/8), WHEAT, 0.05)
            rectWood = fct.rectDrawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+4*cst.h/8), WOOD, 0.05)
            rectWool = fct.rectDrawImage((cst.w/4+cst.w/10-cst.w/20, cst.yoff+yoffset+5*cst.h/8), WOOL, 0.05)

            RECT_ECHANGE_BRICK = pygame.Rect(cst.w/4+2*cst.w/10, cst.yoff+yoffset+cst.h/8, 30, rectBrick.height)
            RECT_ECHANGE_STONE = pygame.Rect(cst.w/4+2*cst.w/10, cst.yoff+yoffset+2*cst.h/8, 30, rectStone.height)
            RECT_ECHANGE_WHEAT = pygame.Rect(cst.w/4+2*cst.w/10, cst.yoff+yoffset+3*cst.h/8, 30, rectWheat.height)
            RECT_ECHANGE_WOOD = pygame.Rect(cst.w/4+2*cst.w/10, cst.yoff+yoffset+4*cst.h/8, 30, rectWood.height)
            RECT_ECHANGE_WOOL = pygame.Rect(cst.w/4+2*cst.w/10, cst.yoff+yoffset+5*cst.h/8, 30, rectWool.height)
            RECT_ECHANGE_BRICK.center = (cst.w/4+2*cst.w/10, cst.yoff+yoffset+cst.h/8)
            RECT_ECHANGE_STONE.center = (cst.w/4+2*cst.w/10, cst.yoff+yoffset+2*cst.h/8)
            RECT_ECHANGE_WHEAT.center = (cst.w/4+2*cst.w/10, cst.yoff+yoffset+3*cst.h/8)
            RECT_ECHANGE_WOOD.center = (cst.w/4+2*cst.w/10, cst.yoff+yoffset+4*cst.h/8)
            RECT_ECHANGE_WOOL.center = (cst.w/4+2*cst.w/10, cst.yoff+yoffset+5*cst.h/8)

            RECT_ECHANGE_BRICK2 = pygame.Rect(cst.w/4+4*cst.w/10, cst.yoff+yoffset+cst.h/8, 30, rectBrick.height)
            RECT_ECHANGE_STONE2 = pygame.Rect(cst.w/4+4*cst.w/10, cst.yoff+yoffset+2*cst.h/8, 30, rectStone.height)
            RECT_ECHANGE_WHEAT2 = pygame.Rect(cst.w/4+4*cst.w/10, cst.yoff+yoffset+3*cst.h/8, 30, rectWheat.height)
            RECT_ECHANGE_WOOD2 = pygame.Rect(cst.w/4+4*cst.w/10, cst.yoff+yoffset+4*cst.h/8, 30, rectWood.height)
            RECT_ECHANGE_WOOL2 = pygame.Rect(cst.w/4+4*cst.w/10, cst.yoff+yoffset+5*cst.h/8, 30, rectWool.height)
            RECT_ECHANGE_BRICK2.center = (cst.w/4+4*cst.w/10, cst.yoff+yoffset+cst.h/8)
            RECT_ECHANGE_STONE2.center = (cst.w/4+4*cst.w/10, cst.yoff+yoffset+2*cst.h/8)
            RECT_ECHANGE_WHEAT2.center = (cst.w/4+4*cst.w/10, cst.yoff+yoffset+3*cst.h/8)
            RECT_ECHANGE_WOOD2.center = (cst.w/4+4*cst.w/10, cst.yoff+yoffset+4*cst.h/8)
            RECT_ECHANGE_WOOL2.center = (cst.w/4+4*cst.w/10, cst.yoff+yoffset+5*cst.h/8)

            text_surface_brick = echangefont.render(textBrick, True, (0, 0, 0))
            text_surface_stone = echangefont.render(textStone, True, (0, 0, 0))
            text_surface_wheat = echangefont.render(textWheat, True, (0, 0, 0))
            text_surface_wood = echangefont.render(textWood, True, (0, 0, 0))
            text_surface_wool = echangefont.render(textWool, True, (0, 0, 0))
            text_surface_brick2 = echangefont.render(textBrick2, True, (0, 0, 0))
            text_surface_stone2 = echangefont.render(textStone2, True, (0, 0, 0))
            text_surface_wheat2 = echangefont.render(textWheat2, True, (0, 0, 0))
            text_surface_wood2 = echangefont.render(textWood2, True, (0, 0, 0))
            text_surface_wool2 = echangefont.render(textWool2, True, (0, 0, 0))

            RECT_ECHANGE_BRICK.width = max(30, text_surface_brick.get_width() + 10)
            RECT_ECHANGE_STONE.width = max(30, text_surface_stone.get_width() + 10)
            RECT_ECHANGE_WHEAT.width = max(30, text_surface_wheat.get_width() + 10)
            RECT_ECHANGE_WOOD.width = max(30, text_surface_wood.get_width() + 10)
            RECT_ECHANGE_WOOL.width = max(30, text_surface_wool.get_width() + 10)
            RECT_ECHANGE_BRICK2.width = max(30, text_surface_brick2.get_width() + 10)
            RECT_ECHANGE_STONE2.width = max(30, text_surface_stone2.get_width() + 10)
            RECT_ECHANGE_WHEAT2.width = max(30, text_surface_wheat2.get_width() + 10)
            RECT_ECHANGE_WOOD2.width = max(30, text_surface_wood2.get_width() + 10)
            RECT_ECHANGE_WOOL2.width = max(30, text_surface_wool2.get_width() + 10)

            if activeTextBrick:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_BRICK, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_BRICK, 2)
            if activeTextStone:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_STONE, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_STONE, 2)
            if activeTextWheat:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_WHEAT, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_WHEAT, 2)
            if activeTextWood:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_WOOD, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_WOOD, 2)
            if activeTextWool:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_WOOL, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_WOOL, 2)
            if activeTextBrick2:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_BRICK2, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_BRICK2, 2)
            if activeTextStone2:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_STONE2, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_STONE2, 2)
            if activeTextWheat2:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_WHEAT2, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_WHEAT2, 2)
            if activeTextWood2:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_WOOD2, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_WOOD2, 2)
            if activeTextWool2:
                pygame.draw.rect(cst.fenetre, (255,102,255), RECT_ECHANGE_WOOL2, 2)
            else:
                pygame.draw.rect(cst.fenetre, (0,0,0), RECT_ECHANGE_WOOL2, 2)

            cst.fenetre.blit(text_surface_brick, (RECT_ECHANGE_BRICK.x + 5, RECT_ECHANGE_BRICK.y + 5))
            cst.fenetre.blit(text_surface_stone, (RECT_ECHANGE_STONE.x + 5, RECT_ECHANGE_STONE.y + 5))
            cst.fenetre.blit(text_surface_wheat, (RECT_ECHANGE_WHEAT.x + 5, RECT_ECHANGE_WHEAT.y + 5))
            cst.fenetre.blit(text_surface_wood, (RECT_ECHANGE_WOOD.x + 5, RECT_ECHANGE_WOOD.y + 5))
            cst.fenetre.blit(text_surface_wool, (RECT_ECHANGE_WOOL.x + 5, RECT_ECHANGE_WOOL.y + 5))
            cst.fenetre.blit(text_surface_brick2, (RECT_ECHANGE_BRICK2.x + 5, RECT_ECHANGE_BRICK2.y + 5))
            cst.fenetre.blit(text_surface_stone2, (RECT_ECHANGE_STONE2.x + 5, RECT_ECHANGE_STONE2.y + 5))
            cst.fenetre.blit(text_surface_wheat2, (RECT_ECHANGE_WHEAT2.x + 5, RECT_ECHANGE_WHEAT2.y + 5))
            cst.fenetre.blit(text_surface_wood2, (RECT_ECHANGE_WOOD2.x + 5, RECT_ECHANGE_WOOD2.y + 5))
            cst.fenetre.blit(text_surface_wool2, (RECT_ECHANGE_WOOL2.x + 5, RECT_ECHANGE_WOOL2.y + 5))

            if echangeBanque:
                text_surface_valider = basefont.render("Valider", True, (0, 0, 0))
                fct.drawImage((cst.w/2, cst.yoff+yoffset+6*cst.h/8), text_surface_valider, 0.08)
                fct.drawImage((cst.w/2, cst.yoff+yoffset+13*cst.h/16), VALIDER_OFF, 0.04)
                RECT_ECHANGE_VALIDER = fct.rectDrawImage((cst.w/2, cst.yoff+yoffset+13*cst.h/16), VALIDER_OFF, 0.04)
            
            if echangeJoueurs:
                text_surface_validerJ1 = basefont.render("Valider J1", True, (0, 0, 0))
                fct.drawImage((cst.w/2 - cst.w/8, cst.yoff+yoffset+6*cst.h/8), text_surface_validerJ1, 0.08)
                text_surface_validerJ2 = basefont.render("Valider J2", True, (0, 0, 0))
                fct.drawImage((cst.w/2 + cst.w/8, cst.yoff+yoffset+6*cst.h/8), text_surface_validerJ2, 0.08)

                if validerJ1:
                    fct.drawImage((cst.w/2 - cst.w/8, cst.yoff+yoffset+13*cst.h/16), VALIDER_ON, 0.04)
                    RECT_ECHANGE_VALIDERJ1 = fct.rectDrawImage((cst.w/2 - cst.w/8, cst.yoff+yoffset+13*cst.h/16), VALIDER_ON, 0.04)
                else:
                    fct.drawImage((cst.w/2 - cst.w/8, cst.yoff+yoffset+13*cst.h/16), VALIDER_OFF, 0.04)
                    RECT_ECHANGE_VALIDERJ1 = fct.rectDrawImage((cst.w/2 - cst.w/8, cst.yoff+yoffset+13*cst.h/16), VALIDER_OFF, 0.04)
                if validerJ2:
                    fct.drawImage((cst.w/2 + cst.w/8, cst.yoff+yoffset+13*cst.h/16), VALIDER_ON, 0.04)
                    RECT_ECHANGE_VALIDERJ2 = fct.rectDrawImage((cst.w/2 + cst.w/8, cst.yoff+yoffset+13*cst.h/16), VALIDER_ON, 0.04)
                else:
                    fct.drawImage((cst.w/2 + cst.w/8, cst.yoff+yoffset+13*cst.h/16), VALIDER_OFF, 0.04)
                    RECT_ECHANGE_VALIDERJ2 = fct.rectDrawImage((cst.w/2 + cst.w/8, cst.yoff+yoffset+13*cst.h/16), VALIDER_OFF, 0.04)
            
            if textInfo != '':
                text_surface_info = basefont.render(textInfo, True, (255, 0, 0))
                fct.drawImage((cst.w/2, cst.yoff+yoffset+7*cst.h/8), text_surface_info, 0.2)

        if deplacerVoleur:
            game = False
            for i, coord in enumerate(hexagon_coords):
                if coord != catan.plateau.voleur.coords:
                    rect = Rect((positions[i][0]+cst.xoff,positions[i][1]+cst.yoff),(20,20))
                    rect.center = (positions[i][0]+cst.xoff,positions[i][1]+cst.yoff)
                    pygame.draw.rect(cst.fenetre, (255,102,255), rect)
                    RECTS_TILES[i] = rect
        
        if carteDevInvention or carteDevMonopole:
            pygame.draw.rect(cst.fenetre, (211,211,211), Rect(cst.w/8, cst.h/3, 3*cst.w/4, cst.h/3))
            fct.drawImage((2*cst.w/8, cst.h/2), BRICK, 0.1)
            fct.drawImage((3*cst.w/8, cst.h/2), STONE, 0.1)
            fct.drawImage((4*cst.w/8, cst.h/2), WHEAT, 0.1)
            fct.drawImage((5*cst.w/8, cst.h/2), WOOD, 0.1)
            fct.drawImage((6*cst.w/8, cst.h/2), WOOL, 0.1)
            RECT_CARTEDEV_BRICK = fct.rectDrawImage((2*cst.w/8, cst.h/2), BRICK, 0.1)
            RECT_CARTEDEV_STONE = fct.rectDrawImage((3*cst.w/8, cst.h/2), STONE, 0.1)
            RECT_CARTEDEV_WHEAT = fct.rectDrawImage((4*cst.w/8, cst.h/2), WHEAT, 0.1)
            RECT_CARTEDEV_WOOD = fct.rectDrawImage((5*cst.w/8, cst.h/2), WOOD, 0.1)
            RECT_CARTEDEV_WOOL = fct.rectDrawImage((6*cst.w/8, cst.h/2), WOOL, 0.1)

        for event in pygame.event.get():
            fct.shouldQuit(event)
            fct.shouldResize(event)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if RECT_NEXTTURN.collidepoint(event.pos):
                    constructionColonie = False
                    constructionVille = False
                    constructionRoute = False
                    carteDeveloppement = False
                    echangeBanque = False
                    choixEchangeJoueurs = False
                    echangeJoueurs = False
                    indicText = False
                    catan.tourSuivant()
                    if catan.valeurDes == 7:
                        deplacerVoleur = True
                elif RECT_COLONIE.collidepoint(event.pos):
                    if joueurActuel.ressourceSuffisante(np.array([1,1,1,1,0])):
                        print("Colonie")
                        constructionColonie = True
                        constructionVille = False
                        constructionRoute = False
                        carteDeveloppement = False
                        echangeBanque = False
                        choixEchangeJoueurs = False
                        echangeJoueurs = False
                        indicText = False

                        vertices_available = [False for i in range(len(vertices))]
                        for i, coord in enumerate(vertices_coords):
                            if catan.plateau.intersectionDispoConstruction(coord):
                                if catan.plateau.routeAdjacenteColonieExiste(joueurActuel, coord):
                                    vertices_available[i] = True
                    else:
                        print("Impossible de construire")
                        indicText = True
                        IndicTextsurface = basefont.render("Pas assez de ressource", False, (255,0,0))
                elif RECT_VILLE.collidepoint(event.pos):
                    if joueurActuel.ressourceSuffisante(np.array([0,0,0,2,3])):
                        print("Ville")
                        constructionColonie = False
                        constructionVille = True
                        constructionRoute = False
                        carteDeveloppement = False
                        echangeBanque = False
                        choixEchangeJoueurs = False
                        echangeJoueurs = False
                        indicText = False
                    else:
                        print("Impossible de construire")
                        indicText = True
                        IndicTextsurface = basefont.render("Pas assez de ressource", False, (255,0,0))
                elif RECT_ROUTE.collidepoint(event.pos):
                    if joueurActuel.ressourceSuffisante(np.array([1,1,0,0,0])):
                        print("Route")
                        constructionColonie = False
                        constructionVille = False
                        constructionRoute = True
                        carteDeveloppement = False
                        echangeBanque = False
                        choixEchangeJoueurs = False
                        echangeJoueurs = False
                        indicText = False
                        edges_available = [False for i in range(len(edges))]
                    else:
                        print("Impossible de construire")
                        indicText = True
                        IndicTextsurface = basefont.render("Pas assez de ressource", False, (255,0,0))
                elif RECT_CARTEDEV.collidepoint(event.pos):
                    if catan.achatCarteDev(joueurActuel):
                        print("CarteDev")
                        constructionColonie = False
                        constructionVille = False
                        constructionRoute = False
                        carteDeveloppement = True
                        echangeBanque = False
                        choixEchangeJoueurs = False
                        echangeJoueurs = False
                        indicText = False
                    else:
                        print("Impossible de construire")
                        indicText = True
                        IndicTextsurface = basefont.render("Pas assez de ressource", False, (255,0,0))
                elif RECT_ECHANGEBANQUE.collidepoint(event.pos):
                    print("Echange Banque")
                    constructionColonie = False
                    constructionVille = False
                    constructionRoute = False
                    carteDeveloppement = False
                    echangeBanque = True
                    choixEchangeJoueurs = False
                    echangeJoueurs = False
                    indicText = False
                    textStone = '0'
                    textBrick = '0'
                    textWheat = '0'
                    textWood = '0'
                    textWool = '0'
                    textBrick2 = '0'
                    textStone2 = '0'
                    textWheat2 = '0'
                    textWood2 = '0'
                    textWool2 = '0'
                    textInfo = ''
                elif RECT_ECHANGEJOUEURS.collidepoint(event.pos):
                    print("Echange Joueurs")
                    constructionColonie = False
                    constructionVille = False
                    constructionRoute = False
                    carteDeveloppement = False
                    echangeBanque = False
                    choixEchangeJoueurs = True
                    echangeJoueurs = False
                    indicText = False
                elif RECT_ANNULER.collidepoint(event.pos):
                    print("Annuler")
                    constructionColonie = False
                    constructionVille = False
                    constructionRoute = False
                    carteDeveloppement = False
                    echangeBanque = False
                    choixEchangeJoueurs = False
                    echangeJoueurs = False
                    indicText = False
                elif RECT_ECHANGE_BRICK.collidepoint(event.pos):
                    activeTextBrick = True
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                elif RECT_ECHANGE_STONE.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = True
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                elif RECT_ECHANGE_WHEAT.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = True
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                elif RECT_ECHANGE_WOOD.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = True
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                elif RECT_ECHANGE_WOOL.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = True
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                elif RECT_ECHANGE_BRICK2.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = True
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                elif RECT_ECHANGE_STONE2.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = True
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                elif RECT_ECHANGE_WHEAT2.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = True
                    activeTextWood2 = False
                    activeTextWool2 = False
                elif RECT_ECHANGE_WOOD2.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = True
                    activeTextWool2 = False
                elif RECT_ECHANGE_WOOL2.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = True
                elif RECT_ECHANGE_VALIDER.collidepoint(event.pos):
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                    if catan.echangeBanque(joueurActuel, np.array([int(textWood), int(textBrick), int(textWool), int(textWheat), int(textStone)]), np.array([int(textWood2), int(textBrick2), int(textWool2), int(textWheat2), int(textStone2)])):
                        echangeBanque = False
                        textStone = '0'
                        textBrick = '0'
                        textWheat = '0'
                        textWood = '0'
                        textWool = '0'
                        textBrick2 = '0'
                        textStone2 = '0'
                        textWheat2 = '0'
                        textWood2 = '0'
                        textWool2 = '0'
                        textInfo = ''
                    else:
                        textInfo = 'Transaction Impossible!'
                elif RECT_ECHANGE_VALIDERJ1.collidepoint(event.pos):
                    validerJ1 = not(validerJ1)
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                    if validerJ1 and validerJ2:
                        if catan.echangeJoueur(joueurActuel, catan.joueurs[numeroJoueurEchange], np.array([int(textWood), int(textBrick), int(textWool), int(textWheat), int(textStone)]), np.array([int(textWood2), int(textBrick2), int(textWool2), int(textWheat2), int(textStone2)])):
                            echangeJoueurs = False
                            textStone = '0'
                            textBrick = '0'
                            textWheat = '0'
                            textWood = '0'
                            textWool = '0'
                            textBrick2 = '0'
                            textStone2 = '0'
                            textWheat2 = '0'
                            textWood2 = '0'
                            textWool2 = '0'
                            textInfo = ''
                        else:
                            textInfo = 'Transaction Impossible!'
                elif RECT_ECHANGE_VALIDERJ2.collidepoint(event.pos):
                    validerJ2 = not(validerJ2)
                    activeTextBrick = False
                    activeTextStone = False
                    activeTextWheat = False
                    activeTextWood = False
                    activeTextWool = False
                    activeTextBrick2 = False
                    activeTextStone2 = False
                    activeTextWheat2 = False
                    activeTextWood2 = False
                    activeTextWool2 = False
                    if validerJ1 and validerJ2:
                        if catan.echangeJoueur(joueurActuel, catan.joueurs[numeroJoueurEchange], np.array([int(textWood), int(textBrick), int(textWool), int(textWheat), int(textStone)]), np.array([int(textWood2), int(textBrick2), int(textWool2), int(textWheat2), int(textStone2)])):
                            echangeJoueurs = False
                            textStone = '0'
                            textBrick = '0'
                            textWheat = '0'
                            textWood = '0'
                            textWool = '0'
                            textBrick2 = '0'
                            textStone2 = '0'
                            textWheat2 = '0'
                            textWood2 = '0'
                            textWool2 = '0'
                            textInfo = ''
                        else:
                            textInfo = 'Transaction Impossible!'
                elif RECT_CARTEDEV_ROUTES.collidepoint(event.pos):
                    print("CARTEDEV_ROUTES")
                    carteDevConstructionRoute = True
                    joueurActuel.removeRoutes()
                elif RECT_CARTEDEV_INVENTION.collidepoint(event.pos):
                    print("CARTEDEV_INVENTION")
                    carteDevInvention = True
                    joueurActuel.removeInvention()
                elif RECT_CARTEDEV_MONOPOLE.collidepoint(event.pos):
                    print("CARTEDEV_MONOPOLE")
                    carteDevMonopole = True
                    joueurActuel.removeMonopole()
                elif RECT_CARTEDEV_CHEVALIER.collidepoint(event.pos):
                    print("CARTEDEV_CHEVALIER")
                    deplacerVoleur = True
                    joueurActuel.removeChevalier()
                elif RECT_CARTEDEV_BRICK.collidepoint(event.pos):
                    if carteDevInvention:
                        nbRessourceRecup += 1
                        joueurActuel.ressource += np.array([0,1,0,0,0])
                        if nbRessourceRecup == 2:
                            carteDevInvention = False
                            nbRessourceRecup = 0
                    elif carteDevMonopole:
                        catan.carteDevMonopole(joueurActuel, 1)
                        carteDevMonopole = False
                elif RECT_CARTEDEV_STONE.collidepoint(event.pos):
                    if carteDevInvention:
                        nbRessourceRecup += 1
                        joueurActuel.ressource += np.array([0,0,0,0,1])
                        if nbRessourceRecup == 2:
                            carteDevInvention = False
                            nbRessourceRecup = 0
                    elif carteDevMonopole:
                        catan.carteDevMonopole(joueurActuel, 4)
                        carteDevMonopole = False
                elif RECT_CARTEDEV_WHEAT.collidepoint(event.pos):
                    if carteDevInvention:
                        nbRessourceRecup += 1
                        joueurActuel.ressource += np.array([0,0,0,1,0])
                        if nbRessourceRecup == 2:
                            carteDevInvention = False
                            nbRessourceRecup = 0
                    elif carteDevMonopole:
                        catan.carteDevMonopole(joueurActuel, 3)
                        carteDevMonopole = False
                elif RECT_CARTEDEV_WOOD.collidepoint(event.pos):
                    if carteDevInvention:
                        nbRessourceRecup += 1
                        joueurActuel.ressource += np.array([1,0,0,0,0])
                        if nbRessourceRecup == 2:
                            carteDevInvention = False
                            nbRessourceRecup = 0
                    elif carteDevMonopole:
                        catan.carteDevMonopole(joueurActuel, 0)
                        carteDevMonopole = False
                elif RECT_CARTEDEV_WOOL.collidepoint(event.pos):
                    if carteDevInvention:
                        nbRessourceRecup += 1
                        joueurActuel.ressource += np.array([0,0,1,0,0])
                        if nbRessourceRecup == 2:
                            carteDevInvention = False
                            nbRessourceRecup = 0
                    elif carteDevMonopole:
                        catan.carteDevMonopole(joueurActuel, 2)
                        carteDevMonopole = False
                elif RECT_PORT.collidepoint(event.pos):
                    portOn = not(portOn)

                for i, rect_joueur in enumerate(RECT_ECHANGE_JOUEURS):
                    if rect_joueur.collidepoint(event.pos):
                        j = 0
                        for joueur in catan.joueurs:
                            if joueur.numero != joueurActuel.numero:
                                if i == j:
                                    numeroJoueurEchange = joueur.numero
                                    choixEchangeJoueurs = False
                                    echangeJoueurs = True
                                j += 1

                for i, rect_tiles in enumerate(RECTS_TILES):
                    if rect_tiles.collidepoint(event.pos):
                        if catan.deplacerVoleur(joueurActuel, hexagon_coords[i]):
                            deplacerVoleur = False
                            game = True

                for i,rect_vertice in enumerate(RECTS_VERTICES):
                    if rect_vertice.collidepoint(event.pos):
                        if startingColonie:
                            if catan.construireColonieGratuit(joueurActuel, vertices_coords[i]):
                                for j, coord in enumerate(vertices_coords):
                                    if coord == vertices_coords[i]:
                                        vertices_available[j] = False
                                    elif coord in catan.plateau.getAdjacentVerticesFromVertice(vertices_coords[i]):
                                        vertices_available[j] = False
                                if catan.tourSuivantDebut():
                                    startingColonie = False
                                    startingRoute = True
                        if constructionColonie:
                            if catan.construireColonie(joueurActuel, vertices_coords[i]):
                                constructionColonie = False
                                constructionVille = False
                                constructionRoute = False
                                carteDeveloppement = False
                                echangeBanque = False
                                choixEchangeJoueurs = False
                                echangeJoueurs = False
                                indicText = False
                        if constructionVille:
                            if catan.construireVille(joueurActuel, vertices_coords[i]):
                                constructionColonie = False
                                constructionVille = False
                                constructionRoute = False
                                carteDeveloppement = False
                                echangeBanque = False
                                choixEchangeJoueurs = False
                                echangeJoueurs = False
                                indicText = False
                for i,rect_edge in enumerate(RECTS_EDGES):
                    if rect_edge.collidepoint(event.pos):
                        if startingRoute:
                            if catan.construireRouteGratuit(joueurActuel, edges_coords[i]):
                                edges_available = [False for i in range(len(edges))]
                                if catan.tourSuivantDebut():
                                    startingRoute = False
                                    catan.ressourceDebut()
                                    catan.lancerDes()
                                    catan.donRessource()
                                    game = True
                        if constructionRoute:
                            if catan.construireRoute(joueurActuel, edges_coords[i]):
                                constructionColonie = False
                                constructionVille = False
                                constructionRoute = False
                                carteDeveloppement = False
                                echangeBanque = False
                                choixEchangeJoueurs = False
                                echangeJoueurs = False
                                indicText = False
                        if carteDevConstructionRoute:
                            if catan.construireRouteGratuit(joueurActuel, edges_coords[i]):
                                edges_available = [False for i in range(len(edges))]
                                nbRouteGratuite += 1
                                if nbRouteGratuite == 2:
                                    carteDevConstructionRoute = False
                                    nbRouteGratuite = 0
            elif event.type == pygame.KEYDOWN:
                if activeTextBrick:
                    if event.key == pygame.K_BACKSPACE:
                        textBrick = textBrick[:-1]
                    else:
                        textBrick += event.unicode
                elif activeTextStone:
                    if event.key == pygame.K_BACKSPACE:
                        textStone = textBrick[:-1]
                    else:
                        textStone += event.unicode
                elif activeTextWheat:
                    if event.key == pygame.K_BACKSPACE:
                        textWheat = textBrick[:-1]
                    else:
                        textWheat += event.unicode
                elif activeTextWood:
                    if event.key == pygame.K_BACKSPACE:
                        textWood = textBrick[:-1]
                    else:
                        textWood += event.unicode
                elif activeTextWool:
                    if event.key == pygame.K_BACKSPACE:
                        textWool = textBrick[:-1]
                    else:
                        textWool += event.unicode
                elif activeTextBrick2:
                    if event.key == pygame.K_BACKSPACE:
                        textBrick2 = textBrick[:-1]
                    else:
                        textBrick2 += event.unicode
                elif activeTextStone2:
                    if event.key == pygame.K_BACKSPACE:
                        textStone2 = textBrick[:-1]
                    else:
                        textStone2 += event.unicode
                elif activeTextWheat2:
                    if event.key == pygame.K_BACKSPACE:
                        textWheat2 = textBrick[:-1]
                    else:
                        textWheat2 += event.unicode
                elif activeTextWood2:
                    if event.key == pygame.K_BACKSPACE:
                        textWood2 = textBrick[:-1]
                    else:
                        textWood2 += event.unicode
                elif activeTextWool2:
                    if event.key == pygame.K_BACKSPACE:
                        textWool2 = textBrick[:-1]
                    else:
                        textWool2 += event.unicode

        pygame.display.update()

def resetRect():
    """
    Réinitialise les rectangles utilisés dans l'affichage
    """
    global RECT_MAIN, RECT_NEXTTURN, RECT_BRICKIMAGE, RECT_STONEIMAGE, RECT_WHEATIMAGE, RECT_WOODIMAGE, RECT_WOOLIMAGE, RECT_PVIMAGE, RECT_COLONIE, RECT_VILLE, RECT_ROUTE, RECT_CARTEDEV, RECT_ANNULER, RECT_ECHANGEBANQUE, RECT_ECHANGEJOUEURS, RECTS_TILES, RECTS_VERTICES, RECTS_EDGES, RECT_ECHANGE_BRICK, RECT_ECHANGE_STONE, RECT_ECHANGE_WHEAT, RECT_ECHANGE_WOOD, RECT_ECHANGE_WOOL, RECT_ECHANGE_BRICK2, RECT_ECHANGE_STONE2, RECT_ECHANGE_WHEAT2, RECT_ECHANGE_WOOD2, RECT_ECHANGE_WOOL2, RECT_ECHANGE_VALIDER, RECT_ECHANGE_VALIDERJ1, RECT_ECHANGE_VALIDERJ2, RECT_ECHANGE_JOUEURS, RECT_CARTEDEV_ROUTES, RECT_CARTEDEV_INVENTION, RECT_CARTEDEV_MONOPOLE, RECT_CARTEDEV_CHEVALIER, RECT_CARTEDEV_BRICK, RECT_CARTEDEV_STONE, RECT_CARTEDEV_WHEAT, RECT_CARTEDEV_WOOD, RECT_CARTEDEV_WOOL, RECT_PORT

    RECT_MAIN = pygame.Rect(0, 0, 0, 0)
    RECT_NEXTTURN = pygame.Rect(0, 0, 0, 0)
    RECT_BRICKIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_STONEIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_WHEATIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_WOODIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_WOOLIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_PVIMAGE = pygame.Rect(0, 0, 0, 0)
    RECT_COLONIE = pygame.Rect(0, 0, 0, 0)
    RECT_VILLE = pygame.Rect(0, 0, 0, 0)
    RECT_ROUTE = pygame.Rect(0, 0, 0, 0)
    RECT_CARTEDEV = pygame.Rect(0, 0, 0, 0)
    RECT_ANNULER = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGEBANQUE = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGEJOUEURS = pygame.Rect(0, 0, 0, 0)
    RECTS_TILES = []
    for t in range(19):
        RECTS_TILES.append(pygame.Rect(0,0,0,0))
    RECTS_VERTICES = []
    for v in range(54):
        RECTS_VERTICES.append(pygame.Rect(0,0,0,0))
    RECTS_EDGES = []
    for e in range(74):
        RECTS_EDGES.append(pygame.Rect(0,0,0,0))
        
    RECT_ECHANGE_BRICK = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_STONE = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_WHEAT = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_WOOD = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_WOOL = pygame.Rect(0, 0, 0, 0)

    RECT_ECHANGE_BRICK2 = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_STONE2 = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_WHEAT2 = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_WOOD2 = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_WOOL2 = pygame.Rect(0, 0, 0, 0)

    RECT_ECHANGE_VALIDER = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_VALIDERJ1 = pygame.Rect(0, 0, 0, 0)
    RECT_ECHANGE_VALIDERJ2 = pygame.Rect(0, 0, 0, 0)

    RECT_CARTEDEV_ROUTES = pygame.Rect(0, 0, 0, 0)
    RECT_CARTEDEV_INVENTION = pygame.Rect(0, 0, 0, 0)
    RECT_CARTEDEV_MONOPOLE = pygame.Rect(0, 0, 0, 0)
    RECT_CARTEDEV_CHEVALIER = pygame.Rect(0, 0, 0, 0)

    RECT_CARTEDEV_BRICK = pygame.Rect(0, 0, 0, 0)
    RECT_CARTEDEV_STONE = pygame.Rect(0, 0, 0, 0)
    RECT_CARTEDEV_WHEAT = pygame.Rect(0, 0, 0, 0)
    RECT_CARTEDEV_WOOD = pygame.Rect(0, 0, 0, 0)
    RECT_CARTEDEV_WOOL = pygame.Rect(0, 0, 0, 0)

    RECT_ECHANGE_JOUEURS = []
    for j in range(3):
        RECT_ECHANGE_JOUEURS.append(pygame.Rect(0, 0, 0, 0))

    RECT_PORT = pygame.Rect(0, 0, 0, 0)

def drawColonie(center_coords, joueur):
    """
    Affiche une nouvelle colonie d'un joueur à l'endroit choisi.

    Paramètres
    ----------
    center_coords : tuple(int)
        Coordonnées de l'instersection où dessiner la colonie
    joueur : Joueur
        Joueur à qui appartient la colonie
    """

    a = 0.05
    if joueur == 0:
        fct.drawImage(center_coords, COLONIE_J1, a)
    elif joueur == 1:
        fct.drawImage(center_coords, COLONIE_J2, a)
    elif joueur == 2:
        fct.drawImage(center_coords, COLONIE_J3, a)
    elif joueur == 3:
        fct.drawImage(center_coords, COLONIE_J4, a)

def drawVille(center_coords, joueur):
    """
    Affiche une nouvelle ville d'un joueur à l'endroit choisi.

    Paramètres
    ----------
    center_coords : tuple(int)
        Coordonnées de l'instersection où dessiner la colonie
    joueur : Joueur
        Joueur à qui appartient la ville
    """

    a = 0.05
    if joueur == 0:
        fct.drawImage(center_coords, VILLE_J1, a)
    elif joueur == 1:
        fct.drawImage(center_coords, VILLE_J2, a)
    elif joueur == 2:
        fct.drawImage(center_coords, VILLE_J3, a)
    elif joueur == 3:
        fct.drawImage(center_coords, VILLE_J4, a)

def drawPort(vertice_coord, port, direction):
    """
    Affiche un port à l'endroit choisi.

    Paramètres
    ----------
    vertice_coords : tuple(int)
        Coordonnées de l'instersection
    port : Port
        Port qui doit être construit
    direction : String
        Direction dans laquelle dessiner le port
    """

    portTextsurface = basefont.render(port.type + " " + str(min(port.echange)) +":1", False, (255,51,153))
    if direction == "N":
        fct.drawImage((vertice_coord[0], vertice_coord[1] - cst.yoff), portTextsurface, 0.07)
    elif direction == "S":
        fct.drawImage((vertice_coord[0], vertice_coord[1] + cst.yoff), portTextsurface, 0.07)
    elif direction == "E":
        fct.drawImage((vertice_coord[0] + cst.xoff, vertice_coord[1]), portTextsurface, 0.07)
    elif direction == "W":
        fct.drawImage((vertice_coord[0] - cst.xoff, vertice_coord[1]), portTextsurface, 0.07)
    