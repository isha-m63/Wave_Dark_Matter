import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp
from parameters import a, H, da_dt, rho_m

#Start date: 2/1/2026

#Coupled ODEs for CDM
def ode_cdm(t, y, k):
    u1, u2 = y      #u1 = delta | u2 = delta_dot
    
    H = 2 / (3 * t)
    quantum_term = 0
    grav_term = 2 / (3 * t**2 * a(t)**3)

    #Solve the following coupled 1st order ODEs
    du1_dt = u2
    du2_dt_cdm = -2*H*u2 + (grav_term - quantum_term)*u1
    return [du1_dt, du2_dt_cdm]


cdm_allkvals = []
for k_i in k_val:
    sol_cdm = solve_ivp(
        ode_cdm_allkvals,
        t_span,
        initial_conditions,
        t_eval=t_eval,
        args=(k_i,),
        #method = 'LSODA'
    )

    for j in range(len(t_eval)):
        cdm_allkvals.append(
            {
                't': t_eval[j],
                'k': k_i,
                'delta_cdm': sol_cdm.y[0][j],
                'delta_dot_cdm': sol_cdm.y[1][j]
            }
        )