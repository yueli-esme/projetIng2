# -*- coding: utf-8 -*-

''' ---------------------- Bagging Classifier ---------------------------- '''

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

SEED = 1

df = pd.read_csv("total_dataset_normalise.csv", sep=';')

# On crée 2 tableaux X et y : X contient les caractéristiques de df et y est la variable cible
y = df['Intrusion']
X = df.drop('Intrusion', axis=1)

# On divise les données en données d'entrainements et de tests
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, stratify=y, random_state = SEED)

dt = DecisionTreeClassifier(max_depth=4, min_samples_leaf=0.16,random_state=SEED)

bc = BaggingClassifier(base_estimator = dt, n_estimators=300, n_jobs=-1)

bc.fit(X_train, y_train)

y_pred=bc.predict(X_test)

accuracy= accuracy_score(y_test, y_pred)

print('Bagging Classifier: {:.3f}'.format(accuracy))
