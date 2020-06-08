# -*- coding: utf-8 -*-

''' -------------------- Nettoyage des données -------------------------------- '''

import pandas as pd
import numpy as np

df_initial = pd.read_csv("df_W_14_copy.csv", sep=';')

del df_initial['Unnamed: 0']

# On choisit 7 features qu'on met dans une df

liste_features = ['Protocol', 'Flow Duration', 'TotLen Fwd Pkts', 
                  'TotLen Bwd Pkts',  
                  'Fwd PSH Flags','Pkt Size Avg','Intrusion']

df_7_features = df_initial[liste_features]

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
    # On remplace els donnees Nan par O et infinie 
    result.fillna(0)
    
    # On arrondie les nb avec 5 chiffres apreès la virgule
    for colonne in result.columns:
        a = np.array((result[colonne]))
        result[colonne] = np.around(a, decimals=5)
    return result
        
def MinMaxFeature(df):
    for feature_name in df.columns:
            max_value = df[feature_name].max()
            min_value = df[feature_name].min()
            print('Feature :', feature_name, '\nMin :', min_value, '\nMax :', max_value)
            

''' NORMALISATION + NETTOYAGE '''
# On ne choisit que celles que l'on veut normaliser
# Ici on veut normaliser : 'Flow Duration', 'TotLen Fwd Pkts', 'TotLen Bwd Pkts'
df_7_normalise = normalize(df_7_features.iloc[:,1:4])

# Puis on concatene nos differentes features
df_7_final_normalise = pd.concat([df_7_features.iloc[:,0:1], df_7_normalise, df_7_features.iloc[:,4:]], axis=1)

# On nettoie nos données de la df
df_7_final_normalise_nettoyee = nettoyage(df_7_final_normalise)

# On met cette dataframe dans un fichier csv pour le conserver et pouvoir le réutiliser par la suite
# Donc df est nettoyée + normalisée
df_7_final_normalise_nettoyee.to_csv("df_7_features_normalise_nettoye.csv", sep=';')

''' NETTOYAGE SEULEMENT '''
# On nettoie nos données de la df
df_7_final_nettoyee = nettoyage(df_7_features)

# On met aussi df non normalisée mais nettoyée dans un fichier csv 
# car certains modeles de ML ne nécessitent pas forcement une normalisation
df_7_final_nettoyee.to_csv("df_7_features_nettoye.csv", sep=';')


# On peut regarder aussi le minimum et maximum de chaque features pour plus tard  
print('-------Min Max df_7_final_normalise_nettoyee')        
MinMaxFeature(df_7_final_normalise_nettoyee)

print('-------Min Max df_7_final_nettoyee')
MinMaxFeature(df_7_final_nettoyee)


# On regarde pour chaque features de la df le min et max pour savoir lesquels comportent 
# Des inf
print('-------Min Max df_initial')
MinMaxFeature(df_initial)

# Il n'y a que ces deux la qui ont inf : Flow Byts/s ; Flow Pkts/s 







def NormalizeAndClean(dataset) :
    
    dataset_features = dataset[liste_features]
    dataset_normalise = normalize(dataset_features.iloc[:,1:4])
    dataset_final_normalise = pd.concat([dataset_features.iloc[:,0:1], dataset_normalise, dataset_features.iloc[:,4:]], axis=1)
    dataset_final_normalise_nettoyee = nettoyage(dataset_final_normalise)
    dataset_final_normalise_nettoyee.to_csv(r"C:\Users\Charles-Alexandre\Desktop\dataset_features_normalise_nettoye.csv", sep=';')
    return dataset_final_normalise_nettoyee
  
  
def nettoyage(dataset):
    result = dataset.copy()
    result.fillna(0)
    return result # rajouter cette ligne a la fonction nettoyage pour que la fonction normalize and clean fonctionne 
