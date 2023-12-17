-- Projet IN513 - LE CORRE Camille et LEFEVRE Laura

CREATE TABLE CARTE (
    num_carte number,
    nom_carte varchar(53),
    typeEPD varchar(1) CHECK(typeEPD IN ('E', 'P', 'D')),
    prix_carte float CHECK(prix_carte >0 AND prix_carte<100),
    CONSTRAINT pk_carte PRIMARY KEY (num_carte)
);

CREATE TABLE FOURNISSEURS (
    num_fournisseur number,
    nom_fournisseur varchar(30),
    ville varchar(30),
    num_tel varchar(14) UNIQUE,
    CONSTRAINT pk_fournisseurs PRIMARY KEY (num_fournisseur)
);

CREATE TABLE BOISSONS (
    num_boisson number,
    nom_boisson varchar(30),
    type_boisson varchar(20) CHECK(type_boisson IN ('eau', 'soda', 'sirop', 'jus', 'biere', 'vin', 'champagne', 'a_fort', 'cafe')),
    unite varchar(20) CHECK(unite IN ('L', 'canette', 'bouteille', 'kg')),
    prix_boisson_vente float CHECK(prix_boisson_vente>0.0),
    num_fournisseur number,
    prix_boisson_achat float CHECK(prix_boisson_achat>0.0),
    CONSTRAINT pk_boissons PRIMARY KEY (num_boisson),
    CONSTRAINT fk_boissons_fournisseurs FOREIGN KEY (num_fournisseur) REFERENCES FOURNISSEURS (num_fournisseur),
    CONSTRAINT marge_boissons CHECK(prix_boisson_achat <= prix_boisson_vente)
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
    num_serveur number,
    num_table number CHECK(num_table BETWEEN 1 AND 15),
    CONSTRAINT pk_commandes PRIMARY KEY (num_commande),
    CONSTRAINT fk_commandes_serveurs FOREIGN KEY (num_serveur) REFERENCES SERVEURS (num_serveur)
);

CREATE TABLE INGREDIENTS (
    num_igd number,
    nom_igd varchar(20),
    unite varchar(20),
    prix_igd float CHECK(prix_igd>0),
    stock number CHECK(stock>=0),
    num_fournisseur number,
    CONSTRAINT pk_igd PRIMARY KEY (num_igd),
    CONSTRAINT fk_igd_fournisseurs FOREIGN KEY (num_fournisseur) REFERENCES FOURNISSEURS (num_fournisseur)
);

CREATE TABLE A_BOIRE (
    num_commande number,
    num_boisson number,
    nb_unites float CHECK(nb_unites>0.0),
    CONSTRAINT pk_a_boire PRIMARY KEY (num_commande, num_boisson),
    CONSTRAINT fk_a_boire_commandes FOREIGN KEY (num_commande) REFERENCES COMMANDES (num_commande),
    CONSTRAINT fk_a_boire_boissons FOREIGN KEY (num_boisson) REFERENCES BOISSONS (num_boisson)
);

CREATE TABLE COMPOSITION (
    num_carte number,
    num_igd number,
    nb_unites float CHECK(nb_unites>0),
    CONSTRAINT pk_composition PRIMARY KEY (num_carte, num_igd),
    CONSTRAINT fk_composition_carte FOREIGN KEY (num_carte) REFERENCES CARTE (num_carte),
    CONSTRAINT fk_composition_igd FOREIGN KEY (num_igd) REFERENCES INGREDIENTS (num_igd)
);

CREATE TABLE EST_COMMANDE (
    num_commande number,
    num_carte number,
    nb_EPD number CHECK(nb_EPD>0),
    CONSTRAINT pk_est_commande PRIMARY KEY (num_commande, num_carte),
    CONSTRAINT fk_est_commande_commandes FOREIGN KEY (num_commande) REFERENCES COMMANDES (num_commande),
    CONSTRAINT fk_est_commande_carte FOREIGN KEY (num_carte) REFERENCES CARTE (num_carte)
);

-- mettre les triggers avant d'inserer les tuples non ?

-- Commandes d'insertion des valeurs
INSERT INTO FOURNISSEURS values (1, 'Fruity&Co', 'Versailles', '01 23 45 67 89');
INSERT INTO FOURNISSEURS values (2, 'Natures Bounty Produce', 'Saint-Germain-en-Laye', '01 34 56 78 90');
INSERT INTO FOURNISSEURS values (3, 'FreshHarvest Market', 'Poissy', '01 29 84 76 53');
INSERT INTO FOURNISSEURS values (4, 'Poissonnerie MerEclat', 'Trouville-sur-Mer', '02 31 45 67 89');
INSERT INTO FOURNISSEURS values (5, 'Mer et saveurs', 'Saint-Germain-en-Laye', '01 49 63 85 27');
INSERT INTO FOURNISSEURS values (6, 'La Ferme Des Limousines', 'Vicq', '06 62 25 82 35');
INSERT INTO FOURNISSEURS values (7, 'Ferme des Trois Chenes', 'Montfort-l_Amaury', '07 27 49 63 85');
INSERT INTO FOURNISSEURS values (8, 'Moulin de la Vallee Blanche', 'Maule', '06 73 92 84 56');
INSERT INTO FOURNISSEURS values (9, 'Ferme des Œufs Dores', 'Auffargis', '01 68 43 57 29');
INSERT INTO FOURNISSEURS values (10, 'Laiterie des Champs Fleuries', 'Houdan', '01 37 59 82 64');
INSERT INTO FOURNISSEURS values (11, 'Chocolaterie Douce Delice', 'Le Vesinet', '07 92 83 46 57');
INSERT INTO FOURNISSEURS values (12, 'Tropic Exotica Fruits', 'Les Mureaux', '01 32 54 76 98');
INSERT INTO FOURNISSEURS values (13, 'Drinks&Co', 'Plaisir', '06 54 32 10 98');
INSERT INTO FOURNISSEURS values (14, 'Arome Divin Distillery', 'Versailles', '01 47 89 12 34');
INSERT INTO FOURNISSEURS values (15, 'Vignoble des Deux Rivieres', 'Le Chesnay', '01 39 45 78 89');
INSERT INTO FOURNISSEURS values (16, 'Chateau Petillant de Marne', 'Chambourcy', '06 12 34 56 78');
INSERT INTO FOURNISSEURS values (17, 'Evian', 'Evian', '01 12 43 00 15');
INSERT INTO FOURNISSEURS values (18, 'Laumont', 'Strasbourg', '01 98 02 76 54');

INSERT INTO  INGREDIENTS  VALUES( 1, 'farine', 'kg', 0.75, 10, 8 );
INSERT INTO  INGREDIENTS  VALUES( 2, 'lait', 'L', 1.3, 15, 10 );
INSERT INTO  INGREDIENTS  VALUES( 3, 'beurre', 'kg', 3, 6, 10 );
INSERT INTO  INGREDIENTS  VALUES( 4, 'oeuf', 'oeufs', 0.15, 360, 9 );
INSERT INTO  INGREDIENTS  VALUES( 5, 'sucre', 'kg', 3, 3.5, 8 );
INSERT INTO  INGREDIENTS  VALUES( 6, 'creme', 'L', 4.2, 4.8, 10 );
INSERT INTO  INGREDIENTS  VALUES( 7, 'pain', 'kg', 3.9, 20, 8 );
INSERT INTO  INGREDIENTS  VALUES( 8, 'levure', 'kg', 12, 0.5, 8 );
INSERT INTO  INGREDIENTS  VALUES( 9, 'riz', 'kg', 2.5, 10, 8 );
INSERT INTO  INGREDIENTS  VALUES( 10, 'riz rond', 'kg', 2.6, 7, 8 );
INSERT INTO  INGREDIENTS  VALUES( 11, 'pate lasagne', 'kg', 1.6, 2.6, 8 );
INSERT INTO  INGREDIENTS  VALUES( 12, 'pdt', 'kg', 2, 25, 3 );
INSERT INTO  INGREDIENTS  VALUES( 13, 'filet mignon', 'kg', 11, 12.3, 7 );
INSERT INTO  INGREDIENTS  VALUES( 14, 'boeuf', 'kg', 15, 14, 6 );
INSERT INTO  INGREDIENTS  VALUES( 15, 'confit canard', 'kg', 18, 6.5, 7 );
INSERT INTO  INGREDIENTS  VALUES( 16, 'cotelette agneaux', 'kg', 17.5, 7.8, 7 );
INSERT INTO  INGREDIENTS  VALUES( 17, 'poulet', 'kg', 13.5, 9, 6 );
INSERT INTO  INGREDIENTS  VALUES( 18, 'jambon blanc', 'kg', 17, 5, 7 );
INSERT INTO  INGREDIENTS  VALUES( 19, 'jambon sec', 'kg', 17.2, 4.7, 7 );
INSERT INTO  INGREDIENTS  VALUES( 20, 'mortadelle', 'kg', 18.5, 4.5, 7 );
INSERT INTO  INGREDIENTS  VALUES( 21, 'rosette', 'kg', 20, 10, 7 );
INSERT INTO  INGREDIENTS  VALUES( 22, 'saumon fume', 'kg', 21, 5, 5 );
INSERT INTO  INGREDIENTS  VALUES( 23, 'sole', 'kg', 17, 3.6, 4 );
INSERT INTO  INGREDIENTS  VALUES( 24, 'st pierre', 'kg', 24, 3.8, 4 );
INSERT INTO  INGREDIENTS  VALUES( 25, 'thon rouge', 'kg', 14, 3.5, 5 );
INSERT INTO  INGREDIENTS  VALUES( 26, 'poulpe', 'kg', 40.8, 5.5, 5 );
INSERT INTO  INGREDIENTS  VALUES( 27, 'couteau', 'kg', 13.5, 11, 4 );
INSERT INTO  INGREDIENTS  VALUES( 28, 'crevette', 'kg', 9, 9.1, 4 );
INSERT INTO  INGREDIENTS  VALUES( 29, 'st jacques', 'kg', 15.5, 6.7, 4 );
INSERT INTO  INGREDIENTS  VALUES( 30, 'langoustine', 'kg', 30, 3.4, 4 );
INSERT INTO  INGREDIENTS  VALUES( 31, 'chevre', 'kg', 14, 1.2, 7 );
INSERT INTO  INGREDIENTS  VALUES( 32, 'mozzarella', 'kg', 10, 1.5, 10 );
INSERT INTO  INGREDIENTS  VALUES( 33, 'emmental', 'kg', 10.5, 5.5, 10 );
INSERT INTO  INGREDIENTS  VALUES( 34, 'mascarpone', 'kg', 9.5, 6, 10 );
INSERT INTO  INGREDIENTS  VALUES( 35, 'parmesan', 'kg', 11, 4, 10 );
INSERT INTO  INGREDIENTS  VALUES( 36, 'feta', 'kg', 8.4, 3.8, 7 );
INSERT INTO  INGREDIENTS  VALUES( 37, 'capres', 'kg', 7, 1, 2 );
INSERT INTO  INGREDIENTS  VALUES( 38, 'citron', 'kg', 2.5, 4.5, 12 );
INSERT INTO  INGREDIENTS  VALUES( 39, 'mangue', 'kg', 10, 4, 12 );
INSERT INTO  INGREDIENTS  VALUES( 40, 'fraise', 'kg', 13.5, 3.9, 3 );
INSERT INTO  INGREDIENTS  VALUES( 41, 'framboises', 'kg', 18, 3.7, 3 );
INSERT INTO  INGREDIENTS  VALUES( 42, 'myrtille', 'kg', 17, 3.5, 3 );
INSERT INTO  INGREDIENTS  VALUES( 43, 'cerise', 'kg', 3, 4.2, 3 );
INSERT INTO  INGREDIENTS  VALUES( 44, 'figue', 'kg', 15, 2, 12 );
INSERT INTO  INGREDIENTS  VALUES( 45, 'abricot', 'kg', 2.4, 3.3, 1 );
INSERT INTO  INGREDIENTS  VALUES( 46, 'ananas', 'kg', 3.2, 2, 12 );
INSERT INTO  INGREDIENTS  VALUES( 47, 'oignon', 'kg', 1.2, 7, 3 );
INSERT INTO  INGREDIENTS  VALUES( 48, 'ail', 'kg', 4, 2.5, 3 );
INSERT INTO  INGREDIENTS  VALUES( 49, 'tomate', 'kg', 3.6, 4.9, 2 );
INSERT INTO  INGREDIENTS  VALUES( 50, 'avocat', 'kg', 16, 3, 2 );
INSERT INTO  INGREDIENTS  VALUES( 51, 'courgette', 'kg', 3.8, 6.5, 3 );
INSERT INTO  INGREDIENTS  VALUES( 52, 'aubergine', 'kg', 1.7, 5.5, 2 );
INSERT INTO  INGREDIENTS  VALUES( 53, 'navet', 'kg', 2.9, 3.4, 2 );
INSERT INTO  INGREDIENTS  VALUES( 54, 'carotte', 'kg', 1.2, 7.1, 2 );
INSERT INTO  INGREDIENTS  VALUES( 55, 'salade', 'kg', 6, 4, 1 );
INSERT INTO  INGREDIENTS  VALUES( 56, 'artichaut', 'kg', 6, 3, 1 );
INSERT INTO  INGREDIENTS  VALUES( 57, 'celeri', 'kg', 2.5, 3, 1 );
INSERT INTO  INGREDIENTS  VALUES( 58, 'poireau', 'kg', 3, 5.5, 2 );
INSERT INTO  INGREDIENTS  VALUES( 59, 'truffe noire', 'kg', 200, 1, 18 );
INSERT INTO  INGREDIENTS  VALUES( 60, 'cepe', 'kg', 50, 6, 18 );
INSERT INTO  INGREDIENTS  VALUES( 61, 'morille', 'kg', 45, 4.5, 18 );
INSERT INTO  INGREDIENTS  VALUES( 62, 'noix', 'kg', 4.5, 3.5, 1 );
INSERT INTO  INGREDIENTS  VALUES( 63, 'biscuit cuillere', 'kg', 5, 3.2, 8 );
INSERT INTO  INGREDIENTS  VALUES( 64, 'speculoos', 'kg', 13, 3, 8 );
INSERT INTO  INGREDIENTS  VALUES( 65, 'chocolat', 'kg', 11.2, 5, 11 );
INSERT INTO  INGREDIENTS  VALUES( 66, 'poudre cacao', 'kg', 4.5, 3.4, 11 );
INSERT INTO  INGREDIENTS  VALUES( 67, 'cafe soluble', 'kg', 3.7, 2, 12 );
INSERT INTO  INGREDIENTS  VALUES( 68, 'asperge', 'kg', 4.6, 3.6, 1 );
INSERT INTO  INGREDIENTS  VALUES( 69, 'raie', 'kg', 17, 3.9, 5 );
INSERT INTO  INGREDIENTS  VALUES( 70, 'glace vanille', 'kg', 6.7, 2, 10 );
INSERT INTO  INGREDIENTS  VALUES( 71, 'glace chocolat', 'kg', 6, 1.9, 10 );
INSERT INTO  INGREDIENTS  VALUES( 72, 'glace framboise', 'kg', 7.1, 2.3, 1 );

INSERT INTO  SERVEURS  VALUES( 0,'Foquet', 'Ambre', 'F' );
INSERT INTO  SERVEURS  VALUES( 1, 'Trottier', 'Nicolas', 'H' );
INSERT INTO  SERVEURS  VALUES( 2, 'Sertin', 'Jerome', 'H' );
INSERT INTO  SERVEURS  VALUES( 3, 'Ricord', 'Stephane', 'H' );
INSERT INTO  SERVEURS  VALUES( 4, 'Lagneux', 'Natalie', 'F' );
INSERT INTO  SERVEURS  VALUES( 5, 'Clissard', 'Thibaut', 'H' );
INSERT INTO  SERVEURS  VALUES( 6, 'Vadili', 'Samantha', 'F' );
INSERT INTO  SERVEURS  VALUES( 7, 'Lecuyer', 'Fabien', 'H' );
INSERT INTO  SERVEURS  VALUES( 8, 'Salois', 'Florine', 'F' );
INSERT INTO  SERVEURS  VALUES( 9, 'Brasseur', 'Elise', 'F' );
INSERT INTO  SERVEURS  VALUES( 10, 'Trudeau', 'Matthieu', NULL );

INSERT INTO  CARTE  VALUES( 1, 'soupe a l oignon', 'E', 11 );
INSERT INTO  CARTE  VALUES( 2, 'pate en croute', 'E', 9 );
INSERT INTO  CARTE  VALUES( 3, 'tomate-mozza', 'E', 9 );
INSERT INTO  CARTE  VALUES( 4, 'planche de charcuterie', 'E', 15.5 );
INSERT INTO  CARTE  VALUES( 5, 'oeuf cocotte a la truffe', 'E', 12 );
INSERT INTO  CARTE  VALUES( 6, 'couteaux en persillade', 'E', 13 );
INSERT INTO  CARTE  VALUES( 7, 'salade cesar', 'E', 13.5 );
INSERT INTO  CARTE  VALUES( 8, 'verrine avocat-crevette', 'E', 12 );
INSERT INTO  CARTE  VALUES( 9, 'tartelette chevre-figue-noix', 'E', 10 );
INSERT INTO  CARTE  VALUES( 10, 'saumon fume', 'E', 13 );
INSERT INTO  CARTE  VALUES( 11, 'st jacques et fondue de poireaux', 'E', 14 );
INSERT INTO  CARTE  VALUES( 12, 'filet mignon aux morilles et ecrase de pdt', 'P', 19.5 );
INSERT INTO  CARTE  VALUES( 13, 'ravioles aux champignons', 'P', 19 );
INSERT INTO  CARTE  VALUES( 14, 'ravioles a la langoustine', 'P', 23 );
INSERT INTO  CARTE  VALUES( 15, 'roti de boeuf sauce au poivre et pommes grenailles', 'P', 25.5 );
INSERT INTO  CARTE  VALUES( 16, 'filet de st pierre et sauce hollandaise', 'P', 23.5 );
INSERT INTO  CARTE  VALUES( 17, 'poulpe roti et puree d artichaut', 'P', 24 );
INSERT INTO  CARTE  VALUES( 18, 'tartare de boeuf frites', 'P', 23 );
INSERT INTO  CARTE  VALUES( 19, 'risotto aux asperges', 'P', 19 );
INSERT INTO  CARTE  VALUES( 20, 'cotelettes d agneau - legumes rotis et pdt persillees', 'P', 22.5 );
INSERT INTO  CARTE  VALUES( 21, 'aubergine rotie a la feta', 'P', 17.5 );
INSERT INTO  CARTE  VALUES( 22, 'parmentier de canard', 'P', 20 );
INSERT INTO  CARTE  VALUES( 23, 'aile de raie aux capres', 'P', 21.5 );
INSERT INTO  CARTE  VALUES( 24, 'thon rouge snacke et puree de celeri', 'P', 22 );
INSERT INTO  CARTE  VALUES( 25, 'lasagnes vegetariennes', 'P', 18 );
INSERT INTO  CARTE  VALUES( 26, 'steak frites', 'P', 20 );
INSERT INTO  CARTE  VALUES( 27, 'escalope de poulet - riz', 'P', 18.5 );
INSERT INTO  CARTE  VALUES( 28, 'sole meuniere - riz', 'P', 18.5 );
INSERT INTO  CARTE  VALUES( 29, 'tiramisu', 'D', 8.5 );
INSERT INTO  CARTE  VALUES( 30, 'tartelette citron meringuee', 'D', 9 );
INSERT INTO  CARTE  VALUES( 31, 'pavlova fruits rouges', 'D', 9 );
INSERT INTO  CARTE  VALUES( 32, 'mousse au chocolat', 'D', 7.5 );
INSERT INTO  CARTE  VALUES( 33, 'mi-cuit au chocolat', 'D', 8 );
INSERT INTO  CARTE  VALUES( 34, 'panna cotta a la mangue', 'D', 8 );
INSERT INTO  CARTE  VALUES( 35, 'cheesecake au speculoos', 'D', 9 );
INSERT INTO  CARTE  VALUES( 36, 'croustillant a l abricot', 'D', 7 );
INSERT INTO  CARTE  VALUES( 37, 'clafouti a la cerise', 'D', 9.5 );
INSERT INTO  CARTE  VALUES( 38, 'riz au lait - caramel beurre sale maison', 'D', 7.5 );
INSERT INTO  CARTE  VALUES( 39, 'brochette de fruits de saison', 'D', 6 );
INSERT INTO  CARTE  VALUES( 40, 'ananas flambe', 'D', 7 );
INSERT INTO  CARTE  VALUES( 41, 'creme brulee', 'D', 7.5 );
INSERT INTO  CARTE  VALUES( 42, 'glace a la vanille', 'D', 3 );
INSERT INTO  CARTE  VALUES( 43, 'glace au chocolat', 'D', 3 );
INSERT INTO  CARTE  VALUES( 44, 'glace a la framboise', 'D', 3 );

INSERT INTO  COMPOSITION  VALUES( 1, 47, 0.25 );
INSERT INTO  COMPOSITION  VALUES( 1, 3, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 1, 6, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 1, 7, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 1, 33, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 2, 1, 0.015 );
INSERT INTO  COMPOSITION  VALUES( 2, 13, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 2, 18, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 2, 55, 0.008 );
INSERT INTO  COMPOSITION  VALUES( 3, 49, 0.25 );
INSERT INTO  COMPOSITION  VALUES( 3, 32, 0.15 );
INSERT INTO  COMPOSITION  VALUES( 4, 18, 0.045 );
INSERT INTO  COMPOSITION  VALUES( 4, 19, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 4, 20, 0.035 );
INSERT INTO  COMPOSITION  VALUES( 4, 21, 0.4 );
INSERT INTO  COMPOSITION  VALUES( 4, 7, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 4, 3, 0.015 );
INSERT INTO  COMPOSITION  VALUES( 5, 4, 2 );
INSERT INTO  COMPOSITION  VALUES( 5, 6, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 5, 59, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 5, 33, 0.035 );
INSERT INTO  COMPOSITION  VALUES( 6, 27, 0.5 );
INSERT INTO  COMPOSITION  VALUES( 6, 3, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 7, 55, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 7, 17, 0.11 );
INSERT INTO  COMPOSITION  VALUES( 7, 35, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 7, 49, 0.15 );
INSERT INTO  COMPOSITION  VALUES( 7, 37, 0.008 );
INSERT INTO  COMPOSITION  VALUES( 7, 6, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 7, 7, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 8, 28, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 8, 50, 0.2 );
INSERT INTO  COMPOSITION  VALUES( 9, 1, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 9, 4, 1 );
INSERT INTO  COMPOSITION  VALUES( 9, 31, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 9, 44, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 9, 62, 0.035 );
INSERT INTO  COMPOSITION  VALUES( 10, 22, 0.09 );
INSERT INTO  COMPOSITION  VALUES( 10, 7, 0.025 );
INSERT INTO  COMPOSITION  VALUES( 10, 3, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 10, 38, 0.023 );
INSERT INTO  COMPOSITION  VALUES( 11, 29, 0.3 );
INSERT INTO  COMPOSITION  VALUES( 11, 58, 0.075 );
INSERT INTO  COMPOSITION  VALUES( 11, 3, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 12, 13, 0.15 );
INSERT INTO  COMPOSITION  VALUES( 12, 61, 0.1 );
INSERT INTO  COMPOSITION  VALUES( 12, 12, 0.23 );
INSERT INTO  COMPOSITION  VALUES( 12, 3, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 12, 47, 0.035 );
INSERT INTO  COMPOSITION  VALUES( 13, 1, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 13, 4, 1 );
INSERT INTO  COMPOSITION  VALUES( 13, 60, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 13, 61, 0.035 );
INSERT INTO  COMPOSITION  VALUES( 13, 59, 0.005 );
INSERT INTO  COMPOSITION  VALUES( 13, 47, 0.003 );
INSERT INTO  COMPOSITION  VALUES( 13, 48, 0.003 );
INSERT INTO  COMPOSITION  VALUES( 13, 6, 0.025 );
INSERT INTO  COMPOSITION  VALUES( 14, 1, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 14, 4, 1 );
INSERT INTO  COMPOSITION  VALUES( 14, 6, 0.025 );
INSERT INTO  COMPOSITION  VALUES( 14, 30, 0.16 );
INSERT INTO  COMPOSITION  VALUES( 14, 47, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 15, 14, 0.19 );
INSERT INTO  COMPOSITION  VALUES( 15, 12, 0.17 );
INSERT INTO  COMPOSITION  VALUES( 15, 6, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 16, 24, 0.15 );
INSERT INTO  COMPOSITION  VALUES( 16, 3, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 16, 4, 0.5 );
INSERT INTO  COMPOSITION  VALUES( 16, 38, 0.045 );
INSERT INTO  COMPOSITION  VALUES( 16, 9, 0.6 );
INSERT INTO  COMPOSITION  VALUES( 16, 51, 0.075 );
INSERT INTO  COMPOSITION  VALUES( 17, 26, 0.5 );
INSERT INTO  COMPOSITION  VALUES( 17, 56, 0.08 );
INSERT INTO  COMPOSITION  VALUES( 17, 3, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 18, 14, 0.13 );
INSERT INTO  COMPOSITION  VALUES( 18, 4, 1 );
INSERT INTO  COMPOSITION  VALUES( 18, 37, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 18, 12, 0.26 );
INSERT INTO  COMPOSITION  VALUES( 19, 10, 0.075 );
INSERT INTO  COMPOSITION  VALUES( 19, 3, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 19, 6, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 19, 68, 0.125 );
INSERT INTO  COMPOSITION  VALUES( 19, 35, 0.013 );
INSERT INTO  COMPOSITION  VALUES( 19, 47, 0.025 );
INSERT INTO  COMPOSITION  VALUES( 20, 16, 0.15 );
INSERT INTO  COMPOSITION  VALUES( 20, 3, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 20, 12, 0.15 );
INSERT INTO  COMPOSITION  VALUES( 20, 54, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 20, 51, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 20, 35, 0.012 );
INSERT INTO  COMPOSITION  VALUES( 20, 53, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 21, 52, 0.15 );
INSERT INTO  COMPOSITION  VALUES( 21, 48, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 21, 36, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 22, 12, 0.23 );
INSERT INTO  COMPOSITION  VALUES( 22, 15, 0.175 );
INSERT INTO  COMPOSITION  VALUES( 22, 33, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 23, 69, 0.18 );
INSERT INTO  COMPOSITION  VALUES( 23, 37, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 23, 38, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 23, 6, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 23, 12, 0.2 );
INSERT INTO  COMPOSITION  VALUES( 24, 25, 0.14 );
INSERT INTO  COMPOSITION  VALUES( 24, 3, 0.028 );
INSERT INTO  COMPOSITION  VALUES( 24, 57, 0.15 );
INSERT INTO  COMPOSITION  VALUES( 24, 12, 0.08 );
INSERT INTO  COMPOSITION  VALUES( 25, 1, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 25, 3, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 25, 11, 0.72 );
INSERT INTO  COMPOSITION  VALUES( 25, 51, 0.1 );
INSERT INTO  COMPOSITION  VALUES( 25, 52, 0.7 );
INSERT INTO  COMPOSITION  VALUES( 25, 47, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 25, 48, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 25, 49, 0.2 );
INSERT INTO  COMPOSITION  VALUES( 25, 54, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 25, 2, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 26, 14, 0.2 );
INSERT INTO  COMPOSITION  VALUES( 26, 3, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 26, 12, 0.27 );
INSERT INTO  COMPOSITION  VALUES( 27, 17, 0.17 );
INSERT INTO  COMPOSITION  VALUES( 27, 3, 0.015 );
INSERT INTO  COMPOSITION  VALUES( 27, 9, 0.061 );
INSERT INTO  COMPOSITION  VALUES( 27, 6, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 28, 23, 0.139 );
INSERT INTO  COMPOSITION  VALUES( 28, 3, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 28, 1, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 28, 9, 0.6 );
INSERT INTO  COMPOSITION  VALUES( 28, 52, 0.07 );
INSERT INTO  COMPOSITION  VALUES( 28, 49, 0.12 );
INSERT INTO  COMPOSITION  VALUES( 28, 51, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 29, 4, 1 );
INSERT INTO  COMPOSITION  VALUES( 29, 34, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 29, 5, 0.012 );
INSERT INTO  COMPOSITION  VALUES( 29, 66, 0.005 );
INSERT INTO  COMPOSITION  VALUES( 29, 67, 0.005 );
INSERT INTO  COMPOSITION  VALUES( 29, 63, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 30, 1, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 30, 4, 0.8 );
INSERT INTO  COMPOSITION  VALUES( 30, 5, 0.1 );
INSERT INTO  COMPOSITION  VALUES( 30, 38, 0.1 );
INSERT INTO  COMPOSITION  VALUES( 30, 3, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 31, 5, 0.07 );
INSERT INTO  COMPOSITION  VALUES( 31, 4, 0.08 );
INSERT INTO  COMPOSITION  VALUES( 31, 40, 0.6 );
INSERT INTO  COMPOSITION  VALUES( 31, 41, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 31, 42, 0.043 );
INSERT INTO  COMPOSITION  VALUES( 31, 43, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 32, 4, 0.08 );
INSERT INTO  COMPOSITION  VALUES( 32, 5, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 32, 3, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 32, 65, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 33, 65, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 33, 1, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 33, 4, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 33, 5, 0.015 );
INSERT INTO  COMPOSITION  VALUES( 33, 70, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 33, 8, 0.001 );
INSERT INTO  COMPOSITION  VALUES( 34, 2, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 34, 6, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 34, 5, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 34, 39, 0.1 );
INSERT INTO  COMPOSITION  VALUES( 35, 64, 0.06 );
INSERT INTO  COMPOSITION  VALUES( 35, 3, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 35, 34, 0.07 );
INSERT INTO  COMPOSITION  VALUES( 35, 5, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 36, 1, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 36, 3, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 36, 5, 0.018 );
INSERT INTO  COMPOSITION  VALUES( 36, 45, 0.12 );
INSERT INTO  COMPOSITION  VALUES( 37, 43, 0.09 );
INSERT INTO  COMPOSITION  VALUES( 37, 1, 0.05 );
INSERT INTO  COMPOSITION  VALUES( 37, 2, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 37, 3, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 37, 4, 0.2 );
INSERT INTO  COMPOSITION  VALUES( 37, 5, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 38, 5, 0.7 );
INSERT INTO  COMPOSITION  VALUES( 38, 3, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 38, 6, 0.006 );
INSERT INTO  COMPOSITION  VALUES( 38, 10, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 38, 2, 0.012 );
INSERT INTO  COMPOSITION  VALUES( 39, 46, 0.035 );
INSERT INTO  COMPOSITION  VALUES( 39, 45, 0.035 );
INSERT INTO  COMPOSITION  VALUES( 39, 41, 0.02 );
INSERT INTO  COMPOSITION  VALUES( 39, 40, 0.04 );
INSERT INTO  COMPOSITION  VALUES( 39, 39, 0.03 );
INSERT INTO  COMPOSITION  VALUES( 40, 46, 0.12 );
INSERT INTO  COMPOSITION  VALUES( 41, 6, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 41, 4, 0.2 );
INSERT INTO  COMPOSITION  VALUES( 41, 1, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 41, 3, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 41, 5, 0.01 );
INSERT INTO  COMPOSITION  VALUES( 42, 70, 0.035 );
INSERT INTO  COMPOSITION  VALUES( 43, 71, 0.035 );
INSERT INTO  COMPOSITION  VALUES( 44, 72, 0.03 );

INSERT INTO  BOISSONS  VALUES( 1, 'eau plate', 'eau', 'L' , 3, 17, 0.2 );
INSERT INTO  BOISSONS  VALUES( 2, 'eau gazeuse', 'eau', 'L', 3, 17, 0.3 );
INSERT INTO  BOISSONS  VALUES( 3, 'Coca Cola', 'soda', 'canette', 3.50, 13, 0.4 );
INSERT INTO  BOISSONS  VALUES( 4, 'Coca Cola Zero', 'soda', 'canette', 3.50, 13, 0.4 );
INSERT INTO  BOISSONS  VALUES( 5, 'Fanta', 'soda', 'canette', 3.50, 13, 0.4 );
INSERT INTO  BOISSONS  VALUES( 6, 'Ice Tea', 'soda', 'canette', 3.50, 13, 0.4 );
INSERT INTO  BOISSONS  VALUES( 7, 'Oasis', 'soda', 'canette', 3.50, 13, 0.4 );
INSERT INTO  BOISSONS  VALUES( 8, 'sirop grenadine', 'sirop', 'L', 116, 13, 0.4 );
INSERT INTO  BOISSONS  VALUES( 9, 'sirop menthe', 'sirop', 'L', 116, 13, 0.4 );
INSERT INTO  BOISSONS  VALUES( 10, 'limonade', 'soda', 'bouteille', 3.4, 13, 0.4 );
INSERT INTO  BOISSONS  VALUES( 11, 'expresso', 'cafe', 'kg', 312.5, 11, 39.9 );
INSERT INTO  BOISSONS  VALUES( 12, 'double expresso', 'cafe', 'kg', 312.5, 11, 39.9 );
INSERT INTO  BOISSONS  VALUES( 13, 'jus orange', 'jus', 'bouteille', 3.2, 2, 0.7 );
INSERT INTO  BOISSONS  VALUES( 14, 'jus pomme', 'jus', 'bouteille', 3.2, 2, 0.7 );
INSERT INTO  BOISSONS  VALUES( 15, 'jus ananas', 'jus', 'bouteille', 3.9, 12, 0.8 );
INSERT INTO  BOISSONS  VALUES( 16, 'jus abricot', 'jus', 'bouteille', 3.8, 1, 0.8 );
INSERT INTO  BOISSONS  VALUES( 17, 'jus framboise', 'jus', 'bouteille', 4.1, 1, 0.9 );
INSERT INTO  BOISSONS  VALUES( 18, 'chateau Pierron rouge', 'vin', 'L', 39.9, 15, 5.8 );
INSERT INTO  BOISSONS  VALUES( 19, 'comte des clos rouge', 'vin', 'L', 37, 15, 4.1 );
INSERT INTO  BOISSONS  VALUES( 20, 'chateauneuf du pape rouge', 'vin', 'L', 55, 15, 12 );
INSERT INTO  BOISSONS  VALUES( 21, 'chateau des rochers rouge', 'vin', 'L', 82, 15, 16 );
INSERT INTO  BOISSONS  VALUES( 22, 'chateau de Valcombe rouge', 'vin', 'L', 22, 15, 7.9 );
INSERT INTO  BOISSONS  VALUES( 23, 'Sonnenta rose', 'vin', 'L', 14.9, 15, 5.9 );
INSERT INTO  BOISSONS  VALUES( 24, 'Dom Brial Helios rose', 'vin', 'L', 14.9, 15, 5.7 );
INSERT INTO  BOISSONS  VALUES( 25, 'Estandon Heritage rose', 'vin', 'L', 16.9, 15, 8.9 );
INSERT INTO  BOISSONS  VALUES( 26, 'Sauvignon blanc', 'vin', 'L', 7.9, 15, 4.95 );
INSERT INTO  BOISSONS  VALUES( 27, 'chateau de Valcombe blanc', 'vin', 'L', 11.2, 15, 6.9 );
INSERT INTO  BOISSONS  VALUES( 28, 'Chardonnay blanc', 'vin', 'L', 14.1, 15, 9.1 );
INSERT INTO  BOISSONS  VALUES( 29, 'la Perriere blanc', 'vin', 'L', 19.9, 15, 13.2 );
INSERT INTO  BOISSONS  VALUES( 30, 'Moet et Chandon', 'champagne', 'L', 59.9, 16, 29.9 );
INSERT INTO  BOISSONS  VALUES( 31, 'Charles Clement', 'champagne', 'L', 39.9, 16, 19.9 );
INSERT INTO  BOISSONS  VALUES( 32, 'biere les 3 Monts', 'biere', 'L', 16, 13, 7.9 );
INSERT INTO  BOISSONS  VALUES( 33, 'whisky', 'a_fort', 'L', 200, 14, 99.99 );
INSERT INTO  BOISSONS  VALUES( 34, 'gin', 'a_fort', 'L', 45.8, 14, 24.99 );
INSERT INTO  BOISSONS  VALUES( 35, 'rhum', 'a_fort', 'L', 197.5, 14, 95.5 );
INSERT INTO  BOISSONS  VALUES( 36, 'limoncello', 'a_fort', 'L', 150, 14, 75 );
INSERT INTO  BOISSONS  VALUES( 37, 'ouzo', 'a_fort', 'L', 195, 14, 88.8 );
INSERT INTO  BOISSONS  VALUES( 38, 'sake', 'a_fort', 'L', 49.9, 14, 25 );
INSERT INTO  BOISSONS  VALUES( 39, 'get 27', 'a_fort', 'L', 39.9, 13, 14 );
INSERT INTO  BOISSONS  VALUES( 40, 'cognac', 'a_fort', 'L', 212.5, 14, 104.9 );

-- TRIGGERS

-- Le prix d'un EPD doit être supérieur à la somme des prix des ingrédients qui le compose

CREATE OR REPLACE trigger prix_EPD_1
    BEFORE INSERT OR UPDATE ON Carte
DECLARE
    cout number(7,4) := 0;
BEGIN
    SELECT sum(I.prix_igd*Co.nb_unites) INTO cout
    FROM Ingredients I, Composition Co
    WHERE :new.num_carte = Co.num_carte
    AND Co.num_igd = I.num_igd;
    IF :new.prix_carte <= cout THEN
        raise application_error(001, 'Le prix de vente cet EPD est trop faible comparé à son coût de production.');
END;
/

CREATE OR REPLACE trigger prix_EPD_2
    BEFORE INSERT OR UPDATE ON Composition
        FOR EACH ROW
DECLARE
    cout number(7,4) := 0;
BEGIN
    SELECT sum(I.prix_igd*:new.nb_unites) INTO cout
    FROM Ingredients I, Carte C
    WHERE :new.num_carte = C.num_carte;
    IF cout >= C.prix_carte THEN
        raise application_error(002, 'Le prix de vente d un EPD est trop faible comparé à son coût de production.');
END;
/

-- Le prix de la boisson à l'achat doit être inférieur à celui à la vente

-- pas trigger normalement, j'ai mis un CHECK dans la création de la table

--CREATE OR REPLACE trigger prix_boissons
--    BEFORE INSERT OR UPDATE ON Boissons
--BEGIN
--    IF :new.prix_boisson_achat > :new.prix_boisson_vente THEN
--        raise application_error(003, 'Le prix de vente d une boisson doit être supérieur à son prix d achat.')
--END;
--/

-- Pour chaque commande, le stock des ingrédients nécessaires aux EPD commandés diminue.
            -- Si le stock n’est pas suffisant à la préparation, alors le client doit en choisir un autre.

CREATE OR REPLACE trigger maj_stocks
    BEFORE INSERT OR UPDATE OR DELETE ON Est_commande
DECLARE
    CURSOR c1 IS (SELECT I.num_igd as constituant, C.nb_EPD as quantite
                    FROM Ingredients I, Est_Commande EC, Composition C
                    WHERE EC.num_carte = C.num_carte
                    AND C.num_igd = I.num_igd
                    AND EC.num_carte = :new.num_carte);
    nv_stock number := 0;
    nv_qte number := 0;
BEGIN
    FOR igd IN c1 LOOP
        IF inserting THEN
            nv_stock := (SELECT stock
                        FROM Ingredients
                        WHERE num_igd = igd.constituant) - (:new.nb_unites * igd.quantite);
            UPDATE Ingredients SET stock = nv_stock
            WHERE num_igd = igd.constituant;
        END IF;
        IF updating or deleting THEN
            IF deleting OR (:new.nb_EPD < :old.nb_EPD) THEN      -- commande annulée : on rajoute les ingrédients dans les stocks
                IF deleting THEN
                    nv_qte := :old.nb_EPD;
                ELSE
                    nv_qte := :old.nb_EPD - :new.nb_EPD;
                END IF;
                nv_stock := (SELECT stock
                        FROM Ingredients
                        WHERE num_igd = igd.constituant) + (nv_qte * igd.quantite);
                UPDATE Ingredients SET stock = nv_stock
                WHERE num_igd = igd.constituant;
                EXIT;
            END IF;
            IF :new.nb_EPD > :old.nb_EPD THEN                   -- ajout d'une commande pour cet EPD
                nv_qte := :new.nb_EPD - :old.nb_EPD;
            ELSE                                                -- nb_EPD n'a pas changé 
                nv_qte := :new.nb_EPD;
            END IF;
            nv_stock := (SELECT stock
                        FROM Ingredients
                        WHERE num_igd = igd.constituant) - (nv_qte * igd.quantite);
            UPDATE Ingredients SET stock = nv_stock
            WHERE num_igd = igd.constituant;
        END IF;        
    END;
/

-- Un client ne peut venir manger dans le restaurant que si le nombre maximum de couverts n’a pas été dépassé (200 couverts par service)

CREATE OR REPLACE trigger max_couverts
    BEFORE INSERT ON Commandes
DECLARE
    nb_couverts number(3) := 0;
BEGIN
    nb_couverts := (SELECT count(num_commande)
                    FROM Commandes
                    WHERE date_commande = :new.date_commande);
    IF nb_couverts >= 200 THEN
        raise application_error(101, 'Le nombre maximum de couverts a été atteint, aucune nouvelle commande ne peut être passée.');
END;
/

-- Chaque entrée, chaque plat et chaque dessert contient au moins un ingrédient

    -- Il y a une dépendance cyclique car dans la table Composition, num_carte est une clé étrangère de Carte(num_carte)
    -- donc il faudrait créer les tuples de la table Carte avant de leur associer des ingrédients dans la table Composition.
    -- Mais la contrainte empêcherait par exemple l'insertion de nouveaux EPD (dans Carte) si ceux-ci ne sont pas déjà dans
    -- la table Composition, ce qui est donc impossible.
    -- Pour cela, il faudrait créér les tables avec une des deux contraintes puis la désactiver (DISABLE CONSTRAINT)
    -- pour créér la deuxième et enfin réactiver la première (ENABLE CONSTRAINT).

ALTER TABLE Composition
    DISABLE CONSTRAINT fk_composition_carte;

ALTER TABLE Carte
    ADD CONSTRAINT composition_EPD
    CHECK (num_carte IN (SELECT num_carte FROM Composition));

ALTER TABLE Composition
    ENABLE CONSTRAINT fk_composition_carte;

-- Une commande est forcément associée à au moins une boisson ou un EPD commandé.

    -- Il s'agit aussi d'une dépendance cyclique.

ALTER TABLE Est_Commande
    DISABLE CONSTRAINT fk_est_commande_commandes;

ALTER TABLE A_Boire
    DISABLE CONSTRAINT fk_a_boire_commandes;

ALTER TABLE Commandes
    ADD CONSTRAINT commande_eat_or_drink
    CHECK (num_commande IN (SELECT num_commande FROM Est_Commande UNION
                            SELECT num_commande FROM A_Boire));

ALTER TABLE Est_Commande
    ENABLE CONSTRAINT fk_est_commande_commandes;

ALTER TABLE A_Boire
    ENABLE CONSTRAINT fk_a_boire_commandes;

-- Certaines boissons ne sont vendues que pour un volume donné.
-- Il faut donc vérifier que nb_unites soit un multiple de ce volume.

    -- Le vin est vendu soit au verre (14 cL) soit à la bouteille (75 cL). Le nombre d'unités (en L) doit donc être
    -- un flottant P tel que P = v * 0.17 + b * 0.75 avec v et b deux entiers <=> (P%0.75)%0.17 doit être égal à 0.

    -- La quantité de bière vendue est de 25cL ou 50cL.
    -- Les sirops sont vendus par dose de 25cL.

    -- L'eau (plate ou gazeuse) est vendue en petite bouteille (33cL) ou en grande bouteille (75cL).

    -- Dans un café, il y a 8g de grains de café pour un expresso, 16g pour un double-expresso.

    -- Le champagne n'est vendu que par bouteille, soit 75cL.

    -- Un alcool fort (de type a_fort) est vendu par dose de 4cL.

    
CREATE OR REPLACE trigger unites_boissons
    BEFORE INSERT OR UPDATE ON A_Boire
DECLARE
    t_boisson varchar(10);
BEGIN
    SELECT type_boisson INTO t_boisson
    FROM Boissons
    WHERE B.num_boisson = :new.num_boisson;
    IF ((t_boisson = 'vin') AND ((:new.nb_unites%0.75)%0.14 != 0))
        OR (((t_boisson = 'biere') OR (t_boisson = 'sirop')) AND (:new.nb_unites%0.25 != 0))
        OR ((t_boisson = 'eau') AND ((:new.nb_unites%0.75)%0.33 != 0))
        OR ((t_boisson = 'cafe') AND (:new.nb_unites%8 != 0))
        OR ((t_boisson = 'champagne') AND (:new.nb_unites%0.75 != 0))
        OR ((t_boisson = 'a_fort') AND (:new.nb_unites%0.04 != 0)) THEN
            raise application_error(200, 'Le nombre d unites n est pas correct');
END;
/

-- Créer la procédure à exécuter pour augmenter les stocks d'un ingrédient,
-- lors de la réception des commandes passées aux fournisseurs par exemple.

CREATE OR REPLACE procedure augmenter_stock (num_ingredient, nb_unites) IS
BEGIN
    UPDATE Ingredients SET stock = stock + nb_unites
        WHERE num_igd = num_ingredient
END;
/


-- REQUETES

-- Combien de bouteilles de vin ont été vendues le samedi 14 octobre 2023 ?
-- Pour rappel, une bouteille de vin a une contenance de 75 cL et un verre de vin est de contenance 17 cL.

DECLARE
    CURSOR c1 AS SELECT * FROM A_boire;
    drink_type varchar(15) := '0';
    nb_tot_bouteilles number := 0;
BEGIN
    FOR tuple IN c1 LOOP
        drink_type := SELECT b.type_boisson
                        FROM Boissons B
                        WHERE B.num_boisson = tuple.num_boisson
        IF drink_type = 'vin' AND mod(tuple.nb_unites, 0.75) = 0 THEN
            nb_tot_bouteilles := nb_tot_bouteilles + (tuple.nb_unites/0.75)
        END IF;
    END LOOP;               -- il faut ensuite renvoyer le resultat
END;
/

-- Quels sont les noms des clients qui ont réservé une table le vendredi 21 avril 2023 ?

SELECT nom_client
FROM Client
WHERE date_commande = 'Ven-21-Avril-2023'
AND nom_client IS NOT NULL;

-- Quels sont les desserts dont le prix est inférieur ou égal à 10 euros ?

SELECT nom_carte
FROM CARTE
WHERE type_EPD = 'D'
AND prix_carte <= 10;

-- Quels sont les serveurs qui n'ont pas travaillé la semaine du 06/11/2023 ?  Combien sont-ils ?

SELECT num_serveur
FROM Serveurs
WHERE num_serveur NOT IN (SELECT num_serveur
                            FROM Serveurs S, Commande C
                            WHERE S.num_serveur = C.num_serveur
                            AND WEEK(C.date_commande) = WEEK (06-11-2023) and YEAR(C.date_commande) = YEAR(06-11-2023));

-- Quels sont les serveurs qui ont travaillé chaque mardi en novembre 2023 ?
-- <=> les serveurs tel qu'il n'existe pas de mardi de novembre 2023 tel qu'il n'existe pas
--                                              de commande servie par ce serveur ce jour-là

SELECT S.*
FROM Serveurs s
WHERE NOT EXISTS (SELECT *
                    FROM Commandes)     -- bizarre car 2 tables seulement

-- Trouver autre division

-- Quels sont les EPD qui contiennent des œufs, du gluten, du lactose, des fruits à coque, du poisson, des fruits de mer ou de céleri ?

SELECT nom_carte as plat, nom_igd as ingredient
FROM Carte C, Ingredients I, Composition Co
WHERE Co.num_carte = C.num_carte
AND Co.num_igd = I.num_igd
AND I.nom_igd IN ('oeuf', 'celeri')
UNION
SELECT distinct(nom_carte) as plat, 'gluten' as ingredient
FROM Carte C, Ingredients I, Composition Co
WHERE Co.num_carte = C.num_carte
AND Co.num_igd = I.num_igd
AND I.nom_igd IN ('farine', 'levure', 'pain', 'pate lasagne', 'biscuit cuillere', 'speculoos', 'glace chocolat', 'poudre cacao')
UNION
SELECT distinct(nom_carte) as plat, 'lactose' as ingredient
FROM Carte C, Ingredients I, Composition Co
WHERE Co.num_carte = C.num_carte
AND Co.num_igd = I.num_igd
AND I.nom_igd IN ('lait', 'beurre', 'creme', 'chevre', 'mozzarella', 'emmental', 'mascarpone', 'parmesan', 'feta')
UNION
SELECT distinct(nom_carte) as plat, 'fruits à coque' as ingredient
FROM Carte C, Ingredients I, Composition Co
WHERE Co.num_carte = C.num_carte
AND Co.num_igd = I.num_igd
AND I.nom_igd IN ('noix', 'speculoos', 'biscuit cuillere', 'glace chocolat')
UNION
SELECT distinct(nom_carte) as plat, 'poisson/fruit de mer' as ingredient
FROM Carte C, Ingredients I, Composition Co
WHERE Co.num_carte = C.num_carte
AND Co.num_igd = I.num_igd
AND I.nom_igd IN ('raie', 'saumon fume', 'sole', 'st pierre', 'thon rouge', 'poulpe', 'couteau', 'crevette', 'st jacques', 'langoustine');

-- En août 2023, combien d’argent les boissons ont-elles générées ? Quel était le prix total de l’achat de ces boissons aux fournisseurs ?

SELECT sum(A.nb_unites*B.prix_boisson_achat) as somme_vente,
        sum(A.nb_unites*B.prix_boisson_vente) as somme_achat,
        (somme_achat-somme_vente) as marge
FROM A_boire A, Boissons B, Commandes C
WHERE A.num_boisson = B.num_boisson
AND A.num_commande = C.num_commande
AND C.date_commande = '%-08-2023';

-- Retourner les ingrédients dont le stock est inférieur à 10 unités ainsi que leur fournisseur.

SELECT I.num_igd, I.nom_igd, F.nom_fournisseur, F.num_tel
FROM Ingredients I, Fournisseurs F
WHERE I.num_fournisseur = F.num_fournisseur
AND I.stock < 10;

-- Donner la dépense moyenne d’un client de la semaine du 04/01/2021 en fonction des services du midi et du soir.

SELECT avg(depenses_midi.depenses) AS moyenne_midi, avg(depenses_soir.depenses) AS moyenne_soir
FROM (SELECT sum(Ca.prix_carte)+sum(B.prix_boisson_vente) as depenses
        FROM Commandes Co, Carte Ca, Boissons B, Est_commande EC, A_boire AB
        WHERE Ca.num_carte = EC.num_carte
        AND EC.num_commande = Co.num_commande
        AND Co.num_commande = AB.num_commande
        AND AB.num_boisson = B.num_boisson
        AND Co.service = 'M'
        AND WEEK(Co.date_commande) = WEEK(04-01-2021) and YEAR(Co.date_commande) = YEAR(04-01-2021))depenses_midi
    (SELECT sum(Ca.prix_carte)+sum(B.prix_boisson_vente) as depenses
        FROM Commandes Co, Carte Ca, Boissons B, Est_commande EC, A_boire AB
        WHERE Ca.num_carte = EC.num_carte
        AND EC.num_commande = Co.num_commande
        AND Co.num_commande = AB.num_commande
        AND AB.num_boisson = B.num_boisson
        AND Co.service = 'S'
        AND WEEK(Co.date_commande) = WEEK(04-01-2021) and YEAR(Co.date_commande) = YEAR(04-01-2021)) depenses_soir;


