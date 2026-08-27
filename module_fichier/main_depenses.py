from gestion_depenses import ajouter_depense, lire_depenses, total_depenses

def main():
    
    ajouter_depense("depense.txt", "PC gamer", 500000.0)
    ajouter_depense("depense.txt", "pull zip", 9000.0)
    ajouter_depense("depense.txt", "ecran connecte", 25000.0)
    print(lire_depenses("depense.txt"))
    print(total_depenses("depense.txt"))
    

if __name__ == "__main__":
    main()
