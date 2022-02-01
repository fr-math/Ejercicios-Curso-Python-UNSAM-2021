#!/usr/bin/env python3
#  iris_seaborn.py
# Ejercicio 12.10

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris_dataset = load_iris()

print("Claves del diccionario iris_dataset:\n", iris_dataset.keys())
print("Target names:", iris_dataset['target_names'])
print("Feature names:\n", iris_dataset['feature_names'])
print("Type of data:", type(iris_dataset['data']))
print("Shape of data:", iris_dataset['data'].shape)
print("First five rows of data:\n", iris_dataset['data'][:5])
print("Type of target:", type(iris_dataset['target']))
print("Shape of target:", iris_dataset['target'].shape)
print("Target:\n", iris_dataset['target'])

import pandas as pd
iris_dataframe = pd.DataFrame(iris_dataset['data'], 
                              columns = iris_dataset.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], 
                           figsize = (15, 15), marker = 'o', 
                           hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)
plt.show()