#!/usr/bin/env python3
# iris_seaborn.py
# Ejercicio 12.10

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris_dataset = load_iris()
    iris_dataframe = pd.DataFrame(iris_dataset['data'], 
                                columns = iris_dataset.feature_names)
    iris_dataframe['target'] = pd.array([iris_dataset['target_names'][i] 
                                        for i in iris_dataset['target']])
    iris_dataframe.rename(columns={'target': 'Especies'}, inplace=True)
    sns.pairplot(iris_dataframe, hue='Especies', diag_kind="hist") 
    plt.show()
    #ATENCIÓN! Soy daltónico, pero cualquier cambio en el color se puede 
    # realizar a través del parámetro opcional 'palette' del pairplot. 
    # Me pareció que no valía la pena armar una función por la simpleza y 
    # longitud del código.