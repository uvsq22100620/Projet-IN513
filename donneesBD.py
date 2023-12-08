import random
import time
from datetime import datetime, timedelta

# Constantes

num_commande = 1

# EPD
num_entrees = [k for k in range(1, 11)]
num_plats = [k for k in range(12, 28)]
num_desserts = [k for k in range(29, 45)]

# boissons
num_eau = [1, 2]
num_ss_alcool = [k for k in range(3,18)]
num_vin = [k for k in range(18,30)]
num_alcool = [k for k in range(30,41)]
num_cafe = [41, 42]

dico_semaine = {'Tuesday':'Mar', 'Wednesday':'Mer', 'Thursday':'Jeu', 'Friday': 'Ven', 'Saturday':'Sam', 'Sunday':'Dim'}
dico_mois = {'January':'Janvier', 'February':'Fevrier', 'March':'Mars', 'April':'Avril', 'May':'Mai', 'June':'Juin', 'July':'Juillet',
             'August':'Aout', 'September':'Septembre', 'October':'Octobre', 'November':'Novembre', 'December':'Decembre'}

liste_noms_clients = ['NULL', 'Auclair', 'Barth', 'Berdrate', 'Bouleau', 'Bourra', 'Brezellec', 'Camion', 'Chairet', 'Chalant', 'Chevalier', 'Corsi', 'Coucheney', 'Cremazy', 'Debat', 'Diab', 'Durand',
                          'Etchebest', 'Fages', 'Farny', 'Ferrat', 'Finance', 'Fourneau', 'Gattoliat', 'Garnier', 'Gaumer', 'Gianfrotta', 'Hoareau', 'Jacquin', 'Jellouli', 'Juliza', 'Keddis', 'Lamy', 'Lebbah',
                          'Le Corre', 'Lefevre', 'Lemaire', 'Lignac', 'Manour', 'Marque', 'Mayer', 'Mediouni', 'Mercorelli', 'Moindjie', 'Moreno', 'Mothor', 'Netter', 'Ninoux',
                          'Prehaud', 'Pret', 'Prieu', 'Quessette', 'Rincheval', 'Rotella', 'Sandu', 'Sapriel', 'Sitterlin', 'Sourdeval', 'Strozecki', 'Szuplewzki', 'Taher',
                          'Terki', 'Thibuta', 'Timsiline', 'Tseveendorj', 'Vial', 'Vincens']

liste_noms_clients_V2 = ['Duval', 'Yapo', 'Barbosa', 'Lam', 'Debat', 'Savary', 'Colin', 'Caron', 'Boulogne', 'Chevon', 'Vaxelaire', 'Bourra', 'Finance', 'Eberlin', 'Rotella', 'Jacques', 'Goudout', 'Diter', 'Benaoudia', 'Emerdjian', 'Cisse', 'Vervel', 'Bonnet', 'Mazzoni', 'Speters', 'Martel', 'Breter', 'Pridal', 'Toso', 'Lavigne', 'Raynal', 'Danest', 'Gros', 'Priquet', 'Ghisolfo', 'Le Bihan', 'Ventre', 'Olive', 'Sourdeval', 'Vogel', 'Prasse', 'Khenoun', 'Dupages', 'Medbouhi', 'Lacroix', 'Jacob', 'Henry', 'Joannet', 'Geneste', 'Lagarde', 'Vixemar', 'Versaveau', 'Allard', 'Viart', 'Hoareau', 'Alix', 'Tijari', 'Schmitt', 'Normand', 'Evrard', 'Trellu', 'Pascal', 'Bulver', 'Garnier', 'Daniel', 'Wu', 'Ursule', 'Laurent', 'Rivera', 'Satterne', 'Ibrame', 'Besson', 'Lepine', 'Rouinvy', 'Aubert', 'Ferrer', 'Jardine', 'Masson', 'Le', 'Bragne', 'Mielle', 'Willaume', 'Levy', 'Bauwens', 'Heron', 'Villate', 'Van', 'Lebreton', 'Neel', 'Maury', 'Wagner', 'Panflet', 'Vial', 'Blanchard', 'Hoarau', 'Carlier', 'Chauvin', 'Leger', 'Gallet', 'Gautier', 'Doutrelon', 'Humery', 'Gianfrotta', 'Aubin', 'Tuzi', 'Cartron', 'Renard', 'Lignac', 'Koita', 'Younsi', 'Labori', 'Dutot', 'Jourdan', 'Garcia', 'Canfrais', 'Dossantos', 'Renaut', 'Timsiline', 'Varoqui', 'Thibault', 'Conti', 'Hargas', 'Jung', 'Brun', 'Cressan', 'Blancher', 'Brogniart', 'Barrier', 'Levesque', 'Ntuti', 'Prat', 'Ruiz', 'Vetillard', 'Heduit', 'Adele-amelie', 'Li', 'Mache', 'Oubir', 'Linard', 'Bienaime', 'Bonnin', 'Bourgeois', 'Bailly', 'Metel', 'Mayer', 'Maitre', 'Imbault', 'Strozik', 'Boucher', 'Cambrete', 'Leroux', 'Peltier', 'Benoit', 'Abdoul', 'Hamad', 'Minoggio', 'Suarez', 'Pichon', 'Allain', 'Khalin', 'Duvalet', 'Blot', 'Guillaume', 'Olivier', 'Guillot', 'Lefevre', 'Tuffet', 'Carre', 'Germette', 'Couture', 'Zemmouri', 'Pinto', 'Charpentier', 'Fontaine', 'Casa', 'Delage', 'Dupuy', 'Said', 'Ferjoux', 'Hoff', 'Keita', 'Honduc', 'Reeb', 'Debruyne', 'Poirier', 'Cabrit', 'Carpentier', 'Masset', 'Lassouani', 'Taher', 'Klepper', 'Dalmais', 'Lolic', 'Aval', 'Renaud', 'Grondin', 'Le Corre', 'Dasilva', 'Fernandez', 'Benard', 'Pruvost', 'Rottenberg', 'Gosse', 'Bouchet', 'Pineau', 'Chalant', 'Godard', 'Richard', 'Raynaud', 'Chatillard', 'Fourgous', 'Lucas', 'Grenier', 'Clement', 'Szuplewzki', 'Jaunet', 'Attour', 'Solomon', 'Faure', 'Li Combeau', 'Prieu', 'Mendes', 'Zagnoni', 'Kevan', 'Pommier', 'Zelamta', 'Poulain', 'Merton', 'Oliveira', 'Bergot', 'Haidi', 'Terki', 'Berna', 'Hilleu', 'Queretti', 'Cozette', 'Djebrouni', 'Reber', 'Boussinet', 'Buades', 'Moulin', 'Gaouditz', 'Chalabi', 'Florent', 'Quessette', 'Bazin', 'Fernandes', 'Philippe', 'Ludiongo', 'Ahmed', 'Fourichon', 'Leconte', 'Marion', 'El Assir', 'Davoli', 'Launay', 'El Moussafer', 'Robuste', 'Lepifre', 'Piouceau', 'Vallet', 'Salimier', 'Juliza', 'Guillemard', 'Phouphetlinthong', 'Rousset', 'Delorme', 'Thibuta', 'Nicolas', 'Fouquet', 'Lagneau', 'Nosel', 'Bruneau', 'Herve', 'Champeval', 'Bourdon', 'Ferenbach', 'Collard', 'Messi', 'Lemba', 'Wielgosz', 'Ferreira', 'Lemaire', 'Mulard', 'Vincetti', 'Leblanc', 'Chairet', 'Pinorelli', 'Bourdin', 'Adri', 'Adriansen', 'Fleury', 'Pages', 'Neto', 'Jacquet', 'Dussaud', 'Merle', 'Baron', 'Cabral', 'Dumeric', 'Dissons', 'Lebon', 'Lengard', 'Colombiani', 'Chouaib', 'Becue', 'Lebouc', 'Chollet', 'Baudry', 'Renault', 'Humbert', 'Da Silva', 'Diomande', 'Sanz', 'Ramos', 'Berrahmane', 'Roy', 'Ninoux', 'Moreau', 'Oster', 'Gherardi', 'Camus', 'Florence', 'Gerneau', 'Sautet', 'Perrot', 'Durand', 'Huet', 'Lepretre', 'Gerard', 'Lesage', 'Munarde', 'Bouzidi', 'Cambert', 'Santrot', 'Assaud', 'Faivre', 'Brisse', 'Coste', 'Sami', 'Gastel', 'Retriss', 'Lefebvre', 'Texier', 'Leclercq', 'Niel', 'Dolet', 'Hubert', 'Riou', 'Le Gall', 'Amoussou', 'Ollivier', 'Blangy', 'Rocher', 'Zenati', 'Guichard', 'Colas', 'Tomas', 'Voile', 'Francois', 'Ladjouze', 'Mokrab', 'Caillet', 'Cotillard', 'Moncler', 'Etienne', 'Reynaud', 'Brion', 'Lebrun', 'Rasamizanany', 'Coustillas', 'Danset', 'Maurice', 'Pencole', 'Joseph', 'Diab', 'Biles', 'Germain', 'Nouri', 'Delangue', 'Le Goff', 'Julien', 'Tardivel', 'Barbe', 'Depry', 'Seddis', 'Chatelin', 'Marchal', 'Seddiki', 'Abalil', 'Girard', 'Paul', 'Litalien', 'Morvan', 'Camion', 'Roche', 'Morin', 'Costa', 'Boyer', 'Hervy', 'Cousin', 'Pipelier', 'Tor', 'Boulanger', 'Rano', 'Dumas', 'Debah', 'Duhamel', 'Fourneau', 'Remy', 'Lanclos', 'Chaouch', 'Mignard', 'Perrin', 'Piot', 'Rodrigues', 'Laborde', 'Marchand', 'Guery', 'Vidal', 'Corsi', 'Benkherouf', 'David', 'Astier', 'Marechal', 'Netter', 'Fzeri', 'Fereira', 'Dubront', 'Labusciere', 'Valette', 'Petit', 'Uthayakumar', 'Rose', 'Raymond', 'Bison', 'Farny', 'Giraud', 'Tothe', 'Van Loo', 'Girondeau', 'Maeght', 'Keddis', 'Bousquet', 'Chevalier', 'Tessier', 'Debrif', 'Picard', 'Rios Campo', 'Martial', 'Grassin', 'Albert', 'Boucaud', 'Guillou', 'Vere', 'Payet', 'Coulon', 'Prevost', 'Grinda', 'Derian', 'Lallement', 'Iken', 'Loisel', 'Breton', 'Mediouni', 'Vanmarque', 'Melek', 'Pereira da cunha', 'Cheboub', 'Toussaint', 'Belmehdi', 'Melin', 'Varenne', 'Benyelles', 'Ait Sahlia', 'Buzin', 'Roussel', 'Tanguy', 'Barcelo', 'Michel', 'Aubry', 'Pericaud', 'Clerc', 'Donald', 'Binay', 'Menard', 'Biot', 'Fertier', 'Ribeiro', 'Guilbert', 'Therage', 'Marin', 'Lebbah', 'Ourdouillie', 'Seromenho', 'Haifi', 'Barre', 'Bonhomme', 'Mallet', 'Sicherre', 'Siaud', 'Marty', 'Leroy', 'Bertrand', 'Saccard', 'Maillar', 'Potier', 'Cohen', 'Lamotte', 'Frejoux', 'Didier', 'Sernaud', 'Thibaudeau', 'Godet', 'Gay', 'Laroche', 'Magnere', 'Ellili', 'Aabirate', 'Valentine', 'Corre', 'Lopez', 'Paule', 'Romero', 'Hachour', 'Salnot', 'Wrobel', 'Combo', 'Hamdi', 'Perrault', 'Iacob', 'Blanchet', 'Collet', 'Nalla', 'Tardieu', 'Pottier', 'Devaux', 'Denis', 'Salic', 'Moreira Da Silva', 'Martin', 'Debienne', 'Batata', 'Diallo', 'Bouchenna', 'Bombart', 'Besiner', 'Aouaouche', 'Escande', 'Doquoy', 'Bisson', 'Lombard', 'Harbane', 'Jonda', 'Soares', 'Cheval', 'Millaniyage', 'Yull', 'Gillet', 'Pardo', 'Piroelle', 'Simart', 'Briand', 'Bouchon', 'Ardourel', 'Benabib', 'Jacquot', 'Cottin', 'Amoyal', 'Pret', 'Pelletier', 'Vivien', 'Michalak', 'Lingrand', 'Bognard', 'Dupuis', 'Sousa', 'Mobre', 'Nguyen', 'Adam', 'Ballgobin', 'Franceries', 'Delattre', 'Turpin', 'Chassat', 'Prehaud', 'Feraud', 'Gaillard', 'Barbier', 'Salmon', 'Baghdasaryan', 'Leveque', 'Nebre', 'Georges', 'Daunizeau', 'Asmaoui', 'Plisson', 'Sailly', 'Mas', 'Phkar', 'Guillon', 'Gilbert', 'Maurin', 'Ploutinet', 'Chabbert', 'Le Cam', 'Wassaf', 'Essallami', 'Khelil', 'Jellouli', 'Corbel', 'Fourault', 'Muller', 'Cozzi', 'Bisiou', 'Hammadi', 'Lepage', 'Verdier', 'Guennegues', 'Royer', 'Le Goueff', 'Dugrond', 'Mambrun', 'Grontier', 'Monnier', 'Cheaib', 'Collin', 'Michaud', 'Manour', 'Barth', 'Harnoufi', 'Besnier', 'Barthelemy', 'Bruges', 'Nemour', 'Legrand', 'Favre', 'Plantard', 'Willay', 'Robin', 'Ducorps', 'Brault', 'Courant', 'Desaulty', 'Rolland', 'Bartholus', 'Magnan', 'Lacombe', 'Maillot', 'Chauvet', 'Guenal', 'Hilaire', 'Legall', 'Marque', 'Sifi', 'Tang', 'Hardy', 'Strozecki', 'Moutarde', 'Tagba', 'Ferre', 'Dufour', 'Boivin', 'Revero', 'Meyer', 'Legoff', 'Brasse', 'Berger', 'Pereira', 'Etchebest', 'Sandu', 'Gaumer', 'Bigot', 'Spanneut', 'Reale', 'Bonneau', 'Martineau', 'Chazel', 'Langlois', 'Lado', 'Walryck', 'Besnard', 'Regaud', 'Kanga', 'Goncalves', 'Valentin', 'Loiseau', 'La Fonta', 'Grise', 'Cara', 'Dinant', 'Adrien', 'Maire', 'Gillieron', 'Hamon', 'Serber', 'Pervenche', 'Courtin', 'Debonne', 'Vaillant', 'Fabre', 'Descamps', 'Friess', 'Person', 'Blin', 'Vincens', 'Cassier', 'Daumas', 'Arnaud', 'Jouliot', 'Delcourt', 'Gauthier', 'Pellegrini', 'Geffray', 'Dumis', 'Lemaitre', 'Perrier', 'Isnard', 'Lenoir', 'Laline', 'Vasseur', 'Trosset', 'Milait', 'Louzet', 'Segaux', 'Baude', 'Striebig', 'Louis', 'Thomas', 'Iliassy', 'Janvier', 'Devillard', 'Taujers', 'Guerveno', 'Jouvet', 'Meunier', 'Delaunay', 'Rouxel', 'Pons', 'Truneaux', 'Courtois', 'Laurin', 'Moutou', 'Fages', 'Morel', 'Gaudin', 'Radelet', 'Boutamine', 'Lambert', 'Decaen', 'Dubluis', 'Auclair', 'Chany', 'Denechere', 'Alves', 'Haddane', 'Briere', 'Hammou', 'Belaidi', 'Casarno', 'Bel-hadj', 'Jean', 'Chekoua (bouers)', 'Voisin', 'Berdrate', 'Boura', 'Coubertin', 'Roger', 'Portelette', 'Ledeme', 'Guyot', 'Maussin', 'Doyurur', 'Mary', 'Martinez', 'Cortes', 'Brezellec', 'Massart', 'Sanchez', 'Bouteau', 'Pierre', 'Conticini', 'Glorieux', 'Imbert', 'Robert', 'Jeouit', 'Foucher', 'Schneider', 'DaSilva', 'Sitterlin', 'Bertin', 'Khezzar', 'Vauthier', 'Caillier', 'Fournier', 'Bchibchi', 'Le Blanc', 'Lefort', 'Balijon', 'Guibert', 'Armand', 'Loutrot', 'Delmas', 'Crespin', 'Tieres', 'Rondey', 'Sauvage', 'Paris', 'Bureau', 'Mercorelli', 'Rabate', 'Mothor', 'Markoulakis', 'Marie', 'Fischer', 'Lerose', 'Lemoine', 'Drepond', 'Flaubert', 'Bettaieb', 'Thierry', 'Dubois', 'Dupont', 'Joyeux', 'Vigier', 'Sinople', 'Blondel', 'Rilly', 'Rossi', 'Charpy', 'Laramendy', 'Auger', 'Lelu', 'Barbey', 'Couturier', 'Gomes', 'Dorido', 'Chayani', 'Leclerc', 'Dupin', 'Viollette', 'Razafindrabary', 'Stephan', 'Osyssek', 'Ferrez', 'Chakroun', 'Pasquier', 'Martins', 'Benitez', 'Bouvier', 'Chartier', 'Baillet', 'Hebert', 'Ferrat', 'Neveu', 'Weber', 'Sarrazin', 'Leduc', 'Berthelot', 'Allouche', 'Gabriel', 'Charrier', 'Noreskal', 'Bouarfa', 'Cordier', 'Plancq', 'Cherif', 'Roux', 'Temprement', 'Messeant', 'Tran', 'Millet', 'Vissault', 'Simoes', 'Moreno', 'Bonnel', 'Joly', 'Poireau', 'El abid', 'Bauzuin', 'Nelo', 'Houllio', 'Guyon', 'Rougier', 'Gomez', 'Vichet', 'Laporte', 'Laroui', 'Merbah', 'Seguin', 'Mathieu', 'Galibert', 'Noel', 'Bernard', 'Sulivan', 'Dore', 'Bouleau', 'Gattoliat', 'Lacoste', 'Hatem', 'Tellier', 'Rey', 'Fonseca', 'Cercus', 'Villain', 'Rincheval', 'Laposi', 'Perez', 'El Malki', 'Perret', 'Screve', 'Gaudray', 'Blanc', 'Guenart', 'Brunet', 'Antoine', 'Maillard', 'Jacquin', 'Bouziane', 'Amallah', 'Vignaud', 'Mignot', 'Artine', 'Paviot', 'Estanboulieh', 'Pigeot', 'Clarisse', 'Vetter', 'Riviere', 'Amara', 'Minard', 'Dos Santos', 'Coucheney', 'Guillet', 'Bodin', 'Gant', 'Arniers', 'Dumont', 'NULL', 'Rami', 'Pain', 'Rili', 'Hassler', 'Tseveendorj', 'Klein', 'Victor', 'Guerin', 'Ouaiche', 'Flejou', 'Cazemajou', 'Restier', 'Henaff', 'Rziki', 'Alvet', 'Pomplere', 'Magaletti', 'Chevallier', 'Alexandre', 'Cremazy', 'Charles', 'Fauchet', 'Jeyakanthan', 'Parodi', 'Dubourgeot', 'Lechien', 'Joubert', 'Mercier', 'Ferrand', 'Mohellibi', 'Royere', 'Moindjie', 'Maillet', 'Deschamps', 'Leboubenec', 'Lavie', 'Isaac', 'Frutiez', 'Andre', 'Seksaoui', 'Guinars', 'Dugelay', 'Gibier', 'Buisson', 'Boutin', 'Gonzalez', 'Lukacs', 'Mehimda', 'Nevers', 'Marteau', 'Fendt', 'Ayuso', 'Hernandez', 'Gabouze', 'Ami', 'Rodriguez', 'Rousseau', 'Gilles', 'Lamy', 'Peignet', 'Vincent', 'Lauriola', 'Lejeune', 'Ledoux', 'Saillard', 'Sapriel', 'Letrange', 'Louvet', 'Lecomte', 'Navarro', 'Tirgo', 'Brunel', 'Simon', 'Boukebouche', 'Chauveau', 'Lopes', 'Praud', 'Orlhac', 'Prive', 'Dacosta', 'Garel', 'Buffin', 'Bertholot', 'Milo']

#li = list(set(liste_noms_clients_V2+[]))
#print(li)
print(len(liste_noms_clients_V2))

liste_num_serveurs = [k for k in range(0,11)]

# tuples de la table COMMANDES

def dates_par_semaine_debut_mardi_sans_lundi():
    liste_annee = []

    for annee in range(2021, 2024):
        debut_annee = datetime(annee, 1, 1)
        fin_annee = datetime(annee, 12, 31)

        semaine = []
        date = debut_annee

        # Recherche du mardi
        while date.strftime("%A") != "Tuesday":
            date += timedelta(days=1)

        while date <= fin_annee:
            if date.strftime("%A") != "Monday":  # Exclure le lundi
                date_tuple = [date.strftime("%A"), date.strftime("%d"), date.strftime("%B"), date.strftime("%Y")]
                semaine.append(date_tuple)

            if date.strftime("%A") == "Sunday":
                liste_annee.append(semaine)
                semaine = []
                date += timedelta(days=2)  # Passer au mardi de la semaine suivante
            else:
                date += timedelta(days=1)

    return liste_annee

liste_annee = dates_par_semaine_debut_mardi_sans_lundi()

def serveurs_travaillant_sachant_service(jour, annee):
    """ Retourne la liste des serveurs travaillant le jour et l'annnée correspondante"""
    if (jour=='Ven') or (jour=='Sam') or (jour=='Dim'):
        nb_serveurs = random.choices([2, 3, 4], [0.25, 0.7, 0.05])[0]
    else:
        nb_serveurs = random.choices([1, 2, 3], [0.2, 0.75, 0.05])[0]

    if annee==2023:      #attention int/str
        serveurs = [k for k in range(2,11)]
    elif annee==2022:
        serveurs = [k for k in range(3, 9)]
    elif annee==2021:
        serveurs = [k for k in range(0,9)]
    else:
        serveurs = [k for k in range(0,7)]
    
    while len(serveurs)!= nb_serveurs:
        serveurs.remove(random.choices(serveurs)[0])

    return serveurs

def transfo_date_python_to_sql(sem):
    for j in sem:
        j_in_english = j[0]
        j[0] = dico_semaine[j_in_english]
        m_in_english = j[2]
        j[2] = dico_mois[m_in_english]
    return sem

def commandes_semaine(l_semaine, fic_commandes):

    global num_commande

    # Nombre de clients par service
    nb_mar_m = random.randint(63, 83)
    nb_mar_s = random.randint(40, 60)
    nb_mer_m = random.randint(65, 85)
    nb_mer_s = random.randint(65, 80)
    nb_jeu_m = random.randint(55, 80)
    nb_jeu_s = random.randint(75, 90)
    nb_ven_m = random.randint(68, 88)
    nb_ven_s = random.randint(110, 140)
    nb_sam_m = random.randint(95, 130)
    nb_sam_s = random.randint(110, 160)
    nb_dim_m = random.randint(80, 100)

    liste_services = [nb_mar_m, nb_mar_s, nb_mer_m, nb_mer_s, nb_jeu_m, nb_jeu_s,
                    nb_ven_m, nb_ven_s, nb_sam_m, nb_sam_s, nb_dim_m]
    l_services = ['M', 'S']

    proba_clients = [0.8]+[(0.2/len(liste_noms_clients)) for k in range(len(liste_noms_clients)-1)]
    proba_tables = [(2/56), (2/56), (2/56), (10/56), (4/56), (2/56), (2/56), (6/56), (2/56), (2/56),
                    (2/56), (6/56), (2/56), (4/56), (8/56)]


    for num_service in range(len(liste_services)):      # pour chaque service
        jour = l_semaine[num_service//2][0]
        num_jour = l_semaine[num_service//2][1]
        mois = l_semaine[num_service//2][2]
        annee = l_semaine[num_service//2][3]
        date_commande = "'" + jour + "-" + num_jour + "-" + mois + "-" + annee + "'"
        serveurs_travaillant = serveurs_travaillant_sachant_service(jour, annee)
        for num_client in range(liste_services[num_service]):       # pour chaque commande
            nom_client = random.choices(liste_noms_clients, proba_clients)[0]
            if nom_client != 'NULL':
                nom_client = "'" + nom_client + "'"        
            service = "'" + l_services[num_service%2] + "'"
            num_serveur = random.choices(serveurs_travaillant)[0]
            num_table = random.choices([k for k in range(1,16)], proba_tables)[0]
            tuple_commande = str(num_commande) + ", " + nom_client + ", " + str(date_commande) + ", " + service + ", " + str(num_serveur) + ", " + str(num_table)
            fic_commandes.write(tuple_commande+'\n')
            num_commande += 1

def commandes():
    fic_commandes = open('commandes.txt', 'w')
    for sem in liste_annee:
        semaine = transfo_date_python_to_sql(sem)
        commandes_semaine(semaine, fic_commandes)
    fic_commandes.close()

#commandes()

# tuples de la table EST_COMMANDE

def est_commande():

    l_choix = ['E', 'P', 'D', 'EP', 'ED', 'PD', 'DD', 'EE', 'PP', 'EPD', 'EPP', 'EEP', 'EED', 'PDD', 'EEPD', 'EPDD']
    probas_choix = [(0.2/16), (2/16), (0.5/16), (3/16), (0.2/16), (5/16), (0.1/16), (0.4/16), (0.1/16), (3/16), (0.2/16), (0.1/16), (0.1/16), (0.5/16), (0.3/16), (0.3/16)]

    with open('commandes.txt', 'r') as fic_commandes:
        lignes = fic_commandes.readlines()
    lignes_corrigees = [ligne.replace("NULL", "'NULL'") for ligne in lignes]
    tuples = [eval(ligne.strip()) for ligne in lignes_corrigees]

    fic_est_commande = open('est_commande.txt', 'w')

    for tpl in tuples:
        num_commande = tpl[0]
        choix = random.choices(l_choix, probas_choix)[0]
        for lettre_EPD in choix:
            if lettre_EPD == 'E':
                EPD = random.choice(num_entrees)
            elif lettre_EPD == 'P':
                EPD = random.choice(num_plats)
            else:
                EPD = random.choice(num_desserts)
            tpl_est_commande = str(num_commande) + ", " + str(EPD) + ", " + '1'     # aucun client n'a commandé 2 fois le meme EPD
            fic_est_commande.write(tpl_est_commande+'\n')
    fic_est_commande.close()

#est_commande()


# pour les boissons, mettre souvent de l'eau
# chaque commande a au moins une boisson associée ou un EPD

#def composition():
    #fic = open('composition.txt', 'a')
    #for i in range(3):
    #    num_EPD = input('EPD :')
        #if num_EPD == 'stop':
        #    break
    #    num_igd = input('ingredient :')
    #    fic.write(str(num_EPD)+', '+str(num_igd))
    #fic.close()
    #return

#composition()


def a_boire():
    # E = eau
    # S = sans alcool
    # V = vin
    # D = digestif
    # C = cafe
    l_choix = ['']
    with open('commandes.txt', 'r') as fic_commandes:
        lignes = fic_commandes.readlines()
    lignes_corrigees = [ligne.replace("NULL", "'NULL'") for ligne in lignes]
    tuples = [eval(ligne.strip()) for ligne in lignes_corrigees]

    fic_a_boire = open('a_boire.txt', 'w')

    for tpl in tuples:
        num_commande = tpl[0]
        lettre_boissons = ""

        eau = random.choices([True, False], [0.5, 0.5])
        if eau :
            lettre_boissons += 'E'

        ss_alcool = random.choices([True, False], [0.5, 0.5])
        if ss_alcool :
            lettre_boissons += 'S'

        vin = random.choices([True, False], [0.5, 0.5])
        if vin :
            lettre_boissons += 'V'    
    
    fic_a_boire.close()

def composition():   
    fic = open('composition.txt', 'a')
    EPD=0
    while EPD != 'stop':
        EPD = input('EPD')
        igd = input('ingredient')
        nb_unites = input('nb_unites')
        fic.write(EPD + ', ' + igd + ', ' + nb_unites + '\n')
    fic.close()
    return

composition()
