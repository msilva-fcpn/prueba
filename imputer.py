# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:48:14 2020

@author: moises
"""


import numpy as np
matriz=[[1,2,3],
        [-4,np.nan,5],
        [6,np.nan,7]]
print(matriz)

from sklearn.impute import SimpleImputer
imputacion = SimpleImputer(missing_values=np.nan,
                           strategy="mean")
matriz_imputer = imputacion.fit_transform(matriz)
print(matriz_imputer)

import pandas as pd
data = pd.read_csv("ejemplo.csv")
print(data)
print(imputacion.fit_transform(data))

from sklearn import preprocessing
matriz_normal = preprocessing.normalize(matriz_imputer)
print(matriz_normal)


