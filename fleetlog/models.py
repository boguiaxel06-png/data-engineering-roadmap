from abc import ABC, abstractmethod
from exceptions import InvalidMileageError, InvalidRegistrationError


class Vehicle(ABC):
    def __init__(self, registration: str, brand: str, mileage: float, max_load_kg: float):
        self.registration = registration
        self.brand = brand
        self.mileage = mileage
        self.max_load_kg = max_load_kg

    @property
    def registration(self) -> str:
        return self._registration

    @registration.setter
    def registration(self, value: str):
        if not value or value.strip() == "":
            raise InvalidRegistrationError(value)
        self._registration = value

    @property
    def mileage(self) -> float:
        return self._mileage

    @mileage.setter
    def mileage(self, value: float):
        current_mileage = getattr(self, "_mileage", 0)
        if value < 0 or value < current_mileage:
            raise InvalidMileageError(value, current_mileage)
        self._mileage = value

    @abstractmethod
    def calculate_maintenance_cost(self) -> float:
        pass

    def add_trip(self, distance: float):
        if distance < 0:
            raise InvalidMileageError(distance, self.mileage)
        self.mileage += distance

    def to_dict(self) -> dict:
        return {
            "registration": self.registration,
            "brand": self.brand,
            "mileage": self.mileage,
            "max_load_kg": self.max_load_kg
        }


class Truck(Vehicle):
    def __init__(self, registration: str, brand: str, mileage: float, max_load_kg: float, axle_count: int):
        super().__init__(registration, brand, mileage, max_load_kg)
        self.axle_count = axle_count

    def calculate_maintenance_cost(self) -> float:
        return (self.mileage * 0.15) + (self.axle_count * 5000)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "Truck"
        data["axle_count"] = self.axle_count
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Truck":
        return cls(
            registration=data["registration"],
            brand=data["brand"],
            mileage=data["mileage"],
            max_load_kg=data["max_load_kg"],
            axle_count=data["axle_count"]
        )


class Van(Vehicle):
    def __init__(self, registration: str, brand: str, mileage: float, max_load_kg: float, refrigerated: bool = False):
        super().__init__(registration, brand, mileage, max_load_kg)
        self.refrigerated = refrigerated

    def calculate_maintenance_cost(self) -> float:
        base_cost = self.mileage * 0.08
        return base_cost + 10000 if self.refrigerated else base_cost

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "Van"
        data["refrigerated"] = self.refrigerated
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Van":
        return cls(
            registration=data["registration"],
            brand=data["brand"],
            mileage=data["mileage"],
            max_load_kg=data["max_load_kg"],
            refrigerated=data["refrigerated"]
        )
    