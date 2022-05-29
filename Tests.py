"""
Module permettant de réaliser des tests unitaires et ainsi vérifier le bon fonctionnement des fonctions, instanciations et méthodes des modules.
"""

import unittest
import Catan
import Joueur
import Plateau
import numpy as np

class TestCatan(unittest.TestCase):
    def test_init(self):
        joueurs = ["Jeep", "Luka", "Nico"]
        catan = Catan.Catan(joueurs)
        for i in range(3):
            self.assertEqual(catan.joueurs[i].nom,Joueur.Joueur(joueurs[i],i,catan.plateau).nom)
            self.assertEqual(catan.joueurs[i].numero,Joueur.Joueur(joueurs[i],i,catan.plateau).numero)
        self.assertIsInstance(catan, Catan.Catan)
        self.assertEqual(catan.joueurActuel, catan.joueurs[catan.numeroJoueurActuel])

    def test_lancerDes(self):
        joueurs = ["Jeep", "Luka", "Nico"]
        catan = Catan.Catan(joueurs)
        univers = [2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12]
        catan.lancerDes()
        self.assertIn(catan.valeurDes, univers)
        self.assertIsInstance(catan.valeurDes, int)

    def test_deplacerVoleur(self):
        joueurs = ["Jeep", "Luka", "Nico"]
        catan = Catan.Catan(joueurs)
        coords=(-1,1)
        anciennesRessources=np.sum(catan.joueurActuel.ressource)
        self.assertFalse(catan.deplacerVoleur(catan.joueurActuel,catan.plateau.voleur.coords))
        self.assertTrue(catan.deplacerVoleur(catan.joueurActuel,coords))
        self.assertEqual(catan.plateau.voleur.coords,coords)
        self.assertGreater(np.sum(catan.joueurActuel.ressource),anciennesRessources-1)

    def test_ajoutPort(self):
        joueurs = ["Jeep", "Luka", "Nico"]
        catan = Catan.Catan(joueurs)
        vertice=(-2,-2)
        nbPorts=len(catan.joueurActuel.ports)
        catan.ajoutPort(catan.joueurActuel,vertice)
        self.assertGreater(len(catan.joueurActuel.ports),nbPorts)

    def test_echangeBanque(self):
        joueurs = ["Jeep", "Luka", "Nico"]
        catan = Catan.Catan(joueurs)
        self.assertFalse(catan.echangeBanque(catan.joueurActuel,np.array([4,0,0,0,0]),np.array([0,1,0,0,0])))
        catan.joueurActuel.ressource=np.array([4,0,0,0,0])
        self.assertTrue(catan.echangeBanque(catan.joueurActuel,np.array([4,0,0,0,0]),np.array([0,1,0,0,0])))

    def test_echangeJoueur(self):
        joueurs = ["Jeep", "Luka", "Nico"]
        catan = Catan.Catan(joueurs)
        self.assertFalse(catan.echangeJoueur(catan.joueurs[0],catan.joueurs[1],np.array([1,0,0,0,0]),np.array([0,1,0,0,0])))
        catan.joueurs[0].ressource=np.array([1,0,0,0,0])
        catan.joueurs[1].ressource=np.array([0,1,0,0,0])
        self.assertTrue(catan.echangeJoueur(catan.joueurs[0],catan.joueurs[1],np.array([1,0,0,0,0]),np.array([0,1,0,0,0])))

    def test_tourSuivant(self):
        joueurs = ["Jeep", "Luka", "Nico"]
        catan = Catan.Catan(joueurs)
        Numjoueurs=[0,1,2]
        for i in range(4):
            catan.tourSuivant()
            self.assertIn(catan.numeroJoueurActuel,Numjoueurs)
            self.assertEqual(catan.joueurActuel,catan.joueurs[catan.numeroJoueurActuel])

    def test_tourSuivantDebut(self):
        joueurs = ["Jeep", "Luka", "Nico"]
        catan = Catan.Catan(joueurs)
        for i in range(5):
            catan.tourSuivantDebut()
            self.assertEqual(catan.numeroJoueurActuelDebut,i+1)
        self.assertTrue(catan.tourSuivantDebut())

    def test_calculPlusGrandeArmee(self):
        joueurs = ["Jeep", "Luka", "Nico"]
        catan = Catan.Catan(joueurs)

class TestJoueur(unittest.TestCase):
    def test_init(self):
        pass

    def test_calculValeurEchange(self):
        pass

    def test_ressourceSuffisante(self):
        pass

    def test_colonieExiste(self):
        pass

    def test_getColonie(self):
        pass

    def test_nombreChevalier(self):
        pass

    def test_calculPV(self):
        pass

    def test_victoire(self):
        plateau = Plateau.Plateau()
        nom1, numero1 = "Guido", 0
        joueur = Joueur.Joueur(nom1, numero1, plateau)
        self.assertFalse(joueur.victoire())
        pioche=Plateau.Pioche()
        joueur.carteDev=[Plateau.DevPV(joueur),Plateau.DevPV(joueur),Plateau.DevPV(joueur),Plateau.DevPV(joueur),Plateau.DevPV(joueur),Plateau.DevPV(joueur),Plateau.DevPV(joueur),Plateau.DevPV(joueur),Plateau.DevPV(joueur),Plateau.DevPV(joueur)]
        self.assertTrue(joueur.victoire())

class TestPlateau(unittest.TestCase):
    def test_init(self):
        pass

class TestPioche(unittest.TestCase):
    def test_init(self):
        pioche=Plateau.Pioche()
        nbCartesDev_test=[0,0,0,0,0]
        nbCartesDev_reel=[2,2,2,14,5]
        for card in pioche.devCards:
            if type(card)==Plateau.DevConstructionDeRoutes:
                nbCartesDev_test[0]+=1
            elif type(card)==Plateau.DevInvention:
                nbCartesDev_test[1]+=1
            elif type(card)==Plateau.DevMonopole:
                nbCartesDev_test[2]+=1
            elif type(card)==Plateau.DevChevalier:
                nbCartesDev_test[3]+=1
            elif type(card)==Plateau.DevPV:
                nbCartesDev_test[4]+=1
        self.assertEqual(nbCartesDev_test,nbCartesDev_reel)

if __name__ == '__main__':
    unittest.main()
