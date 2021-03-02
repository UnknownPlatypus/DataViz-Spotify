# <a>Dataviz Spotify</a><a href="url"><img src="https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/material/.icons/material/webpack.svg" align="left" height="64" width="64" ></a> 

Parser python des données de 'data.csv' et 'data_w_genres.csv' du dataset [Spotify Dataset 1921-2020, 160k+ Tracks](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data_by_genres.csv). Associe à chaque morceau des genres principaux via le fichier 'sousgenre_vers_genre.csv'.

## Table of Contents

 * [Description](#Description)
 * [Utilisation](#Utilisation)

## Description

Parser python des données de 'data.csv' et 'data_w_genres.csv' du dataset [Spotify Dataset 1921-2020, 160k+ Tracks](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data_by_genres.csv). Associe à chaque morceau des genres principaux via le fichier 'sousgenre_vers_genre.csv'.

## Utilisation

1. Placer dans le même dossier les fichiers `data.csv`, `data_w_genres.csv`, `sousgenre_vers_genre.csv` et `parser.py`.
2. Executer le programme `parser_data.py`
3. Le résultat est exporté dans un fichier `data_par_genre_par_annee_out.csv`.
