# -*- coding: utf-8 -*-

'''
----------------------- INTERFACE ---------------------------
'''

import PySimpleGUI as sg
import pandas as pd

def interface():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Veuillez rentrer vos informations :')],
                [sg.Text('index', size=(16, 1)) , sg.InputText(default_text = 44)],
                [sg.Text('Dst Port', size=(16,1)), sg.InputText(default_text = 80)],
                [sg.Text('Tot Bwd Pkts',size=(16,1)), sg.InputText(default_text = 5.77692e-05)],
                [sg.Text('Fwd IAT Std',size=(16,1)), sg.InputText(default_text = 1.357e-06)],
                [sg.Text('Fwd PSH Flags',size=(16,1)), sg.InputText(default_text = 0.0)],
                [sg.Text('Fwd Header Len',size=(16,1)), sg.InputText(default_text = 5.49044e-05)],
                [sg.Text('Fwd Pkts/s',size=(16,1)), sg.InputText(default_text = 1.6638e-07)],
                [sg.Text('Bwd Pkts/s',size=(16,1)), sg.InputText(default_text = 3.32755e-07)],
                [sg.Text('Pkt Len Max',size=(16,1)), sg.InputText(default_text = 0.0150838)],
                [sg.Text('SYN Flag Cnt',size=(16,1)), sg.InputText(default_text = 0.0)],
                [sg.Text('Subflow Fwd Byts',size=(16,1)), sg.InputText(default_text = 2.87643e-05)],
                [sg.Text('Subflow Bwd Byts',size=(16,1)), sg.InputText(default_text = 5.77692e-05)],
                [sg.Text('Init Fwd Win Byts',size=(16,1)), sg.InputText(default_text = 0.41022)],
                [sg.Text('Init Bwd Win Byts',size=(16,1)), sg.InputText(default_text = 0.003357)],
                [sg.Text('Fwd Seg Size Min',size=(16,1)), sg.InputText(default_text = 0.57143)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
    
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
        
    features = ['Index','Dst Port','Tot Bwd Pkts','Fwd IAT Std','Fwd PSH Flags',
                    'Fwd Header Len','Fwd Pkts/s','Bwd Pkts/s','Pkt Len Max',
                    'SYN Flag Cnt','Subflow Fwd Byts','Subflow Bwd Byts','Init Fwd Win Byts','Init Bwd Win Byts','Fwd Seg Size Min']
    
        

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