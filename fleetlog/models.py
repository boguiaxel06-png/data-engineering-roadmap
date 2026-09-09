from abc import ABC, abstractmethod
from exceptions import KilometrageInvalideError, ImmatriculationInvalideError


class Vehicule(ABC):
    def __init__(self, immatriculation: str, marque: str, kilometrage: float, capacite_charge_kg: float):
        self.immatriculation = immatriculation
        self.marque = marque
        self.kilometrage = kilometrage
        self.capacite_charge_kg = capacite_charge_kg

    @property
    def immatriculation(self) -> str:
        return self._immatriculation

    @immatriculation.setter
    def immatriculation(self, valeur: str):
        if not valeur or valeur.strip() == "":
            raise ImmatriculationInvalideError("L'immatriculation ne peut pas être vide.")
        self._immatriculation = valeur

    @property
    def kilometrage(self) -> float:
        return self._kilometrage

    @kilometrage.setter
    def kilometrage(self, valeur: float):
        if valeur < 0:
            raise KilometrageInvalideError("Le kilométrage ne peut pas être négatif.")
        
        if hasattr(self, "_kilometrage") and valeur < self._kilometrage:
            raise KilometrageInvalideError("Le kilométrage ne peut pas être inférieur au kilométrage actuel.")

        self._kilometrage = valeur

    @abstractmethod
    def calculer_cout_entretien(self) -> float:
        pass

    def ajouter_trajet(self, km_parcourus: float):
        if km_parcourus < 0:
            raise KilometrageInvalideError("Les kilomètres parcourus ne peuvent pas être négatifs.")
        self.kilometrage += km_parcourus

    def to_dict(self) -> dict:
        return {
            "immatriculation": self.immatriculation,
            "marque": self.marque,
            "kilometrage": self.kilometrage,
            "capacite_charge_kg": self.capacite_charge_kg
        }


class Camion(Vehicule):
    def __init__(self, immatriculation: str, marque: str, kilometrage: float, capacite_charge_kg: float, nombre_essieux: int):
        super().__init__(immatriculation, marque, kilometrage, capacite_charge_kg)
        self.nombre_essieux = nombre_essieux

    def calculer_cout_entretien(self) -> float:
        resultat = (self.kilometrage * 0.15) + (self.nombre_essieux * 5000)
        return resultat

    def to_dict(self) -> dict:
        data = super().to_dict()  
        data["type"] = "Camion"
        data["nombre_essieux"] = self.nombre_essieux
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Camion":
        return cls(
            immatriculation=data["immatriculation"],
            marque=data["marque"],
            kilometrage=data["kilometrage"],
            capacite_charge_kg=data["capacite_charge_kg"],
        nombre_essieux=data["nombre_essieux"]
        )


class Fourgonnette(Vehicule):
    def __init__(self, immatriculation: str, marque: str, kilometrage: float, capacite_charge_kg: float, refrigerated: bool = False):
        super().__init__(immatriculation, marque, kilometrage, capacite_charge_kg)
        self.refrigerated = refrigerated

    def calculer_cout_entretien(self) -> float:
        if self.refrigerated:
            resultat = self.kilometrage * 0.08 + 10000
        else:
            resultat = self.kilometrage * 0.08
        return resultat

    def to_dict(self) -> dict :
        data = super().to_dict()
        data["type"] = "Fourgonnette"
        data["refrigerated"] = self.refrigerated
        return data

    @classmethod
    def from_dict(cls, data) -> "Fourgonnette":
        return cls(
            immatriculation = data["immatriculation"],
            marque = data["marque"],
            kilometrage = data["kilometrage"],
            capacite_charge_kg = data["capacite_charge_kg"],
            refrigerated = data["refrigerated"]
        )

