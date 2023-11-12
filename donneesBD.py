import random
import time
from datetime import datetime, timedelta

# Constantes

num_commande = 1

num_entrees = random.randint(1, 11)
num_plats = random.randint(12, 28)
num_desserts = random.randint(29, 45)

dico_semaine = {'Tuesday':'Mar', 'Wednesday':'Mer', 'Thursday':'Jeu', 'Friday': 'Ven', 'Saturday':'Sam', 'Sunday':'Dim'}
dico_mois = {'January':'Janvier', 'February':'Fevrier', 'March':'Mars', 'April':'Avril', 'May':'Mai', 'June':'Juin', 'July':'Juillet',
             'August':'Aout', 'September':'Septembre', 'October':'Octobre', 'November':'Novembre', 'December':'Decembre'}

liste_noms_clients = ['NULL', 'Auclair', 'Barth', 'Berdrate', 'Bouleau', 'Bourra', 'Brezellec', 'Camion', 'Chairet', 'Chalant', 'Chevalier', 'Corsi', 'Coucheney', 'Cremazy', 'Debat', 'Diab', 'Durand',
                          'Etchebest', 'Fages', 'Farny', 'Ferrat', 'Finance', 'Fourneau', 'Gattoliat', 'Garnier', 'Gaumer', 'Gianfrotta', 'Hoareau', 'Jacquin', 'Jellouli', 'Juliza', 'Keddis', 'Lamy', 'Lebbah',
                          'Le Corre', 'Lefevre', 'Lemaire', 'Lignac', 'Manour', 'Marque', 'Mayer', 'Mediouni', 'Mercorelli', 'Moindjie', 'Moreno', 'Mothor', 'Netter', 'Ninoux',
                          'Prehaud', 'Pret', 'Prieu', 'Quessette', 'Rincheval', 'Rotella', 'Sandu', 'Sapriel', 'Sitterlin', 'Sourdeval', 'Strozecki', 'Szuplewzki', 'Taher',
                          'Terki', 'Thibuta', 'Timsiline', 'Tseveendorj', 'Vial', 'Vincens']

liste_noms_clients_V2 = ['NULL', 'Aabirate', 'Abalil', 'Adam', 'Adele-amelie', 'Adrien', 'Ahmed', 'Ait Sahlia', 'Albert', 'Alexandre', 'Allain', 'Allard', 'Allouche', 'Alves', 'Alvet', 'Amallah', 'Amoussou', 'Amoyal', 'Andre', 'Antoine', 'Aouaouche', 'Ardourel', 'Armand', 'Arnaud', 'Asmaoui', 'Assaud', 'Astier', 'Attour', 'Aubert', 'Aubry', 'Auclair', 'Auger', 'Aval', 'Ayuso', 'Baghdasaryan', 'Bailly', 'Balijon', 'Ballgobin', 'Barbe', 'Barbier', 'Barbosa', 'Barcelo', 'Baron', 'Barre', 'Barth', 'Barthelemy', 'Bartholus', 'Batata', 'Baude', 'Baudry', 'Bazin', 'Bchibchi', 'Bel-hadj', 'Belaidi', 'Belmehdi', 'Benabib', 'Benaoudia', 'Benard', 'Benitez', 'Benkherouf', 'Benoit', 'Benyelles', 'Berdrate', 'Berger', 'Bergot', 'Berna', 'Bernard', 'Berrahmane', 'Berthelot', 'Bertin', 'Bertrand', 'Besiner', 'Besnard', 'Besson', 'Bettaieb', 'Bigot', 'Biles', 'Binay', 'Bisiou', 'Blanc', 'Blanchard', 'Blanchet', 'Blangy', 'Blin', 'Blondel', 'Blot', 'Bodin', 'Bombart', 'Bonhomme', 'Bonneau', 'Bonnel', 'Bonnet', 'Bonnin', 'Bouarfa', 'Boucaud', 'Bouchenna', 'Boucher', 'Bouchet', 'Boukebouche', 'Boulanger', 'Bouleau', 'Boura', 'Bourdon', 'Bourgeois', 'Bourra', 'Bousquet', 'Boussinet', 'Bouteau', 'Boutin', 'Bouvier', 'Bouziane', 'Bouzidi', 'Boyer', 'Breter', 'Breton', 'Brezellec', 'Briand', 'Brisse', 'Brun', 'Bruneau', 'Brunel', 'Brunet', 'Buades', 'Buffin', 'Buisson', 'Bulver', 'Bureau', 'Buzin', 'Cabral', 'Cambert', 'Camion', 'Camus', 'Cara', 'Carlier', 'Caron', 'Carpentier', 'Carre', 'Cartron', 'Casa', 'Cassier', 'Cercus', 'Chairet', 'Chakroun', 'Chalabi', 'Chalant', 'Champeval', 'Chany', 'Chaouch', 'Charles', 'Charpentier', 'Charpy', 'Charrier', 'Chartier', 'Chassat', 'Chauveau', 'Chauvet', 'Chauvin', 'Chayani', 'Chazel', 'Cheaib', 'Cheboub', 'Chekoua (bouers)', 'Cherif', 'Cheval', 'Chevalier', 'Chevallier', 'Chollet', 'Chouaib', 'Cisse', 'Clarisse', 'Clement', 'Clerc', 'Cohen', 'Colas', 'Colin', 'Collet', 'Collin', 'Conti', 'Conticini', 'Corbel', 'Cordier', 'Corsi', 'Cortes', 'Costa', 'Coste', 'Coubertin', 'Coucheney', 'Coulon', 'Courant', 'Courtois', 'Cousin', 'Coustillas', 'Couturier', 'Cozzi', 'Cremazy', 'Da Silva', 'DaSilva', 'Dacosta', 'Dalmais', 'Danest', 'Daniel', 'Dasilva', 'Daunizeau', 'David', 'Davoli', 'Debah', 'Debat', 'Debienne', 'Debonne', 'Debruyne', 'Decaen', 'Delage', 'Delangue', 'Delattre', 'Delaunay', 'Delcourt', 'Delmas', 'Delorme', 'Denechere', 'Denis', 'Depry', 'Desaulty', 'Descamps', 'Deschamps', 'Devaux', 'Devillard', 'Diab', 'Diallo', 'Didier', 'Dinant', 'Diomande', 'Diter', 'Djebrouni', 'Dolet', 'Donald', 'Doquoy', 'Dorido', 'Dos Santos', 'Dossantos', 'Doyurur', 'Dubois', 'Dubourgeot', 'Ducorps', 'Dufour', 'Dugelay', 'Duhamel', 'Dumas', 'Dumont', 'Dupont', 'Dupuis', 'Dupuy', 'Durand', 'Dussaud', 'Dutot', 'Duval', 'Eberlin', 'El Assir', 'El Malki', 'El Moussafer', 'El abid', 'Ellili', 'Emerdjian', 'Escande', 'Estanboulieh', 'Etchebest', 'Etienne', 'Evrard', 'Fabre', 'Fages', 'Faivre', 'Farny', 'Fauchet', 'Faure', 'Favre', 'Fendt', 'Feraud', 'Fereira', 'Ferenbach', 'Ferjoux', 'Fernandes', 'Fernandez', 'Ferrand', 'Ferrat', 'Ferreira', 'Ferrez', 'Finance', 'Fischer', 'Flaubert', 'Flejou', 'Fleury', 'Fonseca', 'Fontaine', 'Foucher', 'Fouquet', 'Fourault', 'Fourichon', 'Fourneau', 'Fournier', 'Franceries', 'Francois', 'Friess', 'Fzeri', 'Gabouze', 'Gabriel', 'Gaillard', 'Galibert', 'Gallet', 'Gaouditz', 'Garcia', 'Garel', 'Garnier', 'Gattoliat', 'Gaudin', 'Gaudray', 'Gaumer', 'Gauthier', 'Gautier', 'Gay', 'Geffray', 'Geneste', 'Georges', 'Gerard', 'Germain', 'Germette', 'Gherardi', 'Ghisolfo', 'Gianfrotta', 'Gibier', 'Gilbert', 'Gilles', 'Gillet', 'Gillieron', 'Girard', 'Giraud', 'Glorieux', 'Godard', 'Godet', 'Gomes', 'Gomez', 'Goncalves', 'Gonzalez', 'Gosse', 'Goudout', 'Grassin', 'Grenier', 'Grinda', 'Grondin', 'Gros', 'Guenal', 'Guennegues', 'Guerin', 'Guerveno', 'Guery', 'Guibert', 'Guichard', 'Guilbert', 'Guillaume', 'Guillemard', 'Guillet', 'Guillon', 'Guillot', 'Guillou', 'Guyon', 'Guyot', 'Hachour', 'Haddane', 'Haidi', 'Haifi', 'Hamad', 'Hamdi', 'Hammadi', 'Hammou', 'Hamon', 'Harbane', 'Hardy', 'Hargas', 'Harnoufi', 'Hassler', 'Hatem', 'Heduit', 'Henaff', 'Henry', 'Hernandez', 'Herve', 'Hervy', 'Hoarau', 'Hoareau', 'Hoff', 'Hubert', 'Huet', 'Humbert', 'Humery', 'Iken', 'Iliassy', 'Imbault', 'Imbert', 'Isaac', 'Jacob', 'Jacques', 'Jacquet', 'Jacquin', 'Jacquot', 'Jardine', 'Jean', 'Jellouli', 'Jeyakanthan', 'Joannet', 'Joly', 'Jonda', 'Joseph', 'Joubert', 'Jourdan', 'Joyeux', 'Julien', 'Juliza', 'Kanga', 'Keddis', 'Keita', 'Khalin', 'Khelil', 'Khenoun', 'Khezzar', 'Klein', 'Klepper', 'La Fonta', 'Labori', 'Lacombe', 'Lacoste', 'Lacroix', 'Ladjouze', 'Lado', 'Lagarde', 'Lallement', 'Lam', 'Lambert', 'Lamy', 'Lanclos', 'Langlois', 'Laporte', 'Laposi', 'Laramendy', 'Laroche', 'Laroui', 'Lassouani', 'Launay', 'Laurent', 'Laurin', 'Lauriola', 'Lavie', 'Lavigne', 'Le', 'Le Bihan', 'Le Blanc', 'Le Cam', 'Le Corre', 'Le Goueff', 'Le Gall', 'Le Goff', 'Leroux', 'Lebbah', 'Leblanc', 'Lebon', 'Leboubenec', 'Lebouc', 'Lebreton', 'Lebrun', 'Lechien', 'Leclerc', 'Leclercq', 'Lecomte', 'Leconte', 'Ledeme', 'Ledoux', 'Leduc', 'Lefebvre', 'Lefevre', 'Lefort', 'Legall', 'Legoff', 'Leger', 'Legrand', 'Lejeune', 'Lelu', 'Lemaire', 'Lemaitre', 'Lemba', 'Lemoine', 'Lengard', 'Lenoir', 'Lepretre', 'Leroux', 'Leroy', 'Lesage', 'Letrange', 'Leveque', 'Levy', 'Li', 'Li Combeau', 'Lignac', 'Linard', 'Loiseau', 'Loisel', 'Lombard', 'Lopes', 'Lopez', 'Louis', 'Louvet', 'Louzet', 'Lucas', 'Ludiongo', 'Lukacs', 'Mache', 'Maillard', 'Maillet', 'Maillot', 'Maire', 'Mallet', 'Manour', 'Marchal', 'Marchand', 'Marechal', 'Marie', 'Marin', 'Marion', 'Markoulakis', 'Marque', 'Martel', 'Martial', 'Martin', 'Martineau', 'Martinez', 'Martins', 'Marty', 'Mary', 'Massart', 'Masset', 'Masson', 'Mathieu', 'Maurice', 'Maurin', 'Maury', 'Mayer', 'Mazzoni', 'Medbouhi', 'Mediouni', 'Mehimda', 'Melek', 'Melin', 'Menard', 'Mendes', 'Merbah', 'Mercier', 'Mercorelli', 'Merle', 'Merton', 'Messi', 'Metel', 'Meunier', 'Meyer', 'Michalak', 'Michaud', 'Michel', 'Mielle', 'Mignard', 'Mignot', 'Millaniyage', 'Millet', 'Mobre', 'Mohellibi', 'Moindjie', 'Mokrab', 'Moncler', 'Monnier', 'Moreau', 'Moreira Da Silva', 'Morel', 'Moreno', 'Morin', 'Morvan', 'Mothor', 'Moulin', 'Moutou', 'Mulard', 'Muller', 'NULL', 'Nalla', 'Navarro', 'Neel', 'Nelo', 'Nemour', 'Netter', 'Neveu', 'Nguyen', 'Nicolas', 'Ninoux', 'Noel', 'Noreskal', 'Normand', 'Nosel', 'Nouri', 'Olivier', 'Ollivier', 'Orlhac', 'Oster', 'Osyssek', 'Oubir', 'Pardo', 'Paris', 'Parodi', 'Pascal', 'Pasquier', 'Paul', 'Paviot', 'Payet', 'Peignet', 'Pelletier', 'Peltier', 'Pencole', 'Pereira', 'Pereira da cunha', 'Perez', 'Perret', 'Perrier', 'Perrin', 'Perrot', 'Person', 'Petit', 'Philippe', 'Phkar', 'Phouphetlinthong', 'Picard', 'Pichon', 'Pierre', 'Pineau', 'Pinto', 'Piouceau', 'Pipelier', 'Piroelle', 'Plancq', 'Plisson', 'Poirier', 'Pons', 'Portelette', 'Potier', 'Pottier', 'Poulain', 'Prat', 'Praud', 'Prehaud', 'Pret', 'Prevost', 'Prieu', 'Quessette', 'Rabate', 'Radelet', 'Rami', 'Rano', 'Rasamizanany', 'Raymond', 'Raynal', 'Raynaud', 'Razafindrabary', 'Reale', 'Reber', 'Reeb', 'Regaud', 'Remy', 'Renard', 'Renaud', 'Renault', 'Renaut', 'Restier', 'Rey', 'Reynaud', 'Ribeiro', 'Richard', 'Rili', 'Rincheval', 'Rios Campo', 'Riou', 'Rivera', 'Riviere', 'Robert', 'Robin', 'Roche', 'Rocher', 'Rodrigues', 'Rodriguez', 'Roger', 'Rolland', 'Romero', 'Rondey', 'Rossi', 'Rotella', 'Rouinvy', 'Rousseau', 'Roussel', 'Rousset', 'Roux', 'Rouxel', 'Roy', 'Royer', 'Royere', 'Ruiz', 'Rziki', 'Saccard', 'Said', 'Saillard', 'Sailly', 'Salic', 'Salimier', 'Salmon', 'Sami', 'Sanchez', 'Sandu', 'Santrot', 'Sanz', 'Sapriel', 'Sautet', 'Sauvage', 'Schmitt', 'Schneider', 'Screve', 'Seddiki', 'Segaux', 'Seguin', 'Seksaoui', 'Serber', 'Siaud', 'Sicherre', 'Sifi', 'Simoes', 'Simon', 'Sitterlin', 'Soares', 'Solomon', 'Sourdeval', 'Sousa', 'Striebig', 'Strozecki', 'Szuplewzki', 'Tagba', 'Taher', 'Tang', 'Tanguy', 'Tardieu', 'Tardivel', 'Tellier', 'Terki', 'Tessier', 'Texier', 'Therage', 'Thibaudeau', 'Thibault', 'Thibuta', 'Thierry', 'Thomas', 'Tieres', 'Tijari', 'Toso', 'Toussaint', 'Tran', 'Trellu', 'Trosset', 'Tseveendorj', 'Tuffet', 'Turpin', 'Tuzi', 'Ursule', 'Uthayakumar', 'Vaillant', 'Valentin', 'Valette', 'Vallet', 'Van', 'Van Loo', 'Varoqui', 'Vasseur', 'Vauthier', 'Ventre', 'Verdier', 'Versaveau', 'Vervel', 'Vetillard', 'Vetter', 'Vial', 'Viart', 'Vichet', 'Vidal', 'Vignaud', 'Villain', 'Vincens', 'Vincent', 'Vincetti', 'Viollette', 'Vissault', 'Vixemar', 'Voile', 'Voisin', 'Wagner', 'Wassaf', 'Weber', 'Wielgosz', 'Willay', 'Wu', 'Yapo', 'Younsi', 'Zagnoni', 'Zelamta', 'Zemmouri', 'Zenati']


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
print(liste_annee)

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
            tuple_commande = "(" + str(num_commande) + ", " + nom_client + ", " + str(date_commande) + ", " + service + ", " + str(num_serveur) + ", " + str(num_table) + ")"
            fic_commandes.write(tuple_commande+'\n')
            num_commande += 1

def commandes():
    fic_commandes = open('commandes.txt', 'w')
    for sem in liste_annee:
        semaine = transfo_date_python_to_sql(sem)
        commandes_semaine(semaine, fic_commandes)
    fic_commandes.close()

# pour les boissons, mettre souvent de l'eau
# chaque commande a au moins une boisson associée ou un EPD