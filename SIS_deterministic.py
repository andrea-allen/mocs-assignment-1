import euler_steps
import numpy as np
import matplotlib.pyplot as plt
import math


def SIS_euler(N, gamma, beta, step_size_h, steps):
    S_current = 90
    I_current = 10
    S_vec=[S_current]
    I_vec=[I_current]
    time = 0
    time_vec = [0]
    # try:
    for t in range(1, math.floor(steps/step_size_h)):
            dI_dt_current = dI_dt(S_current, I_current, gamma, beta)
            I_plus_t = euler_steps.euler_step(step_size_h, I_current, dI_dt_current)
            I_vec.append(I_plus_t)
            S_vec.append(N-I_plus_t)
            S_current=S_vec[-1]
            I_current=I_vec[-1]
            time += step_size_h
            time_vec.append(time)
    # except OverflowError:
    #     if len(I_vec) > len(time_vec):
    #         I_vec.pop(-1)
    # if (True in np.isinf(I_vec)):
    #     I_vec = I_vec[:np.where(np.isinf(I_vec))[0][0]]
    # if (True in np.isnan(I_vec)):
    #     I_vec = I_vec[:np.where(np.isnan(I_vec))[0][0]]

    time_vec = time_vec[:len(I_vec)]
    # plt.scatter(time_vec, I_vec, label='Euler')
    plt.plot(time_vec, I_vec, alpha=0.6, lw=2, label='Euler')
    plt.legend(loc='lower right')
    print(I_vec)
    return I_vec

def SIS_heun(N, gamma, beta, step_size_h, steps):
    S_current = 90
    I_current = 10
    S_vec=[S_current]
    I_vec=[I_current]
    I_vec_E = [I_current]
    time = 0
    time_vec = [0]
    difference_vec = [0]
    # try:
    for t in range(1, math.floor(steps/step_size_h)):
            dI_dt_current = dI_dt(S_current, I_current, gamma, beta)
            I_t_plus_h_eu = euler_steps.euler_step(step_size_h, I_current, dI_dt_current)
            S_t_plus_h_eu = N - I_t_plus_h_eu
            dI_dt_Eu_t_plus_h = dI_dt(S_t_plus_h_eu, I_t_plus_h_eu, gamma, beta)
            I_t_plus_h_Hu = euler_steps.heun_step(step_size_h, I_current, dI_dt_current, dI_dt_Eu_t_plus_h)
            I_vec.append(I_t_plus_h_Hu)
            S_vec.append(N - I_t_plus_h_Hu)
            S_current=S_vec[-1]
            I_current=I_vec[-1]
            time += step_size_h
            time_vec.append(time)
            difference_vec.append(abs(I_vec[-1]-I_vec_E[-1]))
    # except TypeError or OverflowError:
    #     if len(I_vec_E)>len(time_vec):
    #         I_vec_E.pop(-1)
    #     if len(I_vec) > len(time_vec):
    #         I_vec.pop(-1)
    # if (True in np.isinf(I_vec)):
    #     I_vec = I_vec[:np.where(np.isinf(I_vec))[0][0]]
    # if (True in np.isnan(I_vec)):
    #     I_vec = I_vec[:np.where(np.isnan(I_vec))[0][0]]
    # if (step_size_h==2):
    #     print(step_size_h)
    time_vec = time_vec[:len(I_vec)]
    print(I_vec)
    # plt.scatter(time_vec, I_vec, label='Heun')
    plt.plot(time_vec, I_vec, alpha=0.6, lw=2, label='Heun')
    plt.legend(loc='lower right')
    plt.xlabel('Time t=0 to T=50/h')
    plt.ylabel('I(t): Number Infected at time t')
    return I_vec

def dI_dt(S_t, I_t, gamma, beta):
    try:
        dI = beta*(S_t*I_t)-gamma*I_t
    except OverflowError:
        dI = 0
    if np.isinf(dI) or np.isnan(dI):
        dI=0
    return dI

