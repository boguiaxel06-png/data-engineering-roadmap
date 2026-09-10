class VehicleNotFoundError(Exception):
    """Raised when the vehicle is not found"""
    def __init__(self, registration):
        message = f"registration {registration} not found"
        super().__init__(message)
        self.registration = registration


class InvalidRegistrationError(Exception):
    """Raised when the vehicle registration is invalid"""
    def __init__(self, registration):
        message = f"registration {registration} invalid"
        super().__init__(message)
        self.registration = registration



class InvalidMileageError(Exception):
    """Raised if an entered mileage is negative or lower than the current mileage of the vehicle"""
    def __init__(self, entered_mileage, current_mileage):
        message = f"the entered mileage {entered_mileage} is negative or lower than current mileage {current_mileage}"
        super().__init__(message)
        self.entered_mileage = entered_mileage
        self.current_mileage = current_mileage


class CapacityExceededError(Exception):
    """Raised if the weight of the cargo exceeds the maximum capacity of the vehicle"""
    def __init__(self, cargo_weight, max_capacity):
        message = f"the weight of the cargo {cargo_weight} is greater than the maximum capacity of the vehicle {max_capacity}"
        super().__init__(message)
        self.cargo_weight = cargo_weight
        self.max_capacity = max_capacity
