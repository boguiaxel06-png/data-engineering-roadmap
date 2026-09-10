from models import Vehicle, Truck, Van
from storage import JSONStorage
from exceptions import VehicleNotFoundError


class FleetManager:
    def __init__(self, storage: JSONStorage):
        self.storage = storage
        self.vehicles: list[Vehicle] = []
        self.load_fleet()

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        self.save_fleet()

    def save_fleet(self):
        data = {
            "vehicles": [v.to_dict() for v in self.vehicles]
        }
        self.storage.save(data)

    def load_fleet(self):
        data = self.storage.load()
        for v_dict in data.get("vehicles", []):
            vehicle_type = v_dict.get("type")
            if vehicle_type == "Truck":
                self.vehicles.append(Truck.from_dict(v_dict))
            elif vehicle_type == "Van":
                self.vehicles.append(Van.from_dict(v_dict))

    def find_vehicle(self, registration: str) -> Vehicle:
        for vehicle in self.vehicles:
            if registration == vehicle.registration:
                return vehicle
        raise VehicleNotFoundError(registration)

    def remove_vehicle(self, registration: str):
        vehicle = self.find_vehicle(registration)
        self.vehicles.remove(vehicle)
        self.save_fleet()

    def calculate_total_maintenance_cost(self) -> float:
        return sum(v.calculate_maintenance_cost() for v in self.vehicles)