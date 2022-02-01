# plotear_temperaturas.py 
# Ejercicio 5.8

import numpy as np
import matplotlib.pyplot as plt


def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.figure
    plt.hist(temperaturas,bins=40)
    plt.xlim(36.8,38.2) 
    plt.ylim(0,70) 
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Cantidad de mediciones (1)")
    plt.title("Histograma de las temperaturas corporales medidas.")
    plt.show() 


if __name__ == '__main__':
    plotear_temperaturas()
