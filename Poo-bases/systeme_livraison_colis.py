from abc import ABC, abstractmethod
class TropDeColisErreur(Exception):
    pass


class TropDeColisFragileError(Exception):
    pass


class PoidsMaxDEpasseError(Exception):
    pass


class Colis:
    def __init__(self, nom: str, poids: float, destination: str, est_fragile: bool = False):
        self.poids = poids
        self.destination = destination
        self.est_fragile = est_fragile
        self.nom = nom

    def __str__(self) -> str:
        return (f" COLIS: {self.nom} -- POIDS: {self.poids}kg -- EST CE FRAGILE {self.est_fragile}")

    def __eq__(self, autre) -> bool:
        if self.poids == autre.poids and self.destination == autre.destination:
            return True
        else:
            return False

    def __lt__(self, autre) -> bool:
        if self.poids < autre.poids:
            return True
        else:
            return False

    def frais_manutention(self) -> float:
        if self.est_fragile == True:
            return self.poids * 0.5
        else:
            return 0.0


class Livreur(ABC):
    def __init__(self, pseudo: str, numero: int):
        self.pseudo = pseudo
        self.numero = numero

    @abstractmethod
    def calculer_cout(self, colis_livres: list) -> float:
        pass


class LivreurVelo(Livreur):
    def __init__(self, pseudo: str, numero: int):
        super().__init__(pseudo, numero)
        self.capacite_poids = 15.0  # en kg
        self.capacite_colis_max = 5
        self.capacite_fragiles_max = 2
        self.tarif_par_colis = 500  # en FCFA
        self.tarif_au_kg = 300  # en FCFA

    def calculer_cout(self, colis_livres: list) -> str:
        nb_colis = len(colis_livres)
        total_poids = 0
        somme_frais = 0
        compteur_colis_fragile = 0
        for colis in colis_livres:
            total_poids += colis.poids
            somme_frais += colis.frais_manutention()
            if colis.est_fragile:
                compteur_colis_fragile += 1
        if compteur_colis_fragile > self.capacite_fragiles_max:
            raise TropDeColisFragileError ("impossible d'efectuer cette livraison, vous possedez trop de colis fragile")
        elif nb_colis > self.capacite_colis_max:
            raise TropDeColisErreur ("impossible d'efectuer cette livraison, vous possedez trop de colis")
        elif total_poids > self.capacite_poids:
            raise PoidsMaxDEpasseError ("impossible d'effectuer cette livraison, vous etes en surpoids")
        else:
            cout_total = (total_poids * self.tarif_au_kg) + (nb_colis * self.tarif_par_colis) + somme_frais
            return f"{self.pseudo} a gagner {cout_total}FCFA"


class LivreurMoto(Livreur):
    def __init__(self, pseudo: str, numero: int):
        super().__init__(pseudo, numero)
        self.capacite_poids = 40.0  # en kg
        self.capacite_colis_max = 8
        self.capacite_fragiles_max = 3
        self.tarif_par_colis = 1000  # en FCFA
        self.tarif_au_kg = 200  # en FCFA

    def calculer_cout(self, colis_livres: list) -> str:
        nb_colis = len(colis_livres)
        total_poids = 0
        somme_frais = 0
        compteur_colis_fragile = 0
        for colis in colis_livres:
            total_poids += colis.poids
            somme_frais += colis.frais_manutention()
            if colis.est_fragile:
                compteur_colis_fragile += 1
        if compteur_colis_fragile > self.capacite_fragiles_max:
            raise TropDeColisFragileError ("impossible d'efectuer cette livraison, vous possedez trop de colis fragile")
        elif nb_colis > self.capacite_colis_max:
            raise TropDeColisErreur ("impossible d'efectuer cette livraison, vous possedez trop de colis")
        elif total_poids > self.capacite_poids:
            raise PoidsMaxDEpasseError ("impossible d'effectuer cette livraison, vous etes en surpoids")
        else:
            cout_total = (total_poids * self.tarif_au_kg) + (nb_colis * self.tarif_par_colis) + somme_frais
            return f"{self.pseudo} a gagner {cout_total}FCFA"
        

class LivreurVoiture(Livreur):
    def __init__(self, pseudo: str, numero: int):
        super().__init__(pseudo, numero)
        self.capacite_poids = 150.0  # en kg
        self.capacite_colis_max = 12
        self.capacite_fragiles_max = 4
        self.tarif_par_colis = 1500  # en FCFA
        self.tarif_au_kg = 100  # en FCFA

    def calculer_cout(self, colis_livres: list) -> str:
        nb_colis = len(colis_livres)
        total_poids = 0
        somme_frais = 0
        compteur_colis_fragile = 0
        for colis in colis_livres:
            total_poids += colis.poids
            somme_frais += colis.frais_manutention()
            if colis.est_fragile:
                compteur_colis_fragile += 1
        if compteur_colis_fragile > self.capacite_fragiles_max:
            raise TropDeColisFragileError ("impossible d'efectuer cette livraison, vous possedez trop de colis fragile")
        elif nb_colis > self.capacite_colis_max:
            raise TropDeColisErreur ("impossible d'efectuer cette livraison, vous possedez trop de colis")
        elif total_poids > self.capacite_poids:
            raise PoidsMaxDEpasseError ("impossible d'effectuer cette livraison, vous etes en surpoids")
        else:
            cout_total = (total_poids * self.tarif_au_kg) + (nb_colis * self.tarif_par_colis) + somme_frais
            return f"{self.pseudo} a gagner {cout_total}FCFA"


def main():
    livreur1 = LivreurMoto("elric", 551)
    colis1 = Colis("pull zip", 0.80, "cocody", False)
    colis2 = Colis("television", 3.0, "adzope", True)
    colis3 = Colis("ps5", 2.5, "zone 4", True)
    colis4 = Colis("air force one", 0.45, "bassam", False)

    print(colis1)
    print(colis2)
    print(colis3)
    print(colis4)

    print(livreur1.calculer_cout([colis4, colis3, colis1, colis2]))

    livreur2 = LivreurVoiture("roy", 551)
    livreur3 = LivreurVelo("edward", 551)

    print(livreur2.calculer_cout([colis4, colis3, colis1, colis2]))
    print(livreur3.calculer_cout([colis4, colis3, colis1, colis2]))

    colis5 = Colis("ps4", 2.5, "aboisso", True)
    colis6 = Colis("pc gaming", 2.5, "treicheville", True)
    colis7 = Colis("bouquet de fleur", 2.5, "marcory", True)
    colis8 = Colis("bracelet chrome", 2.5, "adjame", False)
    colis9 = Colis("calculatrice", 2.5, "adjame", False)
    colis10 = Colis("gourde", 2.5, "adjame", False)
    colis11 = Colis("ceinture chrome", 2.5, "adjame", False)


    try:
        print(livreur3.calculer_cout([colis4, colis3, colis1, colis2, colis5, colis6, colis7, colis8]))
    except TropDeColisFragileError as e:
        print(f"Erreur : {e}")

    try: 
        print(livreur1.calculer_cout([colis4, colis8, colis1, colis9, colis5, colis6, colis7, colis10, colis11]))
    except TropDeColisErreur as e:
        print(f"Erreur: {e}") 


if __name__ == "__main__":
    main()
