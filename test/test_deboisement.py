import unittest
import pytest

from forestFire import Carte
from forestFireSimulator import forestFireSimulator


class TestDeboisement(unittest.TestCase):

    def test_compter_propagation_normal(self):
        grille = [
            ['N', 'N', 'N'],
            ['N', 'F', 'N'],
            ['N', 'N', 'N']
        ]
        attendu = 1
        simulator = forestFireSimulator(grille)
        self.assertEqual(simulator.compter_propagation(grille, 1, 1), attendu)

    def test_aucun_arbre(self):
        grille = [
            ['N', 'E'],
            ['E', 'N']
        ]
        attendu = 0
        simulator = forestFireSimulator(grille)
        self.assertEqual(simulator.compter_propagation(grille, 0, 0), attendu)

    def test_tout_brule(self):
        grille = [
            ['F', 'F', 'F'],
            ['F', 'F', 'F'],
            ['F', 'F', 'F']
        ]
        attendu = 9
        simulator = forestFireSimulator(grille)
        self.assertEqual(simulator.compter_propagation(grille, 0, 0), attendu)

    def test_position_invalide(self):
        grille = [
            ['F', 'F'],
            ['F', 'F']
        ]
        attendu = 0
        simulator = forestFireSimulator(grille)
        self.assertEqual(simulator.compter_propagation(grille, -1, -1), attendu)
        self.assertEqual(simulator.compter_propagation(grille, 5, 5), attendu)

    def test_deboisement_nomarl(self):
        grille = [
            ['N', 'F', 'F', 'F', 'F'],
            ['F', 'F', 'F', 'F', 'E'],
            ['E', 'F', 'E', 'F', 'E'],
            ['F', 'F', 'F', 'F', 'N'],
            ['F', 'N', 'F', 'F', 'F']
        ]
        attendu = [
            ['N', 'F', 'F', 'F', 'F'],
            ['F', 'F', 'F', 'F', 'E'],
            ['E', 'F', 'E', 'D', 'E'],
            ['F', 'F', 'D', 'F', 'N'],
            ['F', 'N', 'D', 'F', 'F']
        ]
        newCarte = Carte(grille, 5)
        simulator = forestFireSimulator(newCarte)
        self.assertEqual(simulator.carte.grille, grille)

    def test_deboisement_rien(self):
        grille = [
            ['F', 'F', 'F', 'F', 'E'],
            ['F', 'N', 'E', 'F', 'F'],
            ['N', 'N', 'E', 'E', 'F'],
            ['E', 'F', 'E', 'N', 'F'],
            ['F', 'F', 'F', 'E', 'N'],
        ]
        newCarte = Carte(grille, 5)
        simulator = forestFireSimulator(newCarte)
        with pytest.raises(IndexError): simulator.deboiser_optimise(5, 5)


if __name__ == '__main__':
    unittest.main()
