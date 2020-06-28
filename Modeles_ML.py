# -*- coding: utf-8 -*-


'''
------------------------------ Modeles de ML -----------------------------------
'''

# Librairies utiles 
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import time

# Knn
def knn(df):
    
    t_debut = time.time()
    
    X = df.drop(['Intrusion'], axis = 1)
    y = df['Intrusion']
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.2, random_state=42 )
    
    knn = KNeighborsClassifier(n_neighbors=10)
    
    knn.fit(X, y)
    
    y_pred_knn = knn.predict(X_test)
    
    print('Report Knn \n', classification_report(y_test, y_pred_knn))
    
    t_fin = time.time()
    
    t_total = t_fin - t_debut
    
    print("Temps pour Knn (en sec): ", t_total)
    
    return knn


# prediction
def knnPrediction(df,knn):
    X_new_knn = df
    # Predict and print the label for the new data point X_new
    new_prediction_knn = knn.predict(X_new_knn)
    print("New prediction knn: {}".format(new_prediction_knn))
    return new_prediction_knn


# Random Forest Classifier

def rf(df):
    
    t_debut = time.time()
    
    X = df.drop(['Intrusion'], axis = 1)
    y = df['Intrusion']
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.2, random_state=2 )
    
    rf = RandomForestClassifier(max_depth=2, random_state=0)
    rf.fit(X, y)
    
    y_pred_rf = rf.predict(X_test)
    
    print('Report RF \n', classification_report(y_test, y_pred_rf))
    
    t_fin = time.time()
    
    t_total = t_fin - t_debut
    
    print("Temps pour Random Forest (en sec): ", t_total)
    
    return rf


def rfPrediction(df,rf):
    X_new_rf = df
    # Predict and print the label for the new data point X_new
    new_prediction_rf = rf.predict(X_new_rf)
    print("New prediction rf: {}".format(new_prediction_rf))
    return new_prediction_rf


# Gaussian naive Bayes

def gnb(df):
    
    t_debut = time.time()
    
    X = df.drop(['Intrusion'], axis = 1)
    y = df['Intrusion']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    
    gnb = GaussianNB()
    
    gnb.fit(X_train, y_train)
    
    y_pred_gnb = gnb.predict(X_test)
    
    print('Report GNB \n', classification_report(y_test, y_pred_gnb))
    
    t_fin = time.time()
    
    t_total = t_fin - t_debut
    
    print("Temps pour Gnb (en sec): ", t_total)
    
    return gnb

def gnbPrediction(df,gnb):
    X_new_gnb = df
    # Predict and print the label for the new data point X_new
    new_prediction_gnb = gnb.predict(X_new_gnb)
    print("New prediction gnb: {}".format(new_prediction_gnb))
    return new_prediction_gnb

