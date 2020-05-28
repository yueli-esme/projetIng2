import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('df_T_15_copy.csv')

X = df[['Dst Port','Protocol','Flow Duration']]

np.nan_to_num(X)
y = df['Intrusion']

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                        test_size=0.2, random_state=2)

rf = RandomForestRegressor(n_estimators = 25)
rf.fit(X_train, y_train)

importances = pd.Series(index=X.columns,
                        data=rf.feature_importances_)

importances_sorted = importances.sort_values()

importances_sorted.plot(kind='barh', color='lightgreen')

'''
np.where(df.values >= np.finfo(np.float32).max)
X = df.drop(['Intrusion', 'Unnamed: 0'], axis = 1
np.nan_to_num(X)
'''