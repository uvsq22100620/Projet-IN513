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