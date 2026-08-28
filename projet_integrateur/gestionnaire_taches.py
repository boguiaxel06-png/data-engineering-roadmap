import sqlite3
def initialiser_bdd():
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()
    curseur.execute("create table if not exists taches (id_tache integer primary key, description_tache text,date_debut date, date_fin date, statut TEXT CHECK(statut IN ('a faire', 'en cours', 'terminee')) DEFAULT 'a faire', priorite text check(priorite in('faible', 'moyenne', 'eleve')) default 'moyenne', temps_estime integer, temps_passe integer)")
    connexion.commit()

    connexion.close()

def main():
    initialiser_bdd()
    print("Base de données initialisée avec succès.")
if __name__ == "__main__":
    main()