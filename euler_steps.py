#File for Euler steps
import numpy as np
import matplotlib.pyplot as plt
import math
import random


def euler_step(h, x_t, dx_dt):
    x_t_plus_h = x_t + h*dx_dt
    return x_t_plus_h

def heun_step(h, x_t, dx_dt, dx_dt_eu):
    x_t_plus_h_hn = x_t + (h/2)*(dx_dt + dx_dt_eu)
    return x_t_plus_h_hn