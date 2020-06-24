# -*- coding: utf-8 -*-

'''
----------------------- INTERFACE ---------------------------
'''

import PySimpleGUI as sg
import pandas as pd

def interface(df):
    liste_colonne = list(df.columns)
    print(liste_colonne)
    
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
 
    layout = []
    layout.append([sg.Text('Veuillez rentrer vos informations :')])
        
    for i in range(0,len(liste_colonne)):
        layout.append([sg.Text(liste_colonne[i], size=(16, 1)), sg.InputText(default_text = 0)])
        
    layout.append([sg.Button('Ok'), sg.Button('Cancel')])
    
    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        #df_user = pd.DataFrame(columns = 'entrée1','entrée2', ...)
        #df_new = pd.DataFrame()
        X_new = []
        for i in range (0, len(layout)-2):
            X_new.append(values[i])
        print(X_new)
    
    features = list(df.columns)

    df_new = pd.DataFrame([X_new], columns=features)
    df_new.to_csv('df_new.csv', sep=';', index = False)
    
    
    window.close()
    
    return df_new
    
if __name__ == "__main__":
    interface()
    
def result(pred_knn,pred_rf, pred_gnb):
    
    if(pred_knn == 1.0):
        resultat_knn = 'Intrusion'
    else:
        resultat_knn = 'Benin'
    
    if(pred_rf == 1.0):
        resultat_rf = 'Intrusion'
    else:
        resultat_rf = 'Benin'
    
    if(pred_gnb == 1.0):
        resultat_gnb = 'Intrusion'
    else:
        resultat_gnb = 'Benin'
       
    sg.popup('Resultat', 'Le resultat pour le Knn :{}'.format(resultat_knn),'Le resultat pour le Random Forest :{}'.format(resultat_rf), 'Le resultat pour le Gaussian Naive :{}'.format(resultat_gnb))
    
    