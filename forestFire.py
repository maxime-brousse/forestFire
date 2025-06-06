import random


class Carte:
    def __init__(self, taille=5):
        self.taille = taille
        self.elements_possibles = ['N', 'A', 'E']
        self.grille = self.generer_carte()

    def generer_carte(self, proba_arbre=0.6):
        proba_eau = 0.2
        proba_vide = 1 - proba_arbre - proba_eau
        if proba_vide < 0:
            raise ValueError("Les probabilités sont trop failbe. Elles doivent totaliser au maximum 1.")
        if proba_vide > 1 or proba_arbre < 0:
            raise ValueError("Les probabilités sont trop élévé. Elle doivent totaliser au maximun 1")

        # Construction de la liste pondérée
        elements = (
                ['F'] * int(proba_arbre * 100) +
                ['E'] * int(proba_eau * 100) +
                ['N'] * int(proba_vide * 100)
        )

        self.grille = [
            [random.choice(elements) for _ in range(self.taille)]
            for _ in range(self.taille)
        ]

    def afficher(self):
        for ligne in self.grille:
            print(' '.join(ligne))