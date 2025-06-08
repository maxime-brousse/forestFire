import unittest
from copy import deepcopy
from forestFireSimulator import forestFireSimulator


class FakeCarte:
    def __init__(self, grille):
        self.grille = deepcopy(grille)
        self.taille = len(grille)

    def generer_carte(self, *args, **kwargs):
        pass  # Ne sert pas pour les tests


class TestPropagationFeu(unittest.TestCase):

    def propager(self, grille, x, y):
        carte = FakeCarte(grille)
        simulateur = forestFireSimulator(carte)
        return simulateur.propager_feu(x, y)


    def test_feu_isole(self):
        grille = [
            ['N', 'N', 'N'],
            ['N', 'F', 'N'],
            ['N', 'N', 'N']
        ]
        attendu = [
            ['N', 'N', 'N'],
            ['N', 'X', 'N'],
            ['N', 'N', 'N']
        ]
        self.assertEqual(self.propager(grille, 1, 1), attendu)

    def test_propagation_croix(self):
        grille = [
            ['N', 'F', 'N'],
            ['F', 'F', 'F'],
            ['N', 'F', 'N']
        ]
        attendu = [
            ['N', 'X', 'N'],
            ['X', 'X', 'X'],
            ['N', 'X', 'N']
        ]
        self.assertEqual(self.propager(grille, 1, 1), attendu)

    def test_propagation_diagonale(self):
        grille = [
            ['F', 'N', 'F'],
            ['N', 'F', 'N'],
            ['F', 'N', 'F']
        ]
        attendu = [
            ['X', 'N', 'X'],
            ['N', 'X', 'N'],
            ['X', 'N', 'X']
        ]
        self.assertEqual(self.propager(grille, 1, 1), attendu)

    def test_bloc_eau(self):
        grille = [
            ['F', 'E', 'F'],
            ['E', 'F', 'E'],
            ['F', 'E', 'F']
        ]
        attendu = [
            ['X', 'E', 'X'],
            ['E', 'X', 'E'],
            ['X', 'E', 'X']
        ]
        self.assertEqual(self.propager(grille, 1, 1), attendu)

    def test_coin_superieur_gauche(self):
        grille = [
            ['F', 'F'],
            ['F', 'N']
        ]
        attendu = [
            ['X', 'X'],
            ['X', 'N']
        ]
        self.assertEqual(self.propager(grille, 0, 0), attendu)

    def test_aucun_arbre(self):
        grille = [
            ['N', 'E'],
            ['E', 'N']
        ]
        attendu = [
            ['N', 'E'],
            ['E', 'N']
        ]
        self.assertEqual(self.propager(grille, 0, 0), attendu)

    def test_tout_brule(self):
        grille = [
            ['F', 'F', 'F'],
            ['F', 'F', 'F'],
            ['F', 'F', 'F']
        ]
        attendu = [
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'X', 'X']
        ]
        self.assertEqual(self.propager(grille, 1, 1), attendu)

    def test_position_invalide(self):
        grille = [
            ['F', 'F'],
            ['F', 'F']
        ]
        attendu = [
            ['F', 'F'],
            ['F', 'F']
        ]
        self.assertEqual(self.propager(grille, -1, -1), attendu)
        self.assertEqual(self.propager(grille, 5, 5), attendu)


if __name__ == '__main__':
    unittest.main()
