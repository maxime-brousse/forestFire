# Exemple d'utilisation
from forestFire import Carte
from forestFireSimulator import forestFireSimulator

if __name__ == "__main__":
    carte = Carte()
    simulateur = forestFireSimulator(carte)
    simulateur.afficher_carte()
    simulateur.propager_feu(0 ,0)

    simulateur.deboiser_optimise(0, 0, max_coupes=2)

    print("\nAprès déboisement optimisé :")
    carte.afficher()