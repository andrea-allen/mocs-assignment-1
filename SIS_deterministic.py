import euler_steps
import numpy as np
import matplotlib.pyplot as plt

#S init 90
#I init 10
def SIS(N, gamma, beta, step_size_h, steps):
    S_vec = np.zeros(steps)
    I_vec = np.zeros(steps)
    S = 90
    I = 10
    #At time t+1, S = euler_step()
    S_vec[0]=S
    I_vec[0]=I
    time = 0
    time_vec = [0]

    for t in range(1, steps):
        print(S, I, S+I)
        I_vec[t] = euler_steps.euler_step(step_size_h, I, dI_dt(S, I, gamma, beta))
        S_vec[t] = euler_steps.euler_step(step_size_h, S, dS_dt(S, I, gamma, beta))
        S=S_vec[t]
        I=I_vec[t]
        time += step_size_h
        time_vec.append(time)
    plt.plot(time_vec, I_vec)
    plt.show()
    return I_vec

def dS_dt(S_t, I_t, gamma, beta):
    dS = -int(np.round(beta*S_t*I_t))+int(np.round(gamma*I_t))
    return dS

def dI_dt(S_t, I_t, gamma, beta):
    dI = int(np.round(beta*S_t*I_t))-int(np.round(gamma*I_t))
    return dI