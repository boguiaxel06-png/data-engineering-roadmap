class Personnage:
    def __init__(self, nom: str, points_de_vie: int):
        self.nom = nom
        self.points_de_vie = points_de_vie

    @property
    def points_de_vie(self) -> int:
        return self._points_de_vie

    @points_de_vie.setter
    def points_de_vie(self, valeur: int):
        if valeur < 0:
            valeur = 0
        self._points_de_vie = valeur

    def se_presenter(self):
        print(f"je suis {self.nom}, j'ai {self.points_de_vie} PV")

    def subir_degats(self, degats):
        if degats < 0:
            raise ValueError("Les dégâts ne peuvent pas être négatifs.")
        
        self.points_de_vie -= degats 
        

class Guerrier(Personnage):
    def __init__(self, nom: str, points_de_vie: int, force: int):
        super().__init__(nom, points_de_vie)
        self.force = force

    @property
    def force(self)-> int:
        return self._force

    @force.setter
    def force(self, valeur):
        if valeur < 0:
            raise ValueError("la force ne peut pas etre negative")
        self._force = valeur

    def attaquer(self, cible):
        cible.subir_degats(self.force)
        print(f"{self.nom} attaque {cible.nom} et inflige {self.force} dégâts.")

    def se_presenter(self):
        super().se_presenter()
        print(f"Ma force est de {self.force}.")


def main():
    print("test de personnage")
    personnage1 = Personnage("Alice", 100)
    personnage2 = Personnage("Bob", 100)

    personnage1.se_presenter()
    personnage2.se_presenter()

    personnage1.subir_degats(20)
    personnage2.subir_degats(30)

    personnage1.se_presenter()
    personnage2.se_presenter()

    print("test de guerrier")

    guerrier1 = Guerrier("Conan", 120, 25)
    personnageA = Personnage("Goblin", 80)

    guerrier1.se_presenter()
    personnageA.se_presenter()
    guerrier1.attaquer(personnageA)
    personnageA.se_presenter()


if __name__ == "__main__":
    main()  
   
