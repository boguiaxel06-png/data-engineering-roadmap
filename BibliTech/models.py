from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, titre: str, auteur: str, isbn: str, disponible: bool = True):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn 
        self.disponible = disponible

    @property
    def isbn(self):
        return self._isbn
 
    def str(self):
        return f"Titre :{self.titre}\nAuteur : {self.auteur}\n"

    def afficher_details(self) -> str:
        print(f"Titre       : {self.titre}")
        print(f"Auteur      : {self.auteur}")
        print(f"ISBN        : {self.isbn}")
        print(f"Disponible  : {'Oui' if self.disponible else 'Non'}")

    @abstractmethod
    def calculer_tarif_emprumt(self, jour: int) -> float:
        pass

    def to_dict(self) -> dict:
        return {
            "Titre" == self.titre,
            "Auteur" == self.auteur,
            "Isbn" == self.isbn,
            "Disponible" == self.disponible
        }


class Livre(Document):
    def __init__(self, titre: str, auteur: str, isbn: str, nb_pages: int, disponible: bool = True):
        super().__init__(titre, auteur, isbn, disponible)
        self.nb_pages = nb_pages

    @property
    def nb_pages(self) -> int:
        return self._nb_pages

    @nb_pages.setter
    def nb_pages(self, valeur: int):
        if valeur < 1:
            raise ValueError("Nombres de pages invalide")
        else:
            self._nb_pages = valeur
        

    def calculer_tarif_emprumt(self, jour):
        return jour * 150
    
    def to_dict(self) -> dict:
        data = super().to_dict()
        data["Type"] = "Livre"
        data["Nb_page"] = self.nb_pages
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Livre":
        return cls(
            Titre = data["titre"],
            Auteur = data["auteur"],
            Isbn = data["isbn"],
            Disponible = data["disponible"],
            Nb_pages = data["nb_pages"]
        )


class Dvd(Document):
    def __init__(self, titre: str, auteur: str, isbn: str, duree_minutes: int, disponible: bool = True):
        super().__init__(titre, auteur, isbn, disponible)
        self.duree_minutes = duree_minutes

    @property
    def duree_minutes(self) -> int:
        return self._duree_minutes
    
    @duree_minutes.setter
    def duree_minutes(self, valeur: int):
        if valeur < 1:
            raise ValueError("Nombres de minute invalide")
        else:
            self._duree_minutes = valeur

    def calculer_tarif_emprumt(self, jour):
        pass # l'ennoncer est bizarre je dois ajouter un attribut hd??

    def to_dict(self) -> dict:
        data = super().to_dict
        data["Type"] = "Dvd"
        data["Duree_minutes"] = self.duree_minutes
        return data

    @classmethod #je ne sais toujours pas a quel moment il faut l'utiliser , donner des exemples dans d'autres cas ou on l'utilise
    def from_dict(cls, data: dict) -> "Dvd":
        return cls(
            Titre = data["titre"],
            Auteur = data["auteur"],
            Isbn = data["isbn"],
            Disponible = data["disponible"],
            Duree_minutes = data["duree_minutes"]
        )

    