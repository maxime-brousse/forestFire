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

    def to_html(self):
        couleurs = {
            'N': '#ffffff',  # blanc pour vide
            'A': '#228B22',  # vert forêt pour arbre
            'E': '#1E90FF'  # bleu pour eau
        }

        html = ['<table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">']
        for ligne in self.grille:
            html.append('<tr>')
            for case in ligne:
                couleur = couleurs.get(case, '#000')  # noir par défaut si caractère inconnu
                html.append(
                    f'<td style="background-color:{couleur}; width:30px; height:30px; text-align:center;">{case}</td>')
            html.append('</tr>')
        html.append('</table>')
        return '\n'.join(html)

    def exporter_html(self, nom_fichier="html/carte.html"):
        html_complet = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Carte Générée</title>
    </head>
    <body>
        <h2>Carte aléatoire {self.taille}x{self.taille}</h2>
        {self.to_html()}
    </body>
    </html>
    """
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(html_complet)