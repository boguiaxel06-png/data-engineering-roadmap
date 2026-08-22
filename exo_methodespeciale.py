class Produit:
    def __init__(self, nom: str, prix: float):
        self.nom = nom
        self.prix = prix

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"produit ({self.nom}, {self.prix} FCFA)"

    def __eq__(self, other) -> bool:
        if self.nom == other.nom and self.prix == other.prix:
            return True
        else: 
            return False

    def __lt__(self,other) -> bool:
        if self.prix < other.prix:
            return True
        else: 
            return False


def main():
    produit1 = Produit("stylo", 400)
    produit2 = Produit("gourde", 7000)
    produit3 = Produit("jus", 500)

    print(produit1)
    print(produit2)
    print(produit3)

    comparaison = produit1 == produit3
    liste_produit = [produit3,produit1,produit2]
    resultat_tris = sorted(liste_produit)

    print(comparaison)
    print(resultat_tris)


if __name__ == "__main__":
    main()
    