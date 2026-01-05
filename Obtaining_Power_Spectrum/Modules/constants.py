import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Can be ignored for now

# Constants
#Wavenumber Values (in 1/Mpc)
k_pow = np.arange(-6, 4)   #Mpc^-1
k = 10.0 ** k_pow

G_si = 6.67430e-11  # m^3 kg^-1 s^-2