# -*- coding: utf-8 -*-

''' -------------------- Normalisation des données -------------------------------- '''

import pandas as pd

def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

def NormalizeDataset(dataset) :
    dataset_normalise = normalize(dataset.iloc[:,2:len(dataset)])
    dataset_final_normalise = pd.concat([dataset.iloc[:,0:2], dataset_normalise, dataset.iloc[:,len(dataset):]], axis=1)
    return dataset_final_normalise

