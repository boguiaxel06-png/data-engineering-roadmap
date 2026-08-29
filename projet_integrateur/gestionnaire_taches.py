import sqlite3
def initialiser_bdd():
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()
    curseur.execute("create table if not exists taches (id_tache integer primary key, description_tache text, date_debut date, date_fin date, statut TEXT CHECK(statut IN ('a faire', 'en cours', 'terminee')) DEFAULT 'a faire', priorite text check(priorite in('faible', 'moyenne', 'eleve')) default 'moyenne', temps_estime integer, temps_passe integer)")
    connexion.commit()

    connexion.close()

def ajouter_tache(description_tache: str, priorite: str = "moyenne"):
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()

    curseur.execute("insert into taches (description_tache, priorite) values (?,?)",(description_tache, priorite))
    connexion.commit()
    connexion.close()

def lister_tache():
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()
    curseur.execute("select * from taches")
    taches = curseur.fetchall()
    for tache in taches:
        print(f"NUMERO DE TACHE: {tache[0]}")
        print(f"DESCRIPTION : {tache[1]}")
        print(f"DATE DU DEBUT : {tache[2]}")
        print(f"DATE DE FIN : {tache[3]}")
        print(f"STATUT : {tache[4]}")
        print(f"PRIORITE : {tache[5]}")
        print(f"TEMPS ESTIME: {tache[6]}")
        print(f"TEMPS PASSE : {tache[7]}")
        #JE NE SAVAIS PAS SI JE POUVAIS TOUT AVEC UN PRINT
        #ET COMMENT GERER LES CAS AVEC NONE

    connexion.close()


def main():
    initialiser_bdd()
    print("Base de données initialisée avec succès.")

    ajouter_tache("Réviser SQL", "eleve")
    print("Tâche ajoutée.")

    lister_tache()

    
if __name__ == "__main__":
    main()
