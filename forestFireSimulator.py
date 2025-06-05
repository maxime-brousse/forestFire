from forestFire import Carte

class forestFireSimulator:
    def __init__(self, carte):
        if carte is None:
            self.carte = Carte()
            self.carte.generer_carte(0.6)
        else:
            self.carte = carte

    def afficher_carte(self):
        self.carte.afficher()

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