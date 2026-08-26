class ObjetIntrouvableError(Exception):
    pass


class Objet:
    def __init__(self, nom: str, valeur: float):
        self.nom = nom
        self.valeur = valeur

    def __str__(self):
        return f"objet({self.nom}, {self.valeur})"


class Inventaire:
    def __init__(self):
        self.objets = []

    def ajouter(self, objet: Objet):
        self.objets.append(objet)

    def retirer(self, nom_objet: str):
        for objet in self.objets:
            if objet.nom == nom_objet:
                self.objets.remove(objet)
                return
        raise ObjetIntrouvableError("aucun objet trouvé")

    def valeur_totale(self) -> float:
        totale = 0
        for objet in self.objets:
            totale += objet.valeur
        return totale


def main():
    test = Inventaire()
    objet1 = Objet("PC", 240000)
    objet2 = Objet("portable", 50000)
    objet3 = Objet("livre", 1200)
    test.ajouter(objet1)
    test.ajouter(objet2)
    test.ajouter(objet3)

    print(test.valeur_totale())
    test.retirer("PC")

    print(test.valeur_totale())


    try:
        test.retirer("imprimante")
    except ObjetIntrouvableError as e:
        print(f"erreur: {e}")


if __name__ == "__main__":
    main()
