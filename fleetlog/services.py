from models import Vehicule, Camion, Fourgonnette
from storage import JSONStorage
from exceptions import ImmatriculationInvalideError, VehiculeNonTrouveError

class GestionnaireFlotte:
    def __init__(self, storage: JSONStorage):
        self.storage = storage
        self.vehicules: list[Vehicule] = []
        self.charger_flotte()

    def ajouter_vehicule(self, vehicule: Vehicule):
        self.vehicules.append(vehicule)
        self.sauvegarder_flotte()

    def sauvegarder_flotte(self):
        donnees = {
            "vehicules": [v.to_dict() for v in self.vehicules]
        }
        self.storage.sauvegarder(donnees)
    
    def charger_flotte(self):
        donnes = self.storage.charger()
        for m_dict in donnes.get("vehicules", []):
            type_v = m_dict.get("type")
            if type_v == "Camion":
                self.vehicules.append(Camion.from_dict(m_dict))
            if type_v == "Fourgonnette":
                self.vehicules.append(Fourgonnette.from_dict(m_dict))

    def rechercher_vehicule(self, immatriculation: str) -> Vehicule:
        for vehicule in self.vehicules:
            if immatriculation == vehicule.immatriculation:
                return vehicule
        raise VehiculeNonTrouveError("Véhicule non trouvé")

    def supprimer_vehicule(self, immatriculation: str):
        s_vehicule = self.rechercher_vehicule(immatriculation)
        self.vehicules.remove(s_vehicule)
        self.sauvegarder_flotte()

    def calculer_cout_total_entretien(self) -> float:
        total_cout = sum(v.calculer_cout_entretien() for v in self.vehicules)
        return total_cout

