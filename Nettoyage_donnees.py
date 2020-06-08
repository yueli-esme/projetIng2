# -*- coding: utf-8 -*-

''' -------------------- Nettoyage des données -------------------------------- '''

import pandas as pd
import numpy as np

df_T_15 = pd.read_csv("df_T_15_copy.csv", sep=';')
df_T_22 = pd.read_csv("df_T_22_copy.csv", sep=';')
df_W_21 = pd.read_csv("df_W_21_copy.csv", sep=';')
df_W_14 = pd.read_csv("df_W_14_copy.csv", sep=';')
df_F_02 = pd.read_csv("df_F_02_copy.csv", sep=';')
df_F_23 = pd.read_csv("df_F_23_copy.csv", sep=';')

del df_T_15['Unnamed: 0']
del df_T_22['Unnamed: 0']
del df_W_21['Unnamed: 0']
del df_W_14['Unnamed: 0']
del df_F_02['Unnamed: 0']
del df_F_23['Unnamed: 0']

# FONCTIONS 
def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result


def nettoyage(df):
    result = df.copy()
    # On remplace els donnees Nan par O 
    result.fillna(0)
    
    # On arrondie les nb avec 5 chiffres apreès la virgule
    for colonne in result.columns:
        a = np.array((result[colonne]))
        result[colonne] = np.around(a, decimals=5)
    return result
  
''' NORMALISATION + NETTOYAGE '''

#on ne normalise pas la 1ere et 2eme fature ainsi que la derniere : Dst Port ; Protocol ; Intrusion
def NormalizeAndClean(dataset) :

    dataset_normalise = normalize(dataset.iloc[:,2:len(dataset)])
    dataset_final_normalise = pd.concat([dataset.iloc[:,0:2], dataset_normalise, dataset.iloc[:,len(dataset):]], axis=1)
    dataset_final_normalise_nettoyee = nettoyage(dataset_final_normalise)
    
    return dataset_final_normalise_nettoyee
    
# on normalise et nettoie toutes nos df
df_T_15_NN = NormalizeAndClean(df_T_15)
df_T_22_NN = NormalizeAndClean(df_T_22)
df_W_21_NN = NormalizeAndClean(df_W_21)
df_W_14_NN = NormalizeAndClean(df_W_14)
df_F_02_NN = NormalizeAndClean(df_F_02)
df_F_23_NN = NormalizeAndClean(df_F_23)

# On enregistre toutes ces dataframes dans de nouveaux fichiers csv pour les conserver
df_T_15_NN.to_csv("df_T_15_normalise_nettoye.csv", sep=';')
df_T_22_NN.to_csv("df_T_22_normalise_nettoye.csv", sep=';')
df_W_21_NN.to_csv("df_W_21_normalise_nettoye.csv", sep=';')
df_W_14_NN.to_csv("df_W_14_normalise_nettoye.csv", sep=';')
df_F_02_NN.to_csv("df_F_02_normalise_nettoye.csv", sep=';')
df_F_23_NN.to_csv("df_F_23_normalise_nettoye.csv", sep=';')




''' NETTOYAGE SEULEMENT '''

# on nettoie toutes nos df
df_T_15_N = nettoyage(df_T_15)
df_T_22_N = nettoyage(df_T_22)
df_W_21_N = nettoyage(df_W_21)
df_W_14_N = nettoyage(df_W_14)
df_F_02_N = nettoyage(df_F_02)
df_F_23_N = nettoyage(df_F_23)

# On enregistre toutes ces dataframes dans de nouveaux fichiers csv pour les conserver
df_T_15_N.to_csv("df_T_15_nettoye.csv", sep=';')
df_T_22_N.to_csv("df_T_22_nettoye.csv", sep=';')
df_W_21_N.to_csv("df_W_21_nettoye.csv", sep=';')
df_W_14_N.to_csv("df_W_14_nettoye.csv", sep=';')
df_F_02_N.to_csv("df_F_02_nettoye.csv", sep=';')
df_F_23_N.to_csv("df_F_23_nettoye.csv", sep=';')


