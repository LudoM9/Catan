import pygame, os
from pygame.locals import *
import constantes as cst
import fonctions as fct
import numpy as np

pygame.font.init()
Broadwfont = pygame.font.Font(os.path.join('fonts', 'BROADW.TTF'), 30)
basefont = pygame.font.Font(None, 100)

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

def main(catan):
    global RECT_MAIN, RECT_NEXTTURN, RECT_BRICKIMAGE, RECT_STONEIMAGE, RECT_WHEATIMAGE, RECT_WOODIMAGE, RECT_WOOLIMAGE, RECT_PVIMAGE, RECT_COLONIE, RECT_VILLE, RECT_ROUTE, RECT_CARTEDEV, RECT_ANNULER, RECT_ECHANGEBANQUE, RECT_ECHANGEJOUEURS, RECTS_TILES, RECTS_VERTICES, RECTS_EDGES

    run = True
    startingColonie = False
    startingRoute = False
    game = True
    constructionColonie = False
    constructionVille = False
    constructionRoute = False
    carteDeveloppement = False
    echangeBanque = False
    echangeJoueurs = False
    indicText = False
    xoffset = 5
    yoffset = 5

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
            fct.drawHexagon(hexagons[i], positions[i],numbers[i]) #construction des hexagones, chemins et numéros sur les tuiles
            #fct.drawImage((positions[i][0]+cst.xoff,positions[i][1]+cst.yoff),CERCLE,0.04)

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

        if startingRoute or constructionRoute:
            if startingRoute:
                IndicTextsurface = basefont.render("Placez vos routes", False, (0,0,0))
                fct.drawImageTopRight((cst.w-xoffset, yoffset), IndicTextsurface, 0.04)
            for i in range(len(edges)):
                if edges_available[i]:
                    rect = Rect((edges[i][0]+cst.xoff,edges[i][1]+cst.yoff),(20,20))
                    rect.center = (edges[i][0]+cst.xoff,edges[i][1]+cst.yoff)
                    pygame.draw.rect(cst.fenetre, (255,102,255), rect)
                    RECTS_EDGES[i] = rect
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

        if constructionColonie or constructionVille or constructionRoute or echangeBanque or echangeJoueurs:
            fct.drawImageBotRight((cst.w-xoffset, 3*cst.h/4-yoffset), ANNULER, 0.08)
            RECT_ANNULER = fct.rectDrawImageBotRight((cst.w-xoffset, 3*cst.h/4-yoffset), ANNULER, 0.08)

        if indicText:
            fct.drawImageTopRight((cst.w-xoffset, RECT_NEXTTURN.bottom+yoffset), IndicTextsurface, 0.04)

        if echangeBanque:
            pygame.draw.rect(cst.fenetre, (211,211,211), Rect(cst.w/4, cst.yoff, cst.w/2, cst.h-2*cst.xoff))
            donTextsurface = basefont.render("Don", False, (0,0,0))
            fct.drawImage((cst.w/4+2*cst.w/10, cst.yoff+yoffset), donTextsurface, 0.035)
            tauxTextsurface = basefont.render("Taux", False, (0,0,0))
            fct.drawImage((cst.w/4+3*cst.w/10, cst.yoff+yoffset), tauxTextsurface, 0.035)
            banqueTextsurface = basefont.render("Reçu", False, (0,0,0))
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
                    echangeJoueurs = False
                    indicText = False
                    catan.tourSuivant()
                elif RECT_COLONIE.collidepoint(event.pos):
                    if joueurActuel.ressourceSuffisante(np.array([1,1,1,1,0])):
                        print("Colonie")
                        constructionColonie = True
                        constructionVille = False
                        constructionRoute = False
                        carteDeveloppement = False
                        echangeBanque = False
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
                        echangeJoueurs = False
                        indicText = False
                        edges_available = [False for i in range(len(edges))]
                    else:
                        print("Impossible de construire")
                        indicText = True
                        IndicTextsurface = basefont.render("Pas assez de ressource", False, (255,0,0))
                elif RECT_CARTEDEV.collidepoint(event.pos): #TODO
                    print("CarteDev")
                    constructionColonie = False
                    constructionVille = False
                    constructionRoute = False
                    carteDeveloppement = True
                    echangeBanque = False
                    echangeJoueurs = False
                    indicText = False
                elif RECT_ECHANGEBANQUE.collidepoint(event.pos):
                    print("Echange Banque")
                    constructionColonie = False
                    constructionVille = False
                    constructionRoute = False
                    carteDeveloppement = False
                    echangeBanque = True
                    echangeJoueurs = False
                    indicText = False
                elif RECT_ECHANGEJOUEURS.collidepoint(event.pos):
                    print("Echange Joueurs")
                    constructionColonie = False
                    constructionVille = False
                    constructionRoute = False
                    carteDeveloppement = False
                    echangeBanque = False
                    echangeJoueurs = True
                    indicText = False
                elif RECT_ANNULER.collidepoint(event.pos):
                    print("Annuler")
                    constructionColonie = False
                    constructionVille = False
                    constructionRoute = False
                    carteDeveloppement = False
                    echangeBanque = False
                    echangeJoueurs = False
                    indicText = False
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
                                echangeJoueurs = False
                                indicText = False
                        if constructionVille:
                            if catan.construireVille(joueurActuel, vertices_coords[i]):
                                constructionColonie = False
                                constructionVille = False
                                constructionRoute = False
                                carteDeveloppement = False
                                echangeBanque = False
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
                                echangeJoueurs = False
                                indicText = False

        pygame.display.update()

def resetRect():
    global RECT_MAIN, RECT_NEXTTURN, RECT_BRICKIMAGE, RECT_STONEIMAGE, RECT_WHEATIMAGE, RECT_WOODIMAGE, RECT_WOOLIMAGE, RECT_PVIMAGE, RECT_COLONIE, RECT_VILLE, RECT_ROUTE, RECT_CARTEDEV, RECT_ANNULER, RECT_ECHANGEBANQUE, RECT_ECHANGEJOUEURS, RECTS_TILES, RECTS_VERTICES, RECTS_EDGES

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

def drawColonie(center_coords, joueur):
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
    a = 0.05
    if joueur == 0:
        fct.drawImage(center_coords, VILLE_J1, a)
    elif joueur == 1:
        fct.drawImage(center_coords, VILLE_J2, a)
    elif joueur == 2:
        fct.drawImage(center_coords, VILLE_J3, a)
    elif joueur == 3:
        fct.drawImage(center_coords, VILLE_J4, a)