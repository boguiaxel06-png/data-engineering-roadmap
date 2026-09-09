create table taches(
    id_tache integer primary key,
    description_tache text,
    date_debut date,
    date_fin date,
    statut TEXT CHECK(statut IN ('a faire', 'en cours', 'terminee')) DEFAULT 'a faire',
    priorite text check(priorite in('faible', 'moyenne', 'eleve')) default 'moyenne',
    temps_estime integer,
    temps_passe integer
);
