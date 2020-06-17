# -*- coding: utf-8 -*-

'''
------------------------------ Features Importances -----------------------------------
'''


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

def FeaturesImportances(df):
    
    X = df.drop(['Intrusion','Unnamed: 0'], axis = 1)
    y = df['Intrusion']
    
    for colonne in X.columns:
        a = np.array((X[colonne]))
        X[colonne] = np.around(a, decimals=5)
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.2, random_state=2)
    
    rf = RandomForestRegressor(n_estimators = 25)
    rf.fit(X_train, y_train)
    
    importances1 = pd.Series(index=X.columns[:20],
                            data=rf.feature_importances_[:20])
    importances_sorted1 = importances1.sort_values()
    importances_sorted1.plot(kind='barh', color='red', title='1')
    plt.show()
    
    importances2 = pd.Series(index=X.columns[20:40],
                            data=rf.feature_importances_[20:40])
    importances_sorted2 = importances2.sort_values()
    importances_sorted2.plot(kind='barh', color='red', title='2')
    plt.show()
    
    importances3 = pd.Series(index=X.columns[40:],
                            data=rf.feature_importances_[40:])
    importances_sorted3 = importances3.sort_values()
    importances_sorted3.plot(kind='barh', color='red', title='3')
    plt.show()

# Pour créer une dataframe avec que les colonnes importantes
    
    feature_importances = pd.DataFrame(rf.feature_importances_, index = X_train.columns, columns=['Intrusion']).sort_values('Intrusion',ascending=False)
    
    df_copy = df.copy()
    
    for i in range(0,len(feature_importances)):
        if feature_importances.iloc[i]['Intrusion'] < 0.001:
            print(feature_importances.iloc[i])
            del df_copy[feature_importances.iloc[i].name]
            
  
    return df_copy