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
            df.Intrusion[z] = 0
            
        else :
            df.Intrusion[z] = 1       
        z = z+1
           
def supprimer_colonne_vide(df) :
    for colonne in df:
        compteur = 0
        for valeur in df[colonne]:
            if valeur == 0:
                compteur +=1
                
        if compteur == len(df) or colonne == 'Timestamp' or colonne == 'Label':
            del df[colonne]

def equilibrage_donnees(df):
    #on compte les differentes valeurs de la colonne label
    df['Label'].value_counts() 
    
    #On crée une dataset intrusion
    df_intrusion = df[df['Label'] != 'Benign' ] 
    
    #on crée une dataset benign avec le meme nombre de ligne que la dataset intrusion
    df_benign = df[df['Label'] == 'Benign' ][0:566]

    #on concate les deux datasets
    df = pd.concat([df_intrusion,df_benign]) 
    df = df.reset_index(drop = True)

    return df


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

# On équilibre les données pour chaque dataframe
df_T_15 = equilibrage_donnees(df_T_15)
df_T_22 = equilibrage_donnees(df_T_22)
df_W_21 = equilibrage_donnees(df_W_21)
df_W_14 = equilibrage_donnees(df_W_14)
df_F_02 = equilibrage_donnees(df_F_02)
df_F_23 = equilibrage_donnees(df_F_23)

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
