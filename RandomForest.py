# -*- coding: utf-8 -*-

''' ---------------------- Random Forest Regressor ---------------------------- '''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

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


# On instancie notre modèle avec 100 arbres de décision
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)

# Puis on l'entraîne
rf.fit(X_train, y_train);

# Prediction
y_pred = rf.predict(X_test)


