#File for Euler steps
import numpy as np
import matplotlib.pyplot as plt
import math
import random


def euler_step(h, x_t, dx_dt):
    x_t_plus_h = x_t + h*dx_dt
    print(x_t, x_t_plus_h)
    return x_t_plus_h

def heun_step(h, x_t, dx_dt, x_t_e):
    x_t_plus_h_Hn = 0
    #get dx of euler_step(h,x_t, dx_dt)
    #  by treating euler_step() as X_t and computing dS_dt or dI_dt for that value
    #dx_dt_e = dx of euler_step(h,x_t, dx_dt)
    #x_t_plus_h_Hn = x_t + h*((dx_dt+dx_dt_e)/2)
    return x_t_plus_h_Hn