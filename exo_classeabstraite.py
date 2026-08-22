from abc import ABC, abstractmethod

class MoyenPaiement(ABC):
    def __init__(self, titulaire: str):
        self.titulaire = titulaire

    @abstractmethod
    def payer(self, montant: float):
        pass


class CarteBancaire(MoyenPaiement):
    def __init__(self, titulaire: str, code: int):
        super(). __init__(titulaire)
        self.code = code

    def payer(self, montant: float):
        print(f"paiement de {montant}FCFA par carte bancaire {self.titulaire}")


class Especes(MoyenPaiement):
    def __init__(self, titulaire: str):
        super().__init__(titulaire)

    def payer(self, montant: float):
        print(f"paiement de {montant}FCFA en especes {self.titulaire}")


def main():
    test = [CarteBancaire("Ryan", 10958), Especes("Jean-paul")]
    for element in test:
        element.payer(50)


    try:
        essais = MoyenPaiement("Marie")
    except TypeError as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    main()

#mais ici je n'ai pas creer l'erreur personnaliser en haut est ce correcte


    


            


        


     
