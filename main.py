import numpy as np
import numerical_integrators
import SIS_deterministic
import matplotlib.pyplot as plt

def run_integrators(beta, step_size_h, log=False, save=False):
    SIS_deterministic.SIS_heun(100, 0.25, beta, step_size_h, 50)
    SIS_deterministic.SIS_euler(100, 0.25, beta, step_size_h, 50)
    plt.plot([], [], ' ', label="Beta="+str(beta)+", h="+str(step_size_h))
    plt.legend(loc='lower right')
    if log:
        plt.loglog()
    if save:
        plt.savefig('euler_heun_'+str(beta)+str(step_size_h)+'.png')
    plt.show()

if __name__ == '__main__':
    print("MOCS Assignment 1. \nBy Andrea Allen and Amanda Bertschinger")
    run_integrators(0.03, 0.01, True, True)
    run_integrators(0.06, 0.01, True, True)
    run_integrators(0.1, 0.01, True, True)

    run_integrators(0.03, 0.5, True, True)
    run_integrators(0.06, 0.5, False, True)
    run_integrators(0.1, 0.5, False, True)

    run_integrators(0.03, 2.0, False, True)
    run_integrators(0.06, 2.0, False, True)
    run_integrators(0.1, 2.0, False, True)