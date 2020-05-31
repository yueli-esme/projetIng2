# -*- coding: utf-8 -*-

''' ---------------------- Regression Lineaire ---------------------------- '''

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np


# On importe dans une df notre fichier avec les données nettoyées
# Mais non normalisée car ce modèle n'en a pas besoin
df = pd.read_csv("df_7_features_normalise_nettoye.csv", sep=';')

# Une nouvelle colonne d'index a été crée, on peut la supprimer
del df['Unnamed: 0']

# On crée une fonction pour pouvoir l'appeler pour chaque feature
def plotLinearRegression(df,target, feature):
    # On crée 2 tableaux X et y : X contient les caractéristiques de df et y est la variable cible
    y = df[target].values
    X = df[feature].values
    
    # On affiche les dimensions avant le reshape
    print("Size of y before reshaping: {}".format(y.shape))
    print("Size of X before reshaping: {}".format(X.shape))
    
    # Reshape X et y
    y = y.reshape(-1,1)
    X = X.reshape(-1,1)
    
    # On affiche les dimensions de X et y après le reshape
    print("Size of y after reshaping: {}".format(y.shape))
    print("Size of X after reshaping: {}".format(X.shape))
    
    # On affiche dans un plot la feature et la target Intrusion
    plt.figure()
    plt.scatter(X, y)
    plt.xlabel(feature)
    plt.ylabel(target)
    
    # On crée notre modele
    reg = LinearRegression()
    
    # On lui cree un espace de prediction
    prediction_space = np.linspace(min(X), max(X))
    
    # On entraine le modele
    reg.fit(X, y)
    
    # On predit
    y_pred = reg.predict(prediction_space)
    
    # On affiche le score 
    print(reg.score(X, y))
    
    # Et on affiche la droite de regression lineaire
    plt.plot(prediction_space, y_pred, color='black', linewidth=3)
    
# On appelle donc la fonction pour chaque feature 
for feature in df.columns:
    plotLinearRegression(df,'Intrusion', feature)
    

