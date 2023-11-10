--Projet IN513 : LE CORRE Camille - LEFEVRE Laura

CREATE TABLE Carte (
    num_carte number,
    nom_carte varchar(30),
    typeEPD varchar(1),
    prix_carte float,
    PRIMARY KEY (num_carte)
);

CREATE TABLE Boissons (
    num_boisson number,
    nom_boisson varchar(30),
    type_boisson varchar(20),
    unite varchar(20),
    prix_boisson_vente float,
    prix_boisson_achat float,
    num_fournisseur number,
    PRIMARY KEY (num_boisson)
);

CREATE TABLE Commandes (
    num_commande number,
    nom_client varchar(30),
    date_commande date,
    service varchar(1),
    num_table number,
    num_serveur number,
    PRIMARY KEY (num_commande)
);

CREATE TABLE Serveurs (
    num_serveur number,
    nom_serveur varchar(20),
    prenom_serveur varchar(20),
    sexe_serveur varchar(1),
    PRIMARY KEY (num_serveur)
);

CREATE TABLE INGREDIENTS (
    num_igd number,
    nom_igd varchar(20),
    unite varchar(20),
    prix_igd float,
    stock number,
    num_fournisseur number,
    PRIMARY KEY (num_igd)
);

CREATE TABLE FOURNISSEURS (
    num_fournisseur number,
    nom_fournisseur varchar(20),
    ville varchar(30),
    num_tel varchar(10),
    PRIMARY KEY (num_fournisseur)
);

CREATE TABLE A_BOIRE (
    num_commande number,
    num_boisson number,
    nb_unites float,
    PRIMARY KEY (num_commande, num_boisson)
);

CREATE TABLE COMPOSITION (
    num_carte number,
    num_igd number,
    nb_unites float,
    PRIMARY KEY (num_carte, num_igd)
);

CREATE TABLE EST_COMMANDE (
    num_commande number,
    num_carte number,
    PRIMARY KEY (num_commande, num_carte)
);