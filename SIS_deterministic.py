import euler_steps
import numpy as np
import matplotlib.pyplot as plt

#S init 90
#I init 10
def SIS_euler(N, gamma, beta, step_size_h, steps):
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
    # plt.show()
    return I_vec

def SIS_heun(N, gamma, beta, step_size_h, steps):
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
        I_x_t_e = euler_steps.euler_step(step_size_h, I, dI_dt(S, I, gamma, beta))
        S_x_t_e = euler_steps.euler_step(step_size_h, S, dS_dt(S, I, gamma, beta))
        I_vec[t] = heun_step(step_size_h, I, dI_dt(S, I, gamma, beta), I_x_t_e, "I", S, I, gamma, beta)
        S_vec[t] = heun_step(step_size_h, S, dS_dt(S, I, gamma, beta), S_x_t_e, "S", S, I, gamma, beta)
        S=S_vec[t]
        I=I_vec[t]
        time += step_size_h
        time_vec.append(time)
    plt.plot(time_vec, I_vec)
    # plt.show()
    return I_vec

def dS_dt(S_t, I_t, gamma, beta):
    dS = -int(np.round(beta*S_t*I_t))+int(np.round(gamma*I_t))
    return dS

def dI_dt(S_t, I_t, gamma, beta):
    dI = int(np.round(beta*S_t*I_t))-int(np.round(gamma*I_t))
    return dI

def heun_step(h, x_t, dx_dt, x_t_e, rate_type_var, S_t, I_t, gamma, beta):
    #TODO work in progress
    x_t_plus_h_Hn = 0
    # x_t_e = euler_steps.euler_step(h, x_t, dx_dt)
    if rate_type_var=="I":
        dx_dt_e = dI_dt(S_t, x_t_e, gamma, beta)
    if rate_type_var=="S":
        dx_dt_e = dS_dt(x_t_e, I_t, gamma, beta)
    #get dx of euler_step(h,x_t, dx_dt)
    #  by treating euler_step() as X_t and computing dS_dt or dI_dt for that value
    #dx_dt_e = dx of euler_step(h,x_t, dx_dt)
    x_t_plus_h_Hn = x_t + h*((dx_dt+dx_dt_e)/2)
    return x_t_plus_h_Hn