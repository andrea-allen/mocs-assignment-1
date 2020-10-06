import numpy as np
import numerical_integrators
import SIS_deterministic
import matplotlib.pyplot as plt
import meme_propagation

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

def meme_stuff():
    #Plot 0.5: Same sigma 1 and sigma 2, vary fractions:
    meme_propagation.prop_memes_euler(1000, 1, 999, .5, .5, .80, .90, .001, 50)
    meme_propagation.prop_memes_euler(1000, 1, 999, .5, .5, .30, .10, .001, 50)
    plt.legend(loc='lower right')
    plt.title('Varying fractions with equal sharing rates')
    plt.semilogx()
    plt.show()

    # Plot 1: Vary sigma 1 and 2, leave fractions
    meme_propagation.prop_memes_euler(1000, 1, 999, .1, .3, .99, .05, .001, 50)
    meme_propagation.prop_memes_euler(1000, 1, 999, .1, .6, .99, .05, .001, 50)
    meme_propagation.prop_memes_euler(1000, 1, 999, .01, .3, .99, .05, .001, 50)
    meme_propagation.prop_memes_euler(1000, 1, 999, .01, .6, .99, .05, .001, 50)
    plt.legend(loc='upper left')
    plt.title('Meme Sharing - Varying Sharing Rates')
    plt.semilogx()
    plt.show()
    # Plot 2: Keep sigmas, vary fraction of public who receive memes via friends (N_partition_frac)
    meme_propagation.prop_memes_euler(1000, 1, 999, .05, .1, .25, .15, .001, 50)
    meme_propagation.prop_memes_euler(1000, 1, 999, .05, .1, .25, .05, .001, 50)
    meme_propagation.prop_memes_euler(1000, 1, 999, .05, .1, .99, .15, .001, 50) #fraction of people who recieve from friends matters more than people who share to only their friends
    meme_propagation.prop_memes_euler(1000, 1, 999, .05, .1, .99, .05, .001, 50)
    plt.title('Varying fraction of people who share with/receive from friends')
    plt.semilogx()
    plt.show()
    #Plot 3:  a high sigma_1 will compensate for a low N_frac (frac who recieve via friendships)
    meme_propagation.prop_memes_euler(1000, 1, 999, .05, .1, .15, .1, .001, 50)
    meme_propagation.prop_memes_euler(1000, 1, 999, .05, .1, .15, .5, .001, 50)
    meme_propagation.prop_memes_euler(1000, 1, 999, .90, .1, .15, .1, .001, 50)
    plt.title('Varying Friend-sharing rate with friend-receiving fraction')
    plt.semilogx()
    plt.show()

    #Plot 0: Initial condition plots: Obvious conclusions
    meme_propagation.prop_memes_euler(1000, 200, 800, .1, .3, .99, .05, .001, 50)
    meme_propagation.prop_memes_euler(1000, 1, 999, .1, .3, .99, .05, .001, 50)
    plt.title('Varying Initial Conditions')
    plt.semilogx()
    plt.show()


if __name__ == '__main__':
    print("MOCS Assignment 1. \nBy Andrea Allen and Amanda Bertschinger")
    meme_stuff()

    run_integrators(0.03, 0.01, True, True)
    run_integrators(0.06, 0.01, True, True)
    run_integrators(0.1, 0.01, True, True)

    run_integrators(0.03, 0.5, True, True)
    run_integrators(0.06, 0.5, False, True)
    run_integrators(0.1, 0.5, False, True)

    run_integrators(0.03, 2.0, False, True)
    run_integrators(0.06, 2.0, False, True)
    run_integrators(0.1, 2.0, False, True)