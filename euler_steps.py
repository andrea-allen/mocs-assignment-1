#File for Euler steps
import numpy as np
import matplotlib.pyplot as plt
import math
import random


def euler_step(h, x_t, dx_dt):
    x_t_plus_h = x_t + h*dx_dt
    return x_t_plus_h
