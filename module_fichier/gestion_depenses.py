def ajouter_depense(nom_fichier: str, description: str, montant: float):
    with open(nom_fichier, "a") as f:
        f.write(f"{description}:{montant}\n")


def lire_depenses(nom_fichier: str) -> list:
    depenses = []
    with open(nom_fichier, "r") as f:
        for ligne in f:
            ligne = ligne.strip()
            description, montant = ligne.split(":")
            depenses.append((description, float(montant)))
    return depenses


def total_depenses(nom_fichier: str) -> float:
    lecture_depense = lire_depenses(nom_fichier)
    somme = 0
    for desc, mont in lecture_depense:
        somme += mont
    return somme