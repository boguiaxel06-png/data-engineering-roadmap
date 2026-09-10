from models import Truck, Van
from storage import JSONStorage
from services import FleetManager
from exceptions import (
    InvalidMileageError,
    InvalidRegistrationError,
    VehicleNotFoundError,
)


def display_menu():
    print("\n=== FleetLog - Gestion de Flotte ===")
    print("1. Ajouter un Camion")
    print("2. Ajouter une Fourgonnette")
    print("3. Afficher tous les véhicules")
    print("4. Rechercher un véhicule")
    print("5. Enregistrer un trajet")
    print("6. Supprimer un véhicule")
    print("0. Quitter")


def main():
    storage = JSONStorage("flotte.json")
    fleet_manager = FleetManager(storage)

    while True:
        display_menu()
        choice = input("Votre choix : ").strip()

        try:
            if choice == "1":
                registration = input("Immatriculation : ").strip()
                brand = input("Marque : ").strip()
                mileage = float(input("Kilometrage : "))
                max_load = float(input("Capacite de charge (kg) : "))
                axle_count = int(input("Nombre d'essieux : "))

                truck = Truck(registration, brand, mileage, max_load, axle_count)
                fleet_manager.add_vehicle(truck)
                print("Camion ajouté avec succès !")

            elif choice == "2":
                registration = input("Immatriculation : ").strip()
                brand = input("Marque : ").strip()
                mileage = float(input("Kilometrage : "))
                max_load = float(input("Capacite de charge (kg) : "))
                refrigerated = input("Réfrigérée ? (o/n) : ").strip().lower() == "o"

                van = Van(registration, brand, mileage, max_load, refrigerated)
                fleet_manager.add_vehicle(van)
                print("Fourgonnette ajoutée avec succès !")

            elif choice == "3":
                print("\n--- LISTE DE TOUS LES VEHICULES ---")
                if not fleet_manager.vehicles:
                    print("Aucun véhicule dans la flotte.")
                else:
                    for vehicle in fleet_manager.vehicles:
                        print(
                            f"IMMATRICULATION : {vehicle.registration} | "
                            f"MARQUE : {vehicle.brand} | "
                            f"KILOMETRAGE : {vehicle.mileage} km | "
                            f"CAPACITE : {vehicle.max_load_kg} kg"
                        )
                    total_cost = fleet_manager.calculate_total_maintenance_cost()
                    print(f"\nCoût total d'entretien : {total_cost:.2f} €")

            elif choice == "4":
                registration = input("Entrer l'immatriculation : ").strip()
                vehicle = fleet_manager.find_vehicle(registration)
                print(f"\n[TROUVÉ] {vehicle}")

            elif choice == "5":
                registration = input("Entrer l'immatriculation : ").strip()
                vehicle = fleet_manager.find_vehicle(registration)
                distance = float(input("Entrer le nombre de km parcourus : "))

                vehicle.add_trip(distance)
                fleet_manager.save_fleet()
                print("Trajet enregistré avec succès !")

            elif choice == "6":
                registration = input("Entrer l'immatriculation : ").strip()
                fleet_manager.remove_vehicle(registration)
                print("Véhicule supprimé avec succès !")

            elif choice == "0":
                print("Au revoir !")
                break

            else:
                print("Choix invalide, réessayez.")

        except (InvalidMileageError, InvalidRegistrationError, VehicleNotFoundError) as e:
            print(f"\n[ERREUR MÉTIER] {e}")
        except ValueError:
            print("\n[ERREUR SAISIE] Saisie numérique invalide. Réessayez.")


if __name__ == "__main__":
    main()