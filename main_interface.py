# -*- coding: utf-8 -*-

'''
----------------------- MAIN INTERFACE ---------------------------
'''


import Modeles_ML as ml
import GUI_Machine_Learning as gui
import pickle
import pandas as pd

df = pd.read_csv("total_dataset_normalise.csv", sep=';')

df_test=gui.interface(df)

filename_knn = 'finalized_model_knn.sav'
filename_rf= 'finalized_model_rf.sav'
filename_gnb = 'finalized_model_gnb.sav'

loaded_model_knn = pickle.load(open(filename_knn, 'rb'))
loaded_model_rf = pickle.load(open(filename_rf, 'rb'))
loaded_model_gnb = pickle.load(open(filename_gnb, 'rb'))

pred_knn = ml.knnPrediction(df_test, loaded_model_knn)
pred_rf = ml.rfPrediction(df_test, loaded_model_rf)
pred_gnb = ml.gnbPrediction(df_test, loaded_model_gnb)

gui.result(pred_knn,pred_rf,pred_gnb)