#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import math

data = {
    "6": {
        "h": 3.1,
        "y": 12.6,
        "x": 18.4
    },

    "7": {
        "h": 2.4,
        "y": 8.4,
        "x": 7
    },

    "8": {
        "h": 3.5,
        "y": 3.4,
        "x": 6.2
    },

    "9": {
        "h": 3.3,
        "y": 20.3,
        "x": 24
    },

    "10": {
        "h": 2.5,
        "y": 5.6,
        "x": 7.4
    },

    "11": {
        "h": 2.7,
        "y": 3.3,
        "x": 3.7
    },

    "12": {
        "h": 2.5,
        "y": 5.6,
        "x": 7
    }
}

if __name__=="__main__":
    print("Snellius : making figure")

    # Computing the sinuses
    sing = []
    sing_e = []
    sina = []
    sin2a_e = []

    for i in data:
        sing.append(np.sin((np.pi / 2) - np.arctan(data[i]["y"] / data[i]["x"])))
        sing_e.append(np.abs( ( (1) / (np.sqrt(data[i]["x"]**2 + data[i]["y"]**2)) ) - ( (data[i]["x"]**2) / ( (data[i]["x"]**2 + data[i]["y"]**2)**(3/2) ) ) ) * data[i]["x"]/20 \
                      + np.abs( (-1 * data[i]["y"] * data[i]["x"])/( (data[i]["x"]**2 + data[i]["y"]**2)**(3/2) ) ) * data[i]["y"]/20)
        sina.append(data[i]["h"] / 10)
        sin2a_e.append( np.abs( ( 2 * np.cos( 2 * np.arcsin(data[i]["h"]/10) ) )/( np.sqrt(10**2 - data[i]["h"]**2) ) ) * data[i]["h"]/20 \
                        + np.abs( ( -2 * np.cos( 2 * np.arcsin(data[i]["h"]/10) * data[i]["h"] ) )/( 10 * np.sqrt( 10**2 - data[i]["h"]**2 ) ) ) * 0.1 )

    alpha = np.arcsin(sina)
    sin2a = np.sin(2 * alpha)

    # Plotting our data
    plt.errorbar(sin2a, sing, sing_e, sin2a_e, fmt='o', color='navy', linewidth=1, capsize=4, ms=3)

    # Computing the mean coefficient
    coefs = sing / sin2a
    coef_moy = np.mean(coefs)

    x = np.arange(0, 1, 0.0001)
    y = coef_moy * x

    print("Coefficient moyen : " + str(coef_moy))

    # Plotting our regression
    plt.plot(x, y, color='blue')

    # Plotting the theorical line
    yr = (1.333 / 1.000293) * x
    plt.plot(x, yr, color='red')

    # Making the graph nice
    plt.title("Détermination expérimentale de l'indice de réfraction de l'eau")
    plt.xlabel("$\\sin 2\\alpha$")
    plt.ylabel("$\\sin \\gamma$")
    plt.legend(["Indice moyen", "Laboratoires agréés", "Mesures expérimentales"])
    plt.tight_layout()
    plt.margins(0, 0)
    plt.xlim([0.3, 0.8])
    plt.ylim([0.4, 1])
    plt.grid()

    # Saving the graph
    plt.savefig("snellius.svg", format="svg")
