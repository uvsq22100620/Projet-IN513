-- Projet IN513 - LE CORRE Camille et LEFEVRE Laura

CREATE TABLE CARTE (
    num_carte number,
    nom_carte varchar(30),
    typeEPD varchar(1) CHECK(typeEPD IN ('E', 'P', 'D')),
    prix_carte float CHECK(prix_carte >0 AND prix_carte<100),
    CONSTRAINT pk_carte PRIMARY KEY (num_carte)
);

CREATE TABLE FOURNISSEURS (
    num_fournisseur number,
    nom_fournisseur varchar(30),
    ville varchar(30),
    num_tel varchar(10) UNIQUE,
    CONSTRAINT pk_fournisseurs PRIMARY KEY (num_fournisseur)
);

CREATE TABLE BOISSONS (
    num_boisson number,
    nom_boisson varchar(30),
    type_boisson VARCHAR(20) CHECK(type_boisson IN ('eau', 'soda', 'sirop', 'jus', 'vin', 'champagne', 'aperitif', 'digestif', 'cafe')),
    unite varchar(20) CHECK(unite IN ('L', 'canette', 'bouteille', 'kg')),
    prix_boisson_vente float CHECK(prix_boisson_vente>0.0),
    prix_boisson_achat float CHECK(prix_boisson_achat>0.0),
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
    num_table number CHECK(num_table BETWEEN 1 AND 15),
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
    nb_unites float,
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

-- TRIGGERS

-- Le prix d'un EPD doit être supérieur à la somme des prix des ingrédients qui le compose

CREATE OR REPLACE trigger prix_EPD_1
    BEFORE INSERT OR UPDATE ON Carte
DECLARE
    cout Number(7,4) := 0;
BEGIN
    SELECT sum(I.prix_igd*Co.nb_unites) INTO cout
    FROM Ingredients I, Composition Co
    WHERE :new.num_carte = Co.num_carte
    AND Co.num_igd = I.num_igd
    IF :new.prix_carte <= cout THEN raise application_error(001, 'Le prix de vente cet EPD est trop faible comparé à son coût de production.')
END;
/

CREATE OR REPLACE trigger prix_EPD_2
    BEFORE INSERT OR UPDATE ON Composition
        FOR EACH ROW
DECLARE
    cout Number(7,4) := 0;
BEGIN
    SELECT sum(I.prix_igd*:new.nb_unites) INTO cout
    FROM Ingredients I, Carte C
    WHERE :new.num_carte = C.num_carte
    IF cout >= C.prix_carte THEN raise application_error(002, 'Le prix de vente d un EPD est trop faible comparé à son coût de production')
END;
/

-- Pour chaque commande, le stock des ingrédients nécessaires aux EPD commandés diminue.
-- Si le stock n’est pas suffisant à la préparation, alors le client doit en choisir un autre.

CREATE OR REPLACE trigger assez_igd
    BEFORE INSERT OR UPDATE ON Est_commande
BEGIN
END;
/

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
    nb_tot_bouteilles int := 0;
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

-- Quels sont les EPD qui contiennent du lait ou des œufs ou poisson ou noix ?

SELECT nom_carte, nom_igd
FROM Carte C, Ingredients I, Composition Co
WHERE Co.num_carte = C.num_carte
AND Co.num_igd = I.num_igd
AND I.nom_igd IN ('lait', 'oeuf'); -- ...

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


