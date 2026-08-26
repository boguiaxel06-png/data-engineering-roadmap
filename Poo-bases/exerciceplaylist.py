class ChansonIntrouvableError(Exception):
    pass


class PlaylistVideError(Exception):
    pass


class Chanson:
    def __init__(self, titre: str, duree_seconde: int):
        self.titre = titre
        self.duree_seconde = duree_seconde

    def __str__(self):
        return f"Titre: {self.titre} -- Duree; {self.duree_seconde}"


class Playlist:
    def __init__(self, nom):
        self.nom = nom
        self.chansons = []

    def ajouter(self, chanson: Chanson):
        self.chansons.append(chanson)

    def retirer(self, titre: str):
        for chanson in self.chansons:
            if chanson.titre == titre:
                self.chansons.remove(chanson)
                return
        raise ChansonIntrouvableError("cette chanson n'existe pas dans la playlist")

    def duree_totale(self) -> int:
        totale = 0
        for chanson in self.chansons:
            totale += chanson.duree_seconde 
        return totale

    def chanson_la_plus_longue(self) -> Chanson:
        if not self.chansons:
            raise PlaylistVideError("cette playlist ne contient aucune chanson")

        plus_longue_chanson = self.chansons[0]
        for chanson in self.chansons:
            if chanson.duree_seconde >= plus_longue_chanson.duree_seconde:
                plus_longue_chanson = chanson
        return plus_longue_chanson


def main():
    test = Playlist("smooth")
    chanson1 = Chanson("La vie de Jhonny", 183)
    chanson2 = Chanson("Backstage", 160)
    chanson3 = Chanson("Nostalgie", 175)
    chanson4 = Chanson("kietu", 178)
    test.ajouter(chanson1)
    test.ajouter(chanson2)
    test.ajouter(chanson3)
    test.ajouter(chanson4)

    print(test.duree_totale())
    print(test.chanson_la_plus_longue().titre)

    test.retirer("Backstage")
    print(test.duree_totale())


    try:
        test.retirer("Dis moi que tu m'aime")
    except ChansonIntrouvableError as e:
        print(f"Erreur: {e}")


if __name__ == "__main__":
    main()

