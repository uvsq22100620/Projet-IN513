import random
import time
from datetime import datetime, timedelta

# Constantes

num_commande = 1

# EPD
num_entrees = [k for k in range(1, 11)]
num_plats = [k for k in range(12, 28)]
num_desserts = [k for k in range(29, 44)]

# boissons
num_eau = [1, 2]
num_ss_alcool = [k for k in range(3,11)] + [k for k in range(13,18)]
num_cafe = [11, 12]
num_vin = [k for k in range(18,30)]
num_alcool = [k for k in range(30,41)]

dico_semaine = {'Tuesday':'Mar', 'Wednesday':'Mer', 'Thursday':'Jeu', 'Friday': 'Ven', 'Saturday':'Sam', 'Sunday':'Dim'}
dico_mois = {'January':'Janvier', 'February':'Fevrier', 'March':'Mars', 'April':'Avril', 'May':'Mai', 'June':'Juin', 'July':'Juillet',
             'August':'Aout', 'September':'Septembre', 'October':'Octobre', 'November':'Novembre', 'December':'Decembre'}

liste_noms_clients = ['Le Blanc', 'Valentin', 'Ollivier', 'Delorme', 'Thibuta', 'Fertier', 'Lamy', 'Debussy', 'Boutamine', 'Fabre', 'Roussel', 'Pomplere', 'Rondey', 'Maitre', 'Rilly', 'Cremazy', 'Villain', 'Seksaoui', 'Mas', 'Diallo', 'Vincens', 'Joyeux', 'Guerin', 'Rocher', 'Hammou', 'Santrot', 'Gaillard', 'Julien', 'Jung', 'Dupuis', 'Jourdan', 'Aabirate', 'Lefevre', 'Grenier', 'Seromenho', 'Martinez', 'Sulivan', 'Varoqui', 'Hamdi', 'DaSilva', 'Nguyen', 'El Malki', 'Gomez', 'Sinople', 'Ouaiche', 'Ferreira', 'Mokrab', 'Doutrelon', 'Texier', 'Ranvieux', 'Guilbert', 'Dupont', 'Lepage', 'Arnaud', 'Masset', 'Sartruel', 'Barbosa', 'Raynal', 'Manour', 'Auclair', 'Osyssek', 'Jaunet', 'Carre', 'Fourichon', 'Brun', 'Raymond', 'Aubry', 'Debat', 'Briand', 'Varenne', 'Vaillant', 'Debrif', 'Didier', 'Bragne', 'Antoine', 'Dubois', 'Wrobel', 'Guenart', 'Furic', 'Carlier', 'Combo', 'Charpentier', 'Prasse', 'Germain', 'Portelette', 'Dorido', 'Boutin', 'Cisse', 'Ravier', 'Tothe', 'Vaxelaire', 'Maillet', 'Aouaouche', 'Vichet', 'Gattoliat', 'Pigeot', 'Perrot', 'Masson', 'Berna', 'Blin', 'Asmaoui', 'Guerveno', 'Besnier', 'Tuji', 'Bonnel', 'Markoulakis', 'Allain', 'Chollet', 'Toussaint', 'Len', 'Haddane', 'Bonil', 'Dufour', 'Gilles', 'Rivera', 'Sandu', 'Nicolas', 'Guillou', 'Brunel', 'Keddis', 'Iken', 'Lagarde', 'Barcelo', 'Weber', 'Griffard', 'Buades', 'Walryck', 'Boucaud', 'Bouvier', 'Clement', 'Corbel', 'Niney', 'Mothor', 'Attour', 'Ledeme', 'Choupet', 'Vissault', 'Satterne', 'Leclerc', 'Daniel', 'Paul', 'Leconte', 'Army', 'Cartron', 'Garcia', 'Courtin', 'Joly', 'Pollet', 'Ploutinet', 'Cohen', 'Campignard', 'Ludiongo', 'Poirier', 'Baghdasaryan', 'Pierre', 'Praud', 'Fzeri', 'Maeght', 'Bauzuin', 'Lacoste', 'Netter', 'Barbier', 'Olive', 'Neto', 'Conticini', 'Apollinaire', 'Plouilly', 'Lukacs', 'Cozzi', 'Pelletier', 'Coubertin', 'Leboubenec', 'Chartier', 'Lolic', 'Chalabi', 'Sard', 'Nalla', 'Adam', 'Gauche', 'Daunizeau', 'Debaille', 'Renaud', 'Brunet', 'Devaux', 'Colin', 'Gay', 'Hilaire', 'Caillier', 'Laline', 'Maupassant', 'Jacquin', 'Brasse', 'Guinars', 'Heduit', 'Mohellibi', 'Rotella', 'Goncalves', 'Branve', 'Goudout', 'Corre', 'Chazel', 'Rey', 'Brion', 'Hernandez', 'Singet', 'Tijari', 'Ferjoux', 'Chevallier', 'Launay', 'Anneau', 'Fernandez', 'Duvalet', 'Cherif', 'Gianfrotta', 'Jacques', 'Poireau', 'Blancher', 'Peltier', 'Benitez', 'Pineau', 'Dossantos', 'Philippe', 'Fontaine', 'Dutri', 'Moreno', 'Vogel', 'Delmas', 'Pain', 'Ghisolfo', 'Mondu', 'Lebon', 'Astier', 'Rasamizanany', 'Doyurur', 'Mendes', 'Pruvost', 'Maury', 'Donald', 'Belaidi', 'Laroui', 'Vetter', 'Abdoul', 'Zelamta', 'Boussinet', 'Tor', 'Doquoy', 'Bourgeois', 'Auger', 'Furique', 'Therage', 'Friess', 'Bourra', 'Melvin', 'Wielgosz', 'Magnan', 'Marque', 'Amoussou', 'Bourdon', 'Janvier', 'Riviere', 'Labori', 'Bertholot', 'Maurin', 'Van', 'Haifi', 'Parodi', 'Willay', 'Valentine', 'Curie', 'Jellouli', 'Ami', 'Messi', 'Harnoufi', 'Vatilleau', 'Rolland', 'Arniers', 'Sceaux', 'Person', 'Fachot', 'Bonney', 'Charrier', 'Royer', 'Pommier', 'Koulo', 'Leclercq', 'Buzin', 'Mignot', 'Barrier', 'Gros', 'Phkar', 'Moreira Da Silva', 'Sertier', 'Joannet', 'Marie', 'Lechien', 'Bouchon', 'Trellu', 'Taher', 'Thomas', 'Lenoir', 'Gilbert', 'Heron', 'Coste', 'Mobre', 'Boucher', 'Hassler', 'Plancq', 'Courant', 'Rousseau', 'Pridal', 'Hervy', 'Voile', 'Humery', 'Monnier', 'Bouzidi', 'Leveque', 'Dumont', 'Mulard', 'Reber', 'Revero', 'Sanchez', 'Bureau', 'Bertrand', 'Vere', 'Bartholus', 'Lemaitre', 'Voisin', 'Grontier', 'Keita', 'Charpy', 'Ploutier', 'Moutou', 'Brezellec', 'Bonnin', 'Peignet', 'Millet', 'Rodrigues', 'Pichon', 'Leduc', 'Tseveendorj', 'Lepretre', 'Nino', 'Sarte', 'Muffin', 'Garel', 'Langlois', 'Sicherre', 'Moindjie', 'Gibord', 'Lemoine', 'Gillet', 'Cousin', 'Albert', 'Depry', 'Mambrun', 'Berger', 'Flaubert', 'Bonnet', 'Ribeiro', 'Bouchet', 'Cheval', 'Spanneut', 'Clerc', 'Pasquier', 'Chevon', 'Chairet', 'Moliere', 'Emerdjian', 'Hubert', 'Devillard', 'Noreskal', 'Lacombe', 'Simon', 'Moulin', 'Benyelles', 'Thibault', 'Glorieux', 'Rili', 'Boura', 'Sino', 'Debus', 'Adriansen', 'Ourdouillie', 'Louis', 'Gaudin', 'Michalak', 'Lejeune', 'Wu', 'Barre', 'Amallah', 'Levy', 'Descamps', 'Artine', 'Danest', 'Ferenbach', 'Lingrand', 'Segaux', 'Dutuis', 'Alain', 'Florence', 'Pericaud', 'Dugrond', 'Reale', 'Bruneau', 'Le Bihan', 'Laposi', 'Rousset', 'Vetillard', 'Sami', 'Fereira', 'Lanclos', 'Strozecki', 'Vixemar', 'Carpentier', 'Miran', 'Blagnal', 'Guenal', 'Moreau', 'Feraud', 'Sernaud', 'Martineau', 'Florent', 'Ditran', 'Chauvin', 'Chatillard', 'Suarez', 'Jouneau', 'Munarde', 'Ventre', 'Mediouni', 'Noel', 'Dumeric', 'Brogniart', 'Bouchenna', 'Pipelier', 'Cotillard', 'Cheboub', 'Buffin', 'Viers', 'Rottenberg', 'Tuzi', 'Gaudray', 'Labusciere', 'Benoit', 'Lengard', 'Younsi', 'Martial', 'Savary', 'Blanchard', 'Coucheney', 'El Moussafer', 'Flejou', 'Allouche', 'Lebbah', 'Debonne', 'Perez', 'Jacob', 'Michaud', 'Dore', 'Fages', 'Lauriola', 'Crifours', 'Terki', 'Simart', 'Bisson', 'Loiseau', 'Maussin', 'Ntuti', 'Humbert', 'Berrahmane', 'Siaud', 'Houllio', 'Prive', 'Bisiou', 'Renard', 'Amara', 'Mayer', 'Le Cam', 'Delcourt', 'Francois', 'Tagba', 'Ardourel', 'Le Gall', 'Laurent', 'Vasseur', 'La Fonta', 'Munet', 'Milo', 'Guibert', 'Danset', 'Ligne', 'Cuchet', 'Dolet', 'Alambert', 'Manp', 'Xoon', 'Besiner', 'Cressan', 'Normand', 'Solomon', 'Adele-amelie', 'Boyer', 'Hammadi', 'Saccard', 'Cercus', 'Hoff', 'Bauwens', 'Cabrit', 'Garnier', 'Piroelle', 'Roy', 'Lado', 'Davoli', 'Nelo', 'Melun', 'Lambersart', 'Lamotte', 'Frejoux', 'Rodriguez', 'Cozette', 'Levesque', 'Petit', 'Gerard', 'Colas', 'Roulet', 'Allard', 'Desaulty', 'Cassier', 'Dubluis', 'Buchere', 'Dumis', 'Alvet', 'Legall', 'Joubert', 'Cordier', 'Marchal', 'Baron', 'Besnard', 'Dussaud', 'Marion', 'Becue', 'Le', 'Uthayakumar', 'Couture', 'Jacquet', 'Mary', 'Tran', 'Barbe', 'Magaletti', 'Lebouc', 'Tieres', 'Gibourdin', 'Pervenche', 'Sutterland', 'Chevalier', 'Bettaieb', 'Wasny', 'Sousa', 'Ducorps', 'Truneaux', 'Pereira da cunha', 'Bouarfa', 'Soutre', 'Bognard', 'Lambert', 'Etienne', 'Delangue', 'Bouteau', 'Baillet', 'Berthelot', 'Paule', 'Menard', 'Girondeau', 'Duter', 'Maillar', 'Duhamel', 'Aval', 'Hatem', 'Maillard', 'Lucas', 'Viart', 'Legrand', 'Marin', 'Toso', 'Merbah', 'Lepine', 'Laroche', 'Blanc', 'Potier', 'Etchebest', 'Sautet', 'Flipote', 'Lam', 'Blignac', 'Ait Sahlia', 'Ferrat', 'Piley', 'Maire', 'Hamon', 'Zemmouri', 'Chany', 'Bernard', 'Vincent', 'Rufin', 'Prat', 'Vanmarque', 'Ayuso', 'Le Goueff', 'Zenati', 'Perrault', 'Evrard', 'Ramos', 'Bel-hadj', 'Haidi', 'Bchibchi', 'Saillard', 'Balijon', 'Bertin', 'Malime', 'Chatelin', 'Clarisse', 'Rabate', 'Neveu', 'Nemour', 'Sarrazin', 'Tang', 'Ruiz', 'Binay', 'Mehimda', 'Tardivel', 'Messeant', 'Cambert', 'Denis', 'Paresse', 'Signo', 'Vincetti', 'El abid', 'Dasilva', 'Perret', 'Brisse', 'Legoff', 'Oubir', 'Gally', 'Dissons', 'Besson', 'Valette', 'Priquet', 'Rossi', 'Dupages', 'Blanchet', 'Khenoun', 'Jupe', 'Dalmais', 'Minard', 'Speters', 'Panflet', 'Lallement', 'Leroy', 'Perrier', 'Sapriel', 'Moutarde', 'Kevan', 'Henaff', 'Imbault', 'Versaveau', 'Dos Santos', 'Blot', 'Jean', 'Paviot', 'Muset', 'Baude', 'Iliassy', 'Tanguy', 'Debienne', 'Fourgous', 'Ahmed', 'Huet', 'Thierry', 'Camus', 'Vallet', 'Taujers', 'Deschamps', 'Klepper', 'Louvet', 'Van Loo', 'Collard', 'Caron', 'Da Silva', 'Coustillas', 'Abalil', 'Lemaire', 'Tomas', 'Cabral', 'Leger', 'Roche', 'Belmehdi', 'Lelu', 'Cange', 'Piouceau', 'Dutot', 'Martel', 'Civers', 'Laurin', 'Georges', 'Fonseca', 'Fernandes', 'Baudry', 'Tardieu', 'Alix', 'Escande', 'Leroux', 'Fischer', 'Minoggio', 'Soares', 'Lopes', 'Martin', 'Bourdin', 'Lombard', 'Plisson', 'Frutiez', 'Viet', 'Giraud', 'Reeb', 'Massart', 'Morvan', 'Laborde', 'Mathieu', 'Mercorelli', 'Guillon', 'Germette', 'Pottier', 'Lagneau', 'Blondel', 'Boivin', 'Bousquet', 'Juliza', 'Gonzalez', 'Pascal', 'Schneider', 'Grange', 'Laf', 'Gabriel', 'Mazzoni', 'Blangy', 'Roger', 'Hargas', 'Serber', 'Picard', 'Barthelemy', 'Strozik', 'Imbert', 'Alexandre', 'Fairme', 'Assaud', 'Salimier', 'Ferre', 'Tirgo', 'Flambaer', 'Salic', 'Hebert', 'Debruyne', 'Ballgobin', 'Pares', 'Azer', 'Chayani', 'Romero', 'Dacosta', 'Massier', 'Chauveau', 'Foucher', 'Girard', 'Striebig', 'Michard', 'Defrise', 'Barth', 'Boulogne', 'Hoareau', 'Benkherouf', 'Lavigne', 'Sauvage', 'Fourneau', 'Sanz', 'Cambrete', 'Radelet', 'Screve', 'Maurice', 'Le Goff', 'Bailly', 'Biot', 'Szuplewzki', 'Pare', 'Campagnolo', 'Tzatzooki', 'Perrin', 'Koita', 'Bergot', 'Henry', 'Godard', 'Lavie', 'Guillaume', 'Hachour', 'Joseph', 'Cara', 'Gerneau', 'Maillot', 'Bigot', 'Reynaud', 'Bazin', 'Nosel', 'Roux', 'Pereira', 'Prehaud', 'Chekoua (bouers)', 'Coulon', 'Salnot', 'Collet', 'Lopez', 'Daumas', 'Vigier', 'Li Combeau', 'Restier', 'Milait', 'Piot', 'Melek', 'Dinant', 'Mercier', 'Carfouin', 'Caillet', 'Huile', 'Jardine', 'Colombiani', 'Ibrame', 'Camion', 'Millaniyage', 'Nebre', 'Trosset', 'Derian', 'Delaunay', 'Guery', 'Decaen', 'Rziki', 'Plitane', 'Niel', 'Bonneau', 'Estanboulieh', 'Fulin', 'Chalant', 'Conti', 'Boulanger', 'Franceries', 'Seddis', 'Vauthier', 'Willaume', 'Sailly', 'Vaillan', 'Armand', 'Villate', 'Fournier', 'Couturier', 'Dugelay', 'Merle', 'Lerose', 'Casarno', 'Denechere', 'Letrange', 'Bodin', 'Tessier', 'Rami', 'Delattre', 'Robuste', 'Godet', 'Gaouditz', 'Gant', 'Bruges', 'Pret', 'Bouziane', 'Charles', 'Jeyakanthan', 'Journi', 'Loutrot', 'Navarro', 'Poulain', 'Ganche', 'Linard', 'Richard', 'Hilleu', 'Adri', 'Canfrais', 'Lefort', 'Oliveira', 'Gibier', 'Klein', 'Lemba', 'Fendt', 'Fouquet', 'Regaud', 'Stephan', 'Andre', 'Lesage', 'Adrien', 'Breter', 'Guillot', 'Jacquot', 'Wassaf', 'Seguin', 'Ledoux', 'Favre', 'Li', 'Briere', 'Crespin', 'Mibouche', 'Returne', 'El Assir', 'Loo', 'Gillieron', 'Benaoudia', 'Wagner', 'Ladjouze', 'Faure', 'Djebrouni', 'Kanga', 'Loisel', 'Nevers', 'Tuffet', 'Collin', 'Louzet', 'Geffray', 'Meunier', 'Vivien', 'Prevost', 'Guyot', 'Chouaib', 'Benabib', 'Khalin', 'Moncler', 'Thibaudeau', 'Bulver', 'Medbouhi', 'Martins', 'Lecomte', 'Drepond', 'Lebrun', 'Lignac', 'Dumas', 'Rios Campo', 'Khelil', 'Mielle', 'Renaut', 'Harbane', 'Gabouze', 'Lope', 'Bucher', 'Metel', 'Fleury', 'Marteau', 'Moulier', 'Bison', 'Meyer', 'Pellegrini', 'Dubourgeot', 'Royere', 'Berdrate', 'Lebreton', 'Fourault', 'Diab', 'Bouleau', 'Seddiki', 'Jeouit', 'Renault', 'Finance', 'Aubin', 'Plantard', 'Debah', 'Faivre', 'Sitterlin', 'Chauvet', 'Grassin', 'Brault', 'Buisson', 'Cazemajou', 'Marty', 'Pencole', 'Lefebvre', 'Vervel', 'Marchand', 'Bienaime', 'Tampuits', 'Litalien', 'Pinorelli', 'Riou', 'Mallet', 'Olivier', 'Herve', 'Chakroun', 'Vignaud', 'Timsiline', 'Polet', 'Pages', 'Pinto', 'Cortes', 'Stikziski', 'Mignard', 'Said', 'Choulan', 'Fayet', 'Yapo', 'Chabbert', 'Rouinvy', 'Payet', 'Grondin', 'Michel', 'Barbey', 'Gherardi', 'Verdier', 'Iacob', 'Bleuet', 'Hoarau', 'Jouliot', 'Merton', 'Vial', 'Ninoux', 'Marechal', 'Guichard', 'Lacroix', 'Gallet', 'Magnere', 'Jonda', 'Melin', 'Ferrez', 'Dupin', 'Cottin', 'Leblanc', 'Paris', 'Lancre', 'Sifi', 'Boukebouche', 'Robert', 'David', 'Breton', 'Duval', 'Prieu', 'Essallami', 'Orlhac', 'Dupuy', 'Guennegues', 'Gauthier', 'Pons', 'Pardo', 'Rouxel', 'Ferrand', 'Casa', 'Remy', 'Grinda', 'Dubront', 'Isaac', 'Ferrer', 'Guillet', 'Retriss', 'Chaouch', 'Eberlin', 'Alves', 'Singeau', 'Zagnoni', 'Sourdeval', 'Champeval', 'Batata', 'Mache', 'Cheaib', 'Morel', 'Galibert', 'Dunardt', 'Grise', 'Kufin', 'Oster', 'Corsi', 'Durand', 'Biles', 'Vidal', 'Ursule', 'Hamad', 'Diomande', 'Rose', 'Bonhomme', 'Yull', 'Isnard', 'Simoes', 'Tchebytchev', 'Diter', 'Costa', 'Razafindrabary', 'Benard', 'Queretti', 'Gastel', 'Fauchet', 'Salmon', 'Jouvet', 'Tellier', 'Rincheval', 'Raynaud', 'Lepifre', 'Victor', 'Bombart', 'Geneste', 'Muller', 'Viollette', 'Grigne', 'Phouphetlinthong', 'Hardy', 'Gaumer', 'Laporte', 'Turpin', 'Le Corre', 'Delage', 'Robin', 'Laramendy', 'Lassouani', 'Neel', 'Quessette', 'Honduc', 'Gomes', 'Poire', 'Nouri', 'Ellili', 'Guillemard', 'Morin', 'Rano', 'Courtois', 'Farny', 'Temprement', 'Rougier', 'Chassat', 'Guyon', 'Amoyal', 'Aubert', 'Khezzar', 'Schmitt', 'Gautier', 'Gosse', 'Bourdier', 'Bardella', 'Melanchon', 'Macron']

#li = list(set(liste_noms_clients))
#print(li)
#print(len(liste_noms_clients))

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
                date_tuple = [date.strftime("%A"), date.strftime("%d"), date.strftime("%m"), date.strftime("%Y")]
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
        j[0] = j_in_english[:3]
        #j[0] = dico_semaine[j_in_english]
        #m_in_english = j[2]
        #j[2] = dico_mois[m_in_english]
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

    proba_clients = [0.85]+[(0.15/len(liste_noms_clients)) for k in range(len(liste_noms_clients))]
    proba_tables = [(2/56), (2/56), (2/56), (10/56), (4/56), (2/56), (2/56), (6/56), (2/56), (2/56),
                    (2/56), (6/56), (2/56), (4/56), (8/56)]


    for num_service in range(len(liste_services)):      # pour chaque service
        jour = l_semaine[num_service//2][0]
        num_jour = l_semaine[num_service//2][1]
        mois = l_semaine[num_service//2][2]
        annee = l_semaine[num_service//2][3]
        date_commande = "'" + jour + "-" + num_jour  + "-" +  mois + "-"  + annee + "'"
        serveurs_travaillant = serveurs_travaillant_sachant_service(jour, annee)
        for num_client in range(liste_services[num_service]):       # pour chaque commande
            nom_client = random.choices(['NULL'] + liste_noms_clients, proba_clients)[0]
            #if nom_client != 'NULL':
            nom_client = "'" + nom_client + "'"        
            service = "'" + l_services[num_service%2] + "'"
            num_serveur = random.choices(serveurs_travaillant)[0]
            num_table = random.choices([k for k in range(1,16)], proba_tables)[0]
            tuple_commande = str(num_commande) + ", " + nom_client + ", " + "TO_DATE(" + str(date_commande) + ", 'DY-DD-MM-YYYY')" + ", " + service + ", " + str(num_serveur) + ", " + str(num_table)
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

    l_choix = ['', 'E', 'P', 'D', 'EP', 'ED', 'PD', 'DD', 'EE', 'PP', 'EPD', 'EPP', 'EEP', 'EED', 'PDD', 'EEPD', 'EPDD']
    probas_choix = [(0.2/16), (0.2/16), (2/16), (0.5/16), (3/16), (0.2/16), (5/16), (0.1/16), (0.2/16), (0.1/16), (3/16), (0.2/16), (0.1/16), (0.1/16), (0.5/16), (0.3/16), (0.3/16)]

    with open('commandes.txt', 'r') as fic_commandes:
        lignes = fic_commandes.readlines()
    lignes_corrigees = [ligne.replace("NULL", "'NULL'") for ligne in lignes]
    tuples = [eval(ligne.strip()) for ligne in lignes_corrigees]

    fic_est_commande = open('est_commande.txt', 'w')

    for tpl in tuples:
        num_commande = tpl[0]
        choix = random.choices(l_choix, probas_choix)[0]
        if choix == '':
            pass
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

        # Choix des types des boissons commandées

        lettres_boissons = ""
        if random.choices([True, False], [0.1, 0.9]):
            pass        # pas de commande de boisson
        eau = random.choices([True, False], [0.2, 0.8])
        if eau :
            lettres_boissons += 'E'
        ss_alcool = random.choices([True, False], [0.05, 0.95])
        if ss_alcool :
            lettres_boissons += 'S'
        vin = random.choices([True, False], [0.05, 0.95])
        if vin :
            lettres_boissons += 'V'
        cafe = random.choices([True, False], [0.05, 0.95])
        if cafe :
            lettres_boissons += 'C'
        alcool = random.choices([True, False], [0.05, 0.95])
        if alcool :
            lettres_boissons += 'A'
        
        # Choix des boissons commandées en fonction de leur type

        num_boissons_commandees = []
        for lettre in lettres_boissons:
            if lettre == 'E':
                num_boissons_commandees.append(random.choice(num_eau))
            elif lettre == 'S':
                num_boissons_commandees.append(random.choice(num_ss_alcool))
            elif lettre == 'V':
                num_boissons_commandees.append(random.choice(num_vin))
            elif lettre == 'C':
                num_boissons_commandees.append(random.choice(num_cafe))
            else:
                num_boissons_commandees.append(random.choice(num_alcool))            

        # Rédaction des tuples

        l = []
        for ind_b in range(len(num_boissons_commandees)):
            if num_boissons_commandees[ind_b] not in l:     # si on n'a pas déjà traité ce numéro de boisson
                l.append(num_boissons_commandees[ind_b])
                fic_a_boire.write(str(num_commande) + ', ' + str(num_boissons_commandees[ind_b]) + ', ' + str(num_boissons_commandees.count(num_boissons_commandees[ind_b])) + '\n')

    fic_a_boire.close()

#a_boire()

def composition():   
    fic = open('composition.txt', 'a')
    EPD=0
    while EPD != 'stop':
        EPD = input('EPD : ')
        igd = input('ingredient : ')
        nb_unites = input('nb_unites : ')
        fic.write(EPD + ', ' + igd + ', ' + nb_unites + '\n')
    fic.close()
    return

#composition()

def insertInto(name_file, name_table):
    fic = open(name_file, 'r')
    for ligne in fic:
        print('INSERT INTO ', name_table, ' VALUES(', ligne[:-1], ');')
        #if ligne.count(',') != 6:
            #print('ERROR')
    fic.close()
    return

# Attention, penser à laisser une ligne vide à la fin du fichier

#insertInto('echantillon.txt', 'EST_COMMANDE')

def ajoutvirgule():
    fic = open('est_commande2.txt', 'w')
    fic2 = open('est_commande.txt', 'r')

    l = fic2.readlines()
    for k in l :
        fic.write(k[:-1]+','+'\n')

    fic.close()
    fic2.close()

#ajoutvirgule()

def supr_doublon():
    fic = open('est_commande2.txt', 'r')
    fic2 = open('est_commande3.txt', 'w')

    l  = fic.readlines()
    n = len(l)
    cpt=1
    fic2.write(l[0])
    print(n)
    for i in range(1, n):
        if l[i] != l[i-1]:
            fic2.write(l[i])
            cpt+=1
    print(cpt)
    fic.close()
    fic2.close()

supr_doublon()