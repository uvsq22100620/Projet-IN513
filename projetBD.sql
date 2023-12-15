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
    type_boisson VARCHAR(20) CHECK(type_boisson IN ('eau', 'soda', 'sirop', 'jus', 'biere', 'vin', 'champagne', 'a_fort', 'cafe')),
    unite varchar(20) CHECK(unite IN ('L', 'canette', 'bouteille', 'kg')),
    prix_boisson_vente float CHECK(prix_boisson_vente>0.0),
    prix_boisson_achat float CHECK(prix_boisson_achat>0.0),
    num_fournisseur number,
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
    num_table number CHECK(num_table BETWEEN 1 AND 15),
    num_serveur number,
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


