import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pd.read_csv('Thursday-15-02-2018_copy.csv')

#df.astype(np.float32)
X = df.drop(['Intrusion','Unnamed: 0','Flow Byts/s','Flow Pkts/s'], axis = 1)
X.astype(np.float32)
y = df['Intrusion']



# Puis on concatene nos differentes features
#df_final = pd.concat([X.iloc[:,0:1], X, X.iloc[:,6:]], axis=1)

#df_final.to_csv("df_final.csv")
np.nan_to_num(X)

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

'''

np.where(df.values >= np.finfo(np.float32).max)
X = df.drop(['Intrusion', 'Unnamed: 0'], axis = 1
np.nan_to_num(X)

'''