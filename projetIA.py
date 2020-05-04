import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas_profiling import ProfileReport

        
#df1 = pd.read_csv("Thursday-01-03-2018_TrafficForML_CICFlowMeter.csv") Elle beug car que des objects
df2 = pd.read_csv("Thursday-15-02-2018_TrafficForML_CICFlowMeter.csv")
df3 = pd.read_csv("Thursday-22-02-2018_TrafficForML_CICFlowMeter.csv")

#print(df3.dtypes)

def rajouter_colonne_intrusion(df3) :
    
    df3['Intrusion'] = 0
    z = 0 
    for x in df3.Intrusion:
        if df3.Label[z] == 'Benign':
            df3.Intrusion[z] = 1
            
        elif df3.Label[z] == 'DDOS attack-HOIC':
            df3.Intrusion[z] = 2
        #Généralisation
        #elif df.Label[z] == 'Nom d`\'intrusion':
        #    df.Intrusion[z] = n+1
        else :
            df3.Intrusion[z] = 0        
        z = z+1
           
rajouter_colonne_intrusion(df3)   
#print(df_intrusion.head())
prof = ProfileReport(df3)
profile = ProfileReport(df3, minimal=True)
profile.to_file(output_file="Rapport_Thursday-22-02-2018.html")


'''
#print('Shape de la df:\n',dataFrame.shape)

#print('Nombre de colonnes de la df:\n', dataFrame.columns)
#print('10 premieres lignes:\n',dataFrame.head(10))
#print('10 dernieres lignes\n', dataFrame.tail(10))
'''



'''
Etape : 1.Label Intrusion
        2.Drop labels useless
        3.
    

'''