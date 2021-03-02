# -*- coding: utf-8 -*-
import csv
import ast

liste_data_par_chanson = []

# Récupération des données importantes (titre, artiste et année) des données de départ
with open('data.csv', "r", encoding="utf-8") as csv_data:
    csv_reader = csv.reader(csv_data, delimiter=',')
    line_count = 0
    for row in csv_reader:
        liste_data_par_chanson.append(row)
        #liste_data_par_chanson.append([row[1], row[12], row[18]])
        line_count+=1
    print(f'Fin de data.csv avec {line_count} lignes.')

print(liste_data_par_chanson[:5])
# Récupération du genre
## Création du dictionne artist donne son genre
dico_artist_genre = {}
with open('data_w_genres.csv', "r", encoding="utf-8") as csv_data:
    csv_reader = csv.reader(csv_data, delimiter=',')
    line_count = 0
    for row in csv_reader:
        try: # besoin de ce test car ast.literal_eval transforme avec le bon type mais ne gère pas les decimals
            genre = ast.literal_eval(row[15]) 
        except ValueError:
            corrected = "\'" + row[15] + "\'"
            genre = ast.literal_eval(corrected)
        dico_artist_genre[row[0]]= genre
        line_count+=1
    print(f'Fin de data_w_genres.csv avec {line_count} lignes.')

#print(dico_artist_genre['Dick Haymes'])


## Création dictionnaire sous genre vers genres généraux
dico_genre_sous_genre = {}
with open('sousgenre_vers_genre.csv', "r", encoding="utf-8") as csv_genre:
    csv_reader = csv.reader(csv_genre, delimiter=';')
    line_count = 0
    for row in csv_reader:
        #print(row)
        dico_genre_sous_genre[row[0]]= row[1:]
        line_count+=1
    print(f'Fin de sousgenre_vers_genre.csv avec {line_count} lignes.')


## Ajout du genre
    # Il y a encore des guillemets en trop sur l'output, mais qui n'y sont pas toujours
liste_data_par_chanson[0].append("genres")
for i in range(1, len(liste_data_par_chanson)):
    artists = liste_data_par_chanson[i][1]
    artists = ast.literal_eval(artists)
    #print(artists)
    genres_precis = []
    genres_generaux = []
    for artist in artists:
        if artist != "n/a": # pour eviter ce cas, qui est qu'il n'est pas précisé
            genres_precis+=dico_artist_genre[artist] # récupération des genres parmi les 3000
    for genre in genres_precis:
        try: # pour gérer les genres qu'on n'a pas
            genres_generaux += dico_genre_sous_genre[genre] # récupération des genres généraux
        except KeyError:
            pass
    
    genres_generaux = list(set(genres_generaux)) # pour supprimer les doublons
    if '' in genres_generaux:
        genres_generaux.remove('')
    liste_data_par_chanson[i].append(genres_generaux)

#print(liste_data_par_chanson[150])
print()

# Calcul des données par genre et par année
dico_par_genre_par_annee = {}
liste_genre = ["rock", "blues", "country", "chill", "electro", "folk", "rap", "jazz", "latino", "pop", "r&b", "metal", "classical", "reggae", "soul"]
for genre in liste_genre:
    dico_par_genre_par_annee[genre] = {}

# calcul des sommes des chaque valeur
for row in liste_data_par_chanson[1:]:
    year = row[18]
    genres = row[19]
    #print(row)
    valeurs = {"acousticness" : float(row[0]), "danceability" : float(row[2]), "duration_ms" : float(row[3]), "energy" : float(row[4]), "explicit" : int(row[5]), "instrumentalness" : float(row[7]), "key" : int(row[8]), "liveness" : float(row[9]), "loudness" : float(row[10]), "mode" : float(row[11]), "popularity" : float(row[13]), "speechiness" : float(row[15]), "tempo" : float(row[16]), "valence" : float(row[17]), "nombre" : 1}
    for genre in genres:
        if year not in dico_par_genre_par_annee[genre]:
            dico_par_genre_par_annee[genre][year] = valeurs.copy()
        else:
            for clef in dico_par_genre_par_annee[genre][year]:
                dico_par_genre_par_annee[genre][year][clef] += valeurs[clef]

# normalisation pour avoir une moyenne
for genre in liste_genre:
    for year in dico_par_genre_par_annee[genre]:
        for clef in dico_par_genre_par_annee[genre][year]:
            if clef!= "nombre":
                dico_par_genre_par_annee[genre][year][clef] = dico_par_genre_par_annee[genre][year][clef]/dico_par_genre_par_annee[genre][year]["nombre"]

print(dico_par_genre_par_annee["rock"]["2000"])

# mise dans une liste pour export
liste_out = [["genre", "year","acousticness", "danceability", "duration_ms", "energy", "explicit", "instrumentalness", "key", "liveness", "loudness", "mode", "popularity", "speechiness", "tempo", "valence", "nombre"]]
for genre in liste_genre:
    for year in dico_par_genre_par_annee[genre]:
        liste_append = [genre, year]
        for clef in dico_par_genre_par_annee[genre][year]:
            liste_append.append(dico_par_genre_par_annee[genre][year][clef])
        liste_out.append(liste_append)
        
print(liste_out[150])


# Ecriture en CSV
with open('data_par_genre_par_annee_out.csv', 'w', newline='', encoding="utf-8") as file_out:
    writer = csv.writer(file_out)
    writer.writerows(liste_out)
