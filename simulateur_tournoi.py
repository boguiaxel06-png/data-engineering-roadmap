class NiveauInvalideError(Exception):
    pass


class NombreJoeurInvalideError(Exception):
    pass


class EquipeVideError(Exception):
    pass


class Player:
    def __init__(self, nom: str, niveau: int):
        self.nom = nom
        self.niveau = niveau

    @property
    def niveau(self) -> int:
        return self._niveau

    @niveau.setter
    def niveau(self, valeur: int) -> int:
        if not 1 <= valeur <= 100:
            raise NiveauInvalideError("niveau invalide")
        else:
            self._niveau = valeur

    def __str__(self):
        return(f"NOM: {self.nom} --- NIVEAU: {self.niveau}")


class Team:
    def __init__(self, nom: str):
        self.nom = nom
        self.player = []

    def ajouter_joueur(self, player: Player) -> str:
        if not len(self.player) >= 11:
            self.player.append(player)        
        else:
            raise NombreJoeurInvalideError("nombre de jouer invalide")

    def niveau_moyen(self) -> float:
        moyenne = 0.0
        somme = 0.0
        compt = 0
        for player in self.player:
            somme += player.niveau
            compt += 1
        return somme / compt

    def meilleur_joueur(self) -> Player:
        if not self.player:
            raise EquipeVideError("cette equipe ne possede aucun joueur")
        best_player = self.player[0]
        for player in self.player:
            if player.niveau >= best_player.niveau:
                best_player = player
        return best_player


class Match:
    def __init__(self, domicile: Team, exterieur: Team):
        self.domicile = domicile
        self.exterieur = exterieur

    def simuler(self) -> str:
        if self.domicile.niveau_moyen() > self.exterieur.niveau_moyen():
            return f"{self.domicile.nom} a gagner"
        elif self.domicile.niveau_moyen() < self.exterieur.niveau_moyen():
            return f"{self.exterieur.nom} a gagner"
        else:
            return "match null"


def main():
    equipe1 = Team("Barcelone")
    equipe2 = Team("Real Madrid")

    joueur1 = Player("Rodri", 90)
    joueur2 = Player("Lamine Yamal", 87)
    joueur3 = Player("Raphina", 89)
    joueur4 = Player("Yan Diomande", 85)
    joueur5 = Player("Dumfries", 84)
    joueur6 = Player("silva", 87)

    equipe1.ajouter_joueur(joueur1)
    equipe1.ajouter_joueur(joueur3)
    equipe1.ajouter_joueur(joueur2)
    print(equipe1.niveau_moyen())
    print(equipe1.meilleur_joueur())

    equipe2.ajouter_joueur(joueur4)
    equipe2.ajouter_joueur(joueur5)
    equipe2.ajouter_joueur(joueur6)
    print(equipe2.niveau_moyen())
    print(equipe2.meilleur_joueur())

    match1 = Match(equipe1, equipe2)
    print(match1.simuler())

    try:
        joueur7 = Player("messi", 1000)
        equipe1.ajouter_joueur(joueur7)
    except NiveauInvalideError as e:
        print(f"Erreur: {e}")
        

if __name__ == "__main__":
    main()
    



