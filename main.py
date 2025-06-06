# Exemple d'utilisation
from forestFire import Carte
from forestFireSimulator import forestFireSimulator

if __name__ == "__main__":
    carte = Carte()
    simulateur = forestFireSimulator(carte)
    simulateur.afficher_carte()
    simulateur.propager_feu(2 ,4)