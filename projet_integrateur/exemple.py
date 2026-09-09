import sqlite3

connexion = sqlite3.connect("taches.db")
curseur = connexion.cursor()

curseur.execute("CREATE TABLE IF NOT EXISTS taches (id INTEGER PRIMARY KEY, description TEXT, terminee INTEGER)")
connexion.commit()

curseur.execute("INSERT INTO taches (description, terminee) VALUES (?, ?)", ("Faire les courses", 0))
connexion.commit()

curseur.execute("SELECT * FROM taches")
resultats = curseur.fetchall()
print(resultats)

connexion.close()