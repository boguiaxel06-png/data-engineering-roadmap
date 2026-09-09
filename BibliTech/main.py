from models import Livre, Dvd, Document
from storage import Jsontorage
from exceptions import DocumentNonTrouveError, ISBNInvalideError
from services import GestionnaireMediatheque


def afficher_menu():
    print("\n=== BibliTech - Gestionnaire Mediathèque===")
    print("1. Ajouter un Livre")
    print("2. Ajouter un DVD")
    print("3. Afficher tous les Documents")
    print("4. Rechercher un Document")
    print("5. Emprunter/Retourner un Document")
    print("6. Supprimer un véhicule")
    print("0. Quitter")


def main():
    storage = Jsontorage("mediatheque.json")
    gestionnaire = GestionnaireMediatheque(storage)

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        try:
            if choix == "1":
                #corriger svp

        except (DocumentNonTrouveError, ISBNInvalideError) as e:
            print(f"ERREUR METIER {e}")
        except ValueError:
            print("\n[ERREUR SAISIE] Saisie numérique invalide. Réessayez.")
            



