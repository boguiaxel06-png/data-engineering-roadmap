from models import Camion, Fourgonnette
from storage import JSONStorage
from services import GestionnaireFlotte
from exceptions import (
    KilometrageInvalideError,
    ImmatriculationInvalideError,
    VehiculeNonTrouveError,
)


def afficher_menu():
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
    gestionnaire = GestionnaireFlotte(storage)

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        try:
            if choix == "1":
                immatriculation = input("Immatriculation : ").strip()
                marque = input("Marque : ").strip()
                kilometrage = float(input("Kilometrage : "))
                capacite = float(input("Capacite de charge (kg) : "))
                nombre_essieux = int(input("Nombre d'essieux : "))

                camion = Camion(immatriculation, marque, kilometrage, capacite, nombre_essieux)
                gestionnaire.ajouter_vehicule(camion)
                print("Camion ajouté avec succès !")

            elif choix == "2":
                immatriculation = input("Immatriculation : ").strip()
                marque = input("Marque : ").strip()
                kilometrage = float(input("Kilometrage : "))
                capacite = float(input("Capacite de charge (kg) : "))
                refrigerated = input("Réfrigérée ? (o/n) : ").strip().lower() == "o"

                fourgonnette = Fourgonnette(immatriculation, marque, kilometrage, capacite, refrigerated)
                gestionnaire.ajouter_vehicule(fourgonnette)
                print("Fourgonnette ajoutée avec succès !")

            elif choix == "3":
                print("\n--- LISTE DE TOUS LES VEHICULES ---")
                if not gestionnaire.vehicules:
                    print("Aucun véhicule dans la flotte.")
                else:
                    for vehicule in gestionnaire.vehicules:
                        print(
                            f"IMMATRICULATION : {vehicule.immatriculation} | "
                            f"MARQUE : {vehicule.marque} | "
                            f"KILOMETRAGE : {vehicule.kilometrage} km | "
                            f"CAPACITE : {vehicule.capacite_charge_kg} kg"
                        )
                    cout_total = gestionnaire.calculer_cout_total_entretien()
                    print(f"\nCoût total d'entretien : {cout_total:.2f} €")

            elif choix == "4":
                immatriculation = input("Entrer l'immatriculation : ").strip()
                vehicule = gestionnaire.rechercher_vehicule(immatriculation)
                print(f"\n[TROUVÉ] {vehicule}")

            elif choix == "5":
                immatriculation = input("Entrer l'immatriculation : ").strip()
                vehicule = gestionnaire.rechercher_vehicule(immatriculation)
                km_parcourus = float(input("Entrer le nombre de km parcourus : "))
                
                vehicule.enregistrer_trajet(km_parcourus)
                gestionnaire.storage.sauvegarder(gestionnaire.vehicules)
                print("Trajet enregistré avec succès !")

            elif choix == "6":
                immatriculation = input("Entrer l'immatriculation : ").strip()
                gestionnaire.supprimer_vehicule(immatriculation)
                print("Véhicule supprimé avec succès !")

            elif choix == "0":
                print("Au revoir !")
                break

            else:
                print("Choix invalide, réessayez.")

        except (KilometrageInvalideError, ImmatriculationInvalideError, VehiculeNonTrouveError) as e:
            print(f"\n[ERREUR MÉTIER] {e}")
        except ValueError:
            print("\n[ERREUR SAISIE] Saisie numérique invalide. Réessayez.")


if __name__ == "__main__":
    main()