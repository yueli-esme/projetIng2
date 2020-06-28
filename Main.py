# -*- coding: utf-8 -*-


'''
------------------------------ Main -----------------------------------
'''

import pandas as pd

import Preparation_CSV as pc        
import feature_importances_ as fi
import Normalisation_donnees as nor
import BaggingClassifier as bc
import Modeles_ML as ml
import pickle

df_T_15 = pd.read_csv("Thursday-15-02-2018_TrafficForML_CICFlowMeter.csv")
df_T_22 = pd.read_csv("Thursday-22-02-2018_TrafficForML_CICFlowMeter.csv")
df_W_21 = pd.read_csv("Wednesday-21-02-2018_TrafficForML_CICFlowMeter.csv")
df_W_14 = pd.read_csv("Wednesday-14-02-2018_TrafficForML_CICFlowMeter.csv")
df_F_02 = pd.read_csv("Friday-02-03-2018_TrafficForML_CICFlowMeter.csv")
df_F_23 = pd.read_csv("Friday-23-02-2018_TrafficForML_CICFlowMeter.csv")


df_T_15_copy = pc.Preparation_CSV(df_T_15)
df_T_22_copy = pc.Preparation_CSV(df_T_22)
df_W_21_copy = pc.Preparation_CSV(df_W_21)
df_W_14_copy = pc.Preparation_CSV(df_W_14)
df_F_02_copy = pc.Preparation_CSV(df_F_02)
df_F_23_copy = pc.Preparation_CSV(df_F_23)


# On enregistre toutes ces dataframes dans de nouveaux fichiers csv pour les conserver
df_T_15_copy.to_csv("df_T_15_copy.csv", sep=';')
df_T_22_copy.to_csv("df_T_22_copy.csv", sep=';')
df_W_21_copy.to_csv("df_W_21_copy.csv", sep=';')
df_W_14_copy.to_csv("df_W_14_copy.csv", sep=';')
df_F_02_copy.to_csv("df_F_02_copy.csv", sep=';')
df_F_23_copy.to_csv("df_F_23_copy.csv", sep=';')

# Concaténation de toutes les datasets
dataset = pd.concat([df_T_15_copy,df_T_22_copy,df_W_21_copy,df_W_14_copy,df_F_02_copy,df_F_23_copy])
dataset = dataset.reset_index(drop = True)
dataset.fillna(0, inplace=True)
dataset.to_csv("total_dataset_Equalized_intrusion_SinNull.csv", sep=';', index = False)

# Importances des features
df_features_importances = fi.FeaturesImportances(dataset)

# On enregistre dans un csv ce dataframe pour le sauvegarder
df_features_importances = df_features_importances.reset_index(drop = True)
df_features_importances.to_csv("total_dataset_Features_importances.csv", sep=';', index = False)

# Normalisation des donnees
df_normalise = nor.NormalizeDataset(df_features_importances)
df_normalise = df_normalise.reset_index(drop = True)
df_normalise.to_csv("total_dataset_normalise.csv", sep=';', index = False)


# On appelle nos modeles de ML
# Knn
knn = ml.knn(df_normalise)
filename_knn = 'finalized_model_knn.sav'
pickle.dump(knn, open(filename_knn, 'wb'))

# Random Forest Classifier
rf = ml.rf(df_normalise)
filename_rf= 'finalized_model_rf.sav'
pickle.dump(rf, open(filename_rf, 'wb'))

# Gaussian naive Bayes
gnb = ml.gnb(df_normalise)
filename_gnb = 'finalized_model_gnb.sav'
pickle.dump(knn, open(filename_gnb, 'wb'))

# Bagging Classifier
bc.BaggingClass(df_normalise)