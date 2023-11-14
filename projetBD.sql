--Projet IN513 : LE CORRE Camille - LEFEVRE Laura

CREATE TABLE CARTE (
    num_carte number,
    nom_carte varchar(30),
    typeEPD varchar(1) CHECK(typeEPD IN ('E', 'P', 'D')),
    prix_carte float CHECK(prix_carte>0 AND prix_carte<100),
    CONSTRAINT pk_carte PRIMARY KEY (num_carte)
);

CREATE TABLE FOURNISSEURS (
    num_fournisseur number,
    nom_fournisseur varchar(20),
    ville varchar(30),
    num_tel varchar(10) UNIQUE,
    CONSTRAINT pk_fournisseurs PRIMARY KEY (num_fournisseur)
);

CREATE TABLE BOISSONS (
    num_boisson number,
    nom_boisson varchar(30),
    type_boisson varchar(20) CHECK((type_boisson IN ('eau', 'soda', 'sirop', 'jus', 'vin', 'champagne', 'aperitif', 'digestif', 'cafe'))),
    unite varchar(20),
    prix_boisson_vente float CHECK(prix_boisson_vente>0 AND prix_boisson_vente<100),
    prix_boisson_achat float CHECK(prix_boisson_achat>0 AND prix_boisson_achat<100),
    num_fournisseur number,
    CONSTRAINT pk_boissons PRIMARY KEY (num_boisson),
    CONSTRAINT fk_boissons FOREIGN KEY (num_fournisseur) REFERENCES FOURNISSEURS (num_fournisseur)
);

CREATE TABLE SERVEURS (
    num_serveur number,
    nom_serveur varchar(20),
    prenom_serveur varchar(20),
    sexe_serveur varchar(1) CHECK(sexe_serveur IN ('F', 'H', NULL)),
    CONSTRAINT pk_serveurs PRIMARY KEY (num_serveur)
);

CREATE TABLE COMMANDES (
    num_commande number,
    nom_client varchar(30),
    date_commande date,
    service varchar(1) CHECK(service IN ('M', 'S')),
    num_table number CHECK(num_table>=1 AND num_table<=15),
    num_serveur number,
    CONSTRAINT pk_commandes PRIMARY KEY (num_commande),
    CONSTRAINT fk_commandes FOREIGN KEY (num_serveur) REFERENCES SERVEURS (num_serveur)
);

CREATE TABLE INGREDIENTS (
    num_igd number,
    nom_igd varchar(20),
    unite varchar(20),
    prix_igd float CHECK(prix_igd>0),
    stock number CHECK(stock>=0),
    num_fournisseur number,
    CONSTRAINT pk_igd PRIMARY KEY (num_igd),
    CONSTRAINT fk_igd FOREIGN KEY (num_fournisseur) REFERENCES FOURNISSEURS (num_fournisseur)
);

CREATE TABLE A_BOIRE (
    num_commande number,
    num_boisson number,
    nb_unites float CHECK(nb_unites>0),
    CONSTRAINT pk_A_boire PRIMARY KEY (num_commande, num_boisson),
    CONSTRAINT fk_A_boire_1 FOREIGN KEY (num_commande) REFERENCES COMMANDES (num_commande),
    CONSTRAINT fk_A_boire_2 FOREIGN KEY (num_boisson) REFERENCES BOISSONS (num_boisson)
);

CREATE TABLE COMPOSITION (
    num_carte number,
    num_igd number,
    nb_unites float CHECK(nb_unites>0),
    CONSTRAINT pk_composition PRIMARY KEY (num_carte, num_igd),
    CONSTRAINT fk_composition_1 FOREIGN KEY (num_carte) REFERENCES CARTE (num_carte),
    CONSTRAINT fk_composition_2 FOREIGN KEY (num_igd) REFERENCES INGREDIENTS (num_igd)
);

CREATE TABLE EST_COMMANDE (
    num_commande number,
    num_carte number,
    CONSTRAINT pk_est_commande PRIMARY KEY (num_commande, num_carte),
    CONSTRAINT fk_est_commande_1 FOREIGN KEY (num_commande) REFERENCES COMMANDES (num_commande),
    CONSTRAINT fk_est_commande_2 FOREIGN KEY (num_carte) REFERENCES CARTE (num_carte)
);