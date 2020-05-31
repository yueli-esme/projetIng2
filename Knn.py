# -*- coding: utf-8 -*-

''' ---------------------- Knn ---------------------------- '''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# On importe dans une df notre fichier avec les données nettoyées
# Mais non normalisée car ce modèle n'en a pas besoin
df = pd.read_csv("df_7_features_nettoye.csv", sep=';')

# Une nouvelle colonne d'index a été crée, on peut la supprimer
del df['Unnamed: 0']

# On crée 2 tableaux X et y : X contient les caractéristiques de df et y est la variable cible
y = df['Intrusion']
X = df.drop('Intrusion', axis=1)

# On divise les données en données d'entrainements et de tests
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

# On instancie un KNeighborsClassifier avec 6 voisins 
knn = KNeighborsClassifier(7)

#On entraine le modele
knn.fit(X_train, y_train)


# On calcule et affiche la précision des prédictions du classificateur à l'aide de la méthode score().  
print("test accuracy : {}".format(knn.score(X_test, y_test)))
print("test accuracy : {}".format(knn.score(X_train, y_train)))

# retourne :
# test accuracy : 0.983123779296875
# test accuracy : 0.983458180056483




