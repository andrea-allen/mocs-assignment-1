import numpy as np
import euler_steps
import SIS_deterministic

if __name__ == '__main__':
    print("MOCS Assignment 1. \nBy Andrea Allen and Amanda Bertschinger")
    SIS_deterministic.SIS(100, 0.25, 0.03, 0.01, 500)
    SIS_deterministic.SIS(100, 0.25, 0.06, 0.01, 500)
    SIS_deterministic.SIS(100, 0.25, 0.01, 0.01, 500)
    SIS_deterministic.SIS(100, 0.25, 0.03, 0.5, 500)
    SIS_deterministic.SIS(100, 0.25, 0.06, 0.5, 500)
    SIS_deterministic.SIS(100, 0.25, 0.01, 0.5, 500)
    # SIS_deterministic.SIS(100, 0.25, 0.03, 2, 50)
    # SIS_deterministic.SIS(100, 0.25, 0.06, 2, 50)
    # SIS_deterministic.SIS(100, 0.25, 0.01, 2, 50)