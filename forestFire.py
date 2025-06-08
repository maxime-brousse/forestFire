import random


def to_html(grille):
    html = ['<table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">']
    for ligne in grille:
        html.append('<tr>')
        for case in ligne:
            match case:
                case "N":
                    html.append(
                        f'<td style="width:30px; height:30px; text-align:center;">&#128507;</td>')
                case "D":
                    couleur = '#964B00'
                    html.append(
                        f'<td style="background-color:{couleur}; width:30px; height:30px; text-align:center;">&#128507;</td>')
                case "F":
                    html.append(
                        f'<td style="width:30px; height:30px; text-align:center;">&#127794;</td>')
                case "E":
                    html.append(
                        f'<td style="width:30px; height:30px; text-align:center;">&#128167;</td>')
                case "X":
                    html.append(
                        f'<td style="width:30px; height:30px; text-align:center;">&#128293;</td>')
        html.append('</tr>')
    html.append('</table>')
    return '\n'.join(html)


class Carte:
    def __init__(self, taille=5):
        self.taille = taille
        self.elements_possibles = ['N', 'A', 'E']
        self.grille = None
        self.generer_carte()

    def __init__(self, grille, taille):
        self.grille = grille
        self.taille = taille
        self.elements_possibles = ['N', 'A', 'E']

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
        {to_html(self.grille)}
    </body>
    </html>
    """
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(html_complet)

    def exporter_apres_html(self, grille,  meilleurs, max_coupes, prog_min, nom_fichier="html/carte_apres.html"):
        html_complet = f"""
            <!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <title>Carte Générée</title>
            </head>
            <body>
                <h2>grille de départ :</h2>
                {to_html(grille)}
                <h2>Meilleure grille (zones marrons déboisés) :</h2>
                {to_html(self.grille)}
                <div>
                    <p>Nombres de coupes : {max_coupes}</p>
                    <p>Propagation minimun : {prog_min}</p>
                    <p>Meilleures coupes : {meilleurs}</p>
                </div>
            </body>
            </html>
            """
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(html_complet)
