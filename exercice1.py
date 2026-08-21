class Personnage:
    def __init__(self, nom: str, points_de_vie: int):
        self.nom = nom
        self.points_de_vie = points_de_vie

    def se_presenter(self):
        print(f"je suis {self.nom}, j'ai {self.points_de_vie} PV")

    def subir_degats(self, degats):
        if degats < 0:
            raise ValueError("Les dégâts ne peuvent pas être négatifs.")
        
        self.points_de_vie = max(0, self.points_de_vie - degats) 
        

def main():
    personnage1 = Personnage("Alice", 100)
    personnage2 = Personnage("Bob", 100)

    personnage1.se_presenter()
    personnage2.se_presenter()

    personnage1.subir_degats(20)
    personnage2.subir_degats(30)

    personnage1.se_presenter()
    personnage2.se_presenter()

if __name__ == "__main__":
    main()  