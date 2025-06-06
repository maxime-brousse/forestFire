import unittest
from forestFire import Carte


class TestForestFire(unittest.TestCase):
    def test_generation_normale(self):
        """Test de génération standard avec des probabilités valides"""
        carte = Carte()
        carte.generer_carte(0.3)
        self.assertEqual(len(carte.grille), 5)
        for ligne in carte.grille:
            self.assertEqual(len(ligne), 5)
            for case in ligne:
                self.assertIn(case, ['F', 'E', 'N'])

    def test_proba_negative(self):
        """Test avec une probabilité négative (doit échouer)"""
        carte = Carte()
        with self.assertRaises(ValueError):
            carte.generer_carte(-0.3)

    def test_proba_superieure_a_un(self):
        """Test avec des probabilités qui dépassent 1 (doit échouer)"""
        carte = Carte()
        with self.assertRaises(ValueError):
            carte.generer_carte(1.1)

    def test_generation_zero_probabilites(self):
        """Test avec toutes les probabilités à zéro (carte vide uniquement)"""
        carte = Carte()
        carte.generer_carte(0.0)
        for ligne in carte.grille:
            for case in ligne:
                self.assertIn(case, ['N', 'E'])


if __name__ == '__main__':
    unittest.main()