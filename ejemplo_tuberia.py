# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:05:02 2020

@author: moises
"""

from sklearn.datasets import load_digits
from sklearn.pipeline import make_pipeline

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split 

modeltree = DecisionTreeClassifier()
modelper = Perceptron()

X,Y = load_digits(return_X_y=True)

for i in range(5):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=400)
    print(X_test)


# print (len(X), len(Y))
# print(X.shape, Y.shape)
# print(X_train.shape, Y_train.shape)
# print(X_test.shape, Y_test.shape)

# print(X_test)

# lista_modelo=[('nnn',modelper),('tree',modeltree)]

# for indice, (nombre, modelo) in enumerate(lista_modelo):
#     print(indice, nombre)
#     modelo.fit(X,Y)
#     ypred = modelo.predict([[6.7,3.,5.2,2.3], [6.3,2.5,5.,1.9]])
#     print(ypred)
    
    
    