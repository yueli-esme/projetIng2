# -*- coding: utf-8 -*-

'''
------------------------------ Correlation -----------------------------------
'''

import seaborn as sns
import matplotlib.pyplot as plt

def Correlation(df):
 
    df['Intrusion'].value_counts()
     
    plt.figure(figsize=(20,20))
    sns.heatmap(df.corr())
    sns.heatmap(df.corr(),annot=True)
    
    df_corr = df.corr()
    df_copy = df.copy()
    
    for i in range(0,len(df_corr)):
        if (df_corr.iloc[i]['Intrusion'] < 0.7) and (df_corr.iloc[i]['Intrusion'] > -0.7):
            print(df_corr.iloc[i])
            del df_copy[df_corr.iloc[i].name]
    
    return df_copy

