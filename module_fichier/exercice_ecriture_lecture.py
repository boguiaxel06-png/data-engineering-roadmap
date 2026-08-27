def sauvegarder_scores(nom_fichier: str, scores: dict):
    with open(nom_fichier, "w") as f:
        for nom, score in scores.items():
            f.write(f"{nom}:{score}\n")

def charger_scores(nom_fichier: str) -> dict:
    scores = {}  # dictionnaire vide, on va le remplir au fil de la boucle
    with open(nom_fichier, "r") as f:
        for ligne in f:
            ligne = ligne.strip()
            parties = ligne.split(":")
            nom, score = parties
            scores[nom] = int(score)
    return scores

def main():
    test1 = {"Alice": 90, "Bob": 75, "Charlie": 60}
    sauvegarder_scores("scores.txt", test1)
    scores_recharges = charger_scores("scores.txt")
    print(test1)
    print(scores_recharges)


if __name__ == "__main__":
    main()