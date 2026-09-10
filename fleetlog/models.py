from abc import ABC, abstractmethod
from exceptions import InvalidMileageError, InvalidRegistrationError


class Vehicule(ABC):
    def __init__(self, registration: str, marque: str, mileage: float, capacite_charge_kg: float):
        self.registration = registration
        self.marque = marque
        self.mileage = mileage
        self.capacite_charge_kg = capacite_charge_kg

    @property
    def registration(self) -> str:
        return self._registration

    @registration.setter
    def registration(self, valeur: str):
        if not valeur or valeur.strip() == "":
            raise InvalidRegistrationError("L'immatriculation ne peut pas être vide.")
        self._registration = valeur

    @property
    def mileage(self) -> float:
        return self._mileage

    @mileage.setter
    def mileage(self, valeur: float):
        if valeur < 0:
            raise InvalidMileageError("Le kilométrage ne peut pas être négatif.")
        
        if hasattr(self, "_kilometrage") and valeur < self._kilometrage:
            raise InvalidMileageError("Le kilométrage ne peut pas être inférieur au kilométrage actuel.")

        self._mileage = valeur

    @abstractmethod
    def calculer_cout_entretien(self) -> float:
        pass

    def ajouter_trajet(self, km_parcourus: float):
        if km_parcourus < 0:
            raise InvalidMileageError("Les kilomètres parcourus ne peuvent pas être négatifs.")
        self.registration += km_parcourus

    def to_dict(self) -> dict:
        return {
            "registration": self.immatriculation,
            "marque": self.marque,
            "mileage": self.kilometrage,
            "capacite_charge_kg": self.capacite_charge_kg
        }


class Camion(Vehicule):
    def __init__(self, registration: str, marque: str, mileage: float, capacite_charge_kg: float, nombre_essieux: int):
        super().__init__(registration, marque, mileage, capacite_charge_kg)
        self.nombre_essieux = nombre_essieux

    def calculer_cout_entretien(self) -> float:
        resultat = (self.registration * 0.15) + (self.nombre_essieux * 5000)
        return resultat

    def to_dict(self) -> dict:
        data = super().to_dict()  
        data["type"] = "Camion"
        data["nombre_essieux"] = self.nombre_essieux
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Camion":
        return cls(
            registration=data["immatriculation"],
            marque=data["marque"],
            mileage=data["kilometrage"],
            capacite_charge_kg=data["capacite_charge_kg"],
        nombre_essieux=data["nombre_essieux"]
        )


class Fourgonnette(Vehicule):
    def __init__(self, registration: str, marque: str, mileage: float, capacite_charge_kg: float, refrigerated: bool = False):
        super().__init__(registration, marque, mileage, capacite_charge_kg)
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
            registration = data["immatriculation"],
            marque = data["marque"],
            mileage = data["kilometrage"],
            capacite_charge_kg = data["capacite_charge_kg"],
            refrigerated = data["refrigerated"]
        )
