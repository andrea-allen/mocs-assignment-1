import numerical_integrators
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import rc

#V : Viewed
#N : Not viewed
#ideas: more than one sigma
#V/j*(N/k) gets sigma1 V/(V-j)*(1-(N/K)) gets sigma^2
#sigma_1 only friends , but, note assumptions: still randomly mixed group of groups of friends!
#sigma_2 mass platforms, but, assumption is it will reach everyone.
#sigma: Sharing rate
#assumptions: make sure V/j < ...
#assumptions: once you've seen it from one person, that's it
#asumption: "People's friends" and "general public" are separate groups

def dV_dt(V_t, N_t, sigma_1, sigma_2, j=1, k=1):
    #rate of Viewing sigma
    if (j >= 1 or k >= 1):
        print("j and k must be fractions less than 1 (and greater than 0)")
        return None
    else:
        try:
            dV = sigma_1*((j*V_t)*(N_t*k)) + sigma_2*((V_t-(V_t*j))*(N_t-(N_t*k)))
        except OverflowError:
            dV = 0
        if (np.isnan(dV) or np.isinf(dV)):
            dV = 0
        return dV

def prop_memes_euler(T, V_0, N_0, sigma_1, sigma_2, V_partition_frac, N_partition_frac, step_size_h, steps):
    V_current = V_0
    N_current = N_0
    V_vec=[V_current]
    N_vec=[N_current]
    time = 0
    time_vec = [0]
    for t in range(1, math.floor(steps/step_size_h)):
            dV_dt_current = dV_dt(V_current, N_current, sigma_1, sigma_2, V_partition_frac, N_partition_frac)
            if dV_dt_current is None:
                return None
            V_plus_t = numerical_integrators.euler_step(step_size_h, V_current, dV_dt_current)
            V_vec.append(V_plus_t)
            N_vec.append(T-V_plus_t)
            V_current=V_vec[-1]
            N_current=N_vec[-1]
            time += step_size_h
            time_vec.append(time)
    time_vec = time_vec[:len(V_vec)]
    rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
    rc('text', usetex=True)
    plt.plot(time_vec[1:], V_vec[1:], alpha=0.6, lw=2, label=make_label(sigma_1, sigma_2, V_partition_frac, N_partition_frac))
    plt.xlabel('Log time t with step size '+str(step_size_h))
    plt.ylabel('$V$: number who have viewed the meme')
    plt.legend(loc='lower right')
    return V_vec

def make_label(sigma_1, sigma_2, V_frac, N_frac):
    label = '$\\sigma_1=$' + str(sigma_1) + ', $\\sigma_2=$' + str(sigma_2) + ', $j=$'+str(V_frac)+', $k=$'+str(N_frac)
    return label