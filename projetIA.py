# Librairies 
import pandas as pd
from pandas_profiling import ProfileReport

        
df_T_15 = pd.read_csv("Thursday-15-02-2018_TrafficForML_CICFlowMeter.csv")
df_T_22 = pd.read_csv("Thursday-22-02-2018_TrafficForML_CICFlowMeter.csv")
df_W_21 = pd.read_csv("Wednesday-21-02-2018_TrafficForML_CICFlowMeter.csv")
df_W_14 = pd.read_csv("Wednesday-14-02-2018_TrafficForML_CICFlowMeter.csv")
df_F_02 = pd.read_csv("Friday-02-03-2018_TrafficForML_CICFlowMeter.csv")
df_F_23 = pd.read_csv("Friday-23-02-2018_TrafficForML_CICFlowMeter.csv")



# Les fonctions

def analyser_df(df):
    
    #Analyse rapide
    print("\nShape de la frame :\n", df.shape)
    print("\nNoms des colonnes :\n", df.columns)
    print("\nPremières lignes :\n", df.head())
    print("\nDernières lignes :\n", df.tail())
    
    #On regarde les differentes classes presentes dans la colonne label
    print("\n ELEMENTS DE LA COLONNE LABEL")
    print(df.Label.unique())
        
    #On compte le nombre de fois que chaque element revient
    print("\n ELEMENTS DE LA COLONNE LABEL AVEC NB DE FOIS QU'ILS REVIENNENT")
    print(df.Label.value_counts())

def rajouter_colonne_intrusion(df) :
    
    df['Intrusion'] = 0
    z = 0 
    
    #Généralisation
        #elif df.Label[z] == 'Nom d`\'intrusion':
        #    df.Intrusion[z] = n+1
    
    for x in df.Intrusion:
        if df.Label[z] == 'Benign':
            df.Intrusion[z] = 1
            
        elif df.Label[z] == 'DDOS attack-HOIC':
            df.Intrusion[z] = 2
            
        elif df.Label[z] == 'DDOS attack-LOIC-UDP':
            df.Intrusion[z] = 3
            
        elif df.Label[z] == 'FTP-BruteForce':
            df.Intrusion[z] = 4
            
        elif df.Label[z] == 'SSH-Bruteforce':
            df.Intrusion[z] = 5
            
        elif df.Label[z] == 'Brute Force -Web':
            df.Intrusion[z] = 6
        
        elif df.Label[z] == 'Brute Force -XSS ':
            df.Intrusion[z] = 7
            
        elif df.Label[z] == 'SQL Injection':
            df.Intrusion[z] = 8
            
        elif df.Label[z] == 'DoS attacks-GoldenEye':
            df.Intrusion[z] = 9
        
        elif df.Label[z] == 'DoS attacks-Slowloris':
            df.Intrusion[z] = 10
            
        elif df.Label[z] == 'Bot':
            df.Intrusion[z] = 11
    
        else :
            df.Intrusion[z] = 0        
        z = z+1
           
def supprimer_colonne_vide(df) :
    for colonne in df:
        compteur = 0
        for valeur in df[colonne]:
            if valeur == 0:
                compteur +=1
                
        if compteur == len(df):
            del df[colonne]


# On analyse les dataframes pour mieux les connaitre
print("\n\n------------  df_T_15  ------------\n")
analyser_df(df_T_15)
print("\n\n------------  df_T_22  ------------\n")
analyser_df(df_T_22)
print("\n\n------------  df_W_21  ------------\n")
analyser_df(df_W_21)
print("\n\n------------  df_W_14  ------------\n")
analyser_df(df_W_14)
print("\n\n------------  df_F_02  ------------\n")
analyser_df(df_F_02)
print("\n\n------------  df_F_23  ------------\n")
analyser_df(df_F_23)

# On rajoute la colonne intrusion pour chaque dataframe
rajouter_colonne_intrusion(df_T_15)
rajouter_colonne_intrusion(df_T_22)
rajouter_colonne_intrusion(df_W_21)
rajouter_colonne_intrusion(df_W_14)
rajouter_colonne_intrusion(df_F_02)
rajouter_colonne_intrusion(df_F_23)

# On copie les datasets dans de nouvelles datasets
df_T_15_copy = df_T_15.copy()
df_T_22_copy = df_T_22.copy()
df_W_21_copy = df_W_21.copy()
df_W_14_copy = df_W_14.copy()
df_F_02_copy = df_F_02.copy()
df_F_23_copy = df_F_23.copy()

# On supprime les colonnes vides pour chaque dataframe
supprimer_colonne_vide(df_T_15_copy)
supprimer_colonne_vide(df_T_22_copy)
supprimer_colonne_vide(df_W_21_copy)
supprimer_colonne_vide(df_W_14_copy)
supprimer_colonne_vide(df_F_02_copy)
supprimer_colonne_vide(df_F_23_copy)


# On enregistre toutes ces dataframes dans de nouveaux fichiers csv pour les conserver
df_T_15_copy.to_csv("df_T_15_copy.csv", sep=';')
df_T_22_copy.to_csv("df_T_22_copy.csv", sep=';')
df_W_21_copy.to_csv("df_W_21_copy.csv", sep=';')
df_W_14_copy.to_csv("df_W_14_copy.csv", sep=';')
df_F_02_copy.to_csv("df_F_02_copy.csv", sep=';')
df_F_23_copy.to_csv("df_F_23_copy.csv", sep=';')

# Pour générer un rapport (fonctionne mieux sur Jupyter Note Book)
prof = ProfileReport(df_T_15_copy)
profile = ProfileReport(df_T_15_copy, minimal=True)
profile.to_file(output_file="Rapport_df_T_15_copy.html")

prof = ProfileReport(df_T_22_copy)
profile = ProfileReport(df_T_22_copy, minimal=True)
profile.to_file(output_file="Rapport_df_T_22_copy.html")

prof = ProfileReport(df_W_21_copy)
profile = ProfileReport(df_W_21_copy, minimal=True)
profile.to_file(output_file="Rapport_df_W_21_copy.html")

prof = ProfileReport(df_W_14_copy)
profile = ProfileReport(df_W_14_copy, minimal=True)
profile.to_file(output_file="Rapport_df_W_14_copy.html")

prof = ProfileReport(df_F_02_copy)
profile = ProfileReport(df_F_02_copy, minimal=True)
profile.to_file(output_file="Rapport_df_F_02_copy.html")

prof = ProfileReport(df_F_23_copy)
profile = ProfileReport(df_F_23_copy, minimal=True)
profile.to_file(output_file="Rapport_df_F_23_copy.html")


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