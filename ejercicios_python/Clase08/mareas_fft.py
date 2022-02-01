#!/usr/bin/env python3
# mareas_fft.py
# Ejercicio 8.10/1-


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
#df['12-25-2014':].plot()
#plt.show()

#df['10-15-2014':'12-15-2014'].plot()
#plt.show()

dh = df['12-25-2014':].copy()

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 20 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
plt.show()