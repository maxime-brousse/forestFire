# Exemple d'utilisation
from forestFire import Carte
from forestFireSimulator import forestFireSimulator

if __name__ == "__main__":
    carte = Carte()
    simulateur = forestFireSimulator(carte)
    simulateur.deboiser_optimise(3, 3)

    print("\n Après déboisement optimisé :")
    carte.afficher()