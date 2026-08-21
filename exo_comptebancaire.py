class MontantInvalideError(Exception):
    pass


class SoldeInsuffisantError(Exception):
    pass


class CompteBancaire:
    def __init__(self, titulaire: str, solde: float = 0.0):
        self.titulaire = titulaire
        self._solde = solde

    @property
    def solde(self) -> float:
        return self._solde

    def deposer(self, montant: float):
        if montant <= 0.0:
            raise MontantInvalideError("le montant deposer n'est pas valide")
        self._solde += montant

    def retirer(self, montant: float):
        if montant <= 0.0:
            raise MontantInvalideError("le montant a retirer n'est pas valide")
        if montant > self.solde:
            raise SoldeInsuffisantError("solde insuffisant")
        self._solde -= montant

    @classmethod
    def compte_vide(cls, titulaire):
        return cls(titulaire)  


def main():
    compte = CompteBancaire("Test", 100.0)
    compte.deposer(50)
    compte1 = CompteBancaire.compte_vide("paul")
    print(compte1.solde)
    print(compte.solde)

    try: 
        compte1.deposer(-50000)
    except MontantInvalideError as e:
        print(f"erreur: {e}")

        
    try:
        compte.retirer(1400000)
    except SoldeInsuffisantError as e:
        print(f"erreur: {e}")


if __name__ == "__main__":
    main()
