def ajouter_depense(mon_fichier: str, description: str, montant: float):
    with open(mon_fichier, "a") as f:
        f.write(f"{description}:{montant}\n")

def lire_depenses(nom_fichier: str) -> list:
    depenses = []  
    with open(nom_fichier, "r") as f:
        for ligne in f:
            ligne = ligne.strip()
            description, montant = ligne.split(":")
            depenses.append((description, float(montant)))
    return depenses

def total_depenses(mon_fichier: str) -> float:
    lecture_depense = lire_depenses(mon_fichier)
    somme = 0
    for desc, mont in lecture_depense:
        somme += mont
    return somme


def main():
    
    ajouter_depense("depense.txt", "PC gamer", 500000.0)
    ajouter_depense("depense.txt", "pull zip", 9000.0)
    ajouter_depense("depense.txt", "ecran connecte", 25000.0)
    print(lire_depenses("depense.txt"))
    print(total_depenses("depense.txt"))
    

if __name__ == "__main__":
    main()

