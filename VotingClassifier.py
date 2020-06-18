# -*- coding: utf-8 -*-

''' ---------------------- Voting Classifier ---------------------------- '''

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

def VotingClass(df):
    SEED = 1
    
    # On crée 2 tableaux X et y : X contient les caractéristiques de df et y est la variable cible
    y = df['Intrusion']
    X = df.drop('Intrusion', axis=1)
    
    # On divise les données en données d'entrainements et de tests
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = SEED)
    
    lr = LogisticRegression(random_state=SEED)
    knn = KNN()
    dt = DecisionTreeClassifier(random_state=SEED)
    
    classifiers=[('Logistic Regression', lr), ('K Nearest Neighbors', knn), ('Classification Tree', dt)]
    
    for clf_name, clf in classifiers:
        clf.fit(X_train, y_train)
        y_pred=clf.predict(X_test)
        print('{:s} : {:.3f}'.format(clf_name, accuracy_score(y_test, y_pred)))
        
    vc = VotingClassifier(estimators=classifiers)
    vc.fit(X_train, y_train)
    y_pred = vc.predict(X_test)
    
    print('Voting Classifier: {:.3f}'.format(accuracy_score(y_test, y_pred)))
