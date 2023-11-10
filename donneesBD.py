import random
import time

# Constantes

num_commande = 1

num_entrees = random.randint(1, 11)
num_plats = random.randint(12, 28)
num_desserts = random.randint(29, 45)

liste_noms_clients = ['NULL', 'Auclair', 'Barth', 'Bouleau', 'Bourra', 'Brezellec', 'Camion', 'Chairet', 'Chevalier', 'Corsi', 'Coucheney', 'Cremazy', 'Debat', 'Diab', 'Durand',
                          'Etchebest', 'Fages', 'Ferrat', 'Finance', 'Fourneau', 'Gattoliat', 'Garnier', 'Gaumer', 'Gianfrotta', 'Hoareau', 'Jacquin', 'Jellouli', 'Keddis', 'Lamy', 'Lebbah',
                          'Le Corre', 'Lefevre', 'Lemaire', 'Lignac', 'Manour', 'Marque', 'Mayer', 'Mediouni', 'Moindjie', 'Moreno', 'Mothor', 'Netter',
                          'Prehaud', 'Pret', 'Prieu', 'Quessette', 'Rincheval', 'Rotella', 'Sandu', 'Sapriel', 'Sitterlin', 'Sourdeval', 'Strozecki', 'Szuplewzki', 'Taher',
                          'Terki', 'Timsiline', 'Tseveendorj', 'Vial', 'Vincens']

liste_num_serveurs = [k for k in range(0,11)]

def commandes_semaine():

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
     
    liste_services2 = [2, 3, 5]
    fic_commandes = open('commandes.txt', 'w')

    for num_service in range(len(liste_services2)):      # pour chaque service
        for num_client in range(liste_services2[num_service]):       # pour chaque commande
            nom_client = random.choice(liste_noms_clients, [0.8]+[0.1 for k in range(len(liste_noms_clients)-1)])[0]
            if nom_client != 'NULL':
                nom_client = "'" + nom_client + "'"
            jour = 0
            mois = 0
            annee = 0
            date_commande = 0
            service = "'" + l_services[num_service%2] + "'"
            num_serveur = random.choice(serveurs_travaillant_sachant_service(jour, annee))
            num_table = 0
            tuple_commande = "(" + str(num_commande) + ", " + nom_client + ", " + str(date_commande) + ", " + service + ", " + str(num_serveur) + ", " + str(num_table) + ")"
            fic_commandes.write(tuple_commande)
            num_commande += 1
    fic_commandes.close()

commandes_semaine()

def serveurs_travaillant_sachant_service(jour, annee):
    """ Retourne la liste des serveurs travaillant le jour et l'annnée correspondante"""
    if (jour=='Ven') or (jour=='Sam') or (jour=='Dim'):
        nb_serveurs = random.choice([2, 3, 4], [0.25, 0.7, 0.05])[0]
    else:
        nb_serveurs = random.choice([1, 2, 3], [0.2, 0.75, 0.05])[0]

    if annee==2023:      #attention int/str
        serveurs = [k for k in range(2,11)]
    elif annee==2022:
        serveurs = [k for k in range(3, 9)]
    elif annee==2021:
        serveurs = [k for k in range(0,9)]
    else:
        serveurs = [k for k in range(0,7)]
    
    while len(serveurs)!= nb_serveurs:
        serveurs.remove(random.choice(serveurs))[0]

    return serveurs

# pour les boissons, mettre souvent de l'eau

def tuples_COMMANDES(liste_services):

    ind_cl = 1
    l_jours = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']
    l_services = ['M', 'S']

    for num_service in range(len(liste_services)):
        for client in range(liste_services[num_service]):
            num_commande = str(ind_cl)
            num_client = '9' + str(num_commande)
            # format date : %a-%e-%b
            date = "'" + l_jours[num_service//2] + '-' + str(23+(num_service//2)) + '-' + 'Oct' + "'"
            service = "'" + l_services[num_service%2] + "'"
            num_serveur = 0
            num_table = 0
            print("(" + num_commande + ", " + num_client + ", " + date + ", " + service + ", " + str(num_serveur)
                  + ", " + str(num_table) + ")")
            ind_cl += 1


# chaque commande a au moins une boisson associée