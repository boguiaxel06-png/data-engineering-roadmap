class VehiculeNonTrouveError(Exception):
    """ Exception levée lorsque un vehicule n'existe pas dans le système """
    pass


class ImmatriculationInvalideError(Exception):
    """ Exception levée lorsque une plaque d'immatriculation est vide ou mal formatée """
    pass


class KilometrageInvalideError(Exception):
    """ Exception levée si le kilométrage saisi est négatif ou inférieur au kilométrage actuel du vehicule """
    pass


class CapaciteDepasseeError(Exception):
    """ Exception levée si le poids de la cargaison depasse la capacité maximale du vehicule """
    pass
