from forestFire import Carte
from itertools import combinations
from copy import deepcopy

class forestFireSimulator:
    def __init__(self, carte):
        if carte is None:
            self.carte = Carte()
            self.carte.generer_carte(0.6)
        else:
            self.carte = carte

    def afficher_carte(self):
        self.carte.exporter_html("html/carte_apres_feu.html")

    def propager_feu(self, x, y):
        taille = self.carte.taille
        grille = [ligne[:] for ligne in self.carte.grille]  # Copie de la carte

        def feu(x, y):
            if 0 <= x < taille and 0 <= y < taille:
                if grille[x][y] == 'F':
                    grille[x][y] = 'X'  # 'X' = arbre brûlé
                    # 8 directions (y compris diagonales)
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx != 0 or dy != 0:
                                feu(x + dx, y + dy)

        feu(x, y)

        print("\nCarte après incendie :")
        for ligne in grille:
            print(' '.join(ligne))
        return grille

    def propager_feu_test(self, grille, x, y):
        """Version test de la propagation, sans modifier la vraie grille"""
        taille = len(grille)
        copie = [ligne[:] for ligne in grille]

        def feu(i, j):
            if 0 <= i < taille and 0 <= j < taille:
                if copie[i][j] == 'F':
                    copie[i][j] = 'X'
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx != 0 or dy != 0:
                                feu(i + dx, j + dy)

        feu(x, y)
        return copie

    def compter_propagation(self, grille, x, y):
        """Retourne le nombre de cases brûlées à partir de (x, y)"""
        propagation = self.propager_feu_test(grille, x, y)
        return sum(l.count('X') for l in propagation)

    def deboiser_optimise(self, x, y, max_coupes=3):
        if self.carte.grille[x][y] != 'F':
            print("Point de départ invalide (pas un feu)")
            return

        taille = self.carte.taille
        arbres = [
            (i, j)
            for i in range(taille)
            for j in range(taille)
            if self.carte.grille[i][j] == 'F' and (i, j) != (x, y)
        ]
        propagation_min = self.compter_propagation(self.carte.grille, x, y)
        meilleure_combinaison = []
        meilleure_grille = deepcopy(self.carte.grille)

        for n in range(1, max_coupes + 1):
            for combo in combinations(arbres, n):
                test_grille = deepcopy(self.carte.grille)
                for i, j in combo:
                    test_grille[i][j] = 'N'  # on coupe l’arbre
                propagation = self.compter_propagation(test_grille, x, y)
                if propagation < propagation_min:
                    propagation_min = propagation
                    meilleure_combinaison = combo
                    meilleure_grille = test_grille

        if meilleure_combinaison:
            print("Arbres coupés aux positions :", meilleure_combinaison)
        else:
            print("Aucun arbre coupé. Déboisement inutile.")

        self.carte.grille = meilleure_grille