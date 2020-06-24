# -*- coding: utf-8 -*-

'''
----------------------- MAIN INTERFACE ---------------------------
'''

import Main

import Modeles_ML as ml

import GUI_Machine_Learning as gui


df_test=gui.interface()

pred_knn = ml.knnPrediction(df_test, Main.knn)
pred_rf = ml.rfPrediction(df_test, Main.rf)
pred_gnb = ml.gnbPrediction(df_test, Main.gnb)

gui.result(pred_knn,pred_rf,pred_gnb)


