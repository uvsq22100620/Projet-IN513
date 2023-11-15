import random
import time
from datetime import datetime, timedelta

# Constantes

num_commande = 1

num_entrees = [k for k in range(1, 11)]
num_plats = [k for k in range(12, 28)]
num_desserts = [k for k in range(29, 45)]

dico_semaine = {'Tuesday':'Mar', 'Wednesday':'Mer', 'Thursday':'Jeu', 'Friday': 'Ven', 'Saturday':'Sam', 'Sunday':'Dim'}
dico_mois = {'January':'Janvier', 'February':'Fevrier', 'March':'Mars', 'April':'Avril', 'May':'Mai', 'June':'Juin', 'July':'Juillet',
             'August':'Aout', 'September':'Septembre', 'October':'Octobre', 'November':'Novembre', 'December':'Decembre'}

liste_noms_clients = ['NULL', 'Auclair', 'Barth', 'Berdrate', 'Bouleau', 'Bourra', 'Brezellec', 'Camion', 'Chairet', 'Chalant', 'Chevalier', 'Corsi', 'Coucheney', 'Cremazy', 'Debat', 'Diab', 'Durand',
                          'Etchebest', 'Fages', 'Farny', 'Ferrat', 'Finance', 'Fourneau', 'Gattoliat', 'Garnier', 'Gaumer', 'Gianfrotta', 'Hoareau', 'Jacquin', 'Jellouli', 'Juliza', 'Keddis', 'Lamy', 'Lebbah',
                          'Le Corre', 'Lefevre', 'Lemaire', 'Lignac', 'Manour', 'Marque', 'Mayer', 'Mediouni', 'Mercorelli', 'Moindjie', 'Moreno', 'Mothor', 'Netter', 'Ninoux',
                          'Prehaud', 'Pret', 'Prieu', 'Quessette', 'Rincheval', 'Rotella', 'Sandu', 'Sapriel', 'Sitterlin', 'Sourdeval', 'Strozecki', 'Szuplewzki', 'Taher',
                          'Terki', 'Thibuta', 'Timsiline', 'Tseveendorj', 'Vial', 'Vincens']

liste_noms_clients_V2 = ['Gattoliat', 'Toso', 'Legoff', 'Sandu', 'Ferreira', 'Bourra', 'Rolland', 'Grondin', 'Plantard', 'Cousin', 'Hoareau', 'Blangy', 'Benkherouf', 'Bouziane', 'Jacquet', 'Cozette', 'Devillard', 'Schmitt', 'Guillou', 'Lemoine', 'Brun', 'Brault', 'Dumas', 'Dupin', 'Cohen', 'Mohellibi', 'Lemaitre', 'Gonzalez', 'Gaumer', 'Gant', 'Laroui', 'Binay', 'Perrault', 'Pencole', 'Magaletti', 'Barrier', 'Sourdeval', 'Rivera', 'Debruyne', 'Danset', 'Speters', 'Mielle', 'Baudry', 'Laborde', 'Hamon', 'Rano', 'Godet', 'Henry', 'Mazzoni', 'Grontier', 'Coucheney', 'Dussaud', 'Lepage', 'Rasamizanany', 'Tuffet', 'Morel', 'Michel', 'Fouquet', 'Lopez', 'Maitre', 'Rondey', 'Niel', 'Corsi', 'Garcia', 'Hebert', 'Massart', 'Sernaud', 'Gomes', 'Pereira', 'Bruges', 'Chakroun', 'Chartier', 'Hatem', 'Seddiki', 'Allouche', 'Rios Campo', 'Flejou', 'Finance', 'Denis', 'DaSilva', 'Mathieu', 'Lepine', 'Balijon', 'Harbane', 'Humbert', 'Rabate', 'Andre', 'Salmon', 'Simoes', 'Delorme', 'Dumont', 'Varoqui', 'Djebrouni', 'Gay', 'Strozik', 'Lassouani', 'Sauvage', 'Imbert', 'Gaouditz', 'Vervel', 'Turpin', 'Abalil', 'David', 'Menard', 'Lanclos', 'Rodrigues', 'Boura', 'Chevalier', 'Hernandez', 'Faivre', 'Aouaouche', 'Sarrazin', 'Ledeme', 'Lepifre', 'Thierry', 'Lignac', 'Marion', 'Osyssek', 'Richard', 'Vixemar', 'Francois', 'Screve', 'Sapriel', 'Eberlin', 'Morin', 'Vincent', 'Buisson', 'Merbah', 'Boutamine', 'Vauthier', 'Spanneut', 'Ahmed', 'Lambert', 'Chabbert', 'Salimier', 'Tardieu', 'Pipelier', 'Denechere', 'Boukebouche', 'Ferenbach', 'Gilles', 'Dupont', 'Bourgeois', 'Ferrand', 'Gallet', 'Dolet', 'Tardivel', 'Seguin', 'Trosset', 'Chazel', 'Bertin', 'Roussel', 'Hilaire', 'Seromenho', 'Assaud', 'Garel', 'Debienne', 'Moutou', 'Bombart', 'Mas', 'Renaud', 'Reber', 'Noreskal', 'Corbel', 'Messeant', 'Collin', 'Guillot', 'Davoli', 'Guyon', 'Adriansen', 'Peltier', 'Brunet', 'Albert', 'Pasquier', 'Wu', 'Casa', 'Boyer', 'Guillet', 'Ntuti', 'Bouleau', 'Geneste', 'Seksaoui', 'Younsi', 'Boivin', 'Glorieux', 'Batata', 'Pellegrini', 'Marchand', 'Girondeau', 'Lebon', 'Astier', 'Fernandez', 'Cercus', 'Lingrand', 'Barbe', 'Charpentier', 'Marchal', 'Lavigne', 'Thomas', 'Barbosa', 'Regaud', 'Da Silva', 'Serber', 'Lefebvre', 'Prehaud', 'Bel-hadj', 'Salic', 'Guerveno', 'Rey', 'Mercorelli', 'Koita', 'Siaud', 'Marechal', 'Meyer', 'Mallet', 'Baillet', 'Guyot', 'Sifi', 'Gaillard', 'Cortes', 'Sitterlin', 'Piroelle', 'Razafindrabary', 'Cambert', 'Lagarde', 'Jellouli', 'Wassaf', 'Perrier', 'Dorido', 'Pascal', 'Vincens', 'Dubourgeot', 'Clement', 'Galibert', 'Juliza', 'Merle', 'Plisson', 'Maillard', 'Jourdan', 'Millet', 'Auclair', 'Vetillard', 'Caillier', 'Fournier', 'Belmehdi', 'Gosse', 'Bouzidi', 'Sinople', 'Marty', 'Tor', 'Poulain', 'Segaux', 'Foucher', 'Benard', 'Alves', 'Lejeune', 'Le Bihan', 'Michaud', 'Rougier', 'Carre', 'Guichard', 'Poireau', 'Debonne', 'Haidi', 'Fendt', 'Caillet', 'Leboubenec', 'Trellu', 'Chauvin', 'Vichet', 'Etienne', 'Chalant', 'Villate', 'Romero', 'Mobre', 'Abdoul', 'Buffin', 'Fourault', 'Durand', 'Rose', 'Lemaire', 'Godard', 'Sautet', 'Bettaieb', 'Duvalet', 'Benoit', 'Praud', 'Geffray', 'Michalak', 'Lacombe', 'Camus', 'Giraud', 'Chevallier', 'Fernandes', 'Charpy', 'Paule', 'Herve', 'Adrien', 'Delmas', 'Dasilva', 'Baron', 'Dupuy', 'Van Loo', 'Marin', 'Barre', 'Cabral', 'Magnan', 'Renaut', 'Frejoux', 'Blin', 'Bouchon', 'Moreau', 'Strozecki', 'Lolic', 'Stephan', 'Debat', 'Temprement', 'Aabirate', 'Deschamps', 'Coulon', 'Hamad', 'Leveque', 'Carlier', 'Le Gall', 'Besnard', 'Pichon', 'Martinez', 'Muller', 'Martins', 'Ramos', 'Vasseur', 'Leroy', 'Lopes', 'Bazin', 'Petit', 'Pruvost', 'Perrin', 'Renault', 'Briand', 'Guibert', 'Launay', 'Walryck', 'Cressan', 'Neto', 'Harnoufi', 'Perez', 'Joannet', 'Phkar', 'Bouarfa', 'Oubir', 'Gillet', 'Bchibchi', 'Ribeiro', 'Timsiline', 'Hachour', 'Varenne', 'Hammadi', 'Derian', 'Guennegues', 'Thibault', 'Masson', 'Barcelo', 'Paris', 'Loiseau', 'Remy', 'Bauzuin', 'Cara', 'Laurin', 'Nelo', 'Fourgous', 'Bertrand', 'Bureau', 'Robert', 'Faure', 'Ouaiche', 'Kanga', 'Louvet', 'Pommier', 'Besson', 'Linard', 'Mercier', 'Boucaud', 'Lamy', 'Descamps', 'Dupages', 'Labori', 'Moreno', 'Vogel', 'Allard', 'Hamdi', 'Suarez', 'Boulogne', 'Isnard', 'Clerc', 'Roche', 'Jardine', 'Pages', 'Guilbert', 'Martel', 'Lacroix', 'Boussinet', 'Gaudray', 'Boutin', 'Cheval', 'Leger', 'Lombard', 'Jouvet', 'Bonnel', 'Franceries', 'Yapo', 'Gaudin', 'Ducorps', 'Pereira da cunha', 'Gillieron', 'Dumeric', 'Viart', 'Schneider', 'Ferre', 'Debah', 'Vignaud', 'Sousa', 'Allain', 'Garnier', 'Frutiez', 'Ursule', 'Khezzar', 'Baghdasaryan', 'Phouphetlinthong', 'Lamotte', 'Diallo', 'Ardourel', 'Aval', 'Humery', 'Le', 'Benabib', 'Evrard', 'Ventre', 'Briere', 'Blanchard', 'Auger', 'Maillot', 'Courtin', 'Potier', 'Voile', 'Mokrab', 'Cremazy', 'Zenati', 'Rossi', 'Therage', 'El Moussafer', 'Dore', 'Amoussou', 'Gerard', 'Ourdouillie', 'Hardy', 'Blot', 'Chollet', 'Alexandre', 'Armand', 'Mulard', 'Colas', 'Chevon', 'Corre', 'Rziki', 'Joyeux', 'Baude', 'Nguyen', 'Li', 'Mignard', 'Berthelot', 'Oster', 'Royer', 'Conti', 'Daniel', 'Tessier', 'Berger', 'Zagnoni', 'Laurent', 'Gomez', 'Fonseca', 'Bouchenna', 'Piouceau', 'Chassat', 'Rocher', 'Ollivier', 'Germette', 'Sanchez', 'Depry', 'Langlois', 'Chekoua (bouers)', 'Sami', 'Mediouni', 'Loisel', 'Wielgosz', 'Dupuis', 'Noel', 'Versaveau', 'Saccard', 'Camion', 'Boucher', 'Willaume', 'Texier', 'Lepretre', 'Estanboulieh', 'Roy', 'Vincetti', 'Labusciere', 'Clarisse', 'Blanchet', 'Le Corre', 'Tseveendorj', 'Hoff', 'Bonhomme', 'Moncler', 'Lecomte', 'Mayer', 'Legrand', 'Payet', 'Delcourt', 'Barbier', 'Dissons', 'Guillaume', 'Rincheval', 'Ninoux', 'Laporte', 'Rouxel', 'Guery', 'Blanc', 'El abid', 'Vaxelaire', 'Ferrat', 'Santrot', 'Prat', 'Henaff', 'NULL', 'Bourdon', 'Lengard', 'Bienaime', 'Bigot', 'Paul', 'Charles', 'Lefort', 'Dos Santos', 'Orlhac', 'Collard', 'Moreira Da Silva', 'Combo', 'Fauchet', 'Martineau', 'Caron', 'Milait', 'Navarro', 'Nouri', 'Ayuso', 'Rotella', 'Leclerc', 'Escande', 'Jeyakanthan', 'Delaunay', 'Friess', 'Lucas', 'Toussaint', 'Dossantos', 'Mothor', 'Charrier', 'Chatelin', 'Radelet', 'Jean', 'Lam', 'Rami', 'Ludiongo', 'Bruneau', 'Dubois', 'Maire', 'Valentine', 'Tellier', 'Bonneau', 'Benaoudia', 'Couture', 'Grassin', 'Amallah', 'Bodin', 'Lavie', 'Chauvet', 'Rodriguez', 'El Malki', 'Pardo', 'Hervy', 'Legall', 'Willay', 'Benitez', 'Adele-amelie', 'Chouaib', 'Terki', 'Fontaine', 'Amara', 'Moulin', 'Debrif', 'Reale', 'Roger', 'Ferrez', 'Merton', 'Taher', 'Belaidi', 'Chaouch', 'Didier', 'Lebbah', 'Letrange', 'Flaubert', 'Grinda', 'Ruiz', 'Breter', 'Desaulty', 'Aubert', 'Verdier', 'Vallet', 'Duval', 'Leduc', 'Cozzi', 'Laroche', 'Szuplewzki', 'Guillon', 'Vissault', 'Chalabi', 'Valette', 'Rouinvy', 'Biles', 'Pigeot', 'Bartholus', 'Lebrun', 'Collet', 'Costa', 'Pierre', 'Amoyal', 'Maeght', 'Daumas', 'Gabouze', 'Raynal', 'Lelu', 'Reeb', 'Nalla', 'Chairet', 'Lenoir', 'Becue', 'Rousset', 'Coustillas', 'Lefevre', 'Ferrer', 'Colombiani', 'Dugelay', 'Marque', 'Decaen', 'Berrahmane', 'Zelamta', 'Chayani', 'Pret', 'Dalmais', 'Hoarau', 'Priquet', 'Pinto', 'Prieu', 'Fourneau', 'Le Goff', 'Nicolas', 'Doutrelon', 'Biot', 'Robin', 'Jeouit', 'Dacosta', 'Vigier', 'Delattre', 'Parodi', 'La Fonta', 'Fleury', 'Laramendy', 'Sailly', 'Klepper', 'Heduit', 'Netter', 'Diab', 'Julien', 'Vaillant', 'Tagba', 'Besnier', 'Champeval', 'Perrot', 'Goncalves', 'Fages', 'Benyelles', 'Attour', 'Ledoux', 'Tanguy', 'Leconte', 'Pottier', 'Lado', 'Coubertin', 'Thibuta', 'Villain', 'Morvan', 'Iacob', 'Solomon', 'Maurin', 'Ait Sahlia', 'Normand', 'Gauthier', 'Guenal', 'Striebig', 'Picard', 'Le Cam', 'Bulver', 'Neel', 'Brion', 'Doquoy', 'Portelette', 'Guerin', 'Ladjouze', 'Courant', 'Guenart', 'Gautier', 'Lechien', 'Jacques', 'Cordier', 'Fzeri', 'Bailly', 'Gibier', 'Levy', 'Doyurur', 'Messi', 'Gianfrotta', 'Lesage', 'Adri', 'Quessette', 'Savary', 'Donald', 'Pericaud', 'Carpentier', 'Fourichon', 'Ami', 'Sicherre', 'Feraud', 'Perret', 'Jung', 'Simon', 'Bauwens', 'Tijari', 'Melek', 'Minoggio', 'Lebreton', 'Prive', 'Manour', 'Nemour', 'Joly', 'Barth', 'Saillard', 'Chauveau', 'Wagner', 'Diomande', 'Vidal', 'Lagneau', 'Renard', 'Buzin', 'Delage', 'Etchebest', 'Bouchet', 'Janvier', 'Vanmarque', 'Laposi', 'Crespin', 'Li Combeau', 'Tieres', 'Satterne', 'Boulanger', 'Delangue', 'Person', 'Markoulakis', 'Voisin', 'Guillemard', 'Cherif', 'Bousquet', 'Lukacs', 'Goudout', 'Brezellec', 'Marie', 'Imbault', 'Diter', 'Uthayakumar', 'Ferjoux', 'Germain', 'Neveu', 'Khenoun', 'Aubin', 'Vetter', 'Grenier', 'Jonda', 'Devaux', 'Asmaoui', 'Oliveira', 'Couturier', 'Valentin', 'Georges', 'Farny', 'Leclercq', 'Plancq', 'Cabrit', 'Isaac', 'Bouteau', 'Monnier', 'Heron', 'Breton', 'Besiner', 'Haifi', 'Joubert', 'Jacquin', 'Leroux', 'Tothe', 'Adam', 'Medbouhi', 'Vial', 'Khalin', 'Cheboub', 'Dinant', 'Gilbert', 'Haddane', 'Lallement', 'Said', 'Barbey', 'Pineau', 'Brunel', 'Cazemajou', 'Daunizeau', 'Royere', 'Olivier', 'Cheaib', 'Bisiou', 'Jacquot', 'Raynaud', 'Fischer', 'Essallami', 'Bouvier', 'Cassier', 'Zemmouri', 'Maillar', 'Paviot', 'Duhamel', 'Poirier', 'Peignet', 'Van', 'Hammou', 'Ballgobin', 'El Assir', 'Roux', 'Favre', 'Melin', 'Le Blanc', 'Leblanc', 'Aubry', 'Piot', 'Cisse', 'Tran', 'Keddis', 'Simart', 'Bisson', 'Conticini', 'Mehimda', 'Girard', 'Antoine', 'Bonnin', 'Martin', 'Joseph', 'Dutot', 'Tuzi', 'Rili', 'Lebouc', 'Gherardi', 'Gastel', 'Philippe', 'Marteau', 'Prevost', 'Riou', 'Cartron', 'Moindjie', 'Lauriola', 'Raymond', 'Alvet', 'Chany', 'Hargas', 'Buades', 'Berdrate', 'Millaniyage', 'Mambrun', 'Pelletier', 'Brisse', 'Hubert', 'Keita', 'Chatillard', 'Thibaudeau', 'Berna', 'Blondel', 'Maussin', 'Tang', 'Pain', 'Nosel', 'Metel', 'Maury', 'Meunier', 'Lemba', 'Levesque', 'Hassler', 'Pinorelli', 'Barthelemy', 'Arnaud', 'Bourdin', 'Ghisolfo', 'Mendes', 'Mache', 'Pons', 'Iken', 'Bonnet', 'Fabre', 'Bernard', 'Soares', 'Masset', 'Maillet', 'Casarno', 'Louzet', 'Martial', 'Le Goueff', 'Gros', 'Colin', 'Louis', 'Danest', 'Lacoste', 'Mignot', 'Riviere', 'Restier', 'Huet', 'Courtois', 'Iliassy', 'Weber', 'Viollette', 'Coste', 'Dufour', 'Ellili', 'Emerdjian', 'Klein', 'Maurice', 'Rousseau', 'Jacob', 'Victor', 'Gabriel', 'Wrobel', 'Khelil', 'Fereira', 'Mary', 'Bergot', 'Sanz', 'Reynaud']

li = list(set(liste_noms_clients_V2+[]))
print(li)
print(len(li))

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

def composition():
    
    EPD = input('EPD')
    igd = input('ingredient')
    print('('+str(EPD)+', '+str(igd))
    return
composition()