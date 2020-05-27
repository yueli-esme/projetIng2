# -*- coding: utf-8 -*-
'''
    Machine Learning
'''

import pandas as pd

df = pd.read_csv("df_W_14_copy.csv", sep=';')

del df['Unnamed: 0']

# On choisit 10 features qu'on met dans une df

liste_features = ['Protocol', 'Flow Duration', 'TotLen Fwd Pkts', 
                  'TotLen Bwd Pkts', 'Flow Byts/s','Flow Pkts/s', 
                  'Fwd PSH Flags','Pkt Size Avg','Intrusion']

df_10_features = df[liste_features]

# On normalise nos features
def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

# On ne choisit que celles que l'on veut normaliser
# Ici on veut normaliser : 'Flow Duration', 'TotLen Fwd Pkts', 'TotLen Bwd Pkts', 'Flow Byts/s','Flow Pkts/s'
df_10_normalise = normalize(df_10_features.iloc[:,1:6])

# Puis on concatene nos differentes features
df_final = pd.concat([df_10_features.iloc[:,0:1], df_10_normalise, df_10_features.iloc[:,6:]], axis=1)

df_final.to_csv("df_final.csv", sep=';')

############################################################################

df_final = pd.read_csv("df_final.csv", sep=';')
del df_final['Unnamed: 0']

# On remplace els donnees Nan par O et infinie 
import numpy as np
df_final.fillna(0)
df_final.replace(np.inf, inplace=True)

# On arrondie les nb avec 5 chiffres apreès la virgule
for colonne in df_final.columns:
    a = np.array((df_final[colonne]))
    df_final[colonne] = np.around(a, decimals=5)

y = df_final['Intrusion']

X = df_final.drop('Intrusion', axis=1)

'''
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=21)
 '''
 

import matplotlib.pyplot as plt

features = df_final.drop('Intrusion', axis=1)
target = df_final['Intrusion']

for i, col in enumerate(features):
    plt.show()
    x = df_final[col]
    y = target
    plt.scatter(x, y, marker='o')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('Intrusion')
    
 