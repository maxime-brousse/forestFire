# Exemple d'utilisation
from forestFire import Carte

if __name__ == "__main__":
    carte = Carte()
    carte.generer_carte(0.6)
    carte.exporter_html()
    print("export prêt")
