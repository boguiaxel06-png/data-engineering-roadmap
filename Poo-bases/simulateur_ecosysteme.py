from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, nom: str):
        self.nom = nom
        self.energie = 100

    @abstractmethod
    def agir(self, autre: "Creature") -> str:
        pass

    def est_vivante(self) -> bool:
        if self.energie > 0:
            return True
        else:
            return False

    def __str__(self):
        return (f"Nom: {self.nom} -- Energie: {self.energie}")


class Herbivore(Creature):
    def __init__(self, nom: str):
        super().__init__(nom)

    def agir(self, autre: "Creature"):
        if isinstance(autre, Herbivore):
            return f"{self.nom} ignore {autre.nom}"
        else:
            return f"{self.nom} évite {autre.nom}"


class Predateur(Creature):
    def __init__(self, nom: str, puissance: int):
        super().__init__(nom,)
        self.puissance = puissance

    def agir(self, autre):
        if isinstance(autre, Herbivore) and autre.est_vivante():
            self.energie += self.puissance
            autre.energie = max(0, autre.energie - self.puissance)
            return f"{self.nom} chasse {autre.nom}"
        else:
            return f"{self.nom} ignore {autre.nom}"


def main():
    creature1 = Predateur("fleau", 50)
    creature2 = Herbivore("dokaibebi")
    creature3 = Herbivore("pokemon")

    print(creature1.agir(creature2))
    print(creature1)
    print(creature2)

    print(creature1.agir(creature3))
    print(creature1)
    print(creature3)

    print(creature2.agir(creature3))

    creature1.agir(creature2)
    creature1.agir(creature2)
    creature1.agir(creature2)
    print(creature2.est_vivante())


if __name__ == "__main__":
    main()
