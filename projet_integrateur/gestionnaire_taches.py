import sqlite3


def initialize_db():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            description TEXT,
            start_date DATE,
            end_date DATE,
            status TEXT CHECK(status IN ('to do', 'in progress', 'done')) DEFAULT 'to do',
            priority TEXT CHECK(priority IN ('low', 'medium', 'high')) DEFAULT 'medium',
            estimated_time INTEGER,
            time_spent INTEGER
        )
    """)
    connection.commit()
    connection.close()


def add_task(description: str, priority: str = "medium"):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO tasks (description, priority) VALUES (?, ?)",
        (description, priority)
    )
    connection.commit()
    connection.close()


def list_tasks():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"TASK NUMBER: {task[0]}")
        print(f"DESCRIPTION: {task[1]}")
        print(f"START DATE: {task[2]}")
        print(f"END DATE: {task[3]}")
        print(f"STATUS: {task[4]}")
        print(f"PRIORITY: {task[5]}")
        print(f"ESTIMATED TIME: {task[6]}")
        print(f"TIME SPENT: {task[7]}")
    connection.close()


def complete_task(task_id: int):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()


def delete_task(task_id: int):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()


def menu():
    while True:
        print("HEY!!! QUE VOULEZ VOUS FAIRE")
        print("---- GESTIONNAIRE DE TACHE ----")
        print("Choix 1: Ajouter une tache")
        print("Choix 2: Lister les taches")
        print("Choix 3: Terminer une tache")
        print("Choix 4: Supprimer une tache")
        print("Choix 5: SORTIR")

        try:
            choice = int(input("Entrez le nombre correspondant : "))
        except ValueError:
            print("Choix invalide, entrez un nombre.")
            continue

        if choice == 1:
            description = input("Entrez la description de votre tache : ")
            priority = input("Quelle est sa priorite (low/medium/high) : ")
            try:
                add_task(description, priority)
                print("Tache ajoutee avec succes !")
            except sqlite3.OperationalError:
                print("Priorite invalide. Entrez low, medium ou high.")

        elif choice == 2:
            list_tasks()

        elif choice == 3:
            try:
                task_id = int(input("Entrez le numero de la tache a terminer : "))
            except ValueError:
                print("ID invalide, entrez un nombre.")
                continue
            complete_task(task_id)
            print(f"Tache numero {task_id} terminee avec succes !")

        elif choice == 4:
            try:
                task_id = int(input("Entrez le numero de la tache a supprimer : "))
            except ValueError:
                print("ID invalide, entrez un nombre.")
                continue
            delete_task(task_id)
            print(f"Tache numero {task_id} supprimee avec succes !")

        elif choice == 5:
            print("A plus tard !!!")
            break

        else:
            print("Choix invalide.")


def main():
    initialize_db()
    menu()


if __name__ == "__main__":
    main()