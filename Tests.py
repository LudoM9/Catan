"""
Module permettant de réaliser des tests unitaires et ainsi vérifier le bon fonctionnement des fonctions, instanciations et méthodes des modules.
"""

import unittest
import Joueur
import Plateau


class TestJoueur(unittest.TestCase):
    def test_init(self):
        plateau = Plateau.Plateau()
        nom, numero = "Guido", 1
        joueur = Joueur.Joueur(nom, numero, plateau)
        self.assertEqual(joueur.nom, nom)
        self.assertEqual(joueur.numero, numero)
        self.assertEqual(joueur.__plateau, plateau)
        self.assertFalse(joueur.plusGrandeRoute)
        self.assertFalse(joueur.plusGrandeArmee)
        self.assertIsInstance(joueur, Joueur.Joueur)

    def test_achatCarteDev(self):
        plateau = Plateau.Plateau()
        nom, numero = "Guido", 1
        joueur = Joueur.Joueur(nom, numero, plateau)
        top_card=joueur.__plateau.pioche.devCards[-1]
        joueur.ressource=np.array([1,1,1,1,1])
        old_ressources=joueur.ressource
        new_ressource=old_ressources-joueur.__plateau.CarteDeveloppement.coût
        joueur.achatCarteDev()
        self.assertEqual(joueur.carteDev[-1],top_card)
        self.assertEqual(joueur.ressource, old_ressource)

    def test_victoire(self):
        plateau = Plateau.Plateau()
        nom1, numero1 = "Guido", 1
        nom2, numero2 = "Rossum", 2
        joueur1 = Joueur.Joueur(nom1, numero1, plateau)
        joueur2 = Joueur.Joueur(nom2, numero2, plateau)
        joueur1.pointsVictoire=2
        joueur2.pointsVictoire=10
        self.assertFalse(joueur1.victoire())
        self.assertTrue(joueur2.victoire())

    def test_lancerDés(self):
        plateau = Plateau.Plateau()
        nom, numero = "Guido", 1
        joueur = Joueur.Joueur(nom, numero, plateau)
        resultat=joueur.lancerDés()
        univers=[2,3,4,5,6,8,9,10,11,12]
        self.assertIs(resultat, int)
        self.assertIn(resultat,univers)

if __name__ == '__main__':
    unittest.main()
