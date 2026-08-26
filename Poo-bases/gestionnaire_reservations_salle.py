class PlageHorraireInvalideError(Exception):
    pass


class HeureInvalideError(Exception):
    pass


class CreneauOccupeError(Exception):
    pass


class Salle:
    def __init__(self, nom: str, capacite: int):
        self.nom = nom
        self.capacite = capacite

    def __str__(self):
        return f"Sale: {self.nom} -- Capacite: {self.capacite}"

    def __eq__(self, other) -> bool:
        if self.nom == other.nom and self.capacite == other.capacite:
            return True
        else: 
            return False

    def __lt__(self,other) -> bool:
        if self.capacite < other.capacite:
            return True
        else: 
            return False

        
class Reservation:
    def __init__(self, reservant: str, heure_debut: int, heure_fin: int, salle: Salle):
        self.salle = salle
        self.reservant = reservant
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.valider()

    def __str__(self):
        return f"Reservation de {self.reservant} de {self.heure_debut} Heure a {self.heure_fin} heure"
    
    @property
    def heure_debut(self) -> int:
        return self._heure_debut

    @heure_debut.setter
    def heure_debut(self, valeur: int) -> int:
        if not(0 <= valeur <= 23):
            raise HeureInvalideError ("cette heure est invalide")
        self._heure_debut = valeur
        
    @property
    def heure_fin(self) -> int:
        return self._heure_fin
    
    @heure_fin.setter
    def heure_fin(self, valeur: int) -> int:
        if not(0 <= valeur <= 23):
            raise HeureInvalideError ("cette heure est invalide")
        self._heure_fin = valeur

    def valider(self) -> str:
        if self.heure_fin > self.heure_debut:
            pass
        else:
            raise PlageHorraireInvalideError("plage d'horraie invalide")

    def chevauche(self, autre: "Reservation") -> bool:
        if not(self.heure_fin <= autre.heure_debut or autre.heure_fin <= self.heure_debut):
            return True
        else:
            return False
   

class PlanningSalle:
    def __init__(self, salle: Salle):
        self.salle = salle
        self.reservations = []

    def reserver(self, reservation: Reservation):
        for reservation_existante in self.reservations:
            if reservation.chevauche(reservation_existante):
                raise CreneauOccupeError("reservation indisponible")  
        self.reservations.append(reservation)
            
    def reservation_du_jour(self) -> list:
        return self.reservations


def main():
    salle1 = Salle("Soul society", 1000)
    planning1 = PlanningSalle(salle1)

    reservation1 = Reservation("kenny", 9, 20, salle1)
    reservation2 = Reservation("aizen", 16, 20, salle1)
    reservation3 = Reservation("yamamoto", 4, 7, salle1)

    # Premier créneau : doit réussir
    planning1.reserver(reservation1)
    print("Réservation de kenny acceptée")

    # Deuxième créneau : chevauche reservation1 (9h-20h vs 16h-20h) → doit échouer
    try:
        planning1.reserver(reservation2)
    except CreneauOccupeError as e:
        print(f"Erreur: {e}")

    # Troisième créneau : ne chevauche pas (4h-7h) → doit réussir
    planning1.reserver(reservation3)
    print("Réservation de yamamoto acceptée")

    # Test PlageHorraireInvalideError (heure_fin < heure_debut)
    try:
        reservation4 = Reservation("kenny", 9, 6, salle1)
    except PlageHorraireInvalideError as e:
        print(f"Erreur: {e}")

    # Test HeureInvalideError (heure hors 0-23)
    try:
        reservation5 = Reservation("kenny", 9, 26, salle1)
    except HeureInvalideError as e:
        print(f"Erreur: {e}")


if __name__ == "__main__":
    main()
