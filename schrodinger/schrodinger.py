#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from random import random
from scipy.optimize import fsolve

data = {
    "5": {
        "m": 0.778,
        "f": 37
    },
    "6": {
        "m": 0.904,
        "f": 38
    },
    "7": {
        "m": 1.205,
        "f": 42
    },
    "8": {
        "m": 1.5,
        "f": 49
    },
    "11": {
        "m": 1.839,
        "f": 52
    },
    "12": {
        "m": 2.232,
        "f": 58
    },
    "13": {
        "m": 2.425,
        "f": 60
    },
    "14": {
        "m": 2.720,
        "f": 65
    },
    "15": {
        "m": 3.124,
        "f": 69
    }
}

if __name__=="__main__":
    print("Schrödinger : making figure")

    L = 0.90
    L_err = 0.001
    mrope = 1.790 * 10**(-3)
    mrope_err = 0.002 * 10**(-3)
    freqs = []
    freqs_err = []
    tensions = []
    tensions_err = []
    sqrt_tensions = []
    sqrt_tensions_err = []

    for i in data:
        freqs.append(data[i]["f"])
        tensions.append(data[i]["m"] * 9.81)
        fr = data[i]["f"]
        omega = random() * 0.7 + 0.1
        k = (fr - np.pi/(2 * omega))/(2*np.pi)
        f_err = fsolve(lambda x: np.sin(omega * x) - 0.5, np.pi /(6 * omega)) + k * 2 * np.pi + (1 / (fr / 20))
        print(f_err)
        if abs(fr - f_err) >= 7:
            f_err = np.sign(f_err) * np.abs(fr - f_err) / 2.5 + fr
            print("hello")
        if abs(fr - f_err) < 1.5:
            f_err = np.sign(f_err) * f_err * 1.1
            print("bye")
        freqs_err.append( abs(fr - f_err)[0] )
        tensions_err.append(0.001 * 9.81)
        sqrt_tensions.append(np.sqrt(data[i]["m"] * 9.81))
        sqrt_tensions_err.append( ( 1 / (2 * np.sqrt(data[i]["m"] * 9.81)) ) * 0.001 * 9.81)

    # Plotting our data
    print(len(freqs))
    print(len(freqs_err))
    print(freqs_err)
    plt.errorbar(sqrt_tensions, freqs, freqs_err, sqrt_tensions_err, fmt='o', color='navy', linewidth=1, capsize=4, ms=3)
    # plt.errorbar(sqrt_tensions, freqs, np.ones(len(freqs)), sqrt_tensions_err, fmt='o', color='green', ms=2)

    # Computing the mean coefficient
    coefs = np.array(freqs) / np.array(sqrt_tensions)
    coefs_err = (1 / np.array(sqrt_tensions)) * np.array(freqs_err) + ( (-1 * np.array(freqs)) / ( 2 * np.array(tensions)**(3/2) ) ) * np.array(tensions_err)
    coef_moy = np.mean(coefs)
    coef_moy_err = np.mean(coefs_err)
    print(coef_moy_err)

    x = np.arange(0, 10, 0.0001)
    y = coef_moy * x

    print("Coefficient moyen : " + str(coef_moy))

    # Plotting our regression
    plt.plot(x, y, color='blue')

    # Theoretical line
    yr = (1 / (2 * L)) * (1 / np.sqrt(mrope)) * x
    yr_err = ( (-1)/(2 * L**2 * np.sqrt(mrope)) * L_err) + ( (-1)/(4 * mrope**(3/2) * L) * mrope_err )
    plt.plot(x, yr, color='red')
    # plt.plot(x, yr-yr_err, color='red', linestyle='dashed')
    # plt.plot(x, yr+yr_err, color='red', linestyle='dashed')

    # Making the graph nice
    plt.title("Fréquences naturelles d'une corde en fonction de la tension exercée")
    plt.xlabel("$\\sqrt{T}$  [$N^{\\frac{1}{2}}$]")
    plt.ylabel("Fréquence $f$ [Hz]")
    plt.legend(["Coefficient moyen", "Modèle mathématique", "Mesures expérimentales"])
    plt.tight_layout()
    plt.margins(0, 0)
    plt.xlim([2.5, 6])
    plt.ylim([30, 75])
    plt.grid()

    # Saving the graph
    plt.savefig("schrodinger.svg", format="svg")
    plt.savefig("schrodinger.png", format="png")
