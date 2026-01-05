import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

#Start date: 2/1/2026

#Scale Factor
def a(t):
    return t**(2/3)

#Scale Factor Derivative
def da_dt(t):
    return (2/3)*t**(-1/3)

#Hubble Parameter
def H(t):
    return da_dt(t)/a(t)

#Average Matter Density
def rho_m(t):
    return 1 / (6 * np.pi * G * t**2)


