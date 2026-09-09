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


    connexion.close()

def terminer_tache(id_tache: int):
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()

    curseur.execute("update taches set statut = 'terminee' where id_tache = ?", (id_tache,))

    connexion.commit()
    connexion.close()

def supprimer_tache(id_tache: int):
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()

    curseur.execute("delete from taches where id_tache = ?", (id_tache,))

    connexion.commit()
    connexion.close()

def menu():
    while True:
        print("HEY!!! QUE VOULEZ VOUS FAIRE")
        print("---- GESTIONNAIAIRE DE TACHE ----")
        print("Choix 1: Ajouter une tache")
        print("Choix 2: Lister une tache")
        print("Choix 3: Terminer une tache")
        print("Choix 4: supprimer une tache")
        print("choix 5: SORTIR")

        try:
            choix = int(input("ENTREZ LE NOMBRE CORRESPONDANT"))
        except ValueError:
            print("Choix invalide, entrez un nombre.")
            continue
         
        if choix == 1:
            description_tache = input("Entrez la description de votre tache")
            priorite = input("qu'elle est sa priorite(faible/ moyenne/ elevee)")
            try:
                ajouter_tache(description_tache, priorite)
                print("Tache ajoutee avec succes!!!")
            except sqlite3.OperationalError:
                print("Priorite invalide. Entrez faible, moyenne ou eleve.")
                continue
            ajouter_tache(description_tache, priorite)
            print("Tache ajouter avec succes!!!")
        elif choix == 2:
            lister_tache()
        elif choix == 3:
            try:
                id_tache = int(input("entrer le numero de la tache a terminer"))
            except ValueError:
                print("ID invalide, entrer un nombre")
                continue            
            terminer_tache(id_tache)
            print(f"Tache numero {id_tache} terminer avec succes!!!")
        elif choix == 4:
            try:
                id_tache = int(input("entrer le numero de la tache a supprimer"))
            except ValueError:
                print("ID invalide, entrer un nombre")
                continue
            supprimer_tache(id_tache)
            print(f"Tache numero {id_tache} supprimer avec succes!!!")
        elif choix == 5:
            print("a plus tard!!!")
            break
        else:
            print("Choix Invalide")
    

def main():
    menu()

if __name__ == "__main__":
    main()
